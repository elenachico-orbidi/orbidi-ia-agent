"""
Asistente IA de Customer Success - Orbidi
Interfaz web tipo ChatGPT con Streamlit
"""
import streamlit as st
from groq import Groq

CS_GUIDE = """
PROCESOS
Cómo y a quién escalar tickets/consultas
Desde el área de CS, tenemos diferentes vías para reportar consultas, incidencias, o tickets a otras áreas:
1. Cualquier duda o consulta relacionada con el proyecto, la subvención o el ordenador >>>Ticket en Hubspot en el Pipeline: CS TEAM LEADS (ver proceso en apartado CS Team Leads)
2. Incidencias con el ordenador una vez entregado o en un stage posterior a Listo para enviar >>> Ticket en Hubspot en el Pipeline: INCIDENCIAS PC (ver proceso en apartado Ordenadores/Logística)
3. Fallos o incidencias operativas en Intercom/Huspot (problemas SLA, comunicaciones erróneas, campos que no sincronizan... < por slack directamente al TL
4. Solicitudes de facturas, modificaciones de datos en facturas (sin memoria presentada) >>> Ticket en Hubspot en el Pipeline: FINANCES
Team Leads
El proceso para abrir un ticket a tu TL:
1. Abrir el proyecto en Hubspot
2. Pinchar en "Agregar ticket" en el lado derecho de la pantalla
3. Seleccionar pipeline "CS TEAM LEADS"
4. Añadir el título del ticket > Debe ser claro y conciso
5. Seleccionar la categoría correspondiente
6. Añadir el motivo y la mayor información posible en la nota
7. Asociar el ticket a la Empresa, Negocio, Contacto y Project
8. Poner al TL como propietario del ticket
El TL puede Resolverlo o Bloquearlo.
* Si resuelve > marca Resuelto > CS lo cierra tras contactar al cliente
* Si bloquea > marca Bloqueado > CS lo revisa y desbloquea
Ordenadores/Logística
El proceso para abrir un ticket al equipo de Logística/PCs:
1. En el objeto KD-PC, selecciona Agregar Ticket en la parte derecha
2. Nombre del ticket: motivo resumido (si es baja: BAJA PC + motivo)
3. Pipeline: Incidencias PC
4. Motivo del ticket: del desplegable
5. Propietario: sin propietario
6. Asociar a todos los objetos del cliente
7. Dejar nota con toda la información
Finance
Motivos para abrir tickets:
1. Solicitud de factura
2. Modificación de datos en factura
3. Solicitud devolución de importe (IGIC/pago extra)
4. Incidencia cuando transportista cobra indebidamente
5. Cliente Pendiente de Cobro que ya pagó por transferencia
Flujo:
1. Ir al enlace del cliente en HubSpot
2. En tickets, dar click en Agregar
3. Completar: Nombre, Pipeline: Finance, Propietario: Sin propietario, Categoría, Creador
4. Asociar a objetos correspondientes > Crear
Legal
Notificaciones pérdida de derecho a cobro y/o reintegro:
1. Abrir ticket a Legal en Hubspot
2. Categoría: PDC y/o reintegros
3. Título: notificación cliente
4. Propietario: sin propietario
5. Asociar con todos los objetos
6. Adjuntar la notificación en una nota
IMPORTANTE: NO derivar la conversación a ningún inbox de intercom.
Bajas de ordenadores (Pipeline stages PCs):
- Anterior a Listo para enviar: marcar estado Baja
- Entregado: escalar al team lead
- Listo para enviar: marcar Estado baja y abrir ticket a Logística
- En tránsito o Pedido realizado: abrir ticket a logística antes de confirmar la baja
TRAMITACIÓN
NO se abren tickets de BAJAS ni de consulta o dudas.
Motivos disponibles:
* Crear Acuerdo
* Oficializar acuerdo
* Presentar Subvención
* Presentar o confirmar una Subsanación
* Ayuda con la firma de acuerdos o memorias
* Cambios de PC
* Desistir Acuerdo (TL)
* Renunciar al bono (TL)
Proceso para abrir ticket a Tramitación:
1. Abrir el proyecto en Hubspot
2. Pinchar en "Agregar ticket"
3. Seleccionar pipeline "TRAMITACIÓN"
4. Añadir título del ticket
5. Añadir motivo e información en la nota
6. Poner sin propietario
7. Asociar a Empresa, Negocio, Project y Contacto
Plazos KD:
- Caducidad Bono / Oficialización Acuerdo: 6 meses desde aprobación
- Creación de la factura: 3 meses desde oficialización
- Presentación 1ª memoria: 6 meses desde oficialización
- Presentación 2ª memoria: 15 meses desde inicio prestación de servicio
FASES:
1. Solicitud y OCP - Firma OCP con cliente
2. Resolución de concesión del bono - Red.es aprueba
3. Firma del acuerdo (oficialización) - 6 meses para firmar
4. Ejecución y primera memoria - 3 meses ejecutar, 6 meses para memoria 1
5. Periodo de mantenimiento - Hasta aceptación segunda memoria (12-15 meses)
6. Segunda memoria - 15 meses desde emisión de factura
Bloqueos en Oficialización:
- Pendiente aceptación BENEFICIARIO: cliente no ha firmado
- Bono no encontrado: no aprobado o DNI/CIF incorrecto
- Bono caducado: plazo 6 meses vencido
- Ya existe un acuerdo: ya hay uno oficializado para ese producto
- Sin NIF: error de ventas
- Importe consumido: bono ya gastado
- Bono renunciado: cliente renunció
- Sin PC elegido: cliente no confirmó modelo PC
- Sin criterio facturación: falta código postal en Empresa
Bonos Caducados:
- No se puede reactivar ni prorrogar
- Única opción: nueva solicitud de cero
- Cliente debe renunciar al bono primero
Memorias - Estados en HubSpot:
- EN PROD: memoria en producción
- PRES. MEM. 1: memoria lista para presentar al cliente
- MEM 1 PRESENTADA: cliente firmó y se presentó
- MEMORIA 1 COBRADA: Gobierno pagó la primera memoria
Si cliente no está de acuerdo con la memoria:
1. CS indica al cliente que rechace en portal gestión
2. CS pregunta qué quiere modificar
3. Confirmado el rechazo, CS abre ticket a PO en hubspot
4. PO deriva a tramitación para actualizar la memoria
Errores frecuentes en firmas de memorias:
- Errores del portal: probar en incógnito y con otro navegador
- Error certificado digital: instalar autofirma
- Error acceder a Espacio ADA en lugar de BENEFICIARIO: seleccionar beneficiario al logarse
- Error Kit Consulting en lugar de Kit Digital: Tramitación de acuerdos < Kit Digital
Desistimientos:
- Desistir: cancelar acuerdo oficializado, liberar importe para usar con otro agente
- Renunciar: perder derecho a usar la subvención
- Se desiste de un acuerdo / se renuncia del bono
FACTURAS/FINANZAS:
- Factura marketing: se emite al presentar la primera memoria
- Factura ordenador: se emite tras presentar la 1ª memoria del PC
- NO se pueden modificar facturas una vez presentada la memoria
- Península: No pagan IVA (operación exenta, inversión sujeto pasivo)
- Canarias: Pagan IGIC del 7%
- Pago IGIC por transferencia: Banco Santander ES3000491911712310187542
ORDENADORES - PIPELINE STAGES:
BACKLOG: subvención aprobada + NIF/CIF
PDTE DATOS: PC elegido + datos receptor + código bono + criterio facturación
POR OFICIALIZAR: Estado Acuerdo = Oficializado
PDTE COBRO: verificar pagos e impuestos
LISTO PARA ENVIAR: validación antes de enviar
PEDIDO REALIZADO: pedido enviado al mayorista (15-30 días)
EN TRÁNSITO: recogido por transportista (48-72h Península, 7-15d Canarias)
INCIDENCIA: problema en la entrega
ENTREGADO: ordenador entregado
MEMORIA 1: firma cliente para cobrar 1ª Memoria (800€)
MEMORIA 2: verificación tras 12 meses + segunda firma
NO CALIFICADOS: casos cerrados
Tiempos de entrega:
- Península: 15/20 días desde pedido realizado
- Baleares: 18/22 días
- Canarias: 25/30 días
Soporte técnico PC - Software:
- TD Synnex: 911 177 587
- Valorista: 917 371 244
- Esprinet: 911 177 477
- Intecat: 933 659 784 / kitdigital@intecat.com
- Ticnova: 977 309 147 / soportekdt@ticnova.org
Soporte Hardware (fabricante):
- HP: 913 754 770
- Lenovo: 917 911 799
- Samsung: 916 258 084
- Dell: 902 100 130
- Acer: 91 414 24 14
PCs Windows disponibles:
- ThinkPad L14 Gen 5 Intel
- ThinkBook 16 G8
- ThinkCentre M75q Gen 5
- ThinkCentre M75q TOUCH
- Dell Latitude 3550
- Samsung Galaxy Book 4
Apple disponibles:
- MacBook Air 13 M4 / MacBook Air 15 M4
- MacBook Pro 14 M4 / MacBook Pro 16 M4 Pro
Precios Apple (Península):
- MacBook Air 13" M4: 1.499€ total, cliente paga 499€
- MacBook Air 15" M4: 1.719€ total, cliente paga 719€
- MacBook Pro 14" M4: 1.849€ total, cliente paga 849€
- MacBook Pro 16" M4 Pro: 2.599€ total, cliente paga 1.599€
FAQS PRODUCTOS:
REDES SOCIALES: Una red social (Facebook/Instagram/LinkedIn), 52 posts anuales, Social Media Plan, diseño gráfico, Metricool, informe mensual.
WEB: Activa hasta aceptación segunda memoria. No se puede eliminar antes.
SEO: Estratégico, Técnico, On-Page (3 páginas), Off-Page. Link building mínimo 3 enlaces. Alta en 5 directorios. Resultados en 3-6 meses. Solo WordPress.
FACTURA ELECTRÓNICA: Herramienta Billin. Obligatoria desde Enero 2027. Sin contacto de Billin en 3 días hábiles: ticket al TL (Patrizia). Tel: 918 318 888.
HERRAMIENTAS:
Intercom SLA: 7h WhatsApps, 24h mails. Abiertas: pendientes. Snooze: esperando cliente. Cerradas: gestionadas.
HubSpot objetos: Contacto, Empresa, Negocio, Project (principal en CS), PC.
Ringover: telefonía. SLA llamadas perdidas: procesar indicando cómo se contactó.
Ratificaciones:
- Plazo máximo: 10 días laborables desde notificación
- Si no se hace en plazo: pueden exigir devolución del importe
- Guía: https://www.orbidi.com/guia-ratificacion/
- Red.es: 900 909 001 (info) / 900 903 601 (soporte técnico)
Referidos: Crear contacto HubSpot, estado lead = cualificado. Plan amigo: SÍ si es cliente, NO si es referido interno. Envíos tarjetas Amazon: los viernes.
Bajas: Marcar en Empresa ¿Solicita la baja? = Sí. Tarea automática al CS Owner. Plazo: 1 día.
Plinng: clientes fuera del Kit Digital. Tel: +34604579315. Email: hello@plinng.com. Free Plan: 2 posts Instagram, 5 preguntas Maya, 2 respuestas reseñas.
Cambio de servicio - Acuerdo NO oficializado:
1. CS escala al TL para derivar a Ventas
2. CS crea nuevo proyecto y cancela el antiguo
3. CS completa el brief y mueve a PREPARADOS
Cambio de servicio - Acuerdo oficializado (memoria NO cobrada):
1. CS contacta cliente para confirmar si quiere desistir
2. Si desiste, CS abre ticket a TRAMITACIÓN
3. CS cancela proyecto antiguo y crea nuevo en HubSpot
4. CS completa brief, mueve a PREPARADOS y abre ticket al TL solicitando cambio de OCP
Acuerdo oficializado (memoria COBRADA): NO se puede cambiar de servicio.
2ª Memoria Ordenadores: demostrar uso mediante Bitdefender. Cliente debe encender el ordenador mínimo 3h seguidas una vez al mes. Sin actividad: Red.es puede exigir devolución del 80%.
Documentos importantes:
- Firma acuerdos: https://www.orbidi.com/guia-oficializacion-acuerdos/
- Firma memorias: https://www.orbidi.com/guia-firma-memorias/
- Guía ratificación: https://www.orbidi.com/guia-ratificacion/
Tareas CS colas: Petición baja CS (plazo 1 día), Contacto cliente (máx 48h), Cola Contacto CS.
Notificaciones HubSpot: Activar menciones directas, recordatorios tareas, cambios estado tickets. Desactivar el resto.
"""

SYSTEM_PROMPT = f"""Eres el Asistente IA del equipo de Customer Success de Orbidi, especializado en el programa Kit Digital.
Tu función es ayudar a los agentes de CS a:
- Conocer el procedimiento exacto para cualquier situación
- Saber a qué equipo escalar un ticket y cómo hacerlo
- Entender los estados y plazos del Kit Digital
- Resolver dudas sobre ordenadores, memorias, subvenciones, facturas y herramientas internas
REGLAS DE RESPUESTA:
1. Sé concreto y directo. Da pasos numerados cuando sea un proceso.
2. Si la pregunta implica escalar un ticket, indica exactamente: A QUIÉN, CÓMO y QUÉ incluir.
3. Si hay plazos importantes, resáltalos claramente.
4. Si la situación no está cubierta en la guía, dilo y sugiere consultar al TL.
5. Usa el contenido de la guía como única fuente de verdad.
6. Responde siempre en español.
Guía completa de procesos CS:
---
{CS_GUIDE}
---
Responde basándote exclusivamente en esta guía."""

# ─────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Orbidi IA Agent",
    page_icon="⚡",
    layout="centered",
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

st.markdown("""
<div class="orbidi-header">
    <div class="orbidi-logo">⚡</div>
    <div>
        <p class="orbidi-title">Orbidi IA Agent <span class="badge">CS · Kit Digital</span></p>
        <p class="orbidi-subtitle">Tu asistente de procesos internos · Customer Success</p>
    </div>
</div>
""", unsafe_allow_html=True)

@st.cache_resource
def get_client():
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

client = get_client()

if "messages" not in st.session_state:
    st.session_state.messages = []

col1, col2 = st.columns([5, 1])
with col2:
    if st.session_state.messages:
        if st.button("↺ Limpiar"):
            st.session_state.messages = []
            st.rerun()

if not st.session_state.messages:
    st.markdown("""
    <div style="text-align:center; padding: 48px 0 32px 0;">
        <div style="font-size: 40px; margin-bottom: 12px;">💬</div>
        <p style="font-size:16px; font-weight:600; color:#555; margin:0;">¿En qué puedo ayudarte hoy?</p>
        <p style="font-size:13px; color:#aaa; margin-top:6px;">Pregúntame sobre tickets, plazos, memorias, ordenadores o cualquier proceso CS.</p>
    </div>
    """, unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Escribe tu pregunta sobre procesos CS..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=2048,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *st.session_state.messages
            ],
            stream=True,
        )
        for chunk in stream:
            text = chunk.choices[0].delta.content or ""
            full_response += text
            placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

