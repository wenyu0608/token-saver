#!/usr/bin/env python3
"""Build the reproducible Token Saver launch demo GIF."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "token-saver-demo.gif"
W, H = 960, 540
PAPER, INK, LIME = "#f3efe4", "#11120f", "#c7ff35"
MUTED, WHITE, RED = "#8f9187", "#f8f7f1", "#ff6b5f"
MONO = "/System/Library/Fonts/SFNSMono.ttf"
SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F = {
    "brand": font(BOLD, 26), "hero": font(BOLD, 42), "h2": font(BOLD, 28),
    "body": font(SANS, 20), "small": font(SANS, 15), "mono": font(MONO, 18),
    "mono_small": font(MONO, 14), "mono_bold": font(MONO, 18),
}


def base():
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((42, 28, 90, 76), 8, fill=INK)
    d.text((55, 43), "TS", font=font(BOLD, 16), fill=LIME)
    d.text((104, 38), "Token Saver", font=F["brand"], fill=INK)
    d.text((104, 66), "SPEND CONTEXT LIKE CURRENCY", font=F["mono_small"], fill=MUTED)
    d.line((42, 96, 918, 96), fill="#c9c5bb", width=2)
    return im, d


def terminal(d):
    d.rounded_rectangle((42, 116, 918, 480), 14, fill=INK)
    d.ellipse((64, 137, 76, 149), fill=RED)
    d.ellipse((84, 137, 96, 149), fill="#ffc857")
    d.ellipse((104, 137, 116, 149), fill=LIME)
    d.text((390, 135), "token-saver / demo", font=F["mono_small"], fill=MUTED)
    d.line((42, 164, 918, 164), fill="#30322e", width=1)


def frame_intro(progress):
    im, d = base()
    d.text((70, 164), "Your coding agent doesn't need", font=F["hero"], fill=INK)
    d.text((70, 218), "a bigger context window.", font=F["hero"], fill=INK)
    reveal = int(24 * progress)
    d.rounded_rectangle((70, 302, 890, 386), 10, fill=INK)
    d.text((94, 326), "It needs a budget brain."[:reveal], font=F["h2"], fill=LIME)
    d.text((70, 438), "Open source · local first · correctness-aware", font=F["body"], fill=MUTED)
    return im


def frame_prompt(progress):
    im, d = base(); terminal(d)
    prompt = "$ token-saver analyze DreamZero and explain its architecture"
    shown = prompt[:int(len(prompt) * progress)]
    d.text((72, 196), shown, font=F["mono"], fill=WHITE)
    if progress < 1:
        x = 72 + d.textlength(shown, font=F["mono"])
        d.rectangle((x + 2, 195, x + 12, 218), fill=LIME)
    d.text((72, 438), "One prompt. The router chooses the context budget.", font=F["small"], fill=MUTED)
    return im


def frame_route(progress):
    im, d = base(); terminal(d)
    d.text((72, 192), "$ token-saver analyze DreamZero and explain its architecture", font=F["mono_small"], fill=WHITE)
    rows = [
        ("✓ task classified", "code + paper analysis"),
        ("✓ fidelity selected", "focused context"),
        ("✓ methods enabled", "Repomix + Docs Slice"),
    ]
    for i, (label, value) in enumerate(rows):
        alpha = max(0, min(1, progress * 3 - i))
        if alpha <= 0: continue
        y = 248 + i * 54
        d.text((74, y), label, font=F["mono_small"], fill=LIME)
        d.text((330, y), value, font=F["mono"], fill=WHITE)
    d.rounded_rectangle((70, 415, 890, 455), 8, fill="#242620")
    d.text((88, 426), "Token Saver｜Repomix + Docs Slice", font=F["mono_small"], fill=LIME)
    return im


def frame_funnel(progress):
    im, d = base(); terminal(d)
    d.text((72, 190), "CONTEXT FUNNEL", font=F["mono_small"], fill=LIME)
    start, end = 337_054, 54_855
    current = int(start + (end - start) * progress)
    d.text((72, 226), f"{start:,}", font=F["h2"], fill=WHITE)
    d.text((250, 232), "candidate tokens", font=F["small"], fill=MUTED)
    d.rounded_rectangle((72, 286, 850, 330), 8, fill="#353831")
    width = 778 * (current / start)
    d.rounded_rectangle((72, 286, 72 + width, 330), 8, fill=LIME)
    d.text((72, 354), f"{current:,} focused tokens", font=F["h2"], fill=WHITE)
    saved = 100 * (1 - current / start)
    d.text((660, 354), f"↓ {saved:0.1f}%", font=F["h2"], fill=LIME)
    d.text((72, 426), "Measured on DreamZero commit ab790c1 · never generalized", font=F["mono_small"], fill=MUTED)
    return im


def frame_answer(progress):
    im, d = base(); terminal(d)
    d.text((72, 187), "ARCHITECTURE ANSWER", font=F["mono_small"], fill=LIME)
    files = [
        "base_vla.py", "  └─ joint video-action inference",
        "wan_flow_matching_action_tf.py", "  └─ denoising + action sampling",
        "wan_video_dit_action_casual_chunk.py", "  └─ causal DiT + KV cache",
    ]
    count = max(1, int(len(files) * progress + .5))
    for i, line in enumerate(files[:count]):
        color = WHITE if i % 2 == 0 else MUTED
        d.text((72, 226 + i * 34), line, font=F["mono_small"], fill=color)
    d.rounded_rectangle((625, 190, 878, 420), 10, fill="#242620")
    d.text((649, 216), "CORRECTNESS", font=F["mono_small"], fill=LIME)
    d.text((649, 257), "✓ evidence trail", font=F["mono_small"], fill=WHITE)
    d.text((649, 294), "✓ file pointers", font=F["mono_small"], fill=WHITE)
    d.text((649, 331), "✓ honest receipt", font=F["mono_small"], fill=WHITE)
    d.text((649, 376), "No blind summary.", font=F["mono_small"], fill=MUTED)
    return im


def frame_cta(progress):
    im, d = base()
    d.text((72, 142), "Give your agent", font=F["hero"], fill=INK)
    d.text((72, 194), "a budget brain.", font=F["hero"], fill=INK)
    d.rounded_rectangle((72, 284, 888, 340), 8, fill=INK)
    d.text((94, 302), "codex plugin marketplace add wenyu0608/token-saver --ref main", font=F["mono_small"], fill=LIME)
    d.rounded_rectangle((72, 354, 888, 410), 8, fill=INK)
    d.text((94, 372), "codex plugin add token-saver@token-saver", font=F["mono_small"], fill=WHITE)
    d.text((72, 458), "wenyu0608.github.io/token-saver", font=F["mono"], fill=INK)
    return im


def add_scene(frames, maker, moving, hold=0):
    for i in range(moving):
        frames.append(maker(i / max(1, moving - 1)))
    for _ in range(hold):
        frames.append(maker(1))


def main():
    frames = []
    add_scene(frames, frame_intro, 12, 12)
    add_scene(frames, frame_prompt, 24, 8)
    add_scene(frames, frame_route, 18, 12)
    add_scene(frames, frame_funnel, 25, 12)
    add_scene(frames, frame_answer, 20, 14)
    add_scene(frames, frame_cta, 8, 20)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=140,
                   loop=0, optimize=True, disposal=2)
    print(f"{OUT} | {len(frames)} frames | {len(frames)*0.14:.1f}s")


if __name__ == "__main__":
    main()
