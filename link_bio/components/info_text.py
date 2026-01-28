import reflex as rx
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.colors import Color as color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            size="3",      
            weight="bold",
            color=color.PRIMARY.value
        ),
        rx.text(
            body,
            as_="span",
            size="3",     
            color=text_color.BODY.value
        )
        
    )
