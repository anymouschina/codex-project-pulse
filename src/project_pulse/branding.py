"""Local icons and desktop-read-state badges, independent of UI selection."""
import base64
from functools import lru_cache
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[2] / "assets"


@lru_cache(maxsize=4)
def icon(unread=False, dark=False):
    # PNG avoids SVG-specific template rendering in hosts that support color
    # raster icons. A host may still tint it; this is not a native badge API.
    suffix = "-dark" if dark else ""
    state = "unread" if unread else "outline"
    png = (ASSETS / f"entrypoint-{state}{suffix}.png").read_bytes()
    return {"src": "data:image/png;base64," + base64.b64encode(png).decode(),
            "mimeType": "image/png", "sizes": ["120x120"], "theme": "dark" if dark else "light"}


def entrypoint_icons(unread=False):
    return [icon(unread), icon(unread, dark=True)]


def has_unread(snapshot):
    badge = snapshot.get("unreadBadge", {})
    return badge.get("known") is True and badge.get("count", 0) > 0
