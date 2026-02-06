import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import card_style


def objective_card(title: str, items: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(title, font_size="1.1rem", font_weight="600"),
        rx.vstack(
            *[rx.text(f"• {item}", color=text_color.BODY.value, opacity="0.90") for item in items],
            spacing="2",
            align_items="start",
            width="100%",
        ),
        spacing="3",
        align_items="start",
        width="100%",
        **card_style,
    )


def objectives_section() -> rx.Component:
    return section_container(
        "objetivos",
        rx.box(
            section_header("Objetivos", "Lo que estoy construyendo"),
            class_name="sr-fade-up",
            custom_attrs={"data-sr-delay": "0"},
        ),
        rx.text(
            "Mi foco es construir una base sólida: procesos claros, trazabilidad, y automatizaciones pequeñas pero constantes. "
            "No busco complejidad; busco control, continuidad y mejora real.",
            color=text_color.BODY.value,
            class_name="sr-fade-up",
            custom_attrs={"data-sr-delay": "120"},
        ),
        rx.grid(
            rx.box(
                objective_card(
                    "Corto plazo",
                    [
                        "Estandarizar plantillas y checklists críticos.",
                        "Reducir retrabajo y tiempos muertos en coordinación.",
                        "Mejorar visibilidad de hitos y riesgos por proceso.",
                    ],
                ),
                class_name="sr-card",
                custom_attrs={"data-sr-delay": "240"},
            ),
            rx.box(
                objective_card(
                    "Mediano plazo",
                    [
                        "Automatizar tareas repetitivas (captura, validación, reportes).",
                        "Centralizar seguimiento de procesos (tablero simple, sin sobre-ingeniería).",
                        "Mejorar indicadores de cumplimiento y tiempos de ciclo.",
                    ],
                ),
                class_name="sr-card",
                custom_attrs={"data-sr-delay": "360"},
            ),
            rx.box(
                objective_card(
                    "Largo plazo",
                    [
                        "Consolidar una forma de trabajo sostenida y replicable.",
                        "Escalar mejoras a más áreas y procesos sin perder control.",
                        "Evolucionar hacia roles de gestión/estrategia con base técnica.",
                    ],
                ),
                class_name="sr-card",
                custom_attrs={"data-sr-delay": "480"},
            ),
            columns=rx.breakpoints(initial="1", md="2", lg="3"),
            spacing="4",
            width="100%",
        ),
    )
