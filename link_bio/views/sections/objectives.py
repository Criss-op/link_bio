import reflex as rx
from link_bio.components.section import section_container, section_header


def objectives_section() -> rx.Component:
    return section_container(
        "objetivos",
        section_header("Objetivos"),
        rx.text(
            "Estoy consolidando un perfil híbrido que combine gestión, procesos y tecnología. Mi objetivo es moverme hacia roles donde "
            "pueda diseñar y mejorar sistemas de trabajo, con foco en eficiencia, trazabilidad y toma de decisiones.",
        ),
        rx.text(
            "La automatización y el desarrollo son un medio: los uso para reducir fricción, mejorar calidad y liberar tiempo para lo estratégico.",
        ),
    )
