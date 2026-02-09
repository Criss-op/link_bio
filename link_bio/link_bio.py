import reflex as rx
from link_bio.views.sections.preloader import preloader
from link_bio.components.contact_overlay import contact_overlay
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.components.side_rails import side_rails
from link_bio.constants import TAGLINE
from link_bio.styles import styles
from link_bio.views.projects import projects_page
from link_bio.views.sections import (
   
    contact_section,
    education_section,
    experience_section,
    hero_section,
    methodologies_section,
    objectives_section,
    profile_section,
    skills_section,
)


def index() -> rx.Component:
    return rx.box(
        rx.el.div(class_name="cursor-spotlight"),
        rx.el.div(class_name="cursor-dot"),
        preloader(),
        navbar(),
        side_rails(),
        rx.box(
            hero_section(),
            profile_section(),
            experience_section(),
            education_section(),
            skills_section(),
            methodologies_section(),
            objectives_section(),
            contact_section(),
            footer(),
            id="page-scroll",
            class_name="scroll-container",
        ),
        contact_overlay(),
        rx.script(src="/preloader_boot.js"),
        rx.script(src="/cursor_spotlight.js"),
        rx.script(src="/avatar_tilt.js"),
        rx.script(src="/ui_effects.js"),
        rx.script(src="/rails_docking.js"),
        rx.script(src="/avatar_glow.js"),
        rx.script(src="/navbar_active.js"),
        rx.script(src="https://cdnjs.cloudflare.com/ajax/libs/scrollReveal.js/4.0.9/scrollreveal.min.js"),
        rx.script(src="/scroll_reveal.js"),
        rx.script(src="/education_timeline.js"),
        rx.script(src="/preloader.js"),


    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    title=f"Cris | {TAGLINE}",
    description="Perfil profesional de Cristóbal ‘Cris’ Opazo: procesos, automatización, estrategia y gestión.",
)
app.add_page(projects_page, route="/projects", title="Proyectos privados")
