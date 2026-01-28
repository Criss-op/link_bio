import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color as color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
        rx.text("cris", as_="span", color=color.PRIMARY.value, font_weight="700"),
        rx.text("Ops", as_="span", color=color.SECONDARY.value, font_weight="700"),
        as_="span",
        style=styles.navbar_title_style
        
        ),
        position="sticky",
        bg=color.CONTENT.value,
        padding_x="16px",
        padding_y="8px",
        z_index="999",
        top="0"
    )