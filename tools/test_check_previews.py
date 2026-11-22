import os
import tempfile
import unittest
import zipfile

import check_previews

PNG = b"\x89PNG\r\n\x1a\n"


def make(root, kind, name, members):
    os.makedirs(os.path.join(root, kind), exist_ok=True)
    os.makedirs(os.path.join(root, "previews", kind), exist_ok=True)
    with zipfile.ZipFile(os.path.join(root, kind, name + ".zip"), "w") as zf:
        for m in members:
            zf.writestr(m, "x")
    with open(os.path.join(root, "previews", kind, name + ".png"), "wb") as f:
        f.write(PNG)


class CheckZips(unittest.TestCase):
    def run_check(self, kind, name, members):
        with tempfile.TemporaryDirectory() as root:
            for k in ("chars", "stages"):
                os.makedirs(os.path.join(root, k), exist_ok=True)
            make(root, kind, name, members)
            return check_previews.problems(root)

    def test_valid_char_and_stage(self):
        self.assertEqual(self.run_check("chars", "Ken", ["Ken/Ken.def"]), [])
        self.assertEqual(self.run_check("stages", "Dojo", ["stages/Dojo.def", "stages/Dojo.sff"]), [])

    def test_char_without_def(self):
        self.assertTrue(any("no Ken/Ken.def" in p for p in self.run_check("chars", "Ken", ["Ken/readme.txt"])))

    def test_stage_without_def(self):
        self.assertTrue(any("no stages/*.def" in p for p in self.run_check("stages", "Dojo", ["sound/a.mp3"])))

    def test_unsafe_path(self):
        probs = self.run_check("chars", "Ken", ["Ken/Ken.def", "../evil.txt"])
        self.assertTrue(any("unsafe path" in p for p in probs))

    def test_corrupt_zip(self):
        with tempfile.TemporaryDirectory() as root:
            make(root, "chars", "Ken", ["Ken/Ken.def"])
            os.makedirs(os.path.join(root, "stages"))
            with open(os.path.join(root, "chars", "Ken.zip"), "wb") as f:
                f.write(b"not a zip")
            self.assertTrue(any("unreadable zip" in p for p in check_previews.problems(root)))


class CheckUmf(unittest.TestCase):
    def build(self, root, zip_members, folder_files):
        os.makedirs(os.path.join(root, "umf", "Hero"), exist_ok=True)
        for rel, data in folder_files.items():
            full = os.path.join(root, "umf", "Hero", rel)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "wb") as f:
                f.write(data)
        with zipfile.ZipFile(os.path.join(root, "umf", "Hero.zip"), "w") as zf:
            for arc, data in zip_members.items():
                zf.writestr(arc, data)
        os.makedirs(os.path.join(root, "previews", "umf"), exist_ok=True)
        with open(os.path.join(root, "previews", "umf", "Hero.png"), "wb") as f:
            f.write(PNG)
        for k in ("chars", "stages"):
            os.makedirs(os.path.join(root, k), exist_ok=True)
        return check_previews.problems(root)

    def test_exact_umf_pack_has_meta_instead_of_idle(self):
        files = {"hero.json": b'{"format":"umf/2"}', "sprites/meta.json": b"{}"}
        with tempfile.TemporaryDirectory() as root:
            zipped = {"Hero/" + k: v for k, v in files.items()}
            self.assertEqual(self.build(root, zipped, files), [])

    def test_valid_umf_pack(self):
        files = {"hero.json": b'{"format":"umf/2"}', "sprites/01_idle.png": b"png"}
        with tempfile.TemporaryDirectory() as root:
            zipped = {"Hero/" + k: v for k, v in files.items()}
            self.assertEqual(self.build(root, zipped, files), [])

    def test_stale_zip_and_bad_format(self):
        files = {"hero.json": b'{"format":"umf/2"}', "sprites/01_idle.png": b"png"}
        with tempfile.TemporaryDirectory() as root:
            zipped = {"Hero/hero.json": b'{"format":"nope"}', "Hero/sprites/01_idle.png": b"png"}
            probs = self.build(root, zipped, files)
            self.assertTrue(any("not a umf fighter" in p for p in probs))
            self.assertTrue(any("stale zip" in p for p in probs))

    def test_missing_idle_sprite(self):
        files = {"hero.json": b'{"format":"umf/2"}'}
        with tempfile.TemporaryDirectory() as root:
            probs = self.build(root, {"Hero/hero.json": files["hero.json"]}, files)
            self.assertTrue(any("01_idle.png" in p for p in probs))


if __name__ == "__main__":
    unittest.main()
