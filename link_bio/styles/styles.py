import reflex as rx
from enum import Enum
from .colors import Color as color
from .colors import TextColor as text_color
from .fonts import Font as font
from .fonts import FontWeight as font_weight


MAX_WIDTH = "1100px"
CONTENT_GAP = "2.5rem"
SECTION_PADDING = "5rem"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Fira+Code:wght@400;500&display=swap",
    "/ui_effects.css",
    "/avatar_glow.css",
    "/hero_links.css",
    "/skills_carousel.css",
    "/scroll_reveal.css",
    "/rails_reveal.css",
    "/navbar_reveal.css",
    "/cursor_dot.css",
    "/postit.css",
    "/footer.css",
    "/education_timeline.css",
    "/preloader.css",



]


class Size(Enum):
    XSMALL = "0.75rem"
    SMALL = "0.875rem"
    MEDIUM = "1rem"
    DEFAULT = "1.125rem"
    LARGE = "1.5rem"
    XLARGE = "2rem"
    XXLARGE = "2.5rem"


BASE_STYLE = {
    "font_family": font.DEFAULT.value,
    "font_weight": font_weight.REGULAR.value,
    "background_color": color.BACKGROUND.value,
    "color": text_color.BODY.value,
    "scroll_behavior": "smooth",
    rx.heading: {
        "color": text_color.HEADER.value,
        "font_family": font.TITLE.value,
        "font_weight": font_weight.BOLD.value,
    },
    rx.button: {
        "border_radius": "999px",
        "font_weight": font_weight.MEDIUM.value,
        "_hover": {
            "opacity": "0.9",
        },
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "text_decoration": "none",
        },
    },
}


navbar_title_style = dict(
    font_family=font.LOGO.value,
    font_weight=font_weight.SEMIBOLD.value,
    font_size=Size.LARGE.value,
)

section_heading_style = dict(
    font_size=rx.breakpoints(initial="1.8rem", md="2.2rem"),
    margin_bottom="0.5rem",
)

section_subtitle_style = dict(
    color=text_color.MUTED.value,
    font_size=Size.DEFAULT.value,
)

card_style = dict(
    background_color="transparent",
    border="1px solid transparent",
    border_radius="1.1rem",
    padding="1.5rem",
    box_shadow="none",
    transition="transform 200ms ease, box-shadow 200ms ease, border-color 200ms ease, background-color 200ms ease",
    class_name="card",
)

badge_style = dict(
    background_color=color.SURFACE_LIGHT.value,
    border=f"1px solid {color.BORDER.value}",
    border_radius="999px",
    padding_x="0.75rem",
    padding_y="0.25rem",
    font_size=Size.XSMALL.value,
    color=text_color.MUTED.value,
)
