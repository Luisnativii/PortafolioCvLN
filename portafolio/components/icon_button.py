import reflex as rx

from portafolio.data import localize
from portafolio.styles.styles import primary_button_style, secondary_button_style


def icon_button(icon: str, url: str, theme: dict, text="", solid: bool = False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon, size=18),
            rx.cond(
                text != "",
                rx.text(localize(text)),
            ),
            style=primary_button_style(theme) if solid else secondary_button_style(theme),
        ),
        href=url,
        is_external=True,
    )
