import reflex as rx

from portafolio import data
from portafolio.data import default_text, translate
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
    return portfolio_page(COLOR_THEME)


app = rx.App(
    overlay_component=rx.fragment(),
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="teal",
        radius="large",
    ),
    head_components=[
        rx.html('<link rel="manifest" href="/manifest.json" />'),
        rx.html('<link rel="apple-touch-icon" href="/avatar.jpg" />'),
        rx.script("if ('serviceWorker' in navigator) { window.addEventListener('load', () => {navigator.serviceWorker.register('/sw.js');}); }")
    ]
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
        {"name": "theme-color", "content": "#060816"},
        {"name": "apple-mobile-web-app-capable", "content": "yes"},
        {"name": "apple-mobile-web-app-status-bar-style", "content": "black"},
        {"name": "apple-mobile-web-app-title", "content": "Luis CV"},
    ],
)
