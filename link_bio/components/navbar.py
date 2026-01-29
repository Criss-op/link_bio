import reflex as rx
from link_bio.state import UIState
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
]


def nav_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        class_name="navbar-link",
        color=text_color.BODY.value,
        font_weight="500",
        _hover={"color": color.PRIMARY.value},
        on_click=UIState.close_menu,
    )


def navbar() -> rx.Component:
    desktop_links = rx.hstack(
        *[nav_link(label, href) for label, href in NAV_ITEMS],
        rx.button(
            "Contacto",
            class_name="navbar-link",
            color=text_color.BODY.value,
            font_weight="500",
            variant="ghost",
            _hover={"color": color.PRIMARY.value},
            on_click=UIState.open_contact,
        ),
        rx.link(
            "Proyectos 🔒",
            href="/projects",
            class_name="navbar-link",
            color=text_color.BODY.value,
            font_weight="600",
            _hover={"color": color.PRIMARY.value},
        ),
        spacing="4",
        align="center",
        display=rx.breakpoints(initial="none", md="none", lg="flex"),
    )

    mobile_menu = rx.cond(
        UIState.mobile_open,
        rx.vstack(
            *[nav_link(label, href) for label, href in NAV_ITEMS],
            rx.button(
                "Contacto",
                class_name="navbar-link",
                color=text_color.BODY.value,
                font_weight="500",
                variant="ghost",
                _hover={"color": color.PRIMARY.value},
                on_click=UIState.open_contact,
            ),
            rx.link(
                "Proyectos 🔒",
                href="/projects",
                class_name="navbar-link",
                color=text_color.BODY.value,
                font_weight="600",
                _hover={"color": color.PRIMARY.value},
                on_click=UIState.close_menu,
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
                    desktop_links,
                    rx.button(
                        rx.icon(tag="menu", size=22),
                        variant="ghost",
                        color=text_color.HEADER.value,
                        display=rx.breakpoints(initial="flex", md="flex", lg="none"),
                        on_click=UIState.toggle_menu,
                    ),
                    width="100%",
                    align="center",
                    justify="between",
                ),
                rx.box(
                    mobile_menu,
                    display=rx.breakpoints(initial="block", md="block", lg="none"),
                ),
                max_width=MAX_WIDTH,
                width=rx.breakpoints(initial="calc(100% - 2rem)", md="fit-content"),
                padding_x="1.5rem",
                class_name="navbar-pill",
            ),
            width="100%",
        ),
        class_name="navbar-wrapper",
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="999",
        padding_y="0.75rem",
    )
