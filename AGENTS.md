# AGENTS.md

MUGEN characters and stages packed as `.zip` files for [ultimate-mugen](https://github.com/juninmd/ultimate-mugen). Content only, no application code.

## Stack

- Python 3.12 tools (`tools/`), Pillow and NumPy for previews
- Assets: `chars/*.zip`, `stages/*.zip`, `umf/*.zip` (binary, see `.gitattributes`)

## Commands

```bash
pip install pillow numpy                                  # preview deps
python tools/preview.py chars/NovoChar.zip stages/NovoStage.zip   # generate previews
python tools/pack_umf.py <Nome>                           # rebuild umf/<Nome>.zip from umf/<Nome>/
python tools/check_previews.py                            # CI gate: preview per zip, zip layout
python -m unittest discover -s tools -p "test_*.py"       # CI: tests for the checker and preview
```

## Structure

- `chars/` - character zips, each containing `<Nome>/<Nome>.def`
- `stages/` - stage zips with paths relative to the MUGEN root (`stages/`, `sound/`)
- `umf/` - UMF 2 fighters: `<Nome>/` folder (source) and generated `<Nome>.zip`
- `previews/<chars|stages|umf>/` - one PNG per zip, same name
- `tools/` - packer, preview generator, `.sff` reader, checker and tests
- `.github/workflows/` - previews (PR and push), SAST (semgrep), gitleaks

## Conventions

- Every `chars/`, `stages/` or `umf/` zip needs a matching preview in `previews/`. `check_previews.py` fails the PR otherwise.
- Zip layout must not contain absolute paths or `..` entries.
- `pack_umf.py` uses fixed timestamps for reproducible zips; keep it that way.
- Credit: each pack's author is listed in `README.md`; keep that table when adding content.

## Gotchas

- `umf/<Nome>.zip` is generated. Edit the folder, then run `pack_umf.py`; do not edit the zip by hand.
- Do not commit `__pycache__/` (already in `.gitignore`).
- Repo is about 1 GB of binary assets. Use shallow or sparse clones.
