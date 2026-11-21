"""Build umf/<Name>.zip from the umf/<Name>/ folder (stable order and timestamps)."""
import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAMP = (2026, 1, 1, 0, 0, 0)


def members(folder):
    out = []
    for base, _, files in os.walk(folder):
        for f in files:
            full = os.path.join(base, f)
            out.append((os.path.relpath(full, os.path.dirname(folder)).replace(os.sep, "/"), full))
    return sorted(out)


def build(name, root=ROOT):
    folder = os.path.join(root, "umf", name)
    target = os.path.join(root, "umf", name + ".zip")
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for arc, full in members(folder):
            info = zipfile.ZipInfo(arc, STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            with open(full, "rb") as fh:
                zf.writestr(info, fh.read())
    return target


if __name__ == "__main__":
    for n in sys.argv[1:]:
        print(build(n))
