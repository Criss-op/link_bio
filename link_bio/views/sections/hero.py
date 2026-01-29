import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.section import section_container
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


def hero_section() -> rx.Component:
    show_cv = CV_URL and "{" not in CV_URL
    social_links = [
        link_icon("LinkedIn", "linkedin", LINKEDIN_URL),
        link_icon("GitHub", "github", GITHUB_URL),
        link_icon("Email", "mail", f"mailto:{EMAIL_ADDRESS}"),
    ]
    if show_cv:
        social_links.append(link_icon("CV", "file-text", CV_URL))

    return section_container(
        "inicio",
        rx.flex(
            rx.box(
                rx.image(
                    src="avatar_cris_vector_white.png",
                    alt=FULL_NAME,
                    width=rx.breakpoints(initial="200px", md="240px", lg="260px"),
                    height=rx.breakpoints(initial="200px", md="240px", lg="260px"),
                    border_radius="24px",
                    border=f"1px solid {color.BORDER.value}",
                    background_color=color.SURFACE.value,
                    object_fit="contain",
                    id="cris-avatar",
                    transition="transform 180ms ease-out",
                ),
                id="cris-avatar-wrap",
                class_name="avatar-wrap",
                flex_shrink="0",
            ),
            rx.vstack(
                rx.text(
                    "Hola, mi nombre es",
                    font_size=rx.breakpoints(initial="0.95rem", md="1.05rem"),
                    color=text_color.MUTED.value,
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
                max_width="600px",
            ),
            direction=rx.breakpoints(initial="column", md="row"),
            spacing="6",
            align="center",
            width="100%",
            class_name="hero-layout",
        ),
        rx.box(
            rx.icon(tag="chevron-down", size=36),
            class_name="scroll-indicator",
            color=text_color.MUTED.value,
        ),
    )
