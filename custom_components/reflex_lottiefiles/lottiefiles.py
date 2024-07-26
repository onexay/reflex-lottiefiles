"""Reflex custom component Lottiefiles."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

from typing import Literal, Optional
import reflex as rx

AnimationPlayModes = Literal[
    'forward',
    'reverse',
    'bounce',
    'reverse-bounce',
]

class RenderConfig(rx.Base):
    """Lottiefiles render config."""

    """
    Device pixel ratio
    """
    device_pixel_ratio: rx.Var[int]

class LottieFiles(rx.NoSSRComponent):
    """Lottiefiles component."""

    # The React library to wrap.
    library = "@lottiefiles/dotlottie-react" # https://www.npmjs.com/package/@lottiefiles/dotlottie-react

    # The React component tag.
    tag = "DotLottieReact"

    # Reflex alias
    alias = "LottieFiles"

    # Props

    """
    Auto-starts the animation on load.
    """
    autoplay: Optional[rx.Var[bool]] = False

    """
    Determines if the animation should loop.
    """
    loop: Optional[rx.Var[bool]] = False

    """
    Source
    """
    src: Optional[rx.Var[str]]

    """
    Source as string
    """
    data: Optional[rx.Var[str]]

    """
    Named marker
    """
    marker: Optional[rx.Var[str]]

    """
    Animation play speed
    """
    speed: Optional[rx.Var[int]] = 1

    """
    Animation play mode
    """
    mode: Optional[rx.Var[AnimationPlayModes]] = "forward"

    """
    Background color
    """
    background_color: Optional[rx.Var[str]]

    """
    Render config
    """
    render_config: Optional[rx.Var[RenderConfig]] = {}

    """
    Determines if the animation should play on mouse hover and pause on mouse out.
    """
    play_on_hover: Optional[rx.Var[bool]] = False

    """
    Determines if the animation should update on subframes. If set to false, 
    the original AE frame rate will be maintained. If set to true, it will 
    refresh at each requestAnimationFrame, including intermediate 
    values.
    """
    use_frame_interpolation: Optional[rx.Var[bool]] = True

    """
    Determines if the canvas should resize automatically to its container
    """
    auto_resize_canvas: Optional[rx.Var[bool]] = True

LottieFiles = LottieFiles.create
