import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import card_style


def list_block(title: str, items: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(title, font_size="1.1rem", font_weight="600"),
        rx.vstack(
            *[rx.text(item) for item in items],
            spacing="2",
            color=text_color.BODY.value,
        ),
        spacing="3",
        align_items="start",
        **card_style,
    )


def education_section() -> rx.Component:
    return section_container(
        "formacion",
        section_header("Formación"),
        rx.grid(
            list_block(
                "Formación académica",
                [
                    "Ingeniería en Informática (INACAP)",
                    "Diplomado en Control de Gestión (PUC – Clase Ejecutiva UC)",
                    "Diplomado en Estrategias de Liderazgo Efectivo (PUC – Clase Ejecutiva UC)",
                ],
            ),
            list_block(
                "Cursos y certificaciones",
                [
                    "Compras Públicas (placeholder)",
                    "Automatización / Python (placeholder)",
                    "Gestión / Control (placeholder)",
                ],
            ),
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="4",
            width="100%",
        ),
    )
