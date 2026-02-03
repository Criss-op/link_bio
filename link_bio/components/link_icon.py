import reflex as rx
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color


def link_icon(label: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(tag=icon, size=18),
            rx.text(label),
            spacing="2",
            align="center",
        ),
        href=href,
        is_external=True,
        class_name="social-chip",
    )
