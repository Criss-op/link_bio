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
        padding_x=rx.breakpoints(initial="2.5rem", md="5.5rem", lg="1.5rem"),
        padding_top="var(--navbar-safe-top)",
        padding_bottom=rx.breakpoints(initial="3.5rem", md="4.5rem"),
        scroll_margin_top="6rem",
        color=text_color.BODY.value,
        position="relative",
        class_name="section",
        width="100%",
        box_sizing="border-box",
    )


SPARKLE_LEFT = rx.html("""
<svg width="50" height="22" viewBox="20 0 40 24" fill="none" aria-hidden="true" preserveAspectRatio="xMidYMid meet">
  <path d="
    M50 2
    L54 10
    L60 12
    L54 14
    L50 22
    L46 14
    L20 12
    L46 10
    Z"
    fill="white" fill-opacity="0.92"
  />
  <path d="
    M50 2
    L54 10
    L60 12
    L54 14
    L50 22
    L46 14
    L20 12
    L46 10
    Z"
    stroke="rgba(62,231,255,0.60)"
    stroke-width="1.2"
    stroke-linejoin="round"
  />
</svg>
""")

SPARKLE_RIGHT = rx.html("""
<svg width="50" height="22" viewBox="40 0 40 24" fill="none" aria-hidden="true" preserveAspectRatio="xMidYMid meet">
  <path d="
    M50 2
    L54 10
    L80 12
    L54 14
    L50 22
    L46 14
    L40 12
    L46 10
    Z"
    fill="white" fill-opacity="0.92"
  />
  <path d="
    M50 2
    L54 10
    L80 12
    L54 14
    L50 22
    L46 14
    L40 12
    L46 10
    Z"
    stroke="rgba(62,231,255,0.60)"
    stroke-width="1.2"
    stroke-linejoin="round"
  />
</svg>
""")


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
                        width=rx.breakpoints(initial="225px", md="240px", lg="248px"),
                        height=rx.breakpoints(initial="336px", md="358px", lg="370px"),
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
            class_name="avatar-wrap sr-card",
            custom_attrs={"data-sr-delay": "900"},
            flex_shrink="0",
        ),

        rx.vstack(
            # 1) BLOQUE CENTRADO (manda el TAGLINE)
            rx.vstack(
                rx.text(
                    "Hola, mi nombre es:",
                    font_size=rx.breakpoints(initial="0.95rem", md="1.05rem"),
                    color=text_color.PRIMARY.value,
                    font_weight="700",
                    text_align="center",
                    class_name="sr-fade-up",
                    custom_attrs={"data-sr-delay": "0"},
                ),
                rx.hstack(
                    rx.box(SPARKLE_LEFT, class_name="name-sparkle-wrap left"),
                    rx.heading(
                        "Cristóbal Opazo",
                        font_size=rx.breakpoints(initial="2.2rem", md="3rem", lg="3.4rem"),
                        line_height="1.05",
                        margin="0",
                        class_name="hero-name",
                        flex="1",
                        min_width="0",
                        text_align="center",
                    ),
                    rx.box(SPARKLE_RIGHT, class_name="name-sparkle-wrap right"),
                    align="center",
                    justify="center",
                    spacing="0",
                    width="100%",
                    class_name="sr-fade-up",
                    custom_attrs={"data-sr-delay": "160"},
                ),

                rx.heading(
                    TAGLINE,
                    font_size=rx.breakpoints(initial="1.1rem", md="1.5rem", lg="1.7rem"),
                    line_height="1.05",
                    color=color.PRIMARY.value,
                    font_weight="700",
                    text_align="center",
                    class_name="sr-fade-up",
                    custom_attrs={"data-sr-delay": "320"},
                ),
                spacing="2",
                align_items="center",
                width="fit-content",
                max_width="100%",
                margin_x="auto",
            ),

            # 2) LINKS START (pegados a la izquierda)
            rx.hstack(
                *social_links,
                spacing="4",
                flex_wrap="wrap",
                width="100%",
                justify="start",
                class_name="sr-fade-up",
                custom_attrs={"data-sr-delay": "480"},
            ),

           # PÁRRAFO
            rx.text(
                "Soy Ingeniero en Informática, con experiencia en ",
                rx.el.strong("gestión de procesos, compras públicas y entornos operativos.", style={"fontWeight": "800"}),
                " Disfruto metiéndome donde hay desorden: flujos poco claros, tareas repetidas y sistemas que no conversan. "
                "Me gusta moverme en la intersección entre ",
                rx.el.strong("gestión, tecnología y automatización:", style={"fontWeight": "800"}),
                " ordenar sistemas, optimizar flujos y construir soluciones prácticas que se notan en el día a día. ",
                rx.el.strong("¡Bienvenid@!", style={"fontWeight": "800"}),
                color=text_color.BODY.value,
                font_size=rx.breakpoints(initial="1rem", md="1.05rem", lg="1.1rem"),
                line_height="1.7",
                max_width="800px",
                width="100%",
                class_name="sr-fade-up",
                custom_attrs={"data-sr-delay": "640"},
            ),


            # CARRUSEL PLANO (limitado a 800px y recortado para que no se desborde)
            rx.box(
                rx.box(
                    rx.box(
                        rx.image(src="/icons_skills/asana.png", class_name="skills-icon", alt="Asana"),
                        rx.image(src="/icons_skills/excel.png", class_name="skills-icon", alt="Excel"),
                        rx.image(src="/icons_skills/lean.png", class_name="skills-icon", alt="Lean"),
                        rx.image(src="/icons_skills/justintime.png", class_name="skills-icon", alt="Just in Time"),
                        rx.image(src="/icons_skills/kanban.png", class_name="skills-icon", alt="Kanban"),
                        rx.image(src="/icons_skills/mercadopublico.png", class_name="skills-icon", alt="Mercado Público"),
                        rx.image(src="/icons_skills/scrum.png", class_name="skills-icon", alt="Scrum"),
                        rx.image(src="/icons_skills/php.png", class_name="skills-icon", alt="PHP"),
                        rx.image(src="/icons_skills/python.png", class_name="skills-icon", alt="Python"),
                        rx.image(src="/icons_skills/js.png", class_name="skills-icon", alt="JavaScript"),
                        rx.image(src="/icons_skills/css3.png", class_name="skills-icon", alt="CSS3"),
                        rx.image(src="/icons_skills/sass.png", class_name="skills-icon", alt="Sass"),
                        rx.image(src="/icons_skills/json.png", class_name="skills-icon", alt="JSON"),
                        rx.image(src="/icons_skills/html5.png", class_name="skills-icon", alt="HTML5"),
                        rx.image(src="/icons_skills/github.png", class_name="skills-icon", alt="GitHub"),
                        rx.image(src="/icons_skills/mysql.png", class_name="skills-icon", alt="MySQL"),
                        rx.image(src="/icons_skills/postgres.png", class_name="skills-icon", alt="PostgreSQL"),
                        rx.image(src="/icons_skills/vscode.png", class_name="skills-icon", alt="VS Code"),
                        class_name="skills-set",
                    ),
                    rx.box(
                        rx.image(src="/icons_skills/asana.png", class_name="skills-icon", alt="Asana"),
                        rx.image(src="/icons_skills/excel.png", class_name="skills-icon", alt="Excel"),
                        rx.image(src="/icons_skills/lean.png", class_name="skills-icon", alt="Lean"),
                        rx.image(src="/icons_skills/justintime.png", class_name="skills-icon", alt="Just in Time"),
                        rx.image(src="/icons_skills/kanban.png", class_name="skills-icon", alt="Kanban"),
                        rx.image(src="/icons_skills/mercadopublico.png", class_name="skills-icon", alt="Mercado Público"),
                        rx.image(src="/icons_skills/scrum.png", class_name="skills-icon", alt="Scrum"),
                        rx.image(src="/icons_skills/php.png", class_name="skills-icon", alt="PHP"),
                        rx.image(src="/icons_skills/python.png", class_name="skills-icon", alt="Python"),
                        rx.image(src="/icons_skills/js.png", class_name="skills-icon", alt="JavaScript"),
                        rx.image(src="/icons_skills/css3.png", class_name="skills-icon", alt="CSS3"),
                        rx.image(src="/icons_skills/sass.png", class_name="skills-icon", alt="Sass"),
                        rx.image(src="/icons_skills/json.png", class_name="skills-icon", alt="JSON"),
                        rx.image(src="/icons_skills/html5.png", class_name="skills-icon", alt="HTML5"),
                        rx.image(src="/icons_skills/github.png", class_name="skills-icon", alt="GitHub"),
                        rx.image(src="/icons_skills/mysql.png", class_name="skills-icon", alt="MySQL"),
                        rx.image(src="/icons_skills/postgres.png", class_name="skills-icon", alt="PostgreSQL"),
                        rx.image(src="/icons_skills/vscode.png", class_name="skills-icon", alt="VS Code"),
                        class_name="skills-set",
                        aria_hidden=True,
                    ),
                    class_name="skills-track",
                ),
                class_name="skills-slider sr-card",
                custom_attrs={"data-sr-delay": "760"},
                width="100%",
                max_width=rx.breakpoints(initial="100%", md="800px"),
                overflow="hidden",
            ),

            spacing="4",
            align_items="start",
            max_width=rx.breakpoints(initial="100%", md="800px"),
            width="auto",
            flex="1",
            min_width="0",
        ),

        direction=rx.breakpoints(initial="column", md="row"),
        spacing="6",
        align="center",
        justify="center",
        width="100%",
        class_name="hero-layout",
        position="relative",
        z_index="1",
    )

    scroll_indicator = rx.box(
        rx.icon(tag="chevron-down", size=36),
        class_name="scroll-indicator sr-fade",
        custom_attrs={"data-sr-delay": "820"},
        color=text_color.MUTED.value,
    )

    return hero_container("inicio", main, stars_layer, scroll_indicator)
