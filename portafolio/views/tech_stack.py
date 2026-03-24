import reflex as rx

from portafolio.components.heading import heading
from portafolio.data import Technology, translate
from portafolio.styles.styles import Size, badge_style, panel_style


def tech_stack(technologies: list[Technology], theme: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                translate("Stack", "Stack"),
                color=theme["accent"],
                font_weight="700",
                letter_spacing="0.12em",
                text_transform="uppercase",
                font_size="0.8rem",
            ),
            heading({"en": "Technologies", "es": "Tecnologias"}, theme),
            rx.flex(
                *[
                    rx.badge(
                        rx.box(
                            class_name=technology.icon,
                            font_size="22px",
                        ),
                        rx.text(technology.name),
                        style=badge_style(theme),
                    )
                    for technology in technologies
                ],
                wrap="wrap",
                spacing=Size.SMALL.value,
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        style=panel_style(theme),
    )
