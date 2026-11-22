"""Render a preview PNG for each character/stage zip.

Usage: python tools/preview.py chars/Foo.zip stages/Bar.zip ...
Writes previews/<chars|stages>/<zip name>.png next to the repository root.
"""
import io
import json
import os
import re
import sys
import zipfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sff import SFF, read_act  # noqa: E402

CARD = (480, 270)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Pack:
    """Case-insensitive file access inside a zip, paths normalised to '/'."""

    def __init__(self, path):
        self.zf = zipfile.ZipFile(path)
        self.names = {n.replace("\\", "/").lower(): n for n in self.zf.namelist()}

    def read(self, *candidates):
        for c in candidates:
            key = os.path.normpath(c.replace("\\", "/")).replace("\\", "/").lower()
            if key in self.names:
                return self.zf.read(self.names[key])
        return None

    def require(self, what, *candidates):
        data = self.read(*candidates)
        if data is None:
            raise ValueError("missing %s: %s" % (what, candidates[0]))
        return data

    def close(self):
        self.zf.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


def parse_def(text):
    """Return list of (section, {key: value}) preserving order."""
    out, cur = [], None
    for line in text.splitlines():
        line = line.split(";")[0].strip()
        m = re.match(r"\[(.+?)\]", line)
        if m:
            cur = {}
            out.append((m.group(1).strip().lower(), cur))
        elif cur is not None and "=" in line:
            k, v = line.split("=", 1)
            cur[k.strip().lower()] = v.strip().strip('"')
    return out


def nums(v, default):
    vals = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", v or "")]
    return vals + list(default[len(vals):])


def font(size):
    try:
        return ImageFont.load_default(size)
    except TypeError:
        return ImageFont.load_default()


def fit(img, box):
    s = min(box[0] / img.width, box[1] / img.height, 3)
    if s <= 0:
        return img
    return img.resize((max(1, int(img.width * s)), max(1, int(img.height * s))), Image.NEAREST)


def char_card(pack, zip_name):
    name = os.path.splitext(zip_name)[0]
    raw = pack.read(f"{name}/{name}.def")
    if raw is None:
        raise ValueError("missing %s/%s.def" % (name, name))
    secs = dict(parse_def(raw.decode("latin-1")))
    files, info = secs.get("files", {}), secs.get("info", {})
    sff = SFF(pack.require("sprite file", f"{name}/{files.get('sprite', '')}"))
    act = pack.read(f"{name}/{files['pal1']}") if files.get("pal1") else None
    pal = read_act(act) if act and sff.version == 1 else None

    def spr(g, i, use_act=True):
        s = sff.index.get((g, i))
        if s is None:
            return None
        p = pal if use_act and (s.same_pal or s is sff.sprites[0]) else None
        return Image.fromarray(sff.rgba(s, p), "RGBA")

    card = Image.new("RGBA", CARD, (18, 20, 32, 255))
    grad = np.linspace(40, 10, CARD[1], dtype=np.uint8)[:, None]
    card.paste(Image.fromarray(np.dstack([grad.repeat(CARD[0], 1)] * 3 + [np.full((CARD[1], CARD[0]), 255, np.uint8)])))
    portrait = spr(9000, 1, False) or spr(9000, 0, False)
    idle = spr(0, 0)
    if idle is None:
        idle = Image.fromarray(sff.rgba(sff.sprites[0], pal), "RGBA")
    if portrait is not None:
        p = fit(portrait, (180, 220))
        card.alpha_composite(p, (16, 20 + (220 - p.height) // 2))
    i = fit(idle, (260, 220))
    card.alpha_composite(i, (200 + (264 - i.width) // 2, 230 - i.height))
    title = info.get("displayname") or info.get("name") or name
    d = ImageDraw.Draw(card)
    d.rectangle((0, 238, CARD[0], CARD[1]), fill=(0, 0, 0, 200))
    d.text((12, 242), title, fill=(255, 255, 255, 255), font=font(18))
    return card


def exact_sprites(pack, name):
    meta = pack.read(f"{name}/sprites/meta.json")
    if not meta:
        return None, None
    files = {(s["g"], s["i"]): s["file"] for s in json.loads(meta)["sff"]["sprites"] if s.get("file")}
    read = lambda key: pack.read(f"{name}/sprites/{files[key]}") if key in files else None
    return read((0, 0)), read((9000, 1)) or read((9000, 0))


def umf_card(pack, zip_name):
    name = os.path.splitext(zip_name)[0]
    names = [n for n in pack.names if n.startswith(name.lower() + "/") and n.count("/") == 1 and n.endswith(".json")]
    title = name
    if names:
        title = json.loads(pack.read(names[0])).get("name", name)
    idle_raw, portrait_raw = exact_sprites(pack, name)
    if idle_raw is None:
        idle_raw = pack.require("idle sprite", f"{name}/sprites/01_idle.png")
        portrait_raw = pack.read(f"{name}/sprites/portrait.png")
    idle = Image.open(io.BytesIO(idle_raw)).convert("RGBA")
    card = Image.new("RGBA", CARD, (18, 20, 32, 255))
    grad = np.linspace(40, 10, CARD[1], dtype=np.uint8)[:, None]
    card.paste(Image.fromarray(np.dstack([grad.repeat(CARD[0], 1)] * 3 + [np.full((CARD[1], CARD[0]), 255, np.uint8)])))
    if portrait_raw:
        p = fit(Image.open(io.BytesIO(portrait_raw)).convert("RGBA"), (180, 220))
        card.alpha_composite(p, (16, 20 + (220 - p.height) // 2))
    i = fit(idle, (260, 220))
    card.alpha_composite(i, (200 + (264 - i.width) // 2, 230 - i.height))
    d = ImageDraw.Draw(card)
    d.rectangle((0, 238, CARD[0], CARD[1]), fill=(0, 0, 0, 200))
    d.text((12, 242), title, fill=(255, 255, 255, 255), font=font(18))
    return card


def anim_frames(text):
    acts, cur = {}, None
    for line in text.splitlines():
        line = line.split(";")[0].strip()
        m = re.match(r"\[\s*begin\s+action\s+(-?\d+)\s*\]", line, re.I)
        if m:
            cur = int(m.group(1))
        elif cur is not None and cur not in acts and re.match(r"-?\d+\s*,\s*-?\d+", line):
            g, i, x, y = nums(line, (0, 0, 0, 0))[:4]
            acts[cur] = (int(g), int(i), x, y)
    return acts


def stage_card(pack, zip_name):
    defs = [n for n in pack.names if n.startswith("stages/") and n.endswith(".def")]
    if not defs:
        raise ValueError("no stage .def")
    text = pack.zf.read(pack.names[defs[0]]).decode("latin-1")
    secs = parse_def(text)
    sd = dict(secs)
    w, h = (int(v) for v in nums(sd.get("stageinfo", {}).get("localcoord"), (320, 240))[:2])
    bgdef = next((kv for s, kv in secs if s == "bgdef"), {})
    sprpath = bgdef.get("spr", "")
    sff = SFF(pack.require("stage sprite file", sprpath, "stages/" + sprpath, "stages/" + os.path.basename(sprpath)))
    acts = anim_frames(text)
    canvas = np.zeros((h, w, 3), np.float32)
    elems = [kv for s, kv in secs if s.startswith("bg ") or (s.startswith("bg") and s != "bgdef" and "type" in kv)]
    for layer in (0, 1):
        prev = (0.0, 0.0)
        for kv in elems:
            start = nums(kv.get("start"), (0, 0))[:2]
            if kv.get("positionlink", "0").strip() == "1":
                start = [start[0] + prev[0], start[1] + prev[1]]
            prev = start
            if int(nums(kv.get("layerno"), (0,))[0]) != layer:
                continue
            typ = kv.get("type", "normal").lower()
            off = (0, 0)
            if typ == "anim":
                fr = acts.get(int(nums(kv.get("actionno"), (-1,))[0]))
                if not fr:
                    continue
                g, i, off = fr[0], fr[1], fr[2:]
            else:
                g, i = (int(v) for v in nums(kv.get("spriteno"), (-1, -1))[:2])
            s = sff.index.get((g, i))
            if s is None:
                continue
            img = sff.rgba(s).astype(np.float32)
            if typ == "normal" and kv.get("mask", "0").strip() == "0" and sff.version == 1:
                img[..., 3] = 255
            tx, ty = (int(v) for v in nums(kv.get("tile"), (0, 0))[:2])
            sx, sy = nums(kv.get("tilespacing"), (0, 0))[:2]
            x0 = int(w / 2 + start[0] + off[0] - s.axis[0])
            y0 = int(start[1] + off[1] - s.axis[1])
            stepx, stepy = img.shape[1] + int(sx), img.shape[0] + int(sy)
            xs = _tiles(x0, stepx, tx, w)
            ys = _tiles(y0, stepy, ty, h)
            add = kv.get("trans", "").lower().startswith("add")
            for y in ys:
                for x in xs:
                    _blit(canvas, img, x, y, add)
    out = Image.fromarray(np.clip(canvas, 0, 255).astype(np.uint8), "RGB")
    out = out.resize((CARD[0], int(CARD[0] * h / w)), Image.LANCZOS)
    card = Image.new("RGBA", (CARD[0], out.height + 32), (0, 0, 0, 255))
    card.paste(out, (0, 0))
    title = sd.get("info", {}).get("name") or os.path.splitext(zip_name)[0]
    ImageDraw.Draw(card).text((12, out.height + 6), title, fill=(255, 255, 255, 255), font=font(18))
    return card


def _tiles(p0, step, count, limit):
    if step <= 0 or count == 0:
        return [p0]
    if count == 1:
        first = p0 - ((p0 // step) + 1) * step
        return list(range(first, limit, step))
    return [p0 + k * step for k in range(count)]


def _blit(canvas, img, x, y, add):
    h, w = canvas.shape[:2]
    x1, y1, x2, y2 = max(x, 0), max(y, 0), min(x + img.shape[1], w), min(y + img.shape[0], h)
    if x1 >= x2 or y1 >= y2:
        return
    src = img[y1 - y:y2 - y, x1 - x:x2 - x]
    a = src[..., 3:4] / 255.0
    dst = canvas[y1:y2, x1:x2]
    canvas[y1:y2, x1:x2] = dst + src[..., :3] * a if add else dst * (1 - a) + src[..., :3] * a


def main(paths):
    failed = 0
    for path in paths:
        kind = os.path.basename(os.path.dirname(os.path.abspath(path)))
        zip_name = os.path.basename(path)
        try:
            with Pack(path) as pack:
                card = {"chars": char_card, "umf": umf_card}.get(kind, stage_card)(pack, zip_name)
        except Exception as e:  # report and continue with the next pack
            print("FAIL %s: %s" % (path, e))
            failed += 1
            continue
        out = os.path.join(ROOT, "previews", kind, os.path.splitext(zip_name)[0] + ".png")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        card.convert("RGB").save(out, optimize=True)
        print("ok", out)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
