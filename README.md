# LottieFiles

A Reflex custom component for [LottieFiles](https://lottiefiles.com/)/[dotLottie](https://dotlottie.io/) based on [@lottiefiles/dotlottie-react](https://www.npmjs.com/package/@lottiefiles/dotlottie-react).

## Installation

### PIP

```bash
pip install reflex-lottiefiles
```

### Poetry

```bash
poetry add reflex-lottiefiles
```

## Usage

### Props

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `autoplay` | `bool` | `False` | Auto-starts the animation on load |
| `loop` | `bool` | `False` | Determines if the animation should loop |
| `src` | `string` | | URL to the animation data (.json or .lottie) |
| `data` | `string` | | Source as string |
| `marker` | `string` | | Named marker |
| `speed` | `int` | `1` | | Animation play speed |
| `mode` | `forward` `reverse` `bounce` `reverse-bounce` | `forward` | Animation play mode |
| `background_color` | `string` | | Background color of the canvas. A 6-digit or 8-digit hex color string |
| `play_on_hover` | `bool` | `False` | Determines if the animation should play on mouse hover and pause on mouse out |

### Sample

```python
from reflex_lottiefiles import LottieFiles

def index():
    return LottieFiles(
        src="URL",
        autoplay=True,
        loop=True,
    )
```

See [demo code](https://github.com/onexay/reflex-lottiefiles/blob/main/lottiefiles_demo/lottiefiles_demo/lottiefiles_demo.py) for details.