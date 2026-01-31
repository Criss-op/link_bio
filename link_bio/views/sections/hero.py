import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import MAX_WIDTH
from link_bio.constants import (
    BRAND_NAME,
    CV_URL,
    EMAIL_ADDRESS,
    FULL_NAME,
    GITHUB_URL,
    LINKEDIN_URL,
    TAGLINE,
)
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color


def hero_container(section_id: str, main: rx.Component, *overlays: rx.Component) -> rx.Component:
    return rx.box(
        rx.center(
            rx.box(
                main,
                max_width=MAX_WIDTH,
                width="100%",
            ),
            width="100%",
            min_height=rx.breakpoints(
                initial="calc(100vh - var(--navbar-safe-top) - 3.5rem)",
                md="calc(100vh - var(--navbar-safe-top) - 4.5rem)",
            ),
        ),
        *overlays,
        id=section_id,
        padding_x="1.5rem",
        padding_top="var(--navbar-safe-top)",
        padding_bottom=rx.breakpoints(initial="3.5rem", md="4.5rem"),
        scroll_margin_top="6rem",
        color=text_color.BODY.value,
        position="relative",
        class_name="section",
        width="100%",
    )


def hero_section() -> rx.Component:
    show_cv = CV_URL and "{" not in CV_URL
    social_links = [
        link_icon("LinkedIn", "linkedin", LINKEDIN_URL),
        link_icon("GitHub", "github", GITHUB_URL),
        link_icon("Email", "mail", f"mailto:{EMAIL_ADDRESS}"),
    ]
    if show_cv:
        social_links.append(link_icon("CV", "file-text", CV_URL))

    stars_layer = rx.box(id="hero-stars", class_name="hero-stars")

    main = rx.flex(
        rx.box(
            rx.box(
                rx.box(
                    rx.image(
                        src="avatar_cris_vector_white.png",
                        alt=FULL_NAME,
                        width=rx.breakpoints(initial="225px", md="275px", lg="294px"),
                        height=rx.breakpoints(initial="250px", md="300px", lg="325px"),
                        object_fit="contain",
                        id="cris-avatar",
                        class_name="avatar-img",
                        transition="transform 180ms ease-out",
                    ),
                    class_name="avatar-inner",
                    border_radius="80px",
                ),
                class_name="avatar-frame",
                border_radius="80px",
            ),
            id="cris-avatar-wrap",
            class_name="avatar-wrap",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(
                "Hola, mi nombre es",
                font_size=rx.breakpoints(initial="0.95rem", md="1.05rem"),
                color=text_color.PRIMARY.value,
                font_weight="500",
            ),
            rx.heading(
                "Cristóbal Opazo.",
                font_size=rx.breakpoints(initial="2.2rem", md="3rem", lg="3.4rem"),
                line_height="1.05",
            ),
            rx.text(
                TAGLINE,
                font_size=rx.breakpoints(initial="1rem", md="1.15rem"),
                color=color.PRIMARY.value,
                font_weight="600",
            ),
            rx.hstack(
                *social_links,
                spacing="4",
                flex_wrap="wrap",
            ),
            rx.text(
                """Hola, soy Ingeniero en Informática, con experiencia en gestión de procesos, compras públicas y entornos operativos. 
Disfruto metiéndome donde hay desorden: flujos poco claros, tareas repetidas y sistemas que no conversan. 
Me gusta moverme en la intersección entre gestión, tecnología y automatización: ordenar sistemas, optimizar flujos 
y construir soluciones prácticas que se notan en el día a día. ¡Bienvenid@!""",
                color=text_color.BODY.value,
                font_size=rx.breakpoints(initial="1rem", md="1.05rem", lg="1.1rem"),
                line_height="1.7",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        "Ver Perfil",
                        background_color=color.PRIMARY.value,
                        color="#0a192f",
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                    ),
                    href="#perfil",
                ),
                rx.link(
                    rx.button(
                        "Ver Experiencia",
                        variant="outline",
                        border=f"1px solid {color.BORDER.value}",
                        color=text_color.HEADER.value,
                        padding_x="1.5rem",
                        padding_y="0.75rem",
                    ),
                    href="#experiencia",
                ),
                spacing="3",
                flex_wrap="wrap",
            ),
            spacing="4",
            align_items="start",
            max_width="800px",
        ),
        direction=rx.breakpoints(initial="column", md="row"),
        spacing="6",
        align="center",
        justify="center",
        width="100%",
        class_name="hero-layout",
        position="relative",
        z_index="1",  # siempre arriba del polvo
    )

    scroll_indicator = rx.box(
        rx.icon(tag="chevron-down", size=36),
        class_name="scroll-indicator",
        color=text_color.MUTED.value,
    )

    return hero_container("inicio", main, stars_layer, scroll_indicator)
