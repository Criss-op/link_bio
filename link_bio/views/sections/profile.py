import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.colors import TextColor as text_color


def profile_section() -> rx.Component:
    return section_container(
        "perfil",
        section_header("Perfil", "Cómo trabajo"),
        rx.text(
            "Mi foco es transformar trabajo operativo en sistemas más simples, medibles y sostenibles. "
            "Me muevo cómodo entre lo técnico y lo administrativo: entiendo el proceso, detecto fricción "
            "y priorizo mejoras que se puedan implementar de verdad.",
            color=text_color.BODY.value,
        ),
        rx.text(
            "Me interesa la mejora continua aplicada: automatización donde aporta, estandarización cuando reduce errores "
            "y visibilidad cuando permite tomar mejores decisiones. Prefiero soluciones claras y mantenibles por sobre "
            "complejidad innecesaria.",
            color=text_color.BODY.value,
        ),
        rx.vstack(
            rx.text("Claridad antes que complejidad"),
            rx.text("Automatizar lo repetible, controlar lo crítico"),
            rx.text("Decidir con datos y contexto"),
            spacing="2",
            color=text_color.MUTED.value,
        ),
    )
