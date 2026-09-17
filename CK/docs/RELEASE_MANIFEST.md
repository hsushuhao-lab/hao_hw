# CK v0.4 Online Handoff Manifest

## Canonical repository

- Repo: `hsushuhao-lab/hao_hw`
- Branch: `ck-game`
- Root: `CK/`
- Milestone: `v0.4 Character Animation & Deployment QA`

## Online deliverables

- `index.html` — playable game with full-body doctor and patient stage layers and audio mixer
- `art.html` — browsable art gallery with 21 doctor states and 30 patient states
- `assets/concept/*.svg` — five primary lightweight concept sheets
- `assets/portraits/*.svg` — three doctors + six patients (portrait badge fallbacks)
- `assets/characters/doctors/*.svg` — 21 full-body doctor animation state assets (entrance, idle, prep, cut, cook, serve, ultimate)
- `assets/characters/patients/*.svg` — 30 full-body patient lifecycle animation state assets (walk_in, sit, order, eat, leave)
- `src/data.js`, `src/game.js`, `styles.css` — v0.4 code with full-body animation state machine, procedural layered SFX, BGM, and volume controls
- `PROGRESS.md` — milestone progression log
- `docs/00_START_HERE.md` — handoff index
- `docs/FINAL_HANDOFF.md` — v0.4 completion record and next milestone
- `docs/MASTER_AGENT_PROMPT.md` — master agent execution prompt
- `docs/SCENE_AND_GAME_FLOW.md` — state and scene flow
- `docs/ONLINE_ASSET_INDEX.md` — public asset map
- `docs/ART_BIBLE.md`, `docs/GDD.md`, `docs/ASSET_MANIFEST.md`, `docs/DEPLOYMENT.md`
- `tests/smoke_test.py` — regression test suite asserting 69 files, syntax, and DOM tokens

## Play / review links

- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art.html`
- Repository: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`

## Offline package & public data policy

GitHub copy intentionally uses lightweight SVG derivatives for stable direct web access and zero external runtime dependencies.
Only derived game artwork is public. The original source photographs showing real people are excluded from the public repository.