import reflex as rx

from portafolio import data
from portafolio.data import default_text, translate
from portafolio.state import PortfolioState
from portafolio.styles.styles import (
    BASE_STYLE,
    COLOR_THEME,
    MONO_THEME,
    STYLESHEETS,
    Size,
    page_shell_style,
    panel_style,
    secondary_button_style,
)
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack

DATA = data.data


def control_bar(theme: dict) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                translate("Portfolio Controls", "Controles del Portafolio"),
                color=theme["text_secondary"],
                font_weight="600",
            ),
            rx.spacer(),
            rx.hstack(
                rx.button(
                    rx.icon("languages", size=18),
                    translate("Switch to Spanish", "Cambiar a Ingles"),
                    on_click=PortfolioState.toggle_language,
                    style=secondary_button_style(theme),
                ),
                rx.button(
                    rx.icon("palette", size=18),
                    rx.cond(
                        PortfolioState.monochrome,
                        translate("Back to Color", "Volver a Color"),
                        translate("Black & White", "Blanco y Negro"),
                    ),
                    on_click=PortfolioState.toggle_monochrome,
                    style=secondary_button_style(theme),
                ),
                spacing="3",
                flex_wrap="wrap",
                justify="end",
            ),
            width="100%",
            align="center",
        ),
        style=panel_style(theme),
    )


def portfolio_page(theme: dict) -> rx.Component:
    return rx.box(
        rx.box(
            position="absolute",
            top="-120px",
            left="-80px",
            width="320px",
            height="320px",
            border_radius="999px",
            background=theme["accent_soft"],
            filter="blur(40px)",
        ),
        rx.box(
            position="absolute",
            top="120px",
            right="-120px",
            width="280px",
            height="280px",
            border_radius="999px",
            background=f"radial-gradient(circle, {theme['accent_alt']}22 0%, transparent 70%)",
            filter="blur(24px)",
        ),
        rx.center(
            rx.vstack(
                control_bar(theme),
                header(DATA, theme),
                rx.mobile_only(
                    rx.vstack(
                        about(DATA.about, theme),
                        tech_stack(DATA.technologies, theme),
                        spacing=Size.DEFAULT.value,
                        width="100%",
                    ),
                    width="100%",
                ),
                rx.tablet_and_desktop(
                    rx.grid(
                        about(DATA.about, theme),
                        tech_stack(DATA.technologies, theme),
                        columns="2",
                        spacing=Size.DEFAULT.value,
                        width="100%",
                    ),
                    width="100%",
                ),
                info({"en": "Experience", "es": "Experiencia"}, DATA.experience, theme),
                info({"en": "Projects", "es": "Proyectos"}, DATA.projects, theme),
                info({"en": "Education", "es": "Formacion"}, DATA.training, theme),
                extra(DATA.extras, theme),
                footer(DATA.media, theme),
                spacing=Size.DEFAULT.value,
                style=page_shell_style(theme),
            ),
        ),
        min_height="100vh",
        width="100%",
        position="relative",
        overflow="hidden",
        background=theme["page_gradient"],
    )


def index() -> rx.Component:
    return rx.cond(
        PortfolioState.monochrome,
        portfolio_page(MONO_THEME),
        portfolio_page(COLOR_THEME),
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="teal",
        radius="large",
    ),
)

title = default_text(DATA.title)
description = default_text(DATA.description)
image = default_text(DATA.image)

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image},
    ],
)
