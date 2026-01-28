import os
import reflex as rx
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import MAX_WIDTH, card_style


class ProjectsState(rx.State):
    password_input: str = ""
    authorized: bool = False
    error_message: str = ""

    def validate_password(self):
        expected_password = os.environ.get("PROJECTS_PASSWORD", "")
        if self.password_input and expected_password and self.password_input == expected_password:
            self.authorized = True
            self.error_message = ""
        else:
            self.authorized = False
            self.error_message = "Contraseña incorrecta."

    def clear_error(self):
        self.error_message = ""


def project_item(title: str, status: str, date: str) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(title, font_weight="600"),
            rx.text(status, color=text_color.MUTED.value, font_size="0.9rem"),
            rx.text(date, color=text_color.MUTED.value, font_size="0.9rem"),
            spacing="1",
            align_items="start",
        ),
        width="100%",
        justify="between",
    )


def projects_private_content() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("Proyectos", as_="h1", font_size="2rem"),
                rx.text(
                    "Aquí registro automatizaciones, plantillas y pequeñas herramientas que uso para optimizar trabajo real. "
                    "No es un portafolio público.",
                ),
                rx.vstack(
                    project_item(
                        "Automatización Excel: control de hitos y fechas (placeholder)",
                        "En progreso",
                        "Fecha por definir",
                    ),
                    project_item(
                        "Generador de documentos / plantillas (placeholder)",
                        "En progreso",
                        "Fecha por definir",
                    ),
                    project_item(
                        "Dashboard simple de seguimiento (placeholder)",
                        "Hecho",
                        "Fecha por definir",
                    ),
                    spacing="3",
                    width="100%",
                ),
                spacing="5",
                align_items="start",
                **card_style,
                width="100%",
            ),
            max_width=MAX_WIDTH,
            width="100%",
        ),
        padding_x="1.5rem",
        padding_y=["4rem", "5rem"],
    )


def projects_gate() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("Proyectos privados", as_="h1", font_size="2rem", font_weight="700"),
                rx.text(
                    "Esta sección contiene automatizaciones y herramientas de uso personal. Acceso restringido.",
                    color=text_color.MUTED.value,
                    text_align="center",
                ),
                rx.input(
                    placeholder="Ingresa la contraseña",
                    type_="password",
                    value=ProjectsState.password_input,
                    on_change=ProjectsState.set_password_input,
                    on_focus=ProjectsState.clear_error,
                    width="100%",
                    padding="0.75rem",
                    border=f"1px solid {color.BORDER.value}",
                    border_radius="0.75rem",
                    background_color=color.SURFACE.value,
                    color=text_color.BODY.value,
                ),
                rx.button(
                    "Acceder",
                    on_click=ProjectsState.validate_password,
                    background_color=color.PRIMARY.value,
                    color="white",
                    width="100%",
                ),
                rx.cond(
                    ProjectsState.error_message != "",
                    rx.text(ProjectsState.error_message, color=text_color.MUTED.value),
                ),
                spacing="4",
                width="100%",
                align_items="center",
                **card_style,
            ),
            max_width="480px",
            width="100%",
        ),
        padding_x="1.5rem",
        padding_y=["4rem", "5rem"],
    )


def projects_page() -> rx.Component:
    return rx.cond(
        ProjectsState.authorized,
        projects_private_content(),
        projects_gate(),
    )
