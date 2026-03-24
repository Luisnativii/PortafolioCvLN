import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data, localize, translate
from portafolio.styles.styles import Size, badge_style, panel_style


def header(data: Data, theme: dict) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
                rx.box(
                    rx.avatar(
                        src=data.avatar,
                        size="9",
                        radius="full",
                    ),
                    padding="0.6rem",
                    border_radius="999px",
                    background=theme["accent_soft"],
                    border=f"1px solid {theme['border']}",
                ),
                display="flex",
                align_items="center",
                justify_content="center",
                min_width=["100%", "100%", "260px"],
            ),
            rx.vstack(
                rx.badge(
                    rx.icon("sparkles", size=16),
                    translate(
                        "Open to internships and freelance collaborations",
                        "Disponible para pasantias y colaboraciones freelance",
                    ),
                    style=badge_style(theme),
                ),
                heading(data.name, theme, True),
                rx.text(
                    localize(data.skill),
                    font_size=["1.05rem", "1.1rem", "1.2rem"],
                    font_weight="600",
                    color=theme["accent"],
                ),
                rx.text(
                    localize(data.about),
                    color=theme["text_secondary"],
                    line_height="1.9",
                    font_size=["1rem", "1.05rem", "1.1rem"],
                ),
                rx.flex(
                    rx.badge(
                        rx.icon("map-pin", size=16),
                        data.location,
                        style=badge_style(theme),
                    ),
                    rx.badge(
                        rx.icon("layers", size=16),
                        translate("Portfolio 2026", "Portafolio 2026"),
                        style=badge_style(theme),
                    ),
                    spacing=Size.SMALL.value,
                    flex_wrap="wrap",
                ),
                media(data.media, theme),
                spacing=Size.SMALL.value,
                width="100%",
                align="start",
            ),
            spacing=Size.DEFAULT.value,
            flex_direction=["column", "column", "row"],
            width="100%",
            align="center",
        ),
        style=panel_style(theme),
    )
