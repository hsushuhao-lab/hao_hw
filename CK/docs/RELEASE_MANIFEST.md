# CK v0.4.2 Art Closeout Manifest

## Canonical repository

- Repo: `hsushuhao-lab/hao_hw`
- Branch: `ck-game`
- Root: `CK/`
- Milestone: `v0.4.2 Art Closeout`

## Canonical visual assets

```text
assets/art_direction/source_of_truth/
  doctor_concepts.avif
  clinic_layout.avif
  cooking_mode.avif
  props_station.avif
  patient_npcs.avif
```

These five AVIF files are the only production visual source of truth.

## Runtime files

- `index.html` — playable game shell.
- `styles.css` — base layout/game styles.
- `art-direction.css` — canonical approved-art presentation layer.
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
- deprecated older JPG/WebP source-of-truth copies

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

`tests/smoke_test.py` checks:

- existence of all five canonical AVIF assets;
- non-zero/non-truncated conservative file-size gate;
- canonical runtime/gallery/document references;
- absence of active old `assets/art/*.jpg` runtime mappings;
- preserved doctor/patient legacy fallbacks;
- DOM/gameplay tokens;
- JavaScript syntax when Node is available.

## Frozen gameplay baseline

`doctor select → patient enter → order → clinic transforms → prep/cut → four heat judgements → final toss → serve → patient eat → result → patient leave → next patient`

Failure remains `CRAVING >= 100%`.

## Play / review links

- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`
- Repository: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`

## Deployment note

Native GitHub Pages is not currently enabled for this repository. raw.githack remains the current direct-play surface.

## Public data policy

The public release contains derived game artwork and code only. Original private source photographs are not runtime dependencies.
