import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.colors import Color as color



def header () -> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.avatar(
            name="Cristóbal Opazo", 
            size="8",
            src="avatar_cris_vector_white.png",
            color=text_color.BODY.value,
            bg=color.CONTENT.value,
            padding="2px",
            border="2px solid",
            border_color=color.PRIMARY.value
            ),
        rx.vstack(
            rx.heading("Cristóbal Opazo", size="6",  color=text_color.HEADER.value),
            rx.text("Process · Automation · Strategy · Management", margin_top="0px !important", color=text_color.BODY.value),
            rx.hstack(
                link_icon("https://linkedin.com/in/tu-perfil"),
                link_icon("https://github.com/tu-usuario"),
                link_icon("mailto:tuemail@dominio.cl"),
                link_icon("/cv_cristobal_opazo.pdf")
            ),

            align_items="start"
        ),
        spacing="4"
        ),
        rx.flex(
            info_text("Gestión ", "de procesos"),
            rx.spacer(),
            info_text("Automatización ", "de tareas"),
            rx.spacer(),
            info_text("Estrategia ", "orientada a resultados"),
            width="100%"
        ),

        rx.text("""Soy Ingeniero en Informática con experiencia en gestión de procesos, compras públicas y entornos operativos.
                    Trabajo en la intersección entre gestión, tecnología y automatización, enfocándome en ordenar sistemas, optimizar flujos
                    y diseñar soluciones prácticas que generen impacto real. Este sitio es mi espacio profesional, donde presento mi enfoque,
                    formación y evolución continua. ¡Bienvenid@!""",
                color= text_color.BODY.value),
        spacing="4",
        align_items="start"
    )