import reflex as rx

from portafolio.components.heading import heading
from portafolio.data import localize, translate
from portafolio.styles.styles import panel_style


def about(description, theme: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                translate("Profile", "Perfil"),
                color=theme["accent"],
                font_weight="700",
                letter_spacing="0.12em",
                text_transform="uppercase",
                font_size="0.8rem",
            ),
            heading({"en": "About Me", "es": "Sobre Mi"}, theme),
            rx.text(
                localize(description),
                color=theme["text_secondary"],
                line_height="1.9",
                font_size=["1rem", "1.02rem", "1.06rem"],
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        style=panel_style(theme),
    )
