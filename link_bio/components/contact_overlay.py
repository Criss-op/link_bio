import reflex as rx
from link_bio.constants import EMAIL_ADDRESS, GITHUB_URL, LINKEDIN_URL
from link_bio.state import UIState
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color


def contact_overlay() -> rx.Component:
    return rx.cond(
        UIState.contact_open,
        rx.el.div(
            rx.el.div(
                class_name="contact-backdrop",
                on_click=UIState.close_contact,
            ),
            rx.el.div(
                rx.hstack(
                    rx.text("Contacto", font_size="1.4rem", font_weight="600"),
                    rx.spacer(),
                    rx.button(
                        rx.icon(tag="x", size=20),
                        variant="ghost",
                        on_click=UIState.close_contact,
                    ),
                    width="100%",
                    align="center",
                ),
                rx.text(
                    "¿Hablamos? Puedes escribirme por correo o conectar en LinkedIn para coordinar.",
                    color=text_color.BODY.value,
                ),
                rx.vstack(
                    rx.link(
                        rx.button(
                            "Email",
                            background_color=color.PRIMARY.value,
                            color= color.BACKGROUND.value,
                            padding_x="1.5rem",
                            padding_y="0.75rem",
                        ),
                        href=f"mailto:{EMAIL_ADDRESS}",
                    ),
                    rx.link("LinkedIn", href=LINKEDIN_URL, is_external=True),
                    rx.link("GitHub", href=GITHUB_URL, is_external=True),
                    spacing="3",
                    align_items="start",
                ),
                class_name="contact-phone",
            ),
            class_name="contact-overlay",
        ),
    )
