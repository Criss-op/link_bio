import reflex as rx
from link_bio.styles.colors import TextColor as text_color
from link_bio.styles.styles import MAX_WIDTH, section_heading_style, section_subtitle_style


def section_header(title: str, subtitle: str | None = None) -> rx.Component:
    return rx.vstack(
        rx.heading(title, as_="h2", **section_heading_style),
        rx.text(subtitle, **section_subtitle_style) if subtitle else rx.fragment(),
        spacing="1",
        align_items="start",
    )


def section_container(section_id: str, *children: rx.Component) -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                *children,
                max_width=MAX_WIDTH,
                width="100%",
                spacing="6",
                align_items="start",
            ),
            width="100%",
        ),
        id=section_id,
        padding_x=rx.breakpoints(initial="2.5rem", md="5.5rem", lg="1.5rem"),
        padding_y=rx.breakpoints(initial="3.5rem", md="4.5rem"),
        scroll_margin_top="6rem",
        color=text_color.BODY.value,
        position="relative",
        class_name="section",
    )
