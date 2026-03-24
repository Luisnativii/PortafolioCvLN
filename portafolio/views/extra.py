import reflex as rx

from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.data import Extra
from portafolio.styles.styles import Size, panel_style


def extra(extras: list[Extra], theme: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            heading({"en": "More About Me", "es": "Mas Sobre Mi"}, theme),
            rx.mobile_only(
                rx.vstack(
                    *[
                        card_detail(extra_item, theme)
                        for extra_item in extras
                    ],
                    spacing=Size.DEFAULT.value,
                    width="100%",
                ),
                width="100%",
            ),
            rx.tablet_and_desktop(
                rx.grid(
                    *[
                        card_detail(extra_item, theme)
                        for extra_item in extras
                    ],
                    spacing=Size.DEFAULT.value,
                    columns="3",
                ),
                width="100%",
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        style=panel_style(theme),
    )
