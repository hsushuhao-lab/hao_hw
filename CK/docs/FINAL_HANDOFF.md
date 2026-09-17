# CK Final Handoff — v0.3 Production Slice

## Status

**HANDOFF READY / PLAYABLE / CORE LOOP LOCKED**

The current build is a static web game with no build system and no external runtime dependencies. The core loop is working and should now be treated as the regression baseline.

## Completed

- 3 selectable doctors with different passive mechanics.
- 3 distinct Ultimates.
- 6 patient archetypes and order variants.
- Clinic → Cooking Mode visual transition.
- Ingredient selection.
- Tofu/scallion timing prep.
- Four wok-heat timing steps.
- Final toss timing mini-game.
- CRAVING / FOCUS meters.
- Scoring, streak, win/fail, next-patient loop.
- Patient enter/eat/leave presentation.
- Web Audio feedback + mute.
- Desktop/mobile responsive shell.
- Online lightweight concept art and portrait assets.
- Online art gallery, online build, GDD, Art Bible, asset index, flow doc, deployment notes, tests, and master AGENT prompt.

## Freeze rules

The next agent must NOT:
- add a second recipe,
- add multiplayer,
- build a large hospital map,
- rewrite the current state model for style reasons,
- delete SVG/CSS fallbacks before replacement assets pass QA,
- turn the room into a generic restaurant.

## Next milestone: v0.4 Character Animation & Deployment QA

Priority order:
1. full-body doctor sprite sheets;
2. unique entrance + idle/prep/cook/serve/ultimate states for each doctor;
3. patient walk/sit/order/eat/leave body animation;
4. integrate production SFX/BGM while keeping Web Audio fallback;
5. QA at 390×844, 768×1024, 1440×900;
6. verify direct public deployment.

## Success criteria

A v0.4 release is accepted only if:
- the current v0.3 smoke test still passes or is updated with equivalent coverage;
- each doctor is distinguishable by motion, not only color/name;
- each of six patients can complete enter → sit → eat → leave;
- no broken image paths on online deployment;
- the whole order loop can be completed on phone and desktop;
- CRAVING failure path still works;
- playable build needs no local asset path and no private source photo.

## QA commands

From `CK/`:

```bash
python tests/smoke_test.py
python -m http.server 8000
```

For syntax checks when Node is available:

```bash
node --check src/data.js
node --check src/game.js
```

## Links

- Play: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html
- Art: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art.html
- GitHub: https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK