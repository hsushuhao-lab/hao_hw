# Craving Kitchen — Development Progress

## Milestone v0.3 — PRODUCTION SLICE

Status: **COMPLETE / SMOKE TEST PASS / ONLINE HANDOFF READY**

Implemented:
- v0.2 full gameplay loop retained.
- Lightweight SVG doctor/patient portraits and concept scenes available in the GitHub web build.
- Doctor presence overlay and arrival animation.
- One-use-per-order character Ultimate skills.
- Dedicated final wok-toss timing mini-game.
- Patient eat animation before leaving and result screen.
- Keyboard controls: Space for timing actions, U for Ultimate.
- Direct-play URL documented in GitHub README.
- Online art / environment / character gallery at `CK/art.html`.
- Complete online handoff chain: `00_START_HERE` → `FINAL_HANDOFF` → `MASTER_AGENT_PROMPT` → `SCENE_AND_GAME_FLOW` → `ONLINE_ASSET_INDEX`.
- Release manifest and deployment guide online.
- Original real-person source photos excluded from the public repository; only derived game assets are public.

## Current regression baseline

`doctor select → patient enter → order → clinic transforms → prep/cut → four heat judgements → final toss → serve → patient eat → result → patient leave → next patient`

Failure remains `CRAVING >= 100%`.

## Online URLs

- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Art gallery: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art.html`
- Repository: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`
- Intended GitHub Pages: `https://hsushuhao-lab.github.io/hao_hw/CK/`

## v0.4 — NEXT

1. Transparent production full-body doctor sprites and expression sheets.
2. Character-specific entrance / idle / prep / cook / serve / ultimate animation sequences.
3. Full patient walk / sit / order / eat / leave body animation.
4. Production audio/BGM and volume mixer while retaining Web Audio fallback.
5. GitHub Pages enablement + mobile/tablet/desktop QA.

## v0.4 acceptance emphasis

- Three doctors must be distinguishable by motion, not only by color/name.
- All six patients must visibly complete enter → sit → order → eat → leave.
- No broken online asset paths.
- Existing gameplay mechanics must remain functional.
- Do not add a second recipe until the first recipe has production-quality character animation and deployment QA.

See `docs/MASTER_AGENT_PROMPT.md` for the exact next-agent execution prompt.