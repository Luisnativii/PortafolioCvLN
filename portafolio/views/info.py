import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.data import Info
from portafolio.styles.styles import Size, panel_style


def info(title, info_items: list[Info], theme: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            heading(title, theme),
            rx.vstack(
                *[
                    info_detail(item, theme)
                    for item in info_items
                ],
                spacing=Size.DEFAULT.value,
                width="100%",
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        style=panel_style(theme),
    )
