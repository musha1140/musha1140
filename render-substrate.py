"""Deterministic GIF renderer driven by the supplied sigil-state.json.

This is a new renderer, not a recovered implementation of the original effect.
Requires Python, NumPy and Pillow. Run beside sigil-state.json.
"""
from pathlib import Path
import json
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
state = json.loads((ROOT / 'sigil-state.json').read_text())
p = state['substrate']['parameters']
W, H = 960, 240
FRAMES = 120
rng = np.random.default_rng(state['substrate']['seed'])
count = int(p['voices'])
steps = int(p['pulseSteps'])
angle = rng.uniform(0, 2 * math.pi, count)
radius = np.sqrt(rng.uniform(.025, 1, count))
family = np.arange(count) % steps
phase_offset = family * 2 * math.pi / steps
speed = 1 + family % 3
payload = rng.random(count) < p['payloadRate']
carry = (~payload) & (rng.random(count) < p['karmicCarry'])
category = np.where(payload, 1, np.where(carry, 2, 0))
palette = np.array([tuple(int(c[i:i+2], 16) for i in (1,3,5)) for c in state['substrate']['colorPalette']], dtype=np.float32)
base = np.array([2, 6, 4], dtype=np.float32)
field = np.zeros((3, H, W), dtype=np.float32)
spacing = max(12, round(H * p['latticeScale']))

# A quiet hexagonal lattice beneath the particle field.
underlay = Image.new('RGB', (W,H), tuple(base.astype(int)))
draw = ImageDraw.Draw(underlay)
for x in range(-H, W+H, spacing):
    draw.line((x,0,x+H*.58,H), fill=(7,22,15), width=1)
    draw.line((x,0,x-H*.58,H), fill=(7,22,15), width=1)
for y in range(0,H,round(spacing*.87)):
    draw.line((0,y,W,y), fill=(7,22,15), width=1)
underlay_np = np.asarray(underlay, dtype=np.float32)
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 11)
except OSError:
    font = ImageFont.load_default()

frames = []
for frame in range(FRAMES*2):
    t = 2 * math.pi * (frame % FRAMES) / FRAMES
    theta = angle + t * speed
    pulse = 1 + .055 * np.sin(steps*t + phase_offset)
    a = .385*W*radius*pulse
    b = .345*H*radius*pulse
    x = W/2 + a*np.cos(theta) + .055*W*radius*np.sin(2*theta-t+phase_offset)
    y = H/2 + b*np.sin(theta) + .07*H*radius*np.cos(3*theta+2*t+phase_offset)
    xi = np.clip(np.rint(x).astype(int), 0, W-1)
    yi = np.clip(np.rint(y).astype(int), 0, H-1)
    field *= 1-p['trailFade']
    intensity = .07+.09*(.5+.5*np.sin(theta+t+phase_offset))
    intensity[payload] *= 1.8
    np.add.at(field, (category, yi, xi), intensity)

    # Symmetric short-range diffusion gives the lattice a soft phosphor glow.
    glow = field.copy()
    for axis in (1,2):
        for offset, weight in ((1,.20),(2,.10),(3,.035)):
            glow += weight * (np.roll(field, offset, axis=axis)+np.roll(field, -offset, axis=axis))
    light = np.einsum('chw,cd->hwd', 1-np.exp(-glow*1.25), palette)
    rgb = np.clip(underlay_np + light, 0, 255).astype(np.uint8)
    image = Image.fromarray(rgb)
    d = ImageDraw.Draw(image)
    d.line((20,H-29,W-20,H-29), fill=(13,47,31))
    d.text((22,H-21), 'SAMSARA SUBSTRATE / '+state['identity'], font=font, fill=(151,194,171))
    status = f"SEED {state['substrate']['seed']}  /  {count} VOICES  /  {p['cycleSeconds']}s  /  {steps} STEPS"
    text_width = d.textbbox((0,0), status, font=font)[2]
    d.text((W-22-text_width,H-21), status, font=font, fill=(151,194,171))
    if frame >= FRAMES:
        frames.append(image)

# Compact output; use one shared palette to prevent color flicker.
frames = [f.resize((720,180), Image.Resampling.LANCZOS) for f in frames]
contact = Image.new('RGB',(720,180*8))
for i in range(8): contact.paste(frames[i*FRAMES//8],(0,i*180))
gif_palette = contact.quantize(colors=96, method=Image.Quantize.MEDIANCUT)
indexed = [f.quantize(palette=gif_palette, dither=Image.Dither.NONE) for f in frames]
tick_count = round(p['cycleSeconds']*100)
durations = [(math.floor((i+1)*tick_count/FRAMES)-math.floor(i*tick_count/FRAMES))*10 for i in range(FRAMES)]
destination = ROOT/'assets'/'samsara-substrate.gif'
destination.parent.mkdir(exist_ok=True)
indexed[0].save(destination, save_all=True, append_images=indexed[1:], duration=durations, loop=0, disposal=1, optimize=True)
if (ROOT.parent/'qa').is_dir():
    frames[30].save(ROOT.parent/'qa'/'substrate-frame.png')
print(json.dumps({'path':str(destination),'frames':FRAMES,'duration_ms':sum(durations),'bytes':destination.stat().st_size}))
