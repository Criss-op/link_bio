import reflex as rx
from link_bio.state import UIState
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import MAX_WIDTH
from link_bio.constants import EMAIL_ADDRESS



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


def drawer_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        class_name="mobile-menu-link",
        color=text_color.HEADER.value,
        font_weight="600",
        _hover={"color": color.PRIMARY.value},
        on_click=UIState.close_menu,
    )


def navbar() -> rx.Component:
    # ---------------- Desktop (lg+) ----------------
    desktop_links = rx.hstack(
        *[nav_link(label, href) for label, href in NAV_ITEMS],
        
        rx.link(
            "Proyectos 🔒",
            href="/projects",
            class_name="navbar-link",
            color=text_color.BODY.value,
            font_weight="600",
            _hover={"color": color.PRIMARY.value},
            style={"marginLeft": "0.35rem"},
        ),
        spacing="4",
        align="center",
        display=rx.breakpoints(initial="none", md="flex", lg="flex"),
    )

    desktop_pill = rx.center(
        rx.box(
            rx.hstack(
                desktop_links,
                width="100%",
                align="center",
                justify="between",
            ),
            max_width=MAX_WIDTH,
            width="fit-content",
            padding_x="1.5rem",
            class_name="navbar-pill",
        ),
        width="100%",
        display=rx.breakpoints(initial="none", md="flex", lg="flex"),
    )

    # ---------------- Mobile/Tablet (<lg) ----------------
    hamburger_icon = rx.box(
        rx.box(class_name="hamburger-line"),
        rx.box(class_name="hamburger-line"),
        rx.box(class_name="hamburger-line"),
        class_name=rx.cond(UIState.mobile_open, "hamburger is-open", "hamburger"),
    )

    mobile_bar = rx.hstack(
        rx.button(
            hamburger_icon,
            variant="ghost",
            color=text_color.HEADER.value,
            on_click=UIState.toggle_menu,
            class_name="hamburger-btn",
            style={
                "padding": "0.55rem",
                "background": "transparent",
                "border": "none",
                "boxShadow": "none",
                "outline": "none",
            },
            _hover={
                "background": "transparent",
                "border": "none",
                "boxShadow": "none",
            },
            _active={
                "background": "transparent",
                "border": "none",
                "boxShadow": "none",
            },
            _focus_visible={
                "outline": "none",
                "boxShadow": "none",
            },
        ),
        width="100%",
        align="center",
        justify="end",
    )


    mobile_pill = rx.box(
        rx.box(
            mobile_bar,
            width="fit-content",
            padding_x="1.5rem",   # padding interno del pill
            class_name="navbar-pill",
            margin_right="2rem",
        ),
        width="100%",
        display=rx.breakpoints(initial="flex", md="none", lg="none"),
        justify_content="flex-end",

    )

    # ---------------- Drawer full height + backdrop ----------------
    # Importante: el overlay se mantiene montado para permitir animación al cerrar.
    mobile_drawer = rx.box(
    rx.box(
        class_name="mobile-menu-backdrop",
        on_click=UIState.close_menu,
    ),
    rx.box(
        rx.vstack(
            *[drawer_link(label, href) for label, href in NAV_ITEMS],
            rx.link(
                "Contacto",
                href=f"mailto:{EMAIL_ADDRESS}",
                class_name="mobile-menu-link",
                color=text_color.HEADER.value,
                font_weight="600",
                _hover={"color": color.PRIMARY.value},
                on_click=UIState.close_menu,
                width="100%",
            ),
            rx.link(
                "Proyectos 🔒",
                href="/projects",
                class_name="mobile-menu-link",
                color=text_color.HEADER.value,
                font_weight="600",
                _hover={"color": color.PRIMARY.value},
                on_click=UIState.close_menu,
            ),
            spacing="3",
            align_items="start",
            width="100%",
            class_name="drawer-links",
        ),
        class_name="mobile-menu-panel",
    ),
    class_name=rx.cond(
        UIState.mobile_open,
        "mobile-menu-overlay is-open",
        "mobile-menu-overlay",
    ),
    display=rx.breakpoints(initial="flex", md="none", lg="none"),
)


    # ---------------- Wrapper fixed ----------------
    return rx.box(
        rx.box(
            desktop_pill,
            mobile_pill,
            class_name="navbar-wrapper",
            id="navbar",
            position="fixed",
            top="0",
            left="0",
            right="0",
            z_index="3000",
            padding_y=rx.breakpoints(initial="1rem", md="1rem", lg="0.75rem"),
        ),
        mobile_drawer,
    )
