import reflex as rx

from portafolio.components.icon_button import icon_button
from portafolio.data import Media, translate
from portafolio.styles.styles import Size


def media(data: Media, theme: dict) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{data.email}",
            theme,
            translate("Email Me", "Escribeme"),
            True,
        ),
        rx.hstack(
            icon_button(
                "file-text",
                data.cv,
                theme,
                translate("Resume", "CV"),
            ),
            icon_button(
                "github",
                data.github,
                theme,
                "GitHub",
            ),
            icon_button(
                "linkedin",
                data.likedin,
                theme,
                "LinkedIn",
            ),
            spacing=Size.SMALL.value,
            flex_wrap="wrap",
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"],
        width="100%",
        flex_wrap="wrap",
    )
