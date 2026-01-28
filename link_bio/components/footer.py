import reflex as rx
import datetime
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor as text_color

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"2014-{datetime.date.today().year} MOUREDEV BY BRAIS MOURE V3.",
            href="https://mouredev.com",
            is_external=True
        ),
        rx.text("BUILDING SOFTWARE WITH - GROM GALICIA TO THE WORLD.",
        margin_bottom=Size.BIG.value,
        margin_top="0px !important",
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color= text_color.BODY.value,
        align="center",
    )