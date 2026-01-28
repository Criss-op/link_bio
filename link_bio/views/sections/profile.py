import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.colors import TextColor as text_color


def profile_section() -> rx.Component:
    return section_container(
        "perfil",
        section_header("Perfil", "¿Cómo me gusta trabajar?"),
        rx.text(
            """Me gusta llevar el trabajo operativo a algo más ordenado y fácil de sostener: procesos más simples, medibles y con menos fricción. 
            Me muevo entre lo técnico y lo administrativo: primero entiendo el proceso, luego detecto dónde se pierde tiempo o se cometen errores, 
            y propongo mejoras que sean realistas de implementar""",
            color=text_color.BODY.value,
        ),
        rx.text(
            """Me interesa la mejora continua aplicada: automatizar cuando aporta, estandarizar cuando reduce errores y dar visibilidad cuando ayuda 
            a decidir mejor. Prefiero soluciones claras y mantenibles antes que complejidad innecesaria.""",
            color=text_color.BODY.value,
        ),
        rx.vstack(
            rx.text("Claridad antes que complejidad"),
            rx.text("Automatizar lo repetible, controlar lo crítico"),
            rx.text("Decidir con datos y contexto"),
            spacing="2",
            color=text_color.PRIMARY.value,
        ),
    )
