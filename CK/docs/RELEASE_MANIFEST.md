# CK v0.4.1 Corrected Art Manifest

## Canonical repository

- Repo: `hsushuhao-lab/hao_hw`
- Branch: `ck-game`
- Root: `CK/`
- Milestone: `v0.4.1 Corrected Art Build`

## Canonical visual assets

```text
assets/art_direction/source_of_truth/
  doctor_concepts.webp
  clinic_layout.webp
  cooking_mode.webp
  props_station.webp
  patient_npcs.webp
```

These five WebP files are the current production visual source of truth.

## Runtime files

- `index.html` — playable game shell.
- `styles.css` — base layout/game styles.
- `art-direction.css` — corrected approved-art presentation layer.
- `src/data.js` — doctors, patients, ingredients, cook steps.
- `src/game.js` — core gameplay state machine.
- `src/art-direction.js` — canonical-art runtime bridge.
- `art-original.html` — online canonical art review page.

## Legacy fallback assets

The following remain for compatibility but are not production-final art:

- `assets/concept/*.svg`
- `assets/portraits/*.svg`
- `assets/characters/doctors/*.svg`
- `assets/characters/patients/*.svg`
- deprecated `assets/art/*.jpg`
- deprecated older `assets/art_direction/source_of_truth/*.jpg`

## Documentation

- `README.md`
- `PROGRESS.md`
- `docs/00_START_HERE.md`
- `docs/FINAL_HANDOFF.md`
- `docs/MASTER_AGENT_PROMPT.md`
- `docs/SCENE_AND_GAME_FLOW.md`
- `docs/ONLINE_ASSET_INDEX.md`
- `docs/ART_BIBLE.md`
- `docs/GDD.md`
- `docs/ASSET_MANIFEST.md`
- `docs/DEPLOYMENT.md`

## Regression test

`tests/smoke_test.py` now checks:

- existence of the five canonical WebP assets,
- substantial file size for canonical art,
- approved-art runtime references,
- absence of the old wrong `assets/art/*.jpg` runtime mappings,
- preserved doctor/patient legacy fallbacks,
- DOM/gameplay tokens,
- JavaScript syntax when Node is available.

## Play / review links

- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`
- Repository: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`

## Deployment note

The repository currently reports `has_pages=false`; native GitHub Pages is not enabled. raw.githack remains the current direct-play surface.

## Public data policy

Only derived game artwork is public. Original source photographs showing real people remain outside the public repository.
