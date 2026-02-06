import reflex as rx
from link_bio.components.section import section_container, section_header
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import card_style
from link_bio.styles.colors import Color as color



def profile_section() -> rx.Component:
    return section_container(
        "perfil",
        # Header
        rx.box(
            section_header("Perfil", "¿Cómo me gusta trabajar?"),
            class_name="sr-fade-up",
            custom_attrs={"data-sr-delay": "0"},
        ),
        # Párrafo 1
        rx.text(
            "Me gusta llevar el trabajo operativo a algo más ordenado y fácil de sostener: procesos más simples, medibles y con menos fricción. "
            "Me muevo entre lo técnico y lo administrativo: primero entiendo el proceso, luego detecto dónde se pierde tiempo o se cometen errores, "
            "y propongo mejoras que sean realistas de implementar.",
            color=text_color.BODY.value,
            class_name="sr-fade-up",
            custom_attrs={"data-sr-delay": "120"},
        ),
        # Párrafo 2 (fade sin movimiento)
        rx.text(
            "Me interesa la mejora continua aplicada: automatizar cuando aporta, estandarizar cuando reduce errores y dar visibilidad cuando ayuda "
            "a decidir mejor. Prefiero soluciones claras y mantenibles antes que complejidad innecesaria.",
            color=text_color.BODY.value,
            class_name="sr-fade",
            custom_attrs={"data-sr-delay": "240"},
        ),
        # Card (wrapper con sr-card para no pelear con card_style.class_name)
        rx.box(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            "1",
                            width="26px",
                            height="26px",
                            border_radius="9999px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            font_weight="800",
                            font_size="0.9rem",
                            line_height="1",
                            background="rgba(100,255,218,0.12)",
                            border="1px solid rgba(100,255,218,0.55)",
                            color=color.PRIMARY.value,
                            flex_shrink="0",
                        ),
                        rx.text(
                            "Claridad antes que complejidad",
                            color=text_color.MUTED.value,
                            font_weight="600",
                        ),
                        spacing="3",
                        align="center",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.box(
                            "2",
                            width="26px",
                            height="26px",
                            border_radius="9999px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            font_weight="800",
                            font_size="0.9rem",
                            line_height="1",
                            background="rgba(100,255,218,0.12)",
                            border="1px solid rgba(100,255,218,0.55)",
                            color=color.PRIMARY.value,
                            flex_shrink="0",
                        ),
                        rx.text(
                            "Automatizar lo repetible, controlar lo crítico",
                            color=text_color.MUTED.value,
                            font_weight="600",
                        ),
                        spacing="3",
                        align="center",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.box(
                            "3",
                            width="26px",
                            height="26px",
                            border_radius="9999px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            font_weight="800",
                            font_size="0.9rem",
                            line_height="1",
                            background="rgba(100,255,218,0.12)",
                            border="1px solid rgba(100,255,218,0.55)",
                            color=color.PRIMARY.value,
                            flex_shrink="0",
                        ),
                        rx.text(
                            "Decidir con datos y contexto",
                            color=text_color.MUTED.value,
                            font_weight="600",
                        ),
                        spacing="3",
                        align="center",
                        width="100%",
                    ),
                    spacing="3",
                    align_items="start",
                    width="100%",
                ),
                **card_style,
                width="100%",
            ),
            class_name="sr-card",
            custom_attrs={"data-sr-delay": "360"},
            width="100%",
        ),
        
        rx.box(
            rx.hstack(
                rx.el.div(
                    rx.el.i(class_name="postit-pin"),
                    rx.el.div("Mejora continua", class_name="postit-title"),
                    rx.el.div(
                        "No podemos progresar cuando estamos satisfechos con la situación actual. - Taiichi Ohno",
                        class_name="postit-quote",
                    ),
                    class_name="postit postit--green",
                ),
                spacing="4",
                wrap="wrap",
                justify="center",
                width="100%",
                class_name="postit-wrap",
            ),
            class_name="sr-fade-up",
            custom_attrs={"data-sr-delay": "520"},
            width="100%",
        ),




    )
