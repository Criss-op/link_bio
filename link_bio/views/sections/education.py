import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import card_style


def education_card(title: str, org: str, period: str, bullets: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(title, font_size="1.2rem", font_weight="600"),
        rx.text(org, color=text_color.BODY.value, opacity="0.80"),
        rx.text(period, color=text_color.BODY.value, opacity="0.70"),
        rx.vstack(
            *[rx.text(f"• {item}", color=text_color.BODY.value, opacity="0.90") for item in bullets],
            spacing="2",
            align_items="start",
            width="100%",
        ),
        spacing="3",
        align_items="start",
        width="100%",
        **card_style,
    )


def education_section() -> rx.Component:
    return section_container(
        "formacion",
        rx.box(
            section_header("Formación", "Base técnica + gestión + liderazgo"),
            class_name="sr-fade-up",
            custom_attrs={"data-sr-delay": "0"},
        ),
        rx.grid(
            rx.box(
                education_card(
                    "Ingeniería en Informática",
                    "INACAP",
                    "Formación universitaria",
                    [
                        "Base sólida en desarrollo, lógica y resolución de problemas.",
                        "Enfoque práctico: implementación, mejora y mantenimiento.",
                    ],
                ),
                class_name="sr-card",
                custom_attrs={"data-sr-delay": "180"},
            ),
            rx.box(
                education_card(
                    "Diplomado en Control de Gestión",
                    "Pontificia Universidad Católica de Chile (PUC) — Clase Ejecutiva UC",
                    "En curso / reciente",
                    [
                        "Indicadores, control y seguimiento de desempeño.",
                        "Enfoque en toma de decisiones con métricas y objetivos.",
                    ],
                ),
                class_name="sr-card",
                custom_attrs={"data-sr-delay": "300"},
            ),
            rx.box(
                education_card(
                    "Diplomado en Estrategias para un Liderazgo Efectivo",
                    "Pontificia Universidad Católica de Chile (PUC)",
                    "En curso / reciente",
                    [
                        "Comunicación, coordinación y liderazgo aplicado.",
                        "Herramientas de influencia y gestión de equipos.",
                    ],
                ),
                class_name="sr-card",
                custom_attrs={"data-sr-delay": "420"},
            ),
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="4",
            width="100%",
        ),
    )
