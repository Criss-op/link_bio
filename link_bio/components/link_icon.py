import reflex as rx
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color


def link_icon(label: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(tag=icon, size=18),
            rx.text(label, font_size="0.9rem"),
            spacing="2",
        ),
        href=url,
        is_external=True,
        color=text_color.BODY.value,
        _hover={
            "color": color.PRIMARY.value,
        },
    )
