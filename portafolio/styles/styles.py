from enum import Enum

import reflex as rx

MAX_WIDTH = "1120px"
IMAGE_HEIGHT = "240px"


class EmSize(Enum):
    DEFAULT = "1em"
    MEDIUM = "2em"
    BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    DEFAULT = "4"
    MEDIUM = "6"
    BIG = "8"


STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
    "https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap",
]

COLOR_THEME = {
    "page_background": "#060816",
    "page_gradient": "radial-gradient(circle at top left, rgba(20, 184, 166, 0.18), transparent 35%), radial-gradient(circle at top right, rgba(245, 158, 11, 0.14), transparent 28%), linear-gradient(180deg, #060816 0%, #0a1022 45%, #05070f 100%)",
    "surface": "rgba(8, 14, 30, 0.76)",
    "surface_strong": "rgba(10, 18, 38, 0.92)",
    "surface_soft": "rgba(15, 23, 42, 0.66)",
    "border": "rgba(148, 163, 184, 0.18)",
    "text_primary": "#f8fafc",
    "text_secondary": "#94a3b8",
    "text_muted": "#64748b",
    "accent": "#2dd4bf",
    "accent_soft": "rgba(45, 212, 191, 0.14)",
    "accent_alt": "#f59e0b",
    "button_text": "#04111c",
    "badge_background": "rgba(45, 212, 191, 0.12)",
    "image_filter": "saturate(1)",
    "shadow": "0 24px 80px rgba(2, 8, 23, 0.45)",
}

MONO_THEME = {
    "page_background": "#050505",
    "page_gradient": "radial-gradient(circle at top left, rgba(255, 255, 255, 0.12), transparent 28%), radial-gradient(circle at top right, rgba(255, 255, 255, 0.08), transparent 22%), linear-gradient(180deg, #050505 0%, #0c0c0c 45%, #020202 100%)",
    "surface": "rgba(12, 12, 12, 0.78)",
    "surface_strong": "rgba(20, 20, 20, 0.94)",
    "surface_soft": "rgba(18, 18, 18, 0.72)",
    "border": "rgba(255, 255, 255, 0.14)",
    "text_primary": "#fafafa",
    "text_secondary": "#c7c7c7",
    "text_muted": "#8d8d8d",
    "accent": "#f5f5f5",
    "accent_soft": "rgba(255, 255, 255, 0.09)",
    "accent_alt": "#9f9f9f",
    "button_text": "#050505",
    "badge_background": "rgba(255, 255, 255, 0.08)",
    "image_filter": "grayscale(1)",
    "shadow": "0 24px 80px rgba(0, 0, 0, 0.55)",
}


def page_shell_style(theme: dict) -> dict:
    return {
        "width": "100%",
        "max_width": MAX_WIDTH,
        "padding": ["1.25rem", "1.75rem", "2.5rem"],
        "gap": "1.5rem",
        "position": "relative",
        "z_index": "1",
    }


def panel_style(theme: dict) -> dict:
    return {
        "width": "100%",
        "padding": ["1.25rem", "1.5rem", "1.75rem"],
        "border_radius": "28px",
        "background": theme["surface"],
        "border": f"1px solid {theme['border']}",
        "backdrop_filter": "blur(18px)",
        "box_shadow": theme["shadow"],
    }


def secondary_panel_style(theme: dict) -> dict:
    return {
        **panel_style(theme),
        "background": theme["surface_soft"],
        "box_shadow": "none",
    }


def badge_style(theme: dict) -> dict:
    return {
        "padding": "0.45rem 0.8rem",
        "border_radius": "999px",
        "background": theme["badge_background"],
        "border": f"1px solid {theme['border']}",
        "color": theme["text_primary"],
    }


def primary_button_style(theme: dict) -> dict:
    return {
        "background": theme["accent"],
        "color": theme["button_text"],
        "border_radius": "999px",
        "padding": "0.9rem 1.2rem",
        "font_weight": "700",
        "border": "none",
        "_hover": {
            "opacity": "0.92",
        },
    }


def secondary_button_style(theme: dict) -> dict:
    return {
        "background": theme["accent_soft"],
        "color": theme["text_primary"],
        "border_radius": "999px",
        "padding": "0.9rem 1.2rem",
        "font_weight": "600",
        "border": f"1px solid {theme['border']}",
        "_hover": {
            "background": theme["surface_strong"],
        },
    }


def section_heading_style(theme: dict, h1: bool = False) -> dict:
    return {
        "font_family": "'Space Grotesk', sans-serif",
        "font_size": ["2.3rem", "3rem", "4rem"] if h1 else ["1.45rem", "1.7rem", "2rem"],
        "line_height": "1.05",
        "letter_spacing": "-0.04em" if h1 else "-0.03em",
        "color": theme["text_primary"],
    }


BASE_STYLE = {
    "font_family": "'Manrope', sans-serif",
    "background": "#060816",
    "color": "#f8fafc",
    "scroll_behavior": "smooth",
    rx.link: {
        "text_decoration": "none",
    },
    rx.button: {
        "--cursor-button": "pointer",
        "transition": "all 0.2s ease",
    },
}
