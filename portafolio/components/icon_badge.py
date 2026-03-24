import reflex as rx


def icon_badge(icon: str, theme: dict) -> rx.Component:
    return rx.badge(
        rx.icon(icon, size=30),
        style={
            "background": theme["accent_soft"],
            "color": theme["accent"],
            "border": f"1px solid {theme['border']}",
            "padding": "0.8rem",
            "border_radius": "20px",
        },
    )
