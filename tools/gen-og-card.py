#!/usr/bin/env python3
"""Generate the social-share card and apple-touch-icon from the full-res headshot.

Outputs (committed, served verbatim by Quarto):
  img/og-card.png          1200x630  -- Open Graph / Twitter summary_large_image
  img/apple-touch-icon.png  180x180  -- iOS home-screen bookmark

Palette + type mirror the site (warm white #fdfdfc, ink #1c1c1c, ink-navy #27496d,
muted #6b6b6b; Newsreader's fallback is Georgia, IBM Plex's is a system sans/Arial).
Source is the gitignored full-res original `profile_pic.jpg`. Re-run if it changes:
    python tools/gen-og-card.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "profile_pic.jpg"
IMG = ROOT / "img"

BG = (253, 253, 252)      # #fdfdfc warm white
INK = (28, 28, 28)        # #1c1c1c
NAVY = (39, 73, 109)      # #27496d
MUTED = (107, 107, 107)   # #6b6b6b

FONTS = Path("C:/Windows/Fonts")
def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)

GEORGIA_B = "georgiab.ttf"
ARIAL = "arial.ttf"


def circle_crop(im, size):
    """Center-square crop -> resize -> circular alpha mask (antialiased)."""
    w, h = im.size
    s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))
    ss = size * 4  # supersample for smooth edge
    im = im.resize((ss, ss), Image.LANCZOS).convert("RGBA")
    mask = Image.new("L", (ss, ss), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, ss, ss), fill=255)
    im.putalpha(mask)
    return im.resize((size, size), Image.LANCZOS)


def make_og_card():
    W, H = 1200, 630
    card = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(card)

    # --- portrait, right side, circular ---
    photo_d = 350
    photo = circle_crop(Image.open(SRC).convert("RGB"), photo_d)
    px = W - photo_d - 95
    py = (H - photo_d) // 2
    # subtle navy ring
    ring = Image.new("RGBA", (photo_d + 16, photo_d + 16), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((0, 0, photo_d + 15, photo_d + 15), outline=NAVY, width=3)
    card.paste(photo, (px, py), photo)
    card.paste(ring, (px - 8, py - 8), ring)

    # --- text column, left ---
    x = 90
    name = "Mauricio Romero"
    f_name = font(GEORGIA_B, 70)
    f_role = font(ARIAL, 32)
    f_sub = font(ARIAL, 27)
    f_url = font(ARIAL, 24)

    # vertically center the text block against the photo
    name_h = f_name.getbbox(name)[3]
    block_top = 235
    d.text((x, block_top), name, font=f_name, fill=INK)

    rule_y = block_top + name_h + 26
    d.line((x, rule_y, x + 360, rule_y), fill=NAVY, width=3)

    d.text((x, rule_y + 26), "Associate Professor of Economics · ITAM",
           font=f_role, fill=NAVY)
    d.text((x, rule_y + 72), "Co-Editor, Journal of Development Economics",
           font=f_sub, fill=MUTED)

    d.text((x, H - 60), "mauricio-romero.com", font=f_url, fill=MUTED)

    out = IMG / "og-card.png"
    card.save(out, "PNG")
    print(f"wrote {out}  ({out.stat().st_size // 1024} KB)")


def make_apple_icon():
    size = 180
    im = Image.open(SRC).convert("RGB")
    w, h = im.size
    s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))
    im = im.resize((size, size), Image.LANCZOS)
    out = IMG / "apple-touch-icon.png"
    im.save(out, "PNG")
    print(f"wrote {out}  ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    IMG.mkdir(exist_ok=True)
    make_og_card()
    make_apple_icon()
