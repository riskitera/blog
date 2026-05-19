#!/usr/bin/env python3
"""
Generate cover images for Riskitera blog posts.
Brand colors: navy #0b1220, blue #3b82f6, violet #8b5cf6, cyan #06b6d4
Size: 1024x576 (16:9)
"""

import os
import hashlib
import math
import textwrap
import yaml
from PIL import Image, ImageDraw, ImageFont

# === Config ===
WIDTH, HEIGHT = 1024, 576
POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "es", "posts")

# Brand colors
BG_DARK = (11, 18, 32)       # #0b1220
BLUE = (59, 130, 246)         # #3b82f6
VIOLET = (139, 92, 246)       # #8b5cf6
CYAN = (6, 182, 212)          # #06b6d4
TEXT_WHITE = (230, 234, 242)  # #e6eaf2
TEXT_SEC = (136, 146, 164)    # #8892a4
CARD_BG = (17, 24, 39)       # #111827

# Category color mapping
CATEGORY_COLORS = {
    "GRC": BLUE,
    "SOC": CYAN,
    "CTI": VIOLET,
    "General": BLUE,
    "Compliance": BLUE,
    "Sector": CYAN,
}

# Category icons (geometric patterns)
CATEGORY_ICONS = {
    "GRC": "shield",
    "SOC": "radar",
    "CTI": "crosshair",
    "General": "grid",
    "Compliance": "check",
    "Sector": "building",
}

# Fonts
FONT_BOLD = "/System/Library/Fonts/SFNS.ttf"
FONT_REGULAR = "/System/Library/Fonts/SFNS.ttf"
FALLBACK_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FALLBACK_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"


def load_font(path, size, fallback=None):
    try:
        return ImageFont.truetype(path, size)
    except (OSError, IOError):
        if fallback:
            return ImageFont.truetype(fallback, size)
        return ImageFont.load_default()


def seed_from_slug(slug):
    """Deterministic seed from slug for reproducible patterns."""
    return int(hashlib.md5(slug.encode()).hexdigest()[:8], 16)


def draw_grid_pattern(draw, seed, accent_color):
    """Draw subtle geometric grid pattern."""
    import random
    rng = random.Random(seed)

    # Diagonal lines
    for _ in range(12):
        x1 = rng.randint(0, WIDTH)
        y1 = rng.randint(0, HEIGHT)
        length = rng.randint(80, 200)
        angle = rng.choice([math.pi/4, -math.pi/4, math.pi/6, -math.pi/6])
        x2 = x1 + int(length * math.cos(angle))
        y2 = y1 + int(length * math.sin(angle))
        opacity = rng.randint(15, 35)
        color = (*accent_color[:3], opacity)
        draw.line([(x1, y1), (x2, y2)], fill=color, width=1)

    # Dots at intersections
    for _ in range(20):
        x = rng.randint(0, WIDTH)
        y = rng.randint(0, HEIGHT)
        r = rng.randint(2, 4)
        opacity = rng.randint(20, 50)
        color = (*accent_color[:3], opacity)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=color)

    # Circles (radar/tech feel)
    for _ in range(3):
        cx = rng.randint(WIDTH//2, WIDTH)
        cy = rng.randint(0, HEIGHT//2)
        radius = rng.randint(60, 180)
        opacity = rng.randint(10, 25)
        color = (*accent_color[:3], opacity)
        draw.ellipse([cx-radius, cy-radius, cx+radius, cy+radius], outline=color, width=1)


def draw_hex_pattern(draw, seed, accent_color):
    """Draw hexagonal grid pattern (tech/security feel)."""
    import random
    rng = random.Random(seed)

    hex_size = 40
    for row in range(-1, HEIGHT // (hex_size * 2) + 2):
        for col in range(-1, WIDTH // (hex_size * 2) + 2):
            cx = col * hex_size * 1.75 + (row % 2) * hex_size * 0.875
            cy = row * hex_size * 1.5
            if rng.random() > 0.6:
                continue
            opacity = rng.randint(8, 25)
            color = (*accent_color[:3], opacity)
            points = []
            for i in range(6):
                angle = math.pi / 3 * i - math.pi / 6
                px = cx + hex_size * 0.5 * math.cos(angle)
                py = cy + hex_size * 0.5 * math.sin(angle)
                points.append((px, py))
            if len(points) >= 3:
                draw.polygon(points, outline=color)


def draw_circuit_pattern(draw, seed, accent_color):
    """Draw circuit-board style pattern."""
    import random
    rng = random.Random(seed)

    for _ in range(15):
        x = rng.randint(0, WIDTH)
        y = rng.randint(0, HEIGHT)
        opacity = rng.randint(15, 40)
        color = (*accent_color[:3], opacity)

        # Horizontal or vertical lines with right-angle turns
        segments = rng.randint(2, 5)
        points = [(x, y)]
        for _ in range(segments):
            length = rng.randint(30, 120)
            direction = rng.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
            nx = points[-1][0] + direction[0] * length
            ny = points[-1][1] + direction[1] * length
            points.append((nx, ny))

        for i in range(len(points) - 1):
            draw.line([points[i], points[i+1]], fill=color, width=1)

        # Node dots at turns
        for p in points:
            r = 3
            draw.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=color)


def draw_gradient_bar(draw, y, height, color_left, color_right):
    """Draw horizontal gradient bar."""
    for x in range(WIDTH):
        ratio = x / WIDTH
        r = int(color_left[0] * (1 - ratio) + color_right[0] * ratio)
        g = int(color_left[1] * (1 - ratio) + color_right[1] * ratio)
        b = int(color_left[2] * (1 - ratio) + color_right[2] * ratio)
        draw.line([(x, y), (x, y + height)], fill=(r, g, b, 180))


def wrap_title(title, font, max_width):
    """Word-wrap title to fit max_width."""
    words = title.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = font.getbbox(test)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def generate_cover(slug, title, category, tags):
    """Generate a cover image for a blog post."""
    accent = CATEGORY_COLORS.get(category, BLUE)
    seed = seed_from_slug(slug)
    pattern_type = seed % 3  # 0=grid, 1=hex, 2=circuit

    # Create image with alpha for patterns
    img = Image.new("RGBA", (WIDTH, HEIGHT), (*BG_DARK, 255))
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)

    # Draw pattern
    if pattern_type == 0:
        draw_grid_pattern(draw_overlay, seed, accent)
    elif pattern_type == 1:
        draw_hex_pattern(draw_overlay, seed, accent)
    else:
        draw_circuit_pattern(draw_overlay, seed, accent)

    img = Image.alpha_composite(img, overlay)

    # Convert to RGB for final drawing
    final = img.convert("RGB")
    draw = ImageDraw.Draw(final)

    # Gradient accent bar at top
    for x in range(WIDTH):
        ratio = x / WIDTH
        r = int(accent[0] * (1 - ratio) + VIOLET[0] * ratio)
        g = int(accent[1] * (1 - ratio) + VIOLET[1] * ratio)
        b = int(accent[2] * (1 - ratio) + VIOLET[2] * ratio)
        draw.line([(x, 0), (x, 4)], fill=(r, g, b))

    # Category badge
    font_cat = load_font(FONT_BOLD, 18, FALLBACK_BOLD)
    cat_text = category.upper()
    cat_bbox = font_cat.getbbox(cat_text)
    cat_w = cat_bbox[2] - cat_bbox[0] + 24
    cat_h = cat_bbox[3] - cat_bbox[1] + 14
    cat_x, cat_y = 60, 50
    # Rounded rect for badge
    draw.rounded_rectangle(
        [cat_x, cat_y, cat_x + cat_w, cat_y + cat_h],
        radius=6,
        fill=(*accent, ),
    )
    draw.text((cat_x + 12, cat_y + 4), cat_text, fill=TEXT_WHITE, font=font_cat)

    # Tags (smaller, below category)
    if tags:
        font_tag = load_font(FONT_REGULAR, 14, FALLBACK_REG)
        tag_text = " · ".join(tags[:3])
        draw.text((62, cat_y + cat_h + 16), tag_text, fill=TEXT_SEC, font=font_tag)

    # Title
    font_title = load_font(FONT_BOLD, 42, FALLBACK_BOLD)
    max_title_w = WIDTH - 120
    lines = wrap_title(title, font_title, max_title_w)

    # Position title vertically centered in remaining space
    line_height = 52
    total_title_h = len(lines) * line_height
    title_y = max(cat_y + cat_h + 60, (HEIGHT - total_title_h) // 2)

    for i, line in enumerate(lines):
        draw.text(
            (60, title_y + i * line_height),
            line,
            fill=TEXT_WHITE,
            font=font_title,
        )

    # Bottom bar with gradient
    bar_y = HEIGHT - 50
    for x in range(WIDTH):
        ratio = x / WIDTH
        r = int(accent[0] * ratio)
        g = int(accent[1] * ratio)
        b = int(accent[2] * ratio)
        a = int(60 * ratio)
        # Blend with background
        bg_r, bg_g, bg_b = BG_DARK
        fr = int(bg_r * (1 - a/255) + r * (a/255))
        fg = int(bg_g * (1 - a/255) + g * (a/255))
        fb = int(bg_b * (1 - a/255) + b * (a/255))
        draw.line([(x, bar_y), (x, HEIGHT)], fill=(fr, fg, fb))

    # Riskitera wordmark bottom-right
    font_brand = load_font(FONT_BOLD, 16, FALLBACK_BOLD)
    draw.text((WIDTH - 160, HEIGHT - 35), "RISKITERA", fill=TEXT_SEC, font=font_brand)

    # Subtle separator line
    draw.line([(60, bar_y - 1), (WIDTH - 60, bar_y - 1)], fill=(*accent, ), width=1)

    return final


def get_post_metadata(post_dir):
    """Read frontmatter from index.md."""
    index_path = os.path.join(post_dir, "index.md")
    if not os.path.exists(index_path):
        return None

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return None

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None

    try:
        meta = yaml.safe_load(parts[1])
        return meta
    except yaml.YAMLError:
        return None


def main():
    generated = 0
    skipped = 0

    for entry in sorted(os.listdir(POSTS_DIR)):
        post_dir = os.path.join(POSTS_DIR, entry)
        if not os.path.isdir(post_dir) or entry.startswith("_"):
            continue

        cover_path = os.path.join(post_dir, "cover.png")
        if os.path.exists(cover_path):
            skipped += 1
            continue

        meta = get_post_metadata(post_dir)
        if not meta:
            print(f"  SKIP (no meta): {entry}")
            continue

        title = meta.get("title", entry.replace("-", " ").title())
        categories = meta.get("categories", ["General"])
        category = categories[0] if categories else "General"
        tags = meta.get("tags", [])

        img = generate_cover(entry, title, category, tags)
        img.save(cover_path, "PNG", quality=95)
        generated += 1
        print(f"  OK: {entry}")

    print(f"\nDone: {generated} generated, {skipped} skipped (already had cover)")


if __name__ == "__main__":
    main()
