"""Fail if any chars/stages zip lacks a PNG preview in previews/, or a preview has no zip.

Also checks that each zip is readable, follows the layout documented in the README
(chars: <Name>/<Name>.def; stages: stages/*.def) and has no absolute or ".." paths.
"""
import os
import sys
import zipfile

PNG_SIG = b"\x89PNG\r\n\x1a\n"


def zip_problems(path, kind, name):
    try:
        with zipfile.ZipFile(path) as zf:
            names = zf.namelist()
    except (zipfile.BadZipFile, OSError) as e:
        return [f"unreadable zip: {kind}/{name}.zip ({e})"]
    out = []
    for n in names:
        if n.startswith(("/", "\\")) or ".." in n.replace("\\", "/").split("/"):
            out.append(f"unsafe path in {kind}/{name}.zip: {n}")
    if kind == "chars" and f"{name}/{name}.def" not in names:
        out.append(f"layout: {kind}/{name}.zip has no {name}/{name}.def")
    if kind == "stages" and not any(n.startswith("stages/") and n.lower().endswith(".def") for n in names):
        out.append(f"layout: {kind}/{name}.zip has no stages/*.def")
    return out


def problems(root):
    out = []
    for kind in ("chars", "stages"):
        zips = {f[:-4] for f in os.listdir(os.path.join(root, kind)) if f.lower().endswith(".zip")}
        pdir = os.path.join(root, "previews", kind)
        pngs = {f[:-4] for f in os.listdir(pdir) if f.endswith(".png")} if os.path.isdir(pdir) else set()
        for name in sorted(zips):
            out.extend(zip_problems(os.path.join(root, kind, name + ".zip"), kind, name))
        for name in sorted(zips - pngs):
            out.append(f"missing preview: previews/{kind}/{name}.png (for {kind}/{name}.zip)")
        for name in sorted(pngs - zips):
            out.append(f"orphan preview: previews/{kind}/{name}.png")
        for name in sorted(zips & pngs):
            with open(os.path.join(pdir, name + ".png"), "rb") as f:
                if f.read(8) != PNG_SIG:
                    out.append(f"invalid PNG: previews/{kind}/{name}.png")
    return out


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    errs = problems(root)
    for e in errs:
        print(e)
    print("previews: %s" % ("FAIL (%d)" % len(errs) if errs else "OK"))
    sys.exit(1 if errs else 0)
