import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.styles import card_style


def methodologies_section() -> rx.Component:
    return section_container(
        "metodologias",
        section_header("Metodologías", "Cómo las aplico"),
        rx.text(
            "Uso metodologías como herramientas, no como discurso. Cuando el contexto lo permite, estructuro el trabajo en ciclos "
            "cortos, con hitos claros y revisión frecuente. Defino estándares mínimos (nombres, plantillas, criterios) para reducir "
            "errores y acelerar coordinación.",
        ),
        rx.grid(
            rx.box("Gestión por hitos y control de avance", **card_style),
            rx.box("Estandarización y checklists", **card_style),
            rx.box("Mejora continua (iteración)", **card_style),
            rx.box("Automatización incremental", **card_style),
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="4",
            width="100%",
        ),
    )
