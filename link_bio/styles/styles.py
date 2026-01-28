import reflex as rx
from enum import Enum
from .colors import Color as color
from .colors import TextColor as text_color
from .fonts import Font as font
from .fonts import FontWeight as font_weight


# Constans
MAX_WIDTH= "650px"

# Sizes
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
]


class Size(Enum):
    SMALL="0.8em"
    MEDIUM = "0.1em"
    DEFAULT= "1.3em"
    LARGE= "1.7em"
    BIG= "2em"

#styles
BASE_STYLE = {
    "font_family": font.DEFAULT.value,
    "font_weight": font_weight.LIGHT.value,
    "background_color": color.BACKGROUND.value,
    rx.heading: {
        "color": text_color.HEADER.value,
        "font_family": font.TITLE.value,
        "font_weight": font_weight.MEDIUM.value
    },
    rx.button: {
        "width" : "100%",
        "height" : "100%",
        "padding" : Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": text_color.HEADER.value,
        "background_color": color.CONTENT.value, 
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=font.LOGO.value,
    font_weight=font_weight.MEDIUM.value,
    font_size=Size.LARGE.value,
    
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value
)

button_title_style = dict(
    font_family=font.TITLE.value,
    font_weight=font_weight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color=text_color.HEADER.value
)
button_body_style = dict(
    font_weight=font_weight.LIGHT.value,
    font_size=Size.SMALL.value,
    color=text_color.BODY.value
)


