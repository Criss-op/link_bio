import json
import reflex as rx
import urllib.parse


from link_bio.components.section import section_container, section_header


def _logo_path(base_name: str) -> str:
    # Asumimos PNG. Si tus logos son .svg, cambia a f"/iconos_education/{base_name}.svg"
    return f"/iconos_education/{base_name}.png"


def _bullets_stub(kind: str) -> list[str]:
    # 3-4 bullets inventados (placeholder) para no bloquear UI.
    if kind == "Titulación":
        return [
            "Base sólida en desarrollo de software y fundamentos de sistemas.",
            "Énfasis en resolución de problemas y estructura de proyectos.",
            "Trabajo aplicado orientado a resultados y mejora continua.",
            "Enfoque práctico con entregables y evaluaciones periódicas.",
        ]
    if kind == "Diplomado":
        return [
            "Herramientas aplicables a gestión, control y toma de decisiones.",
            "Metodologías para medir desempeño y alinear objetivos.",
            "Casos prácticos y aplicación en contexto real.",
            "Estructura y disciplina para ejecución sostenida.",
        ]
    # Curso
    return [
        "Contenidos aplicables de forma inmediata a contexto profesional.",
        "Conceptos clave + práctica guiada para consolidar habilidades.",
        "Estandarización de criterios y mejora del trabajo diario.",
    ]


# Datos del usuario (ordenados cronológicamente)
EDUCATION_ITEMS = [
    {
        "type": "Titulación",
        "title": "Ingeniería en Informática",
        "org": "Universidad Tecnológica de Chile (INACAP)",
        "year": "2022",
        "logo": _logo_path("inacap_education"),
        "bullets": _bullets_stub("Titulación"),
    },
    {
        "type": "Curso",
        "title": "Inducción a la Administración General del Estado",
        "org": "Contraloría General de la República",
        "year": "2023",
        "logo": _logo_path("contraloria_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Fundamentos en Ciberseguridad",
        "org": "Universidad de Santiago de Chile (USACH)",
        "year": "2023",
        "logo": _logo_path("usach_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Certificación de competencias en compras públicas (Nivel básico)",
        "org": "ChileCompra",
        "year": "2023",
        "logo": _logo_path("chilecompra_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Certificación de competencias en compras públicas (Nivel intermedio)",
        "org": "ChileCompra",
        "year": "2023",
        "logo": _logo_path("chilecompra_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Certificación de competencias en compras públicas (Nivel avanzado)",
        "org": "ChileCompra",
        "year": "2024",
        "logo": _logo_path("chilecompra_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Excel avanzado",
        "org": "Biblioredes",
        "year": "2024",
        "logo": _logo_path("biblioredes_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Herramientas de trabajo en equipo",
        "org": "Biblioredes",
        "year": "2024",
        "logo": _logo_path("biblioredes_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Procedimientos disciplinarios",
        "org": "FENPRUSS",
        "year": "2024",
        "logo": _logo_path("fenpruss_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Aplicación de Estrategias de Eficacia Operacional",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2025",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Storytelling: La estrategia como relato",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2025",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Metodologías para el control de la gestión de los recursos",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2026",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Herramientas para la gestión de la ética y responsabilidad social en la empresa",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2026",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Diseño de Técnicas de Gestión de la Calidad en las Organizaciones",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2026",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Diseño de Estrategias de Negociación para la Gestión",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2026",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Estrategias de Análisis de los Estados Financieros en las Organizaciones",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2026",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Curso",
        "title": "Habilidades de liderazgo y coaching para el entrenamiento de equipos",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2026",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Curso"),
    },
    {
        "type": "Diplomado",
        "title": "Control de gestión",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2026",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Diplomado"),
    },
    {
        "type": "Diplomado",
        "title": "Estrategias en liderazgo efectivo",
        "org": "Pontificia Universidad Católica de Chile",
        "year": "2026",
        "logo": _logo_path("puc_education"),
        "bullets": _bullets_stub("Diplomado"),
    },
]


def _desktop_card(item: dict, idx: int) -> rx.Component:
    pos_class = "edu-card--top" if idx % 2 == 0 else "edu-card--bottom"
    bullets_json = json.dumps(item["bullets"], ensure_ascii=False)
    bullets_payload = urllib.parse.quote(bullets_json, safe="")

    return rx.el.div(
        rx.el.div(item["type"], class_name="edu-chip"),
        rx.el.div(item["title"], class_name="edu-title"),
        rx.el.div(item["org"], class_name="edu-org"),
        rx.el.div(item["year"], class_name="edu-year"),
        rx.el.img(src=item["logo"], alt=item["org"], class_name="edu-logo"),
        class_name=f"edu-card {pos_class}",
        tab_index=0,
        role="button",
        aria_label=f"Ver detalle: {item['title']}",
        **{
            "data-type": item["type"],
            "data-title": item["title"],
            "data-org": item["org"],
            "data-year": item["year"],
            "data-logo": item["logo"],
            "data-bullets": bullets_payload,
        },
    )


def _mobile_item(item: dict) -> rx.Component:
    return rx.el.details(
        rx.el.summary(
            rx.el.div(
                rx.el.div(
                    rx.el.span(item["type"], class_name="edu-chip"),
                    rx.el.span("▶", class_name="edu-caret"),
                    class_name="edu-m-chiprow",
                ),
                rx.el.div(item["title"], class_name="edu-m-summary-title"),
                class_name="edu-m-summary-left",
            ),
            rx.el.div(
                rx.el.span(item["year"], class_name="edu-m-year"),
                rx.el.img(src=item["logo"], alt=item["org"], class_name="edu-m-logo"),
                class_name="edu-m-summary-right",
            ),
        ),
        rx.el.div(
            rx.el.div(item["org"], class_name="edu-m-org"),
            rx.el.ul(
                *[rx.el.li(b) for b in item["bullets"][:4]],
                class_name="edu-m-ul",
            ),
            class_name="edu-m-body",
        ),
        class_name="edu-m-item",
            **{"data-type": item["type"]},
    )


def _overlay() -> rx.Component:
    # Nota: sin “click para ver detalle”. El contrato es: click en card => overlay.
    return rx.el.div(
        rx.el.div(
            rx.el.button(
                "✕",
                id="edu-overlay-close",
                class_name="edu-overlay__close",
                type="button",
                aria_label="Cerrar",
            ),

            # Header: [tipo] [título] .......... [año] [logo]
            rx.el.div(
                rx.el.div(
                    rx.el.div(id="edu-o-type", class_name="edu-chip"),
                    rx.el.div(id="edu-o-title", class_name="edu-overlay__title"),
                    class_name="edu-overlay__left",
                ),
                rx.el.div(
                    rx.el.img(id="edu-o-logo", class_name="edu-overlay__logo", alt="Logo"),
                    class_name="edu-overlay__right",
                ),

                class_name="edu-overlay__header",
                
            ),
            


            # Segunda línea: institución
            rx.el.div(id="edu-o-org", class_name="edu-overlay__org"),

            # Bullets
            rx.el.ul(id="edu-o-bullets", class_name="edu-bullets"),
            rx.el.div(id="edu-o-year", class_name="edu-overlay__year edu-overlay__year--corner"),

            class_name="edu-overlay__panel",
            
        ),

        id="edu-overlay",
    )



def education_section() -> rx.Component:
    return section_container(
        "formacion",
        # CSS/JS locales del módulo (no ensucia global)
        rx.el.link(rel="stylesheet", href="/education_timeline.css"),
        rx.script(src="/education_timeline.js"),
        section_header(
            "Formación",
            "Aprendizaje autodidacta continuo en paralelo.",
        ),
        rx.el.div(
            # MOBILE
            rx.el.div(
                rx.el.div(
                    *[_mobile_item(item) for item in EDUCATION_ITEMS],
                    class_name="edu-mobile-list",
                ),
                class_name="edu-mobile",
            ),
            # DESKTOP
          rx.el.div(
            rx.el.div(
                rx.el.div(
                    *[_desktop_card(item, i) for i, item in enumerate(EDUCATION_ITEMS)],

                    # 👇 esto va DESPUÉS del último card
                    rx.el.div("Continuará ...", class_name="edu-endcap"),

                    class_name="edu-track",
                ),
                class_name="edu-viewport",
            ),
            _overlay(),
            class_name="edu-desktop",
        ),        
            class_name="edu-shell",
        ),
    )
