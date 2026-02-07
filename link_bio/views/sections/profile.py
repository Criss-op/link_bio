import reflex as rx

from link_bio.components.section import section_container, section_header
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import card_style


def profile_section() -> rx.Component:
    return section_container(
        "perfil",

        # Bloque superior: Post-it flotando a la derecha + Header + párrafos.
        # Esto NO puede ser hijo directo del rx.vstack (flex) del section_container.
        rx.box(
            # Post-it: flota y “nace” arriba dentro del padding del section_container.
            rx.el.div(
                rx.el.div(
                    rx.el.i(class_name="postit-pin"),
                    rx.el.div("Mejora continua", class_name="postit-title"),
                    rx.el.div(
                        "“No podemos progresar cuando estamos satisfechos con la situación actual.”",
                        class_name="postit-quote",
                        ),
                        rx.el.div(
                        "- Taiichi Ohno",
                        class_name="postit-author",
                        ),

                    class_name="postit postit--green",
                ),
                class_name="postit-float-right sr-postit",
                custom_attrs={"data-sr-delay": "700"},
            ),

            rx.box(
                section_header("Perfil", "¿Cómo me gusta trabajar?"),
                class_name="sr-fade-up",
                custom_attrs={"data-sr-delay": "0"},
            ),

            rx.text(
                "Me gusta llevar el trabajo operativo a algo más ",
                rx.el.strong("ordenado y fácil de sostener", style={"fontWeight": "800"}),
                ": procesos más ",
                rx.el.strong("simples, medibles y con menos fricción.", style={"fontWeight": "800"}),
                " Me muevo entre lo técnico y lo administrativo: primero entiendo el proceso, luego detecto dónde se pierde tiempo o se cometen errores, y propongo ",
                rx.el.strong("mejoras", style={"fontWeight": "800"}),
                " que sean realistas de implementar.",
                color=text_color.BODY.value,
                class_name="sr-fade-up",
                custom_attrs={"data-sr-delay": "120"},
            ),


            rx.text(
                "Me interesa la ",
                rx.el.strong("mejora continua", style={"fontWeight": "800"}),
                " aplicada: ",
                rx.el.strong("automatizar", style={"fontWeight": "800"}),
                " cuando aporta, ",
                rx.el.strong("estandarizar", style={"fontWeight": "800"}),
                " cuando reduce errores y dar visibilidad cuando ayuda a decidir mejor. Prefiero ",
                rx.el.strong("soluciones", style={"fontWeight": "800"}),
                " claras y ",
                rx.el.strong("mantenibles", style={"fontWeight": "800"}),
                " antes que complejidad innecesaria.",
                color=text_color.BODY.value,
                class_name="sr-fade",
                custom_attrs={"data-sr-delay": "240"},
            ),


            # Cierra el float dentro de este bloque para que lo siguiente no se solape.
            rx.el.div(class_name="postit-clear"),
            width="100%",
        ),

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
    )
