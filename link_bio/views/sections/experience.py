import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import card_style


def experience_card(title: str, context: str, detail: str, bullets: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(title, font_size="1.2rem", font_weight="600"),
        rx.text(context, color=text_color.MUTED.value),
        rx.text(detail, color=text_color.BODY.value),
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
        rx.box(
            section_header("Experiencia"),
            class_name="sr-fade-up",
            custom_attrs={"data-sr-delay": "0"},
        ),
        rx.grid(
            rx.box(
                experience_card(
                    "2023–2025 | Hospital San Juan de Dios de Cauquenes (Sector público)",
                    "Departamento de Abastecimiento — Compras públicas, licitaciones y contratos.",
                    "Rol: Gestión y coordinación de procesos de abastecimiento.",
                    [
                        "Coordinación de procesos entre áreas técnicas y administrativas.",
                        "Responsable de la gestión de procesos licitatorios y contratos asociados.",
                        "Seguimiento de hitos, plazos y respaldos para asegurar trazabilidad.",
                        "Estandarización de documentos, plantillas y checklists para reducir retrabajo.",
                    ],
                ),
                class_name="sr-card",
                custom_attrs={"data-sr-delay": "180"},
            ),
            columns=rx.breakpoints(initial="1", md="1"),
            spacing="4",
            width="100%",
        ),
    )
