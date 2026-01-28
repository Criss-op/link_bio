import reflex as rx
import link_bio.styles.styles as styles


def link_button(title: str, body:str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_big_right",
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin= styles.Size.MEDIUM.value,
                    
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="2",
                    align_items="start",
                    margin= "0px !important",
                    padding_y= styles.Size.SMALL.value,
                    padding_right= styles.Size.SMALL.value
                ),
                width="100%",
                align_items="center"
                
            )
        ),
        href=url,
        is_external=True,
        width="100%"
        
    ) 