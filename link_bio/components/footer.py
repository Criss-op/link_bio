import datetime
import reflex as rx
from link_bio.constants import EMAIL_ADDRESS, GITHUB_URL, LINKEDIN_URL
from link_bio.styles.colors import TextColor as text_color


def footer() -> rx.Component:
    year = datetime.date.today().year

    return rx.box(
        # Franja superior (más clara)
        rx.box(
            rx.box(
                rx.text(
                    "Cris (Cristóbal Opazo)",
                    class_name="footer-topbar-name",
                ),
                class_name="footer-topbar-inner",
            ),
            class_name="footer-topbar",
        ),

        # Contenido inferior
        rx.box(
            rx.box(
                rx.box(
                    rx.box(
                        # Izquierda
                        rx.box(
                            rx.text(
                                "Procesos · Automatización · Estrategia · Gestión",
                                class_name="footer-title",
                            ),
                            rx.text(
                                "Built with Reflex",
                                class_name="footer-built",
                            ),
                                rx.box(
                                    rx.vstack(
                                        rx.heading("Navegación", size="2", class_name="footer-col-title"),
                                        rx.link("Inicio", href="#inicio"),
                                        rx.link("Perfil", href="#perfil"),
                                        rx.link("Experiencia", href="#experiencia"),
                                        rx.link("Formación", href="#formacion"),
                                        rx.link("Habilidades", href="#habilidades"),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                    rx.vstack(
                                        rx.heading("Contacto", size="2", class_name="footer-col-title"),
                                        rx.link("LinkedIn", href=LINKEDIN_URL, is_external=True),
                                        rx.link("GitHub", href=GITHUB_URL, is_external=True),
                                        rx.link("+56 9 79 500 691", href="tel:+56979500691"),
                                        rx.text(EMAIL_ADDRESS, color=text_color.FOOTER.value),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                    class_name="footer-links",
                                ),

                            rx.text(f"© {year}", class_name="footer-bottom"),
                        ),

                        # Derecha (md+): imagen siempre al lado, nunca abajo
                        rx.box(
                            rx.box(
                                rx.image(
                                    src="/yo_programador_footer.png",
                                    alt="Ilustración programador",
                                    class_name="footer-img",
                                ),
                                class_name="footer-float",
                            ),
                            class_name="footer-figure",
                        ),

                        class_name="footer-grid",
                        width="100%",
                    ),
                    class_name="footer-inner",
                ),
                width="100%",
            ),
            class_name="footer-main",
        ),

        id="footer",
        class_name="app-footer",
        width="100%",
    )
