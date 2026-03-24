import reflex as rx

from portafolio.components.media import media
from portafolio.data import Media, translate
from portafolio.styles.styles import Size, panel_style


def footer(data: Media, theme: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                translate(
                    "Built to stay simple, sharp, and adaptable for future updates.",
                    "Construido para mantenerse simple, solido y adaptable a futuras mejoras.",
                ),
                color=theme["text_secondary"],
                text_align="center",
            ),
            media(data, theme),
            spacing=Size.SMALL.value,
            width="100%",
            align="center",
        ),
        style=panel_style(theme),
    )
