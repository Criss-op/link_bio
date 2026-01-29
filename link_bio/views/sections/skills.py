import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.styles import card_style


def skill_list(title: str, items: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(title, font_size="1.1rem", font_weight="600"),
        rx.vstack(*[rx.text(item) for item in items], spacing="2"),
        spacing="3",
        align_items="start",
        **card_style,
    )


def skills_section() -> rx.Component:
    technical = [
        "Automatización (Python / scripts / plantillas)",
        "Análisis y estructuración de información",
        "Documentación y control de procesos",
        "Gestión de herramientas (por definir)",
    ]
    professional = [
        "Pensamiento estratégico aplicado",
        "Gestión de procesos y coordinación",
        "Priorización y toma de decisiones",
        "Comunicación clara con stakeholders",
    ]
    personal = [
        "Criterio y enfoque en lo esencial",
        "Autonomía",
        "Aprendizaje continuo",
        "Orden y consistencia",
    ]

    desktop_grid = rx.grid(
        skill_list("Técnicas", technical),
        skill_list("Profesionales", professional),
        skill_list("Personales aplicadas", personal),
        columns=rx.breakpoints(initial="1", md="3"),
        spacing="4",
        width="100%",
        display=rx.breakpoints(initial="none", md="none", lg="grid"),
    )

    mobile_accordion = rx.vstack(
        rx.el.details(
            rx.el.summary("Técnicas"),
            rx.vstack(*[rx.text(item) for item in technical], spacing="2"),
            **card_style,
        ),
        rx.el.details(
            rx.el.summary("Profesionales"),
            rx.vstack(*[rx.text(item) for item in professional], spacing="2"),
            **card_style,
        ),
        rx.el.details(
            rx.el.summary("Personales aplicadas"),
            rx.vstack(*[rx.text(item) for item in personal], spacing="2"),
            **card_style,
        ),
        spacing="3",
        width="100%",
        display=rx.breakpoints(initial="block", md="block", lg="none"),
    )

    return section_container(
        "habilidades",
        section_header("Habilidades"),
        desktop_grid,
        mobile_accordion,
    )
