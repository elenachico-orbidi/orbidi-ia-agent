"""
Configuración RAG: 102 procedimientos de la Guía Customer Success
Cada procedimiento tiene categoría, título y keywords para búsqueda precisa.

El índice BM25 usa: título + keywords + contenido de Notion.
Así la IA detecta correctamente la intención del agente aunque use palabras distintas.
"""

PROCEDURES_CONFIG = [

    # ═══════════════════════════════════════════
    # CATEGORÍA: PROCESOS
    # ═══════════════════════════════════════════
    {
        "id": "escalamiento",
        "category": "PROCESOS",
        "title": "Cómo y a quién escalar tickets/consultas",
        "keywords": [
            "escalar", "escalamiento", "ticket", "incidencia", "canal",
            "a quién escalo", "cómo escalo", "dónde abro ticket",
            "pipeline", "cs team leads", "finances", "logística",
            "slack tl", "hubspot ticket", "quién gestiona",
        ],
    },
    {
        "id": "team_leads",
        "category": "PROCESOS",
        "title": "Team Leads - Proceso abrir ticket",
        "keywords": [
            "team lead", "tl", "ticket team lead", "pipeline cs team leads",
            "abrir ticket hubspot", "crear ticket", "consulta proyecto",
            "duda subvención", "duda ordenador", "escalado team lead",
        ],
    },
    {
        "id": "ordenadores_logistica_ticket",
        "category": "PROCESOS",
        "title": "Ordenadores/Logística - Abrir ticket",
        "keywords": [
            "ticket logística", "incidencia pc", "ordenador entregado",
            "pipeline incidencias pc", "problema ordenador", "pc entregado",
            "listo para enviar", "incidencia logística",
        ],
    },
    {
        "id": "finance_ticket",
        "category": "PROCESOS",
        "title": "Finance - Abrir ticket (facturas y finanzas)",
        "keywords": [
            "ticket finance", "factura", "modificar factura", "solicitar factura",
            "pipeline finances", "corrección fiscal", "datos factura",
            "devolución igic", "incidencia transportista", "pendiente cobro",
        ],
    },
    {
        "id": "helpdesk",
        "category": "PROCESOS",
        "title": "Helpdesk - Alcance y procesos",
        "keywords": [
            "helpdesk", "help desk", "viafirma", "envío automático documentación",
            "proforma", "alcance helpdesk", "documentación automática",
        ],
    },
    {
        "id": "legal",
        "category": "PROCESOS",
        "title": "Legal - Notificaciones PDC y reintegros",
        "keywords": [
            "legal", "pdc", "pérdida derecho cobro", "reintegro",
            "notificación gobierno", "notificación pérdida", "inbox intercom legal",
        ],
    },
    {
        "id": "enmascaramiento_dominios",
        "category": "PROCESOS",
        "title": "Guía de enmascaramiento de dominios",
        "keywords": [
            "enmascaramiento", "dominio", "cambio dominio", "web dominio distinto",
            "memoria presentada dominio", "dominio diferente", "redireccionamiento",
        ],
    },
    {
        "id": "cambios_servicio",
        "category": "PROCESOS",
        "title": "Cambios de servicio",
        "keywords": [
            "cambio servicio", "cambiar servicio", "modificar servicio",
            "acuerdo no oficializado", "acuerdo oficializado cambio",
            "cambio antes oficialización", "cambio después oficialización",
        ],
    },
    {
        "id": "notificaciones_hubspot",
        "category": "PROCESOS",
        "title": "Configuración de notificaciones en HubSpot",
        "keywords": [
            "notificaciones hubspot", "configurar notificaciones",
            "alertas hubspot", "no recibo notificaciones", "muchas notificaciones",
        ],
    },
    {
        "id": "tareas_cs",
        "category": "PROCESOS",
        "title": "Tareas CS - Cola y seguimiento de contactos",
        "keywords": [
            "tareas cs", "cola contacto", "cliente acuerdo oficializado",
            "cliente habla con otro equipo", "seguimiento cliente",
            "tarea pendiente", "cola cs",
        ],
    },
    {
        "id": "referidos",
        "category": "PROCESOS",
        "title": "Referidos - Cómo marcar en HubSpot",
        "keywords": [
            "referido", "referidos", "cliente referido", "marcar referido",
            "cómo añadir referido", "referral", "cliente referencia",
        ],
    },
    {
        "id": "bajas",
        "category": "PROCESOS",
        "title": "Bajas - Gestión de cancelaciones de clientes",
        "keywords": [
            "baja", "bajas", "cancelar", "cancelación", "dar de baja",
            "cliente quiere irse", "gestión baja", "proceso baja",
            "cliente quiere cancelar", "tramitar baja",
        ],
    },
    {
        "id": "reseñas",
        "category": "PROCESOS",
        "title": "Reseñas - Proceso tras conseguir reseña positiva",
        "keywords": [
            "reseña", "reseñas", "reseña positiva", "gestión reseñas",
            "cliente deja reseña", "google review", "marcar reseña hubspot",
        ],
    },
    {
        "id": "bonos_caducados",
        "category": "PROCESOS",
        "title": "Bonos caducados - Qué hacer",
        "keywords": [
            "bono caducado", "bono expirado", "bono vencido", "caducidad bono",
            "no pudimos oficializar", "plazo bono", "bono sin efecto",
        ],
    },
    {
        "id": "desbloqueo_proyectos",
        "category": "PROCESOS",
        "title": "Desbloqueo de proyectos",
        "keywords": [
            "desbloquear", "desbloqueo", "proyecto desbloqueado", "quitar bloqueo",
            "retirar tag bloqueo", "proyecto bloqueado se desbloquea",
            "clickup bloqueo", "proyecto avanza",
        ],
    },
    {
        "id": "traspaso_plinng",
        "category": "PROCESOS",
        "title": "Traspaso clientes Orbidi ↔ Plinng",
        "keywords": [
            "plinng", "traspaso plinng", "saas", "servicio fuera kit digital",
            "derivar plinng", "cliente interesado saas", "plan orbidi",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: TRAMITACIÓN
    # ═══════════════════════════════════════════
    {
        "id": "tramitacion_tickets",
        "category": "TRAMITACIÓN",
        "title": "Tramitación - Proceso de tickets",
        "keywords": [
            "ticket tramitación", "abrir ticket tramitación",
            "escalar tramitación", "duda tramitación", "consultar tramitación",
        ],
    },
    {
        "id": "plazos_kit_digital",
        "category": "TRAMITACIÓN",
        "title": "Plazos y estados del Kit Digital",
        "keywords": [
            "plazo", "plazos", "kit digital plazo", "fecha límite",
            "cuánto tiempo", "cuándo caduca", "6 meses", "3 meses", "15 meses",
            "plazos subvención", "plazos memoria", "plazos acuerdo",
            "tiempo para firmar", "vencimiento",
        ],
    },
    {
        "id": "fase_solicitud_ocp",
        "category": "TRAMITACIÓN",
        "title": "Fase 1: Solicitud y OCP",
        "keywords": [
            "ocp", "orden confirmación proyecto", "solicitud kit digital",
            "firma ocp", "inicio tramitación", "fase 1", "primera fase",
        ],
    },
    {
        "id": "fase_resolucion_concesion",
        "category": "TRAMITACIÓN",
        "title": "Fase 2: Resolución de concesión del bono",
        "keywords": [
            "resolución concesión", "bono concedido", "aprobación red.es",
            "importe asignado", "fase 2", "concesión bono",
        ],
    },
    {
        "id": "fase_firma_acuerdo",
        "category": "TRAMITACIÓN",
        "title": "Fase 3: Firma del acuerdo (oficialización)",
        "keywords": [
            "firma acuerdo", "oficialización", "oficializar", "firmar acuerdo",
            "acps", "acuerdo prestación servicios", "fase 3",
        ],
    },
    {
        "id": "fase_ejecucion_memoria1",
        "category": "TRAMITACIÓN",
        "title": "Fase 4: Ejecución y primera memoria",
        "keywords": [
            "primera memoria", "memoria 1", "ejecución", "implantación",
            "fase 4", "presentar primera memoria", "3 meses memoria",
        ],
    },
    {
        "id": "fase_mantenimiento",
        "category": "TRAMITACIÓN",
        "title": "Fase 5: Periodo de mantenimiento",
        "keywords": [
            "mantenimiento", "periodo mantenimiento", "factura emitida",
            "memoria cobrada", "fase 5", "tras primera memoria",
        ],
    },
    {
        "id": "fase_memoria2",
        "category": "TRAMITACIÓN",
        "title": "Fase 6: Segunda memoria de justificación",
        "keywords": [
            "segunda memoria", "memoria 2", "justificación final",
            "15 meses", "12 meses", "fase 6", "memoria final",
        ],
    },
    {
        "id": "estados_subvencion",
        "category": "TRAMITACIÓN",
        "title": "Estados de la Subvención en HubSpot",
        "keywords": [
            "estado subvención", "estados subvención", "por presentar",
            "en tramitación", "concedido", "denegado", "estado en hubspot",
            "dónde veo estado", "empresa hubspot estado",
        ],
    },
    {
        "id": "tipos_notificaciones",
        "category": "TRAMITACIÓN",
        "title": "Tipos de Notificaciones y su Significado",
        "keywords": [
            "notificación gobierno", "notificación red.es", "tipo notificación",
            "qué significa notificación", "notificación cliente", "propietario notificación",
            "acción notificación",
        ],
    },
    {
        "id": "bloqueos_solicitud",
        "category": "TRAMITACIÓN",
        "title": "Bloqueos en la Presentación de la Solicitud del Kit Digital",
        "keywords": [
            "bloqueo solicitud", "bloqueo presentación", "bloqueo kit digital",
            "falta documentación", "subsanación", "bloqueo tramitación solicitud",
        ],
    },
    {
        "id": "bloqueos_oficializacion",
        "category": "TRAMITACIÓN",
        "title": "Bloqueos en la Oficialización de Acuerdos MKT/PC",
        "keywords": [
            "bloqueo oficialización", "no puede firmar", "error firma",
            "bloqueo acuerdo", "bloqueo mkt", "bloqueo pc", "oficialización bloqueada",
            "tipo bloqueo", "descripción bloqueo", "acción bloqueo",
        ],
    },
    {
        "id": "campos_hubspot_tramitacion",
        "category": "TRAMITACIÓN",
        "title": "Campos a consultar en HubSpot (tramitación)",
        "keywords": [
            "campos hubspot", "campo empresa hubspot", "número expediente",
            "expediente kit digital", "fecha tracking", "solicitud previa",
            "qué campos revisar",
        ],
    },
    {
        "id": "memorias_firma",
        "category": "TRAMITACIÓN",
        "title": "Memorias - Proceso de firma",
        "keywords": [
            "firma memoria", "firmar memoria", "cliente firma memoria",
            "portal gestión memoria", "certificado electrónico memoria",
            "acceder portal memoria", "cómo firma el cliente",
        ],
    },
    {
        "id": "desistimientos",
        "category": "TRAMITACIÓN",
        "title": "Desistimientos y Renuncias",
        "keywords": [
            "desistimiento", "desistir", "renunciar", "renuncia bono",
            "cancelar acuerdo oficializado", "liberar importe",
            "diferencia desistir renunciar",
        ],
    },
    {
        "id": "iva_igic",
        "category": "TRAMITACIÓN",
        "title": "IVA / IGIC - Fiscalidad de la subvención",
        "keywords": [
            "iva", "igic", "canarias", "sin iva", "fiscalidad",
            "factura sin iva", "por qué sin iva", "canarias igic",
            "impuestos", "factura exenta",
        ],
    },
    {
        "id": "bono_caducado_mkt",
        "category": "TRAMITACIÓN",
        "title": "Bono Caducado MKT - Qué es y opciones del cliente",
        "keywords": [
            "bono caducado marketing", "bono caducado mkt", "bono sin efecto",
            "recuperar bono", "nueva solicitud bono", "6 meses sin firmar",
            "qué decirle al cliente bono caducado",
        ],
    },
    {
        "id": "bono_caducado_pc",
        "category": "TRAMITACIÓN",
        "title": "Bono Caducado PC (Puesto de Trabajo Seguro)",
        "keywords": [
            "bono caducado pc", "puesto trabajo seguro caducado",
            "bono pc caducado", "renovar bono pc", "renunciar bono pc",
        ],
    },
    {
        "id": "glosario_tramitacion",
        "category": "TRAMITACIÓN",
        "title": "Glosario de tramitación Kit Digital",
        "keywords": [
            "glosario", "definición", "qué es bono", "qué es acps",
            "qué es memoria", "qué es red.es", "qué es expediente",
            "período mantenimiento qué es", "ocp qué es",
        ],
    },
    {
        "id": "faqs_tramitacion",
        "category": "TRAMITACIÓN",
        "title": "FAQs Tramitación",
        "keywords": [
            "faq tramitación", "preguntas frecuentes tramitación",
            "puesto trabajo seguro sin memoria", "ampliación 1000",
            "requisitos acuerdo pc",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: ORDENADORES
    # ═══════════════════════════════════════════
    {
        "id": "specs_pc",
        "category": "ORDENADORES",
        "title": "Especificaciones técnicas de los PCs",
        "keywords": [
            "especificaciones pc", "specs ordenador", "características ordenador",
            "windows mac kit digital", "qué ordenador", "modelo pc",
            "ficha técnica ordenador",
        ],
    },
    {
        "id": "stock_pc",
        "category": "ORDENADORES",
        "title": "Stock y disponibilidad de ordenadores",
        "keywords": [
            "stock pc", "disponibilidad ordenador", "hay stock",
            "cuándo hay ordenadores", "disponible ordenador",
        ],
    },
    {
        "id": "pipeline_pc",
        "category": "ORDENADORES",
        "title": "Pipeline y estados de los PCs en HubSpot",
        "keywords": [
            "pipeline pc", "estados pc", "estado ordenador hubspot",
            "backlog", "en tránsito", "entregado", "listo para enviar",
            "pedido realizado", "flujo pc", "stages pc",
        ],
    },
    {
        "id": "envio_ceuta_melilla",
        "category": "ORDENADORES",
        "title": "Envío de ordenadores a Ceuta y Melilla",
        "keywords": [
            "ceuta", "melilla", "envío ceuta", "envío melilla",
            "seur ceuta", "aduana", "dua", "trámites aduaneros pc",
            "cobro inesperado envío",
        ],
    },
    {
        "id": "incidencias_pc",
        "category": "ORDENADORES",
        "title": "Incidencias de PCs - Tipos y proceso",
        "keywords": [
            "incidencia pc", "incidencia ordenador", "problema ordenador",
            "ordenador roto", "ordenador no funciona", "avería",
            "qué hago si el ordenador falla",
        ],
    },
    {
        "id": "incidencia_hardware",
        "category": "ORDENADORES",
        "title": "Incidencias de Hardware",
        "keywords": [
            "incidencia hardware", "problema hardware", "pieza rota",
            "pantalla rota", "teclado roto", "fabricante", "garantía hardware",
        ],
    },
    {
        "id": "incidencia_software",
        "category": "ORDENADORES",
        "title": "Incidencias de Software",
        "keywords": [
            "incidencia software", "problema software", "virus",
            "sistema operativo", "pts", "mayorista software",
            "soporte software", "windows no arranca",
        ],
    },
    {
        "id": "memoria2_pc",
        "category": "ORDENADORES",
        "title": "Segunda Memoria de Ordenadores",
        "keywords": [
            "segunda memoria pc", "memoria 2 ordenador", "evidencias pc",
            "segunda evidencia ordenador", "justificación pc segunda",
        ],
    },
    {
        "id": "formulario_pc",
        "category": "ORDENADORES",
        "title": "Formulario de selección de PC",
        "keywords": [
            "formulario pc", "seleccionar ordenador", "elegir pc",
            "formulario selección", "objeto pc hubspot", "kd-pc",
        ],
    },
    {
        "id": "ampliacion_1000",
        "category": "ORDENADORES",
        "title": "Ampliación de 1.000€ en PC",
        "keywords": [
            "ampliación 1000", "ampliar bono 1000", "1000 euros adicionales",
            "solicitar ampliación", "ampliación pc", "1000€ más",
        ],
    },
    {
        "id": "accesorios_pc",
        "category": "ORDENADORES",
        "title": "Accesorios incluidos en el envío de PC",
        "keywords": [
            "accesorios pc", "qué incluye envío", "qué viene con el ordenador",
            "cargador incluido", "ratón incluido", "accesorios kit digital pc",
        ],
    },
    {
        "id": "faqs_ordenadores",
        "category": "ORDENADORES",
        "title": "FAQs Ordenadores",
        "keywords": [
            "faq ordenadores", "preguntas frecuentes pc", "150 euros ordenador",
            "hay que pagar pc", "coste ordenador cliente",
            "plazo entrega pc", "cuándo llega el ordenador",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: RATIFICACIONES
    # ═══════════════════════════════════════════
    {
        "id": "guia_ratificaciones",
        "category": "RATIFICACIONES",
        "title": "Guía de Ratificaciones",
        "keywords": [
            "ratificación", "ratificaciones", "guía ratificación",
            "qué es ratificación", "proceso ratificación",
        ],
    },
    {
        "id": "plantillas_ratificaciones",
        "category": "RATIFICACIONES",
        "title": "Plantillas de respuesta para ratificaciones",
        "keywords": [
            "plantilla ratificación", "respuesta ratificación",
            "qué decirle al cliente ratificación", "mensaje ratificación",
            "texto ratificación cliente",
        ],
    },
    {
        "id": "escalado_prod_ratificaciones",
        "category": "RATIFICACIONES",
        "title": "Formulario para escalar tickets a PROD (ratificaciones)",
        "keywords": [
            "escalar producción ratificación", "ticket prod ratificación",
            "formulario clickup ratificación", "escalar a prod",
        ],
    },
    {
        "id": "certificado_digital",
        "category": "RATIFICACIONES",
        "title": "Guía certificado digital / clave pin",
        "keywords": [
            "certificado digital", "clave pin", "cómo obtener certificado",
            "certificado electrónico", "acceder con certificado",
            "no tiene certificado digital",
        ],
    },
    {
        "id": "errores_ratificaciones",
        "category": "RATIFICACIONES",
        "title": "Errores comunes en ratificaciones",
        "keywords": [
            "error ratificación", "problema ratificación",
            "certificado incorrecto", "número bono incorrecto ratificación",
            "no puede ratificar", "error al ratificar",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: FACTURA ELECTRÓNICA
    # ═══════════════════════════════════════════
    {
        "id": "billin_info",
        "category": "FACTURA ELECTRÓNICA",
        "title": "Billin - Información general y funcionalidades",
        "keywords": [
            "billin", "factura electrónica", "facturación online",
            "qué es billin", "herramienta facturación", "obligación factura electrónica",
            "ley factura electrónica",
        ],
    },
    {
        "id": "billin_pipeline",
        "category": "FACTURA ELECTRÓNICA",
        "title": "Estados del Pipeline de Factura Electrónica",
        "keywords": [
            "pipeline factura electrónica", "estados billin",
            "inbox billin", "por derivar", "derivado billin",
            "estado factura electrónica",
        ],
    },
    {
        "id": "escalar_billin",
        "category": "FACTURA ELECTRÓNICA",
        "title": "Cómo escalar algo a Billin",
        "keywords": [
            "escalar billin", "ticket billin", "cliente no recibe contacto billin",
            "problema billin", "equipo billin", "judith billin", "patrizia billin",
        ],
    },
    {
        "id": "ampliacion_billin",
        "category": "FACTURA ELECTRÓNICA",
        "title": "Ampliación 1.000€ para Factura Electrónica",
        "keywords": [
            "ampliación factura electrónica", "1000 euros factura electrónica",
            "ampliar bono factura", "2000 euros factura electrónica",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: FACTURAS / FINANZAS
    # ═══════════════════════════════════════════
    {
        "id": "que_es_factura",
        "category": "FACTURAS/FINANZAS",
        "title": "Qué es la factura y cómo funciona",
        "keywords": [
            "qué es factura", "factura kit digital", "factura subvención",
            "para qué sirve factura", "documento fiscal",
        ],
    },
    {
        "id": "proceso_factura",
        "category": "FACTURAS/FINANZAS",
        "title": "Proceso cuando el cliente pide una factura",
        "keywords": [
            "cliente pide factura", "dónde está la factura",
            "portal cliente factura", "no aparece factura", "ticket finanzas factura",
            "cómo consigo la factura",
        ],
    },
    {
        "id": "fiscalidad_factura",
        "category": "FACTURAS/FINANZAS",
        "title": "Fiscalidad de la subvención - IVA/IGIC por región",
        "keywords": [
            "iva factura", "igic factura", "sin iva subvención",
            "factura sin iva por qué", "canarias factura",
            "fiscalidad kit digital", "impuestos subvención",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: FAQS PRODUCTOS
    # ═══════════════════════════════════════════
    {
        "id": "linkedin_admin",
        "category": "FAQS PRODUCTOS",
        "title": "Cómo añadir administrador en LinkedIn",
        "keywords": [
            "linkedin admin", "administrador linkedin", "añadir admin linkedin",
            "página empresa linkedin", "gestionar linkedin",
        ],
    },
    {
        "id": "metricool_error_400",
        "category": "FAQS PRODUCTOS",
        "title": "Error 400 Session Invalid - Instagram en Metricool",
        "keywords": [
            "error 400", "session invalid", "metricool instagram error",
            "no conecta instagram metricool", "error vincular instagram",
            "400 session invalid",
        ],
    },
    {
        "id": "videos_clientes",
        "category": "FAQS PRODUCTOS",
        "title": "Vídeos útiles para compartir con clientes",
        "keywords": [
            "vídeo cliente", "tutorial cliente", "cómo vincular linkedin",
            "vídeo configuración", "enlace tutorial", "youtu.be",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: INTERCOM
    # ═══════════════════════════════════════════
    {
        "id": "que_es_intercom",
        "category": "INTERCOM",
        "title": "Qué es Intercom y cómo está estructurado",
        "keywords": [
            "intercom", "qué es intercom", "plataforma intercom",
            "mensajería intercom", "soporte intercom", "vista intercom",
        ],
    },
    {
        "id": "intercom_bandeja",
        "category": "INTERCOM",
        "title": "Buenas prácticas - Bandeja Open en Intercom",
        "keywords": [
            "bandeja open", "conversaciones abiertas", "open intercom",
            "conversación sin contestar", "buenas prácticas intercom",
            "snooze intercom", "gestión bandeja",
        ],
    },
    {
        "id": "intercom_barra_izquierda",
        "category": "INTERCOM",
        "title": "Intercom - Barra lateral izquierda",
        "keywords": [
            "barra izquierda intercom", "menú intercom", "bandeja entrada intercom",
            "contactos intercom", "navegación intercom",
        ],
    },
    {
        "id": "intercom_barra_derecha",
        "category": "INTERCOM",
        "title": "Intercom - Barra lateral derecha (datos del contacto)",
        "keywords": [
            "barra derecha intercom", "datos contacto intercom",
            "información cliente intercom", "propiedades intercom",
            "historial intercom",
        ],
    },
    {
        "id": "intercom_barra_centro",
        "category": "INTERCOM",
        "title": "Intercom - Barra central (conversaciones)",
        "keywords": [
            "barra central intercom", "mensajes intercom",
            "lista conversaciones intercom", "responder intercom",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: HUBSPOT
    # ═══════════════════════════════════════════
    {
        "id": "hubspot_objeto_project",
        "category": "HUBSPOT",
        "title": "Objeto Project en HubSpot",
        "keywords": [
            "objeto project", "project hubspot", "gestión proyecto hubspot",
            "dónde está el proyecto", "hubspot project",
        ],
    },
    {
        "id": "hubspot_objeto_pc",
        "category": "HUBSPOT",
        "title": "Objeto PC en HubSpot",
        "keywords": [
            "objeto pc hubspot", "pc hubspot", "kd-pc", "ordenador hubspot",
            "seguimiento ordenador hubspot",
        ],
    },
    {
        "id": "hubspot_tickets",
        "category": "HUBSPOT",
        "title": "Objeto Tickets en HubSpot - Cómo abrirlos",
        "keywords": [
            "tickets hubspot", "abrir ticket hubspot", "crear ticket hubspot",
            "cómo abro ticket", "pipeline ticket", "objeto ticket",
        ],
    },
    {
        "id": "hubspot_tareas",
        "category": "HUBSPOT",
        "title": "Gestión de tareas en HubSpot",
        "keywords": [
            "tareas hubspot", "crear tarea", "asignar tarea",
            "seguimiento tarea", "tarea pendiente hubspot",
        ],
    },
    {
        "id": "hubspot_paneles",
        "category": "HUBSPOT",
        "title": "Paneles e informes en HubSpot",
        "keywords": [
            "panel hubspot", "informe hubspot", "dashboard hubspot",
            "ver cartera", "proyectos bloqueados panel", "estado pipeline panel",
        ],
    },
    {
        "id": "hubspot_informe_semanal",
        "category": "HUBSPOT",
        "title": "Informe de Seguimiento Semanal HubSpot",
        "keywords": [
            "informe semanal", "seguimiento semanal", "informe cs",
            "revisión semanal proyectos", "informe más importante",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: CLICKUP
    # ═══════════════════════════════════════════
    {
        "id": "clickup_secciones",
        "category": "CLICKUP",
        "title": "ClickUp - Secciones y campos clave",
        "keywords": [
            "clickup", "secciones clickup", "campos clickup",
            "detalle clickup", "subtareas clickup",
        ],
    },
    {
        "id": "clickup_estados_memoria",
        "category": "CLICKUP",
        "title": "ClickUp - Estados de Memoria",
        "keywords": [
            "estados memoria clickup", "flujo memoria", "fdk", "en progreso memoria",
            "revisión memoria", "completado memoria", "estados producción",
        ],
    },
    {
        "id": "clickup_subtareas",
        "category": "CLICKUP",
        "title": "ClickUp - Gestión de subtareas y cambios de estado",
        "keywords": [
            "subtareas clickup", "cerrar subtarea", "cambiar estado clickup",
            "completar subtarea", "revisión cliente clickup",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: RINGOVER
    # ═══════════════════════════════════════════
    {
        "id": "ringover_webapp",
        "category": "RINGOVER",
        "title": "Ringover - WebApp para llamadas",
        "keywords": [
            "ringover", "llamadas ringover", "hacer llamada",
            "auth ringover", "configurar audio ringover",
        ],
    },
    {
        "id": "ringover_dashboard",
        "category": "RINGOVER",
        "title": "Ringover - Dashboard de actividad",
        "keywords": [
            "dashboard ringover", "actividad telefónica", "team lead ringover",
            "monitor llamadas",
        ],
    },
    {
        "id": "ringover_tips",
        "category": "RINGOVER",
        "title": "Ringover - Tips y recomendaciones",
        "keywords": [
            "tips ringover", "auriculares ringover", "buenas prácticas llamadas",
            "no poner en espera", "calidad llamada",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: MARKUP
    # ═══════════════════════════════════════════
    {
        "id": "markup_feedback",
        "category": "MARKUP",
        "title": "MarkUp - Cómo dejar feedback en webs",
        "keywords": [
            "markup", "feedback web", "dejar comentario web",
            "revisar diseño", "comentar en web", "revisión web markup",
        ],
    },
]
