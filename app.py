"""
Asistente IA de Customer Success - Orbidi
Conectado directamente a Notion (API) para respuestas siempre actualizadas.
RAG con 102 procedimientos definidos y organizados por categoría.
"""
import os
import re
import time
import unicodedata
import streamlit as st
from groq import Groq
from rank_bm25 import BM25Okapi
from procedures_config import PROCEDURES_CONFIG

# ─────────────────────────────────────────────
# PÁGINAS NOTION A INDEXAR
# Añade aquí los IDs de las páginas clave de tu workspace
# ─────────────────────────────────────────────
NOTION_KEY_PAGES = [
    ("224f25573a1e80809556ea9e17f178a0", "Guía Customer Success"),
    ("2c9f25573a1e809ba48bf31a7e96d733", "Escalamiento Squad Titan"),
    ("11bf25573a1e80d5b81cf66d57459fe0", "BAJAS"),
    ("201f25573a1e80feac62c49fe91b6f01", "Gestión Tickets PROD"),
    ("2c5f25573a1e8056a41ff135e54d7e38", "Rechazo de Memoria"),
    ("230f25573a1e80678475c33f8f69502f", "Tipologías Bloqueos"),
    ("14af25573a1e80038b3fecb8cdd36544", "Ordenadores"),
    ("190f25573a1e80e39118d01a19b22565", "Tramitación FAQ"),
    ("2a4f25573a1e805ca2e1cd4b88da0b40", "Tramitación Equipo Front"),
    ("2edf25573a1e810d847cee790d067a2f", "Ratificaciones de Memoria"),
    ("2f5f25573a1e8002865ee9af250e77bb", "Gestión Bajas con Memoria Cobrada"),
]

# Fallback: directorio local con archivos .md
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
    text = text.lower()
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    text = re.sub(r'[^\w\s]', ' ', text)
    return [t for t in text.split() if t not in SPANISH_STOPWORDS and len(t) > 1]


# ─────────────────────────────────────────────
# NOTION API: EXTRACCIÓN DE BLOQUES
# ─────────────────────────────────────────────

def _rich_text_to_str(rich_text: list) -> str:
    return ''.join(rt.get('plain_text', '') for rt in rich_text)


def _block_to_line(block: dict, depth: int = 0) -> str:
    bt = block.get('type', '')
    data = block.get(bt, {})
    text = _rich_text_to_str(data.get('rich_text', []))
    indent = '  ' * depth

    if bt == 'heading_1':
        return f"# {text}"
    if bt == 'heading_2':
        return f"## {text}"
    if bt == 'heading_3':
        return f"### {text}"
    if bt == 'bulleted_list_item':
        return f"{indent}- {text}"
    if bt == 'numbered_list_item':
        return f"{indent}{text}"
    if bt == 'to_do':
        checked = '✓' if data.get('checked') else '•'
        return f"{indent}{checked} {text}"
    if bt in ('callout', 'quote'):
        return f"{indent}> {text}"
    if bt == 'divider':
        return "---"
    if bt == 'table_row':
        cells = data.get('cells', [])
        row = ' | '.join(_rich_text_to_str(cell) for cell in cells)
        return f"| {row} |"
    if bt == 'column_list':
        return ''
    if text:
        return f"{indent}{text}"
    return ''


def _fetch_blocks(notion, block_id: str, depth: int = 0, max_depth: int = 4) -> list[str]:
    """Fetches all blocks from a Notion block recursively (depth-limited)."""
    if depth > max_depth:
        return []

    lines = []
    cursor = None
    while True:
        try:
            resp = notion.blocks.children.list(
                block_id=block_id,
                start_cursor=cursor,
                page_size=100,
            )
        except Exception:
            time.sleep(0.5)
            break

        for block in resp.get('results', []):
            bt = block.get('type', '')
            # Skip child pages/databases (fetch separately if needed)
            if bt in ('child_page', 'child_database', 'unsupported'):
                continue

            line = _block_to_line(block, depth)
            if line:
                lines.append(line)

            if block.get('has_children'):
                children = _fetch_blocks(notion, block['id'], depth + 1, max_depth)
                lines.extend(children)

        if not resp.get('has_more'):
            break
        cursor = resp.get('next_cursor')
        time.sleep(0.1)  # respeta rate limit de Notion

    return lines


def _fetch_notion_page(notion, page_id: str, page_title: str) -> list[dict]:
    """Fetches a Notion page and returns it as a list of procedures."""
    try:
        lines = _fetch_blocks(notion, page_id)
    except Exception as e:
        return []

    if not lines:
        return []

    text = '\n'.join(lines)
    # Reutilizar la lógica de splitting
    return _split_markdown_into_procedures(text, page_title)


# ─────────────────────────────────────────────
# PARSING DE MARKDOWN EN PROCEDIMIENTOS
# ─────────────────────────────────────────────

def _clean_notion_title(filename: str) -> str:
    name = os.path.splitext(filename)[0]
    name = re.sub(r'\s+[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', '', name)
    name = re.sub(r'\s+[0-9a-f]{32}$', '', name)
    return name.strip()


def _extract_title_from_content(text: str) -> str:
    for line in text.splitlines()[:10]:
        line = line.strip()
        if line.startswith('# ') and not line.startswith('## '):
            return line[2:].strip()
    return ''


def _split_markdown_into_procedures(text: str, source_file: str) -> list[dict]:
    """Divide markdown en procedimientos individuales."""
    procedures = []
    h1_count = len(re.findall(r'^# [^#]', text, re.MULTILINE))
    h2_count = len(re.findall(r'^## [^#]', text, re.MULTILINE))
    h3_count = len(re.findall(r'^### [^#]', text, re.MULTILINE))

    if h2_count >= 2:
        h2_splits = re.split(r'\n(?=## [^#])', text)
        for section in h2_splits:
            section = section.strip()
            if not section or len(section) < 20:
                continue
            first_line = section.splitlines()[0].strip()
            if first_line.startswith('# ') and not first_line.startswith('## '):
                title = first_line[2:].strip()
                content_lines = [l for l in section.splitlines()[1:] if l.strip()]
                if len(content_lines) > 2:
                    procedures.append({'title': f"Introducción: {title}", 'content': section, 'source': source_file})
                continue
            if first_line.startswith('## '):
                title = first_line[3:].strip()
                title = re.sub(r'\*\*([^*]+)\*\*', r'\1', title).strip()
            else:
                title = first_line[:80]
            content_lines = [l for l in section.splitlines()[1:] if l.strip()]
            real_content = [l for l in content_lines if not re.match(r'^\[.*\]\(.*\.md\)$', l.strip())]
            if len(real_content) < 2:
                continue
            procedures.append({'title': title, 'content': section, 'source': source_file})

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

    else:
        title = _extract_title_from_content(text) or source_file
        if title and len(text.strip()) > 20:
            procedures.append({'title': title, 'content': text.strip(), 'source': source_file})

    return procedures


# ─────────────────────────────────────────────
# FALLBACK: LEER ARCHIVOS .MD LOCALES
# ─────────────────────────────────────────────

def _read_markdown_files(data_dir: str) -> list[dict]:
    all_procedures = []
    if not os.path.isdir(data_dir):
        return []
    for root, _dirs, files in os.walk(data_dir):
        for filename in sorted(files):
            if not filename.lower().endswith('.md'):
                continue
            filepath = os.path.join(root, filename)
            try:
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
            text = ''.join(c for c in text if ord(c) < 0xD800 or ord(c) > 0xDFFF)
            text = re.sub(r'!\[.*?\]\(.*?\)', '', text).strip()
            if not text or len(text) < 30:
                continue
            clean_name = _clean_notion_title(filename)
            all_procedures.extend(_split_markdown_into_procedures(text, clean_name or filename))
    return all_procedures


def _deduplicate(procedures: list[dict]) -> list[dict]:
    seen = {}
    unique = []
    for p in procedures:
        key = re.sub(r'\s+', ' ', p['title'].lower().strip())
        if key in seen:
            existing = seen[key]
            if len(p.get('content', '')) > len(existing.get('content', '')):
                idx = unique.index(existing)
                unique[idx] = p
                seen[key] = p
        else:
            seen[key] = p
            unique.append(p)
    return unique


# ─────────────────────────────────────────────
# CARGA PRINCIPAL DEL KNOWLEDGE BASE
# ─────────────────────────────────────────────

@st.cache_resource(ttl=3600, show_spinner=False)
def load_knowledge_base():
    """
    Carga procedimientos desde Notion API (si hay token) o archivos .md locales.
    Se refresca automáticamente cada hora.
    """
    procedures = []
    source = "local"

    notion_token = st.secrets.get("NOTION_TOKEN", "")

    if notion_token:
        # ── Carga desde Notion API ──────────────────────────
        try:
            from notion_client import Client as NotionClient
            notion = NotionClient(auth=notion_token)
            source = "notion"

            progress = st.progress(0, text="Conectando con Notion…")
            total = len(NOTION_KEY_PAGES)

            for i, (page_id, title) in enumerate(NOTION_KEY_PAGES):
                progress.progress((i + 1) / total, text=f"Cargando: {title}…")
                procs = _fetch_notion_page(notion, page_id, title)
                procedures.extend(procs)
                time.sleep(0.3)  # evitar rate limiting

            progress.empty()

        except ImportError:
            st.warning("Instala notion-client: `pip install notion-client`")
            source = "local"
        except Exception as e:
            st.warning(f"Error conectando con Notion: {e}. Usando archivos locales.")
            source = "local"

    if source == "local" or not procedures:
        # ── Fallback: archivos .md locales ─────────────────
        procedures = _read_markdown_files(DATA_DIR)

    if not procedures:
        return None

    procedures = _deduplicate(procedures)

    # Enriquecer con keywords y categorías de procedures_config
    config_by_title = {c['title'].lower(): c for c in PROCEDURES_CONFIG}
    for p in procedures:
        p['text'] = f"## {p['title']}\n{p['content']}"
        title_lower = p['title'].lower()
        cfg = config_by_title.get(title_lower)
        if not cfg:
            # Match parcial si no hay match exacto
            for cfg_title, cfg_data in config_by_title.items():
                if cfg_title in title_lower or title_lower in cfg_title:
                    cfg = cfg_data
                    break
        if cfg:
            p['category'] = cfg.get('category', p.get('source', ''))
            p['keywords'] = cfg.get('keywords', [])
        else:
            p['category'] = p.get('source', '')
            p['keywords'] = []

    # BM25: título + keywords definidos + categoría + contenido
    tokenized = [
        _normalize(
            f"{p['title']} "
            f"{' '.join(p.get('keywords', []))} "
            f"{p.get('category', '')} "
            f"{p['content']}"
        )
        for p in procedures
    ]
    valid = [(p, t) for p, t in zip(procedures, tokenized) if t]
    if not valid:
        return None

    procedures, tokenized = zip(*valid)
    procedures = list(procedures)
    tokenized = list(tokenized)

    bm25 = BM25Okapi(tokenized)
    return procedures, bm25, source


def retrieve(query: str, kb, top_k: int = 8) -> list[dict]:
    """Recupera los procedimientos más relevantes usando BM25."""
    if kb is None:
        return []
    procedures, bm25, _ = kb
    tokens = _normalize(query)
    if not tokens:
        return []
    scores = bm25.get_scores(tokens)
    ranked = sorted(range(len(scores)), key=lambda i: -scores[i])
    return [procedures[i] for i in ranked[:top_k] if scores[i] > 0.0]


# ─────────────────────────────────────────────
# SYSTEM PROMPT
# ─────────────────────────────────────────────

CS_GUIDE_FALLBACK = """
PROCESOS - Cómo y a quién escalar tickets/consultas:
1. Duda sobre proyecto/subvención/ordenador → Ticket HubSpot Pipeline: CS TEAM LEADS
2. Incidencias PC (entregado o posterior) → Ticket HubSpot Pipeline: INCIDENCIAS PC
3. Fallos Intercom/HubSpot → Slack directo al TL
4. Solicitud/modificación facturas → Ticket HubSpot Pipeline: FINANCES
Plazos Kit Digital: Bono caduca 6 meses, Factura 3 meses, 1ª Memoria 6 meses, 2ª Memoria 15 meses.
"""


def build_system_prompt(retrieved: list[dict]) -> str:
    if retrieved:
        context = "\n\n---\n\n".join(p['text'] for p in retrieved)
        source_note = f"(Fuente: {len(retrieved)} procedimiento(s) de Notion)"
    else:
        context = CS_GUIDE_FALLBACK
        source_note = "(Fuente: guía básica de referencia)"

    return f"""Eres el Asistente IA del equipo de Customer Success de Orbidi (Kit Digital).
Ayudas a los agentes CS a resolver cualquier situación con respuestas concretas y exactas.

REGLAS:
1. Responde SIEMPRE en español.
2. Usa SOLO la información de los procedimientos de abajo. Si no está ahí, dilo claramente.
3. Da pasos numerados cuando sea un proceso.
4. Si hay que escalar, indica exactamente: A QUIÉN, CÓMO y QUÉ incluir en el ticket.
5. Resalta plazos importantes.
6. Cita el nombre del procedimiento cuando sea útil.

{source_note}

PROCEDIMIENTOS RELEVANTES:
---
{context}
---

Responde basándote EXCLUSIVAMENTE en los procedimientos anteriores."""


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
.orbidi-title { font-size: 26px; font-weight: 700; color: #1a1a2e; margin: 0; letter-spacing: -0.5px; }
.orbidi-subtitle { font-size: 13px; color: #8a8a9a; margin: 2px 0 0 0; }
.badge { display: inline-block; background: #f0ebff; color: #6C3CE1; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; margin-left: 8px; vertical-align: middle; }
.notion-badge { display: inline-block; background: #e8f5e9; color: #2e7d32; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; margin-left: 4px; vertical-align: middle; }
.local-badge { display: inline-block; background: #fff3e0; color: #e65100; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; margin-left: 4px; vertical-align: middle; }
[data-testid="stChatMessage"] * { color: #1a1a2e !important; }
[data-testid="stChatMessage"] { background: #fafafa; border-radius: 14px; color: #1a1a2e !important; padding: 4px 8px; margin-bottom: 6px; border: 1px solid #f0f0f0; }
[data-testid="stChatInput"] textarea { border-radius: 14px !important; border: 1.5px solid #e8e8f0 !important; background: #fafafa !important; font-size: 15px !important; color: #1a1a2e !important; }
[data-testid="stChatInput"] textarea:focus { border-color: #6C3CE1 !important; box-shadow: 0 0 0 3px rgba(108,60,225,0.1) !important; }
.stButton > button { border-radius: 10px !important; border: 1.5px solid #e8e8f0 !important; color: #6C3CE1 !important; background: #fafafa !important; font-size: 13px !important; font-weight: 500 !important; padding: 4px 16px !important; }
.stButton > button:hover { background: #f0ebff !important; border-color: #6C3CE1 !important; }
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
kb_source = kb[2] if using_kb else "none"

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    source_label = "Notion API ✓" if kb_source == "notion" else "Archivos locales"
    source_color = "#2e7d32" if kb_source == "notion" else "#e65100"
    st.markdown(f"""
    <div style="padding: 8px 0 16px 0; border-bottom: 1px solid #eee; margin-bottom: 16px;">
        <p style="font-size: 18px; font-weight: 700; color: #1a1a2e; margin: 0;">Base de Conocimiento</p>
        <p style="font-size: 13px; color: {source_color}; margin: 4px 0 2px 0; font-weight: 600;">{source_label}</p>
        <p style="font-size: 13px; color: #888; margin: 0;">{proc_count} procedimientos cargados</p>
    </div>
    """, unsafe_allow_html=True)

    # Botón de refresh
    if st.button("🔄 Refrescar desde Notion", use_container_width=True):
        st.cache_resource.clear()
        st.rerun()

    st.markdown("---")

    if all_procedures:
        search_filter = st.text_input("Buscar procedimiento", placeholder="Escribe para filtrar…", label_visibility="collapsed")

        from collections import defaultdict
        groups = defaultdict(list)
        for i, proc in enumerate(all_procedures):
            groups[proc.get('source', 'Sin categoría')].append((i, proc))

        filter_lower = search_filter.lower().strip() if search_filter else ""

        for source, procs in sorted(groups.items()):
            filtered = [
                (i, p) for i, p in procs
                if not filter_lower or filter_lower in p['title'].lower() or filter_lower in p.get('content', '').lower()
            ]
            if not filtered:
                continue
            with st.expander(f"📁 {source} ({len(filtered)})", expanded=bool(filter_lower)):
                for idx, proc in filtered:
                    if st.button(f"📄 {proc['title'][:65]}", key=f"proc_{idx}", use_container_width=True):
                        st.session_state['selected_proc'] = idx

        if 'selected_proc' in st.session_state:
            sel = st.session_state['selected_proc']
            if 0 <= sel < len(all_procedures):
                st.markdown("---")
                proc = all_procedures[sel]
                st.markdown(f"### {proc['title']}")
                st.markdown(proc.get('content', ''))
    else:
        st.error("No se cargaron procedimientos.")
        st.markdown("""
        **Para conectar con Notion:**
        1. Ve a [notion.so/my-integrations](https://www.notion.so/my-integrations)
        2. Crea una integración interna
        3. Copia el token
        4. Añádelo en `.streamlit/secrets.toml`:
        ```
        NOTION_TOKEN = "secret_..."
        GROQ_API_KEY = "..."
        ```
        5. Comparte las páginas con la integración
        """)

# ─────────────────────────────────────────────
# HEADER PRINCIPAL
# ─────────────────────────────────────────────
if kb_source == "notion":
    badge = f'<span class="notion-badge">✓ Notion · {proc_count} procedimientos</span>'
elif using_kb:
    badge = f'<span class="local-badge">⚠ Archivos locales · {proc_count} procedimientos</span>'
else:
    badge = '<span class="local-badge">⚠ Sin datos</span>'

st.markdown(f"""
<div class="orbidi-header">
    <div class="orbidi-logo">⚡</div>
    <div>
        <p class="orbidi-title">Orbidi IA Agent <span class="badge">CS · Kit Digital</span>{badge}</p>
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
    st.markdown(f"""
    <div style="text-align:center; padding: 48px 0 32px 0;">
        <div style="font-size: 40px; margin-bottom: 12px;">💬</div>
        <p style="font-size:16px; font-weight:600; color:#555; margin:0;">¿En qué puedo ayudarte hoy?</p>
        <p style="font-size:13px; color:#aaa; margin-top:6px;">Pregúntame sobre tickets, plazos, memorias, ordenadores, bajas o cualquier proceso CS.</p>
    </div>
    """, unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ─────────────────────────────────────────────
# CHAT CON RAG
# ─────────────────────────────────────────────
if prompt := st.chat_input("Escribe tu pregunta sobre procesos CS…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

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

    if retrieved:
        with st.expander(f"📚 Procedimientos consultados ({len(retrieved)})", expanded=False):
            for r in retrieved:
                cat = r.get('category', r.get('source', ''))
                st.markdown(f"- **{r['title']}** — `{cat}`")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
