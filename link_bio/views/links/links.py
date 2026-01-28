import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("MIS ENLACES"),
        link_button("Twich", "tutoriales semanales", "https://twitch.tv/mouredev"),
        link_button("YouTube", "Tutoriales de programación", "https://youtube.com/@mouredev"),
        link_button("YouTube (canal secundario)", "Tutoriales de programación", "https://youtube.com/@mouredevtv"),
        link_button("Discord", "Comunidad de desarrolladores", "https://discord.gg/mouredev"),
        title("MIS ENLACES"),
        link_button("Twich", "tutoriales semanales", "https://twitch.tv/mouredev"),
        link_button("YouTube", "Tutoriales de programación", "https://youtube.com/@mouredev"),
        link_button("YouTube (canal secundario)", "Tutoriales de programación", "https://youtube.com/@mouredevtv"),
        link_button("Discord", "Comunidad de desarrolladores", "https://discord.gg/mouredev"),
        title("CONTACTO"),
        link_button("Email", "criss.op98@gmail.com", f"mailto:criss.op98@gmail.com"),
        link_button("Numero", "+56979500691", "tel:+56979500691"),
        width="100%",
        spacing="2"
    )