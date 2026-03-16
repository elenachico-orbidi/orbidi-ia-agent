"""
Asistente IA de Customer Success - Orbidi
Interfaz web tipo ChatGPT con Streamlit + RAG sobre archivos Markdown (export Notion)
"""
import os
import re
import unicodedata
import streamlit as st
from groq import Groq
from rank_bm25 import BM25Okapi

# ─────────────────────────────────────────────
# DIRECTORIO DE DATOS (export Notion en Markdown)
# ─────────────────────────────────────────────
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notion_export")

# ─────────────────────────────────────────────
# TOKENIZADOR ESPAÑOL PARA BM25
# ─────────────────────────────────────────────
SPANISH_STOPWORDS = {
    'de', 'la', 'el', 'en', 'y', 'a', 'los', 'las', 'un', 'una', 'con',
    'por', 'para', 'del', 'al', 'es', 'se', 'que', 'no', 'si', 'su', 'lo',
    'le', 'o', 'e', 'u', 'hay', 'son', 'ser', 'ha', 'han', 'tiene', 'tienen',
    'puede', 'pueden', 'este', 'esta', 'estos', 'estas', 'como', 'cuando',
    'donde', 'quien', 'cual', 'cuales', 'más', 'mas', 'pero', 'sino', 'porque',
    'aunque', 'desde', 'hasta', 'entre', 'sobre', 'bajo', 'ante', 'tras',
    'todo', 'toda', 'todos', 'todas', 'otro', 'otra', 'otros', 'otras',
    'ser', 'estar', 'haber', 'hacer', 'ir', 'ver', 'dar', 'saber',
}


def _normalize(text: str) -> list[str]:
    """Convierte texto a tokens normalizados (sin acentos, minúsculas, sin stopwords)."""
    text = text.lower()
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    text = re.sub(r'[^\w\s]', ' ', text)
    return [t for t in text.split() if t not in SPANISH_STOPWORDS and len(t) > 1]


# ─────────────────────────────────────────────
# CARGA DE ARCHIVOS MARKDOWN
# ─────────────────────────────────────────────

def _clean_notion_title(filename: str) -> str:
    """Limpia el nombre de archivo de Notion eliminando UUIDs y extensión.
    Ejemplo: 'Mi Procedimiento 404bfe8d-bc26-491a-a504-7731d31141dd.md' -> 'Mi Procedimiento'
    """
    name = os.path.splitext(filename)[0]
    # Eliminar UUID al final (formato: 8-4-4-4-12 hex)
    name = re.sub(r'\s+[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', '', name)
    # Eliminar UUID al final sin guiones (32 hex)
    name = re.sub(r'\s+[0-9a-f]{32}$', '', name)
    # Eliminar prefijo ExportBlock-UUID
    name = re.sub(r'^ExportBlock-[0-9a-f-]+', '', name).strip(' -_')
    return name.strip()


def _extract_title_from_content(text: str) -> str:
    """Extrae el título del primer header # del contenido markdown."""
    for line in text.splitlines()[:10]:
        line = line.strip()
        if line.startswith('# ') and not line.startswith('## '):
            return line[2:].strip()
    return ''


def _split_markdown_into_procedures(text: str, source_file: str) -> list[dict]:
    """
    Divide un archivo markdown en procedimientos individuales.

    Estrategia (prioriza la división más granular):
    1. Si tiene headers ## (h2), SIEMPRE divide por h2 (típico de Notion)
    2. Si no tiene h2 pero sí múltiples h1, divide por h1
    3. Si no tiene headers claros, trata como un solo procedimiento
    """
    procedures = []

    # Contar headers reales (no splits)
    h1_count = len(re.findall(r'^# [^#]', text, re.MULTILINE))
    h2_count = len(re.findall(r'^## [^#]', text, re.MULTILINE))
    h3_count = len(re.findall(r'^### [^#]', text, re.MULTILINE))

    # PRIORIDAD 1: Si hay secciones ## (h2), dividir por h2
    # Esto es lo típico de Notion: un título # seguido de muchos ##
    if h2_count >= 2:
        h2_splits = re.split(r'\n(?=## [^#])', text)
        for section in h2_splits:
            section = section.strip()
            if not section or len(section) < 20:
                continue

            first_line = section.splitlines()[0].strip()

            # Si es un header h1 solo (intro/título del documento)
            if first_line.startswith('# ') and not first_line.startswith('## '):
                title = first_line[2:].strip()
                content_lines = [l for l in section.splitlines()[1:] if l.strip()]
                if len(content_lines) > 2:
                    procedures.append({'title': f"INTRO: {title}", 'content': section, 'source': source_file})
                continue

            # Extraer título h2
            if first_line.startswith('## '):
                title = first_line[3:].strip()
                # Limpiar markdown del título (negritas, emojis de numeración)
                title = re.sub(r'\*\*([^*]+)\*\*', r'\1', title).strip()
            else:
                title = first_line[:80]

            # Filtrar secciones que son solo links a otros archivos (sin contenido real)
            content_lines = [l for l in section.splitlines()[1:] if l.strip()]
            # Si solo tiene links a otros .md y nada más, saltar
            real_content = [l for l in content_lines if not re.match(r'^\[.*\]\(.*\.md\)$', l.strip())]
            if len(real_content) < 2:
                continue

            procedures.append({'title': title, 'content': section, 'source': source_file})

    # PRIORIDAD 2: Si hay muchas secciones ### pero pocas ##, dividir por h3
    elif h3_count >= 2:
        h3_splits = re.split(r'\n(?=### [^#])', text)
        for section in h3_splits:
            section = section.strip()
            if not section or len(section) < 20:
                continue
            first_line = section.splitlines()[0].strip()
            if first_line.startswith('### '):
                title = first_line[4:].strip()
            elif first_line.startswith('# '):
                title = first_line.lstrip('# ').strip()
            else:
                title = first_line[:80]
            procedures.append({'title': title, 'content': section, 'source': source_file})

    # PRIORIDAD 3: Si hay múltiples h1, dividir por h1
    elif h1_count >= 2:
        h1_splits = re.split(r'\n(?=# [^#])', text)
        for section in h1_splits:
            section = section.strip()
            if not section or len(section) < 20:
                continue
            title = _extract_title_from_content(section)
            if not title:
                title = section.splitlines()[0][:80] if section.splitlines() else source_file
            procedures.append({'title': title, 'content': section, 'source': source_file})

    # PRIORIDAD 4: Sin headers claros - archivo completo como un procedimiento
    else:
        title = _extract_title_from_content(text) or _clean_notion_title(source_file)
        if title and len(text.strip()) > 20:
            procedures.append({'title': title, 'content': text.strip(), 'source': source_file})

    return procedures


def _read_markdown_files(data_dir: str) -> list[dict]:
    """Lee todos los archivos .md de un directorio (recursivo) y extrae procedimientos."""
    all_procedures = []

    if not os.path.isdir(data_dir):
        return []

    for root, _dirs, files in os.walk(data_dir):
        for filename in sorted(files):
            if not filename.lower().endswith('.md'):
                continue
            filepath = os.path.join(root, filename)
            try:
                # Intentar múltiples encodings (exports Notion pueden variar)
                text = None
                for enc in ('utf-8', 'utf-8-sig', 'latin-1', 'cp1252'):
                    try:
                        with open(filepath, 'r', encoding=enc, errors='ignore') as f:
                            text = f.read()
                        break
                    except Exception:
                        continue
                if text is None:
                    continue
            except Exception:
                continue

            # Limpiar caracteres problemáticos
            text = ''.join(c for c in text if ord(c) < 0xD800 or ord(c) > 0xDFFF)
            # Eliminar referencias a imágenes locales (no aportan al texto)
            text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
            text = text.strip()

            if not text or len(text) < 30:
                continue

            clean_name = _clean_notion_title(filename)
            procedures = _split_markdown_into_procedures(text, clean_name or filename)
            all_procedures.extend(procedures)

    return all_procedures


def _deduplicate(procedures: list[dict]) -> list[dict]:
    """Elimina procedimientos duplicados basándose en el título normalizado."""
    seen = {}
    unique = []
    for p in procedures:
        # Normalizar título para comparación
        key = re.sub(r'\s+', ' ', p['title'].lower().strip())
        if key in seen:
            # Mantener el que tenga más contenido
            existing = seen[key]
            if len(p.get('content', '')) > len(existing.get('content', '')):
                unique[unique.index(existing)] = p
                seen[key] = p
        else:
            seen[key] = p
            unique.append(p)
    return unique


@st.cache_resource(show_spinner="Cargando procedimientos desde archivos Markdown…")
def load_knowledge_base():
    """
    Carga todos los procedimientos de archivos .md en notion_export/
    y construye el índice BM25 para búsqueda rápida.
    """
    procedures = _read_markdown_files(DATA_DIR)

    if not procedures:
        return None

    # Eliminar duplicados (Notion exporta archivos repetidos en distintas carpetas)
    procedures = _deduplicate(procedures)

    # Preparar textos formateados para el prompt
    for p in procedures:
        p['text'] = f"## {p['title']}\n{p['content']}"

    # Construir índice BM25
    tokenized = [_normalize(f"{p['title']} {p['content']}") for p in procedures]
    # Filtrar procedimientos con tokens vacíos
    valid = [(p, t) for p, t in zip(procedures, tokenized) if t]
    if not valid:
        return None
    procedures, tokenized = zip(*valid)
    procedures = list(procedures)
    tokenized = list(tokenized)

    bm25 = BM25Okapi(tokenized)
    return procedures, bm25


def retrieve(query: str, kb, top_k: int = 6) -> list[dict]:
    """Recupera los procedimientos más relevantes para la consulta usando BM25."""
    if kb is None:
        return []
    procedures, bm25 = kb
    tokens = _normalize(query)
    if not tokens:
        return []
    scores = bm25.get_scores(tokens)
    ranked = sorted(range(len(scores)), key=lambda i: -scores[i])
    return [procedures[i] for i in ranked[:top_k] if scores[i] > 0.0]


# ─────────────────────────────────────────────
# GUÍA ESTÁTICA (fallback)
# ─────────────────────────────────────────────
CS_GUIDE_FALLBACK = """
PROCESOS - Cómo y a quién escalar tickets/consultas
1. Duda/consulta proyecto/subvención/ordenador → Ticket Pipeline CS TEAM LEADS
2. Incidencias PC (entregado o posterior a Listo para enviar) → Ticket Pipeline INCIDENCIAS PC
3. Fallos operativos Intercom/HubSpot → Slack directo al TL
4. Solicitud/modificación facturas → Ticket Pipeline FINANCES

Team Leads - Proceso abrir ticket:
1. Abrir proyecto en HubSpot → Agregar ticket → Pipeline CS TEAM LEADS
2. Título claro, categoría, motivo detallado en nota
3. Asociar a Empresa, Negocio, Contacto y Project
4. TL como propietario

Finance - Motivos: solicitud factura, modificación datos, devolución IGIC, incidencia transportista, cliente pendiente cobro
Legal - PDC y/o reintegros: abrir ticket, adjuntar notificación, NO derivar a inbox Intercom

TRAMITACIÓN - Motivos: Crear/Oficializar acuerdo, Presentar subvención/subsanación, Firma acuerdos/memorias, Cambios PC, Desistir(TL), Renunciar bono(TL)
Plazos: Bono caduca 6 meses, Factura 3 meses desde oficialización, 1ª memoria 6 meses, 2ª memoria 15 meses

ORDENADORES - Stages: BACKLOG → PDTE DATOS → POR OFICIALIZAR → PDTE COBRO → LISTO PARA ENVIAR → PEDIDO REALIZADO → EN TRÁNSITO → ENTREGADO → MEMORIA 1 → MEMORIA 2
Entregas: Península 15-20 días, Baleares 18-22, Canarias 25-30

Si la información no cubre tu caso, consulta al Team Lead.
"""


def build_system_prompt(retrieved: list[dict]) -> str:
    """Construye el system prompt con los procedimientos relevantes recuperados."""
    if retrieved:
        context = "\n\n---\n\n".join(p['text'] for p in retrieved)
        source_note = f"(Mostrando {len(retrieved)} procedimiento(s) relevante(s) de {', '.join(set(p.get('source', '?') for p in retrieved))})"
    else:
        context = CS_GUIDE_FALLBACK
        source_note = "(Usando guía local de referencia)"

    return f"""Eres el Asistente IA del equipo de Customer Success de Orbidi, especializado en el programa Kit Digital.
Tu función es ayudar a los agentes de CS a:
- Conocer el procedimiento exacto para cualquier situación
- Saber a qué equipo escalar un ticket y cómo hacerlo
- Entender los estados y plazos del Kit Digital
- Resolver dudas sobre ordenadores, memorias, subvenciones, facturas y herramientas internas

REGLAS DE RESPUESTA:
1. Sé concreto y directo. Da pasos numerados cuando sea un proceso.
2. Si la pregunta implica escalar un ticket, indica exactamente: A QUIÉN, CÓMO y QUÉ incluir.
3. Si hay plazos importantes, resáltalos claramente.
4. Si la información no está en los procedimientos proporcionados, dilo claramente y sugiere consultar al TL.
5. Usa ÚNICAMENTE el contenido de los procedimientos de abajo como fuente de verdad. No inventes información.
6. Responde siempre en español.
7. Cita el nombre del procedimiento o sección cuando sea útil para que el agente lo localice.

{source_note}

PROCEDIMIENTOS RELEVANTES:
---
{context}
---
Responde basándote EXCLUSIVAMENTE en los procedimientos anteriores. Si la pregunta no se puede responder con ellos, indícalo."""


# ─────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Orbidi IA Agent",
    page_icon="⚡",
    layout="wide",
)
st.markdown("""
<style>
.stApp { background-color: #ffffff; }
[data-testid="stHeader"] { background-color: #ffffff; }
.orbidi-header {
    display: flex; align-items: center; gap: 14px;
    padding: 28px 0 8px 0;
    border-bottom: 2px solid #f0f0f0;
    margin-bottom: 24px;
}
.orbidi-logo {
    width: 44px; height: 44px;
    background: linear-gradient(135deg, #6C3CE1 0%, #9B6DFF 100%);
    border-radius: 12px; display: flex; align-items: center;
    justify-content: center; font-size: 22px;
    box-shadow: 0 4px 14px rgba(108,60,225,0.25);
}
.orbidi-title {
    font-size: 26px; font-weight: 700; color: #1a1a2e;
    margin: 0; letter-spacing: -0.5px;
}
.orbidi-subtitle { font-size: 13px; color: #8a8a9a; margin: 2px 0 0 0; }
.badge {
    display: inline-block; background: #f0ebff; color: #6C3CE1;
    font-size: 11px; font-weight: 600; padding: 3px 10px;
    border-radius: 20px; margin-left: 8px; vertical-align: middle;
}
.notion-badge {
    display: inline-block; background: #e8f5e9; color: #2e7d32;
    font-size: 11px; font-weight: 600; padding: 3px 10px;
    border-radius: 20px; margin-left: 4px; vertical-align: middle;
}
[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] span, [data-testid="stChatMessage"] div:not([class]) {
    color: #1a1a2e !important;
}
[data-testid="stChatMessage"] * { color: #1a1a2e !important; }
[data-testid="stChatMessage"] {
    background: #fafafa; border-radius: 14px; color: #1a1a2e !important;
    padding: 4px 8px; margin-bottom: 6px; border: 1px solid #f0f0f0;
}
[data-testid="stChatInput"] textarea {
    border-radius: 14px !important; border: 1.5px solid #e8e8f0 !important;
    background: #fafafa !important; font-size: 15px !important; color: #1a1a2e !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: #6C3CE1 !important;
    box-shadow: 0 0 0 3px rgba(108,60,225,0.1) !important;
}
.stButton > button {
    border-radius: 10px !important; border: 1.5px solid #e8e8f0 !important;
    color: #6C3CE1 !important; background: #fafafa !important;
    font-size: 13px !important; font-weight: 500 !important;
    padding: 4px 16px !important; transition: all 0.2s !important;
}
.stButton > button:hover {
    background: #f0ebff !important; border-color: #6C3CE1 !important;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# INICIALIZACIÓN
# ─────────────────────────────────────────────
@st.cache_resource
def get_groq_client():
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

groq_client = get_groq_client()
kb = load_knowledge_base()
using_kb = kb is not None
proc_count = len(kb[0]) if using_kb else 0
all_procedures = kb[0] if using_kb else []

# ─────────────────────────────────────────────
# SIDEBAR: LISTADO COMPLETO DE PROCEDIMIENTOS
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="padding: 8px 0 16px 0; border-bottom: 1px solid #eee; margin-bottom: 16px;">
        <p style="font-size: 18px; font-weight: 700; color: #1a1a2e; margin: 0;">
            Base de Conocimiento
        </p>
        <p style="font-size: 13px; color: #888; margin: 4px 0 0 0;">
            {proc_count} procedimientos cargados
        </p>
    </div>
    """, unsafe_allow_html=True)

    if all_procedures:
        # Buscador de procedimientos
        search_filter = st.text_input(
            "Buscar procedimiento",
            placeholder="Escribe para filtrar...",
            label_visibility="collapsed",
        )

        # Agrupar por source (archivo de origen)
        from collections import defaultdict
        groups = defaultdict(list)
        for i, proc in enumerate(all_procedures):
            groups[proc.get('source', 'Sin categoría')].append((i, proc))

        # Filtrar si hay búsqueda
        filter_lower = search_filter.lower().strip() if search_filter else ""

        shown = 0
        for source, procs in sorted(groups.items()):
            filtered = [
                (i, p) for i, p in procs
                if not filter_lower or filter_lower in p['title'].lower() or filter_lower in p.get('content', '').lower()
            ]
            if not filtered:
                continue

            with st.expander(f"📁 {source} ({len(filtered)})", expanded=bool(filter_lower)):
                for idx, proc in filtered:
                    title = proc['title'][:70]
                    preview = proc.get('content', '')[:100].replace('\n', ' ')
                    if st.button(f"📄 {title}", key=f"proc_{idx}", use_container_width=True):
                        st.session_state['selected_proc'] = idx
                    shown += 1

        if filter_lower and shown == 0:
            st.info("No se encontraron procedimientos con ese filtro.")

        # Mostrar procedimiento seleccionado
        if 'selected_proc' in st.session_state:
            sel = st.session_state['selected_proc']
            if 0 <= sel < len(all_procedures):
                st.markdown("---")
                proc = all_procedures[sel]
                st.markdown(f"### {proc['title']}")
                st.markdown(proc.get('content', ''), unsafe_allow_html=False)
    else:
        st.warning("No se encontraron archivos .md en `notion_export/`")
        st.markdown("""
        **Para conectar tu guía de Notion:**
        1. Exporta desde Notion como Markdown
        2. Coloca los archivos `.md` en la carpeta `notion_export/`
        3. Reinicia la app
        """)

# ─────────────────────────────────────────────
# CONTENIDO PRINCIPAL
# ─────────────────────────────────────────────

# Header
kb_badge = f'<span class="notion-badge">✓ {proc_count} procedimientos</span>' if using_kb else ''
st.markdown(f"""
<div class="orbidi-header">
    <div class="orbidi-logo">⚡</div>
    <div>
        <p class="orbidi-title">Orbidi IA Agent <span class="badge">CS · Kit Digital</span>{kb_badge}</p>
        <p class="orbidi-subtitle">Tu asistente de procesos internos · Customer Success</p>
    </div>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

col1, col2 = st.columns([5, 1])
with col2:
    if st.session_state.messages:
        if st.button("↺ Limpiar"):
            st.session_state.messages = []
            st.rerun()

if not st.session_state.messages:
    label = f"{proc_count} procedimientos cargados" if using_kb else "guía local (coloca archivos .md en notion_export/)"
    st.markdown(f"""
    <div style="text-align:center; padding: 48px 0 32px 0;">
        <div style="font-size: 40px; margin-bottom: 12px;">💬</div>
        <p style="font-size:16px; font-weight:600; color:#555; margin:0;">¿En qué puedo ayudarte hoy?</p>
        <p style="font-size:13px; color:#aaa; margin-top:6px;">Pregúntame sobre tickets, plazos, memorias, ordenadores o cualquier proceso CS.</p>
        <p style="font-size:11px; color:#bbb; margin-top:4px;">Base de conocimiento: {label}</p>
    </div>
    """, unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ─────────────────────────────────────────────
# BUCLE DE CHAT CON RAG
# ─────────────────────────────────────────────
if prompt := st.chat_input("Escribe tu pregunta sobre procesos CS..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # RAG: recuperar procedimientos relevantes
    retrieved = retrieve(prompt, kb, top_k=8)
    system_prompt = build_system_prompt(retrieved)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        stream = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=2048,
            messages=[
                {"role": "system", "content": system_prompt},
                *[m for m in st.session_state.messages if m["role"] != "system"],
            ],
            stream=True,
        )
        for chunk in stream:
            text = chunk.choices[0].delta.content or ""
            full_response += text
            placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)

    # Mostrar qué procedimientos se usaron para la respuesta
    if retrieved:
        with st.expander(f"📚 Procedimientos consultados ({len(retrieved)})", expanded=False):
            for r in retrieved:
                st.markdown(f"- **{r['title']}** _{r.get('source', '')}_")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
