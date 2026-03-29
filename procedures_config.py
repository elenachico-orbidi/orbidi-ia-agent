"""
Configuración RAG: procedimientos de la Guía Customer Success (359 secciones)
Organizado en 20 categorías con keywords para búsqueda precisa en BM25.

El índice BM25 usa: título + keywords + categoría + contenido de Notion.
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

    # ═══════════════════════════════════════════
    # CATEGORÍA: REDES SOCIALES
    # ═══════════════════════════════════════════
    {
        "id": "rrss_que_incluye",
        "category": "REDES SOCIALES",
        "title": "Redes Sociales - Qué incluye el servicio",
        "keywords": [
            "qué redes sociales incluye", "kit digital redes sociales",
            "cuántas publicaciones", "publicaciones al año",
            "qué incluye rrss", "servicio redes sociales",
            "qué hace orbidi en redes", "social media plan",
        ],
    },
    {
        "id": "rrss_sugerir_cambios",
        "category": "REDES SOCIALES",
        "title": "Redes Sociales - Cambios y aprobación de contenidos",
        "keywords": [
            "sugerir cambios contenido", "aprobar publicaciones",
            "cambiar contenido redes", "no me gusta el contenido",
            "modificar publicación", "revisar contenido rrss",
        ],
    },
    {
        "id": "rrss_contraseñas",
        "category": "REDES SOCIALES",
        "title": "Redes Sociales - Accesos y contraseñas",
        "keywords": [
            "contraseña redes sociales", "acceso instagram facebook",
            "credenciales redes", "necesitáis contraseña",
            "dar acceso redes", "permisos redes sociales",
        ],
    },
    {
        "id": "metricool_vincular",
        "category": "REDES SOCIALES",
        "title": "Pasos para vincular Instagram y Facebook a Metricool",
        "keywords": [
            "vincular metricool", "conectar metricool", "metricool instagram",
            "metricool facebook", "crear marca metricool", "vincular cuenta metricool",
            "cómo vincular redes metricool", "conectar facebook metricool",
            "conectar instagram metricool", "pasos metricool",
        ],
    },
    {
        "id": "metricool_crear_marca",
        "category": "REDES SOCIALES",
        "title": "Metricool - Crear una marca (paso imprescindible)",
        "keywords": [
            "crear marca metricool", "nueva marca metricool",
            "primer paso metricool", "configurar metricool",
        ],
    },
    {
        "id": "metricool_conectar_facebook",
        "category": "REDES SOCIALES",
        "title": "Metricool - Conectar Facebook",
        "keywords": [
            "conectar facebook metricool", "facebook metricool",
            "vincular facebook", "página facebook metricool",
            "no conecta facebook", "error facebook metricool",
        ],
    },
    {
        "id": "metricool_conectar_instagram",
        "category": "REDES SOCIALES",
        "title": "Metricool - Conectar Instagram",
        "keywords": [
            "conectar instagram metricool", "instagram metricool",
            "vincular instagram", "cuenta profesional instagram",
            "no conecta instagram", "error instagram metricool",
        ],
    },
    {
        "id": "linkedin_admin_rrss",
        "category": "REDES SOCIALES",
        "title": "Cómo añadir administrador en LinkedIn",
        "keywords": [
            "administrador linkedin", "añadir admin linkedin",
            "gestionar linkedin", "página empresa linkedin admin",
            "acceso linkedin", "dar acceso linkedin",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: WEB
    # ═══════════════════════════════════════════
    {
        "id": "web_que_incluye",
        "category": "WEB",
        "title": "WEB - Qué incluye el Kit Digital Web",
        "keywords": [
            "qué incluye web", "kit digital web", "qué es kd web",
            "presencia en internet", "sitio web kit digital",
            "dominio hosting web", "páginas web kit digital",
            "wordpress kit digital", "accesibilidad web",
        ],
    },
    {
        "id": "web_hosting_dominio",
        "category": "WEB",
        "title": "Web - Hosting y dominio: qué pasa al acabar la subvención",
        "keywords": [
            "hosting dominio subvención acaba", "qué pasa con el dominio",
            "dominio después subvención", "hosting tras kit digital",
            "renovar dominio", "dominio propiedad cliente",
            "quién tiene el dominio", "hosting orbidi",
        ],
    },
    {
        "id": "web_dominio_compra",
        "category": "WEB",
        "title": "Web - Compra de dominio",
        "keywords": [
            "comprar dominio", "compra dominio", "nuevo dominio",
            "registrar dominio", "cliente sin dominio", "falta dominio",
            "nombre dominio", "dominio disponible",
        ],
    },
    {
        "id": "web_migracion_hosting",
        "category": "WEB",
        "title": "Web - Migración de hosting y dominio",
        "keywords": [
            "migrar hosting", "migración dominio", "crear web migrar",
            "traspasar dominio", "cambiar hosting", "mover web",
            "web en otro hosting", "migrar wordpress",
        ],
    },
    {
        "id": "web_presentacion_cliente",
        "category": "WEB",
        "title": "Web - Presentación de la web al cliente",
        "keywords": [
            "presentar web cliente", "presentación web",
            "entregar web cliente", "revisión web cliente",
            "guion presentación web", "llamada presentación web",
        ],
    },
    {
        "id": "web_wordpress",
        "category": "WEB",
        "title": "Web - WordPress y gestión del sitio",
        "keywords": [
            "wordpress", "gestión wordpress", "panel wordpress",
            "editar wordpress", "acceso wordpress", "plugin wordpress",
            "actualizar wordpress", "web wordpress",
        ],
    },
    {
        "id": "web_alistamiento",
        "category": "WEB",
        "title": "Web - Alistamiento (inicio del proyecto web)",
        "keywords": [
            "alistamiento web", "inicio proyecto web", "brief web",
            "arrancar proyecto web", "primeros pasos web",
            "datos necesarios web", "formulario web",
        ],
    },
    {
        "id": "web_bloqueos",
        "category": "WEB",
        "title": "Web - Bloqueos frecuentes en proyectos web",
        "keywords": [
            "bloqueo web", "proyecto web bloqueado", "web no avanza",
            "bloqueo diseño web", "bloqueo dominio web",
            "falta información web", "cliente no responde web",
            "web no carga", "sitio web no funciona",
        ],
    },
    {
        "id": "web_modificaciones_diseño",
        "category": "WEB",
        "title": "Web - Modificaciones de diseño",
        "keywords": [
            "modificar diseño web", "cambio diseño", "cambiar diseño web",
            "modificación web", "ajuste diseño", "cambiar colores web",
            "cambiar logo web", "feedback diseño web",
        ],
    },
    {
        "id": "web_faqs",
        "category": "WEB",
        "title": "FAQs Web - Preguntas frecuentes de clientes",
        "keywords": [
            "faq web", "preguntas frecuentes web", "dudas web cliente",
            "cuántas páginas", "qué incluye web", "web ecommerce",
            "tienda online kit digital", "cuánto tarda la web",
            "qué pasa si no me gusta la web",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: SEO
    # ═══════════════════════════════════════════
    {
        "id": "seo_que_es",
        "category": "SEO",
        "title": "SEO - Qué es y por qué lo necesito",
        "keywords": [
            "qué es seo", "para qué sirve seo", "seo explicación",
            "posicionamiento google", "aparecer en google",
            "seo kit digital", "por qué seo",
        ],
    },
    {
        "id": "seo_tiempo_resultados",
        "category": "SEO",
        "title": "SEO - Cuánto tarda en verse resultados",
        "keywords": [
            "cuánto tarda seo", "tiempo resultados seo",
            "cuándo veo resultados seo", "seo resultados",
            "meses seo", "plazo seo",
        ],
    },
    {
        "id": "seo_que_incluye",
        "category": "SEO",
        "title": "SEO - Qué incluye y qué NO incluye el servicio",
        "keywords": [
            "qué incluye seo", "qué no incluye seo", "alcance seo",
            "límites seo", "servicio seo kit digital",
            "análisis web seo", "pestañas seo",
        ],
    },
    {
        "id": "seo_vs_google_ads",
        "category": "SEO",
        "title": "SEO vs Google Ads - Diferencias",
        "keywords": [
            "seo vs google ads", "seo vs sem", "diferencia seo ads",
            "google ads seo mismo", "publicidad pagada seo",
            "anuncios google seo",
        ],
    },
    {
        "id": "seo_necesito_aportar",
        "category": "SEO",
        "title": "SEO - Qué necesita aportar el cliente",
        "keywords": [
            "qué aporta cliente seo", "información para seo",
            "datos necesarios seo", "accesos seo",
            "colaboración cliente seo",
        ],
    },
    {
        "id": "seo_cliente_no_contento",
        "category": "SEO",
        "title": "SEO - Cliente no contento con los resultados",
        "keywords": [
            "cliente no contento seo", "no veo resultados seo",
            "cliente insatisfecho seo", "seo no funciona",
            "cliente queja seo", "malos resultados seo",
            "no aparece en google",
        ],
    },
    {
        "id": "seo_herramientas",
        "category": "SEO",
        "title": "SEO - Herramientas que usamos",
        "keywords": [
            "herramientas seo", "qué herramientas seo",
            "tools seo", "semrush", "ahrefs", "search console",
            "plataformas seo",
        ],
    },
    {
        "id": "seo_palabras_clave",
        "category": "SEO",
        "title": "SEO - Palabras clave y posicionamiento",
        "keywords": [
            "palabras clave seo", "keywords seo", "cuántas keywords",
            "posicionar palabras clave", "seo local vs general",
            "seo local", "términos búsqueda seo",
        ],
    },
    {
        "id": "seo_alistamiento",
        "category": "SEO",
        "title": "SEO - Alistamiento (inicio del proyecto)",
        "keywords": [
            "alistamiento seo", "inicio proyecto seo", "brief seo",
            "arrancar seo", "primeros pasos seo",
            "datos necesarios seo proyecto",
        ],
    },
    {
        "id": "seo_bloqueos",
        "category": "SEO",
        "title": "SEO - Bloqueos en proyectos SEO",
        "keywords": [
            "bloqueo seo", "proyecto seo bloqueado", "seo sin web",
            "web no apta seo", "seo no avanza",
            "falta acceso search console", "falta acceso analytics",
        ],
    },
    {
        "id": "seo_faqs",
        "category": "SEO",
        "title": "FAQs SEO - Preguntas frecuentes de clientes",
        "keywords": [
            "faq seo", "preguntas frecuentes seo",
            "garantía posición google", "primer puesto google",
            "seo ecommerce", "seo todos los sectores",
            "gestionar seo yo mismo",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: INTERCOM (detallado)
    # ═══════════════════════════════════════════
    {
        "id": "intercom_abrir_conversacion",
        "category": "INTERCOM",
        "title": "Intercom - Abrir primera conversación con cliente",
        "keywords": [
            "abrir conversación intercom", "iniciar conversación",
            "primera conversación cliente", "nuevo mensaje intercom",
            "contactar cliente intercom", "enviar mensaje intercom",
        ],
    },
    {
        "id": "intercom_desde_hubspot",
        "category": "INTERCOM",
        "title": "Intercom - Abrir conversación desde HubSpot",
        "keywords": [
            "intercom desde hubspot", "conversación hubspot intercom",
            "abrir intercom hubspot", "on-going hubspot",
            "contactar cliente desde hubspot",
        ],
    },
    {
        "id": "intercom_buscar_cliente",
        "category": "INTERCOM",
        "title": "Intercom - Cómo buscar a un cliente",
        "keywords": [
            "buscar cliente intercom", "encontrar cliente intercom",
            "buscar contacto intercom", "cómo busco intercom",
        ],
    },
    {
        "id": "intercom_tickets",
        "category": "INTERCOM",
        "title": "Intercom - Abrir tickets en Intercom",
        "keywords": [
            "ticket intercom", "abrir ticket intercom",
            "crear ticket desde intercom", "ticket en conversación",
        ],
    },
    {
        "id": "intercom_inbox",
        "category": "INTERCOM",
        "title": "Intercom - Cómo funciona el Inbox",
        "keywords": [
            "inbox intercom", "bandeja entrada intercom",
            "cómo funciona inbox", "gestión inbox",
            "organizar inbox intercom",
        ],
    },
    {
        "id": "intercom_plantillas_macros",
        "category": "INTERCOM",
        "title": "Intercom - Plantillas y Macros",
        "keywords": [
            "plantillas intercom", "macros intercom",
            "respuestas guardadas", "plantilla mensaje intercom",
            "cómo usar plantillas intercom", "respuesta rápida intercom",
        ],
    },
    {
        "id": "intercom_whatsapp",
        "category": "INTERCOM",
        "title": "Intercom - Reglas de uso de WhatsApp",
        "keywords": [
            "whatsapp intercom", "reglas whatsapp", "usar whatsapp intercom",
            "cuando usar whatsapp", "normas whatsapp intercom",
        ],
    },
    {
        "id": "intercom_asignacion_tiempos",
        "category": "INTERCOM",
        "title": "Intercom - Asignación y tiempos de respuesta",
        "keywords": [
            "asignar conversación intercom", "tiempo respuesta intercom",
            "sla intercom", "asignación intercom",
            "cuánto tiempo responder intercom",
        ],
    },
    {
        "id": "intercom_reasignacion",
        "category": "INTERCOM",
        "title": "Intercom - Reasignación de conversaciones",
        "keywords": [
            "reasignar intercom", "reasignación conversación",
            "cambiar asignación intercom", "pasar conversación intercom",
            "transferir conversación intercom",
        ],
    },
    {
        "id": "intercom_merge",
        "category": "INTERCOM",
        "title": "Intercom - Fusionar conversaciones (merge)",
        "keywords": [
            "merge intercom", "fusionar conversaciones",
            "unir conversaciones intercom", "combinar mensajes intercom",
        ],
    },
    {
        "id": "intercom_vistas",
        "category": "INTERCOM",
        "title": "Intercom - Vistas personalizadas",
        "keywords": [
            "vistas intercom", "vistas personalizadas intercom",
            "crear vista intercom", "filtros intercom",
            "organizar conversaciones intercom",
        ],
    },
    {
        "id": "intercom_snooze",
        "category": "INTERCOM",
        "title": "Intercom - Snooze y buenas prácticas bandeja Open",
        "keywords": [
            "snooze intercom", "posponer conversación",
            "bandeja open intercom", "buenas prácticas intercom",
            "cuándo usar snooze", "gestión bandeja",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: HUBSPOT (detallado)
    # ═══════════════════════════════════════════
    {
        "id": "hubspot_que_es",
        "category": "HUBSPOT",
        "title": "Qué es HubSpot y ventajas para CS",
        "keywords": [
            "qué es hubspot", "para qué sirve hubspot",
            "hubspot crm", "ventajas hubspot", "cómo funciona hubspot",
        ],
    },
    {
        "id": "hubspot_objeto_empresa",
        "category": "HUBSPOT",
        "title": "HubSpot - Objeto Empresa (dónde está la info del cliente)",
        "keywords": [
            "objeto empresa hubspot", "empresa hubspot",
            "dónde veo info cliente hubspot", "ficha cliente hubspot",
            "datos empresa hubspot", "campos empresa hubspot",
            "comprobante igic hubspot",
        ],
    },
    {
        "id": "hubspot_tickets_categorias",
        "category": "HUBSPOT",
        "title": "HubSpot - Categorías de tickets y cuándo usarlos",
        "keywords": [
            "categorías ticket hubspot", "tipo ticket hubspot",
            "qué categoría ticket", "cuándo abro ticket",
            "categoría correcta ticket", "ticket prioridad",
            "ticket incidencia", "ticket cambio memoria",
            "ticket reclamación",
        ],
    },
    {
        "id": "hubspot_ticket_po",
        "category": "HUBSPOT",
        "title": "HubSpot - Cómo abrir ticket a PO (Product Owner)",
        "keywords": [
            "ticket po", "ticket product owner", "escalar po",
            "abrir ticket po hubspot", "cuándo escalar po",
        ],
    },
    {
        "id": "hubspot_project_pipeline",
        "category": "HUBSPOT",
        "title": "HubSpot - Project Pipeline Stage (estados del proyecto)",
        "keywords": [
            "project pipeline", "estado proyecto hubspot",
            "pipeline stage hubspot", "estado project",
            "cambiar estado proyecto hubspot",
        ],
    },
    {
        "id": "hubspot_referidos_proceso",
        "category": "HUBSPOT",
        "title": "HubSpot - Proceso completo de referidos",
        "keywords": [
            "proceso referidos hubspot", "crear referido hubspot",
            "pasos referido", "marcar referido hubspot",
            "cómo añadir referido hubspot",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: BLOQUEOS (transversal)
    # ═══════════════════════════════════════════
    {
        "id": "bloqueos_tipos",
        "category": "BLOQUEOS",
        "title": "Tipos de bloqueos en proyectos CS",
        "keywords": [
            "tipos bloqueo", "qué es un bloqueo", "proyecto bloqueado",
            "bloqueo qué hacer", "tag bloqueo", "motivo bloqueo",
            "bloqueo cliente", "bloqueo interno",
        ],
    },
    {
        "id": "bloqueos_formulario_cliente",
        "category": "BLOQUEOS",
        "title": "Bloqueos - Comunicación con cliente",
        "keywords": [
            "formulario bloqueo cliente", "comunicar bloqueo",
            "decirle al cliente que está bloqueado",
            "plantilla bloqueo cliente", "mensaje bloqueo",
        ],
    },
    {
        "id": "bloqueos_memoria",
        "category": "BLOQUEOS",
        "title": "Bloqueos en creación de Memoria 1 y 2",
        "keywords": [
            "bloqueo memoria", "memoria bloqueada", "error memoria",
            "bloqueo creación memoria", "bloqueo presentación memoria",
            "web caída memoria", "sitio no carga memoria",
        ],
    },
    {
        "id": "bloqueos_tipologias_prd",
        "category": "BLOQUEOS",
        "title": "Tipologías de bloqueos CS ↔ PRD",
        "keywords": [
            "tipologías bloqueos", "bloqueos producción",
            "bloqueo prd", "guia bloqueos prd",
            "bloqueo web prd", "bloqueo seo prd", "bloqueo rrss prd",
            "tabla bloqueos", "causa bloqueo acción",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: TRAMITACIÓN (ampliado)
    # ═══════════════════════════════════════════
    {
        "id": "tramitacion_seo",
        "category": "TRAMITACIÓN",
        "title": "Tramitación SEO - Requisitos para la memoria",
        "keywords": [
            "tramitación seo", "memoria seo", "requisitos memoria seo",
            "evidencias seo", "justificación seo",
            "automáticamente genera seo",
        ],
    },
    {
        "id": "tramitacion_web",
        "category": "TRAMITACIÓN",
        "title": "Tramitación WEB/ECOM - Requisitos para la memoria",
        "keywords": [
            "tramitación web", "memoria web", "requisitos memoria web",
            "evidencias web", "justificación web ecom",
            "condiciones memoria web",
        ],
    },
    {
        "id": "tramitacion_rrss",
        "category": "TRAMITACIÓN",
        "title": "Tramitación RRSS - Requisitos para la memoria",
        "keywords": [
            "tramitación rrss", "memoria rrss", "requisitos memoria redes",
            "evidencias redes sociales", "justificación rrss",
            "condiciones memoria redes",
        ],
    },
    {
        "id": "tramitacion_pc",
        "category": "TRAMITACIÓN",
        "title": "Tramitación PC - Requisitos para la memoria",
        "keywords": [
            "tramitación pc", "memoria pc", "requisitos memoria pc",
            "evidencias pc ordenador", "justificación pc",
            "condiciones memoria ordenador",
        ],
    },
    {
        "id": "estados_memoria_hubspot_clickup",
        "category": "TRAMITACIÓN",
        "title": "Estados de Memoria en ClickUp ↔ HubSpot",
        "keywords": [
            "estados memoria clickup hubspot", "sincronización memoria",
            "estado memoria en qué sistema", "clickup hubspot memoria",
            "memoria estado sincronizado",
        ],
    },
    {
        "id": "errores_firma_memoria",
        "category": "TRAMITACIÓN",
        "title": "Errores frecuentes en firmas de memorias",
        "keywords": [
            "error firma memoria", "cliente no puede firmar memoria",
            "problema firma memoria", "dominio incorrecto memoria",
            "red social incorrecta memoria", "error en mi memoria",
        ],
    },

    # ═══════════════════════════════════════════
    # CATEGORÍA: AUTOMATIZACIONES
    # ═══════════════════════════════════════════
    {
        "id": "automatizacion_intercom_web",
        "category": "AUTOMATIZACIONES",
        "title": "Automatización en Intercom para proyectos web",
        "keywords": [
            "automatización intercom", "automatización web intercom",
            "qué hace la automatización", "activar automatización",
            "bot intercom web",
        ],
    },
    {
        "id": "automatizacion_proyecto_producido",
        "category": "AUTOMATIZACIONES",
        "title": "Automatización: Proyecto producido WEB-RRSS-SEO",
        "keywords": [
            "automatización proyecto producido", "proyecto listo automatización",
            "automatizar entrega", "web producida automatización",
            "seo producido automatización",
        ],
    },
]
