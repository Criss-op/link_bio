import datetime
import reflex as rx
from link_bio.constants import BRAND_NAME, FULL_NAME, GITHUB_URL, LINKEDIN_URL
from link_bio.styles.colors import Color as color
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import MAX_WIDTH


def footer() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.text(
                    f"{BRAND_NAME} ({FULL_NAME})",
                    color=text_color.FOOTER.value,
                    font_weight="500",
                ),
                rx.text(
                    f"© {datetime.date.today().year}",
                    color=text_color.FOOTER.value,
                ),
                rx.hstack(
                    rx.link("LinkedIn", href=LINKEDIN_URL, is_external=True),
                    rx.link("GitHub", href=GITHUB_URL, is_external=True),
                    spacing="4",
                    color=text_color.FOOTER.value,
                ),
                spacing="3",
                align="center",
                padding_y="2.5rem",
                max_width=MAX_WIDTH,
                width="100%",
            ),
            width="100%",
        ),
        border_top=f"1px solid {color.BORDER.value}",
        background_color=color.BACKGROUND.value,
        padding_x="1.5rem",
    )
