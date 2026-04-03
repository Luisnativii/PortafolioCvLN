import reflex as rx

from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info, localize, translate
from portafolio.styles.styles import IMAGE_HEIGHT, Size, badge_style, secondary_panel_style


def info_detail(info: Info, theme: dict) -> rx.Component:
    actions = rx.hstack(
        rx.cond(
            info.url != "",
            icon_button(
                "link",
                info.url,
                theme,
                translate("Open Project", "Abrir Proyecto"),
            ),
        ),
        rx.cond(
            info.github != "",
            icon_button(
                "github",
                info.github,
                theme,
                "GitHub",
            ),
        ),
        rx.cond(
            info.certificate != "",
            icon_button(
                "shield-check",
                info.certificate,
                theme,
                translate("Certificate", "Certificado"),
                True,
            ),
        ),
        spacing=Size.SMALL.value,
        flex_wrap="wrap",
    )

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.cond(
                    info.date != "",
                    rx.badge(info.date, style=badge_style(theme)),
                ),
                width="100%",
                justify="end",
            ),
            rx.flex(
                rx.hstack(
                    icon_badge(info.icon, theme),
                    rx.vstack(
                        rx.text(
                            localize(info.title),
                            font_size="1.1rem",
                            font_weight="700",
                            color=theme["text_primary"],
                        ),
                        rx.text(
                            localize(info.subtitle),
                            color=theme["accent"],
                            font_weight="600",
                        ),
                        rx.text(
                            localize(info.description),
                            color=theme["text_secondary"],
                            line_height="1.8",
                        ),
                        rx.cond(
                            info.technologies,
                            rx.flex(
                                *[
                                    rx.badge(
                                        rx.box(class_name=technology.icon, font_size="18px"),
                                        technology.name,
                                        style=badge_style(theme),
                                    )
                                    for technology in info.technologies
                                ],
                                wrap="wrap",
                                spacing=Size.SMALL.value,
                            ),
                        ),
                        actions,
                        spacing=Size.SMALL.value,
                        width="100%",
                        align="start",
                    ),
                    spacing=Size.DEFAULT.value,
                    width="100%",
                    align="start",
                ),
                rx.cond(
                    info.image != "",
                    rx.box(
                        rx.image(
                            src=info.image,
                            height=[IMAGE_HEIGHT, IMAGE_HEIGHT, "100%"],
                            width="100%",
                            object_fit="cover",
                            border_radius="22px",
                            style={
                                "filter": theme["image_filter"],
                            },
                        ),
                        width=["100%", "100%", "280px"],
                        min_width=["100%", "100%", "280px"],
                    ),
                ),
                flex_direction=["column", "column", "row"],
                spacing=Size.DEFAULT.value,
                width="100%",
                align="stretch",
            ),
            spacing=Size.SMALL.value,
            width="100%",
            height="100%",
        ),
        height="100%",
        style=secondary_panel_style(theme),
    )
