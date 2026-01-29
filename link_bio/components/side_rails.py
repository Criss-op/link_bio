import reflex as rx
from link_bio.constants import EMAIL_ADDRESS, GITHUB_URL, LINKEDIN_URL


def side_rails() -> rx.Component:
    email_text = "criss.op98@gmail.com"
    email_href = EMAIL_ADDRESS if "{" not in EMAIL_ADDRESS else email_text
    return rx.fragment(
        rx.box(
            rx.link(rx.icon(tag="linkedin", size=20), href=LINKEDIN_URL, is_external=True),
            rx.link(rx.icon(tag="github", size=20), href=GITHUB_URL, is_external=True),
            rx.link(rx.icon(tag="mail", size=20), href=f"mailto:{email_href}"),
            class_name="side-rail left",
        ),
        rx.box(
            rx.link(
                email_text,
                href=f"mailto:{email_href}",
                class_name="email",
            ),
            class_name="side-rail right",
        ),
    )
