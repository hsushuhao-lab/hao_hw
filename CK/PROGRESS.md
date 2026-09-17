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

## Milestone v0.4 — CHARACTER ANIMATION & DEPLOYMENT QA

Status: **COMPLETE / SMOKE TEST PASS / ONLINE DEPLOYMENT READY**

Implemented:
- 21 full-body SVG character animation state assets across 3 doctors (DR. SPEED, DR. HEAT, DR. STRATEGY) covering 7 distinct states: entrance, idle, prep, cut, cook, serve, ultimate.
- Distinct animation identities and signature ultimates: 閃電備料 (lightning & dual knife flurry), 精準火候 (roaring flame inferno & target reticle), Craving 處方 (glowing clinical Rx seal & analytical diagnostic beam).
- 30 full-body SVG lifecycle assets for all 6 patient archetypes (Office Worker, Student, Driver, Auntie, Quiet Youth, Repeat Patron) across 5 visit lifecycle states: walk_in, sit, order, eat, leave.
- Stage visual integration: `#doctorStage` and `#patientStage` dynamic layers in `#clinicStage` with CSS keyframe animations and fallback preservation for original portraits.
- Production Web Audio synthesizer with multi-harmonic acoustic sound design, procedural clinic-kitchen BGM groove loop, and independent volume mixer UI (Master, Music, SFX, BGM toggle).
- Comprehensive test harness hardening: `tests/smoke_test.py` validates 69 asset and code files, DOM structure, CSS animation classes, and syntax checks.
- Art showcase gallery at `CK/art.html` expanded with full interactive galleries for all 21 doctor animation states and 30 patient lifecycle states.
- Documentation updated across `FINAL_HANDOFF.md`, `ONLINE_ASSET_INDEX.md`, `RELEASE_MANIFEST.md`, and `PROGRESS.md`.

## Current regression baseline

`doctor select → patient enter → order → clinic transforms → prep/cut → four heat judgements → final toss → serve → patient eat → result → patient leave → next patient`

Failure remains `CRAVING >= 100%`.

## Online URLs

- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Art gallery: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art.html`
- Repository: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`
- Intended GitHub Pages: `https://hsushuhao-lab.github.io/hao_hw/CK/`

## Milestone v0.5 — NEXT (Order Complexity & Difficulty Curve)

1. Multi-step order modifications / clinical customizations (spice tolerance, texture preference, allergy contraindications).
2. Dynamic craving curve and patient patience timers based on archetype.
3. Expanded combo scoring and clinical diagnosis precision metrics.
4. Second recipe research & prototyping (only after v0.4 is formally locked).