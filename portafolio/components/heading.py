import reflex as rx

from portafolio.data import localize
from portafolio.styles.styles import section_heading_style


def heading(text, theme: dict, h1: bool = False) -> rx.Component:
    return rx.heading(
        localize(text),
        as_="h1" if h1 else "h2",
        style=section_heading_style(theme, h1),
    )
