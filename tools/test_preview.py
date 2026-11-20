import io
import unittest
import zipfile

import preview


def pack_with(members):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for name, text in members.items():
            zf.writestr(name, text)
    return preview.Pack(buf)


class MissingSprite(unittest.TestCase):
    def test_char_without_sprite_file_names_the_file(self):
        pack = pack_with({"Foo/Foo.def": "[Files]\nsprite = Foo.sff\n"})
        with self.assertRaisesRegex(ValueError, "missing sprite file: Foo/Foo.sff"):
            preview.char_card(pack, "Foo.zip")

    def test_stage_without_sprite_file_names_the_file(self):
        pack = pack_with({"stages/Bar.def": "[BGdef]\nspr = bar.sff\n"})
        with self.assertRaisesRegex(ValueError, "missing stage sprite file: bar.sff"):
            preview.stage_card(pack, "Bar.zip")


if __name__ == "__main__":
    unittest.main()
