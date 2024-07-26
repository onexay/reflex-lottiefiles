# -*- coding: utf-8 -*-


import reflex as rx

from reflex_lottiefiles import LottieFiles

font = "https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap"

class State(rx.State):
    """The app state."""

    url: str

    def set_url(self, url: str) -> None:
        self.url = url

    @rx.var
    def get_url(self) -> str:
        return self.url

def config_option(title: str, description: str) -> rx.Component:
    return rx.vstack(
        rx.text.strong(
            title, 
            size="2"
        ),
        rx.text(
            description, 
            size="2"
        ),
        rx.input(
            placeholder="Enter a URL",
            type="url",
            width="100%",
            on_change=State.set_url
        ),
        width="100%",
        spacing="1"
    )

def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position='top-right'),
        rx.hstack(
            rx.vstack(
                rx.heading(
                    "Reflex Lottiefiles Demo", 
                    size="8"
                ),
                rx.text(
                    "A Lottie is a JSON-based animation file format that uses "\
                    "a textual, descriptive representation of the animation "\
                    "elements and movement, with support for image assets and "\
                    "has dynamic scripting. Lottie format files are much smaller "\
                    "in size compared to the alternative of using videos or "\
                    "animated image formats such as APNG or GIF while preserving "\
                    "resolution independence with the use of vector graphics.",
                    size="2"
                ),
                rx.hstack(
                    rx.button(
                        "LottieFiles",
                        on_click=rx.redirect("https://lottiefiles.com/", external=True)
                    ),
                    rx.button(
                        "dotLottie",
                        on_click=rx.redirect("https://dotlottie.io/", external=True)
                    ),
                    spacing="2"
                ),
                config_option(
                    "Source",
                    "URL to the animation data (.json or .lottie)."
                ),
                rx.flex(
                    rx.cond(
                        State.get_url is not None,
                        LottieFiles(
                            src=State.get_url,
                            autoplay=True,
                            loop=False,
                            play_on_hover=True,
                            width="25em"
                        )
                    ),
                    width="100%",
                    height="100%",
                ),
                align="start",
                justify="start",
                spacing="2em",
                min_width="100%"
            ),
            margin_top="5rem",
            width="100%"
        ),
        min_height="85vh",
        size="md",
    )

# Add state and page to the app.
app = rx.App(
        stylesheets=[font], 
        style={"fontFamily": "Manrope"}
    )
app.add_page(index)
