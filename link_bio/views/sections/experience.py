import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import card_style


def experience_card(role: str, context: str, bullets: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(role, font_size="1.2rem", font_weight="600"),
        rx.text(context, color=text_color.MUTED.value),
        rx.vstack(
            *[rx.text(f"• {item}") for item in bullets],
            spacing="2",
            color=text_color.BODY.value,
        ),
        spacing="3",
        align_items="start",
        **card_style,
    )


def experience_section() -> rx.Component:
    return section_container(
        "experiencia",
        section_header("Experiencia"),
        rx.grid(
            experience_card(
                "Gestión de contratos y procesos",
                "Sector público / entornos administrativos con múltiples actores y cumplimiento normativo.",
                [
                    "Coordinación de procesos con unidades técnicas y administrativas.",
                    "Estandarización de flujos y control de hitos para reducir retrasos.",
                    "Mejora de trazabilidad documental y orden operativo.",
                    "Priorización basada en riesgo, plazos y continuidad de servicio.",
                ],
            ),
            experience_card(
                "Automatización y soporte a la gestión",
                "Implementación progresiva de herramientas para reducir tareas manuales.",
                [
                    "Identificación de tareas repetitivas con alto costo de tiempo.",
                    "Diseño de automatizaciones y plantillas para acelerar ejecución.",
                    "Estructuración de información para reporting y control.",
                ],
            ),
            columns=["1", "2"],
            spacing="4",
            width="100%",
        ),
    )
