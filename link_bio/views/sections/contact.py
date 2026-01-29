import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.constants import EMAIL_ADDRESS, GITHUB_URL, LINKEDIN_URL
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import card_style


def contact_section() -> rx.Component:
    return section_container(
        "contacto",
        section_header("Contacto"),
        rx.text(
            "Si quieres conversar por una oportunidad profesional, colaboración o un proyecto específico, escríbeme. "
            "Respondo con claridad y directo al punto.",
        ),
        rx.box(
            rx.vstack(
                rx.text(EMAIL_ADDRESS, font_weight="600"),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Escríbeme",
                            background_color=color.PRIMARY.value,
                            color="white",
                            padding_x="1.5rem",
                            padding_y="0.75rem",
                        ),
                        href=f"mailto:{EMAIL_ADDRESS}",
                    ),
                    spacing="3",
                ),
                rx.hstack(
                    rx.link("LinkedIn", href=LINKEDIN_URL, is_external=True),
                    rx.link("GitHub", href=GITHUB_URL, is_external=True),
                    spacing="4",
                    color=text_color.MUTED.value,
                ),
                spacing="3",
                align_items="start",
            ),
            **card_style,
            width="100%",
        ),
    )
