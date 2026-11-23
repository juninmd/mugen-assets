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
- `umf/` - UMF 2 fighters: `<Nome>.zip`; the `<Nome>/` source folder is optional (legacy packs keep it)
- `previews/<chars|stages|umf>/` - one PNG per zip, same name
- `tools/` - packer, preview generator, `.sff` reader, checker and tests
- `.github/workflows/` - previews (PR and push), SAST (semgrep), gitleaks

## Conventions

- Every `chars/`, `stages/` or `umf/` zip needs a matching preview in `previews/`. `check_previews.py` fails the PR otherwise.
- Zip layout must not contain absolute paths or `..` entries.
- `pack_umf.py` uses fixed timestamps for reproducible zips; keep it that way.
- Credit: each pack's author is listed in `README.md`; keep that table when adding content.
- Zip only: upload each character as one whole `.zip`. Do not also commit an extracted folder duplicating the zip's content; the zip keeps the repo organized and grouped. Existing folders are not deleted without an explicit request.
- `check_previews.py` compares a `umf/<Nome>.zip` with `umf/<Nome>/` only when that folder exists; zip-only UMF packs are valid.

## Regras (pt-BR)

- Só o zip: suba cada personagem como um único `.zip` completo. Não commite também a pasta extraída duplicando o conteúdo do zip; o zip deixa o repositório mais organizado e agrupado. Pastas já existentes não são apagadas sem pedido explícito.
- O `check_previews.py` só compara `umf/<Nome>.zip` com `umf/<Nome>/` quando a pasta existe; pacotes UMF só com zip são válidos.

## Gotchas

- If `umf/<Nome>/` exists, `umf/<Nome>.zip` is generated from it: edit the folder, then run `pack_umf.py`; do not edit the zip by hand.
- Do not commit `__pycache__/` (already in `.gitignore`).
- Repo is about 1 GB of binary assets. Use shallow or sparse clones.
