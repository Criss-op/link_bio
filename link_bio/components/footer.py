import datetime
import reflex as rx
from link_bio.constants import BRAND_NAME, EMAIL_ADDRESS, FULL_NAME, GITHUB_URL, LINKEDIN_URL, TAGLINE
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import MAX_WIDTH


def footer() -> rx.Component:
    return rx.box(
        rx.box(class_name="footer-accent"),
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            f"{BRAND_NAME} ({FULL_NAME})",
                            color=text_color.HEADER.value,
                            font_weight="600",
                        ),
                        rx.text(TAGLINE, color=text_color.FOOTER.value),
                        rx.text(
                            "Built with Reflex • Process / Automation / Strategy",
                            class_name="footer-microcopy",
                        ),
                        spacing="2",
                        align_items="start",
                        max_width="360px",
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Navegación", color=text_color.HEADER.value, font_weight="600"),
                            rx.link("Inicio", href="#inicio"),
                            rx.link("Perfil", href="#perfil"),
                            rx.link("Experiencia", href="#experiencia"),
                            rx.link("Formación", href="#formacion"),
                            rx.link("Habilidades", href="#habilidades"),
                            spacing="2",
                            align_items="start",
                            color=text_color.FOOTER.value,
                        ),
                        rx.vstack(
                            rx.text("Contacto", color=text_color.HEADER.value, font_weight="600"),
                            rx.text(EMAIL_ADDRESS, color=text_color.FOOTER.value),
                            rx.link("LinkedIn", href=LINKEDIN_URL, is_external=True),
                            rx.link("GitHub", href=GITHUB_URL, is_external=True),
                            spacing="2",
                            align_items="start",
                            color=text_color.FOOTER.value,
                        ),
                        spacing="6",
                        width="100%",
                        justify="between",
                        flex_wrap="wrap",
                    ),
                    spacing="6",
                    width="100%",
                    justify="between",
                    flex_wrap="wrap",
                ),
                rx.text(
                    f"© {datetime.date.today().year}",
                    color=text_color.FOOTER.value,
                ),
                spacing="6",
                align="start",
                padding_y="3.5rem",
                max_width=MAX_WIDTH,
                width="100%",
            ),
            width="100%",
        ),
        border_top=f"1px solid {color.BORDER.value}",
        background_color=color.SURFACE.value,
        padding_x="1.5rem",
        id="footer",
    )
