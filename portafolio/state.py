import reflex as rx


class PortfolioState(rx.State):
    language: str = "en"
    monochrome: bool = False

    def toggle_language(self):
        self.language = "es" if self.language == "en" else "en"

    def toggle_monochrome(self):
        self.monochrome = not self.monochrome
