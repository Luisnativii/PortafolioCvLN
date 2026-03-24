import reflex as rx

from portafolio.data import Extra, localize
from portafolio.styles.styles import IMAGE_HEIGHT, secondary_panel_style


def card_detail(extra: Extra, theme: dict) -> rx.Component:
    card = rx.card(
        rx.vstack(
            rx.box(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover",
                    border_radius="22px",
                    style={
                        "filter": theme["image_filter"],
                    },
                ),
                overflow="hidden",
                width="100%",
            ),
            rx.text(
                localize(extra.title),
                font_size="1.05rem",
                font_weight="700",
                color=theme["text_primary"],
            ),
            rx.text(
                localize(extra.description),
                color=theme["text_secondary"],
                line_height="1.8",
            ),
            spacing="3",
            width="100%",
            align="start",
        ),
        width="100%",
        style=secondary_panel_style(theme),
    )

    return rx.cond(
        extra.url != "",
        rx.link(
            card,
            href=extra.url,
            is_external=True,
            width="100%",
        ),
        card,
    )
