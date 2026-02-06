import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.styles import card_style


def methodologies_section() -> rx.Component:
    return section_container(
        "metodologias",
        rx.box(
            section_header("Metodologías", "Cómo las aplico"),
            class_name="sr-fade-up",
        ),
        rx.text(
            "Uso metodologías como herramientas, no como discurso. Cuando el contexto lo permite, estructuro el trabajo en ciclos "
            "cortos, con hitos claros y revisión frecuente. Defino estándares mínimos (nombres, plantillas, criterios) para reducir "
            "errores y acelerar coordinación.",
            class_name="sr-fade-up",
        ),
        rx.grid(
            rx.box(rx.box("Gestión por hitos y control de avance", **card_style), class_name="sr-card"),
            rx.box(rx.box("Estandarización y checklists", **card_style), class_name="sr-card"),
            rx.box(rx.box("Mejora continua (iteración)", **card_style), class_name="sr-card"),
            rx.box(rx.box("Automatización incremental", **card_style), class_name="sr-card"),
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="4",
            width="100%",
        ),
    )
