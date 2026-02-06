import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.styles import card_style


def skill_card(title: str, items: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(title, font_size="1.1rem", font_weight="600"),
        rx.vstack(*[rx.text(item) for item in items], spacing="2"),
        spacing="3",
        align_items="start",
        width="100%",
        **card_style,
    )


def skills_section() -> rx.Component:
    cards = [
        (
            "Técnicas",
            [
                "Automatización (Python / scripts / plantillas)",
                "Análisis y estructuración de información",
                "Documentación y control de procesos",
                "Gestión de herramientas (por definir)",
            ],
            "180",
        ),
        (
            "Profesionales",
            [
                "Pensamiento estratégico aplicado",
                "Gestión de procesos y coordinación",
                "Priorización y toma de decisiones",
                "Comunicación clara con stakeholders",
            ],
            "300",
        ),
        (
            "Personales aplicadas",
            [
                "Criterio y enfoque en lo esencial",
                "Autonomía",
                "Aprendizaje continuo",
                "Orden y consistencia",
            ],
            "420",
        ),
    ]

    return section_container(
        "habilidades",
        rx.box(
            section_header("Habilidades"),
            class_name="sr-fade-up",
            custom_attrs={"data-sr-delay": "0"},
        ),
        rx.grid(
            *[
                rx.box(
                    skill_card(title, items),
                    class_name="sr-card",
                    custom_attrs={"data-sr-delay": delay},
                )
                for title, items, delay in cards
            ],
            columns=rx.breakpoints(initial="1", md="2", lg="3"),
            spacing="4",
            width="100%",
        ),
    )
