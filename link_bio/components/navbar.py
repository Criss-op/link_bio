import reflex as rx
from link_bio.constants import BRAND_NAME
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import MAX_WIDTH


NAV_ITEMS = [
    ("Inicio", "#inicio"),
    ("Perfil", "#perfil"),
    ("Experiencia", "#experiencia"),
    ("Formación", "#formacion"),
    ("Habilidades", "#habilidades"),
    ("Metodologías", "#metodologias"),
    ("Objetivos", "#objetivos"),
    ("Contacto", "#contacto"),
]


class NavbarState(rx.State):
    mobile_open: bool = False

    def toggle_menu(self):
        self.mobile_open = not self.mobile_open

    def close_menu(self):
        self.mobile_open = False


def nav_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        color=text_color.BODY.value,
        font_weight="500",
        _hover={"color": color.PRIMARY.value},
        on_click=NavbarState.close_menu,
    )


def navbar() -> rx.Component:
    desktop_links = rx.hstack(
        *[nav_link(label, href) for label, href in NAV_ITEMS],
        rx.link(
            "Proyectos 🔒",
            href="/projects",
            color=text_color.BODY.value,
            font_weight="600",
            _hover={"color": color.PRIMARY.value},
        ),
        spacing="5",
        align="center",
        display=["none", "none", "flex"],
    )

    mobile_menu = rx.cond(
        NavbarState.mobile_open,
        rx.vstack(
            *[nav_link(label, href) for label, href in NAV_ITEMS],
            rx.link(
                "Proyectos 🔒",
                href="/projects",
                color=text_color.BODY.value,
                font_weight="600",
                _hover={"color": color.PRIMARY.value},
                on_click=NavbarState.close_menu,
            ),
            spacing="4",
            align_items="start",
            padding_top="1rem",
            padding_bottom="1rem",
        ),
    )

    return rx.box(
        rx.center(
            rx.box(
                rx.hstack(
                    rx.text(
                        BRAND_NAME,
                        color=text_color.HEADER.value,
                        font_weight="600",
                        font_size="1.2rem",
                    ),
                    rx.spacer(),
                    desktop_links,
                    rx.button(
                        rx.icon(tag="menu", size=22),
                        variant="ghost",
                        color=text_color.HEADER.value,
                        display=["flex", "flex", "none"],
                        on_click=NavbarState.toggle_menu,
                    ),
                    width="100%",
                    align="center",
                ),
                rx.box(
                    mobile_menu,
                    display=["block", "block", "none"],
                ),
                max_width=MAX_WIDTH,
                width="100%",
                padding_x="1.5rem",
            ),
            width="100%",
        ),
        position="sticky",
        top="0",
        z_index="999",
        background_color=color.BACKGROUND.value,
        border_bottom=f"1px solid {color.BORDER.value}",
        padding_y="0.75rem",
    )
