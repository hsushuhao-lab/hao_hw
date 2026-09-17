# MASTER AGENT PROMPT — Craving Kitchen v0.4

You are taking over **Craving Kitchen (CK)** from an already playable v0.3 Production Slice. Work directly from the repository and preserve existing behavior.

## REPOSITORY

- Repository: `hsushuhao-lab/hao_hw`
- Branch: `ck-game`
- Project root: `CK/`
- Play build: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Art gallery: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art.html`

Read in this order before modifying code:
1. `CK/docs/00_START_HERE.md`
2. `CK/docs/FINAL_HANDOFF.md`
3. `CK/docs/SCENE_AND_GAME_FLOW.md`
4. `CK/docs/ART_BIBLE.md`
5. `CK/docs/ONLINE_ASSET_INDEX.md`
6. `CK/docs/GDD.md`
7. `CK/PROGRESS.md`
8. `CK/src/data.js`
9. `CK/src/game.js`
10. `CK/tests/smoke_test.py`

## GOAL

Advance CK to **v0.4 Character Animation & Deployment QA** without breaking the v0.3 loop. The deliverable is not a redesign. It is a visually finished animation pass over the current game.

The established loop is:

`doctor select → patient enter → order → clinic transforms → prep/cut → four heat judgements → final toss → serve → patient eat → result → patient leave → next patient`

Failure remains `CRAVING >= 100%`.

## VISUAL SOURCE OF TRUTH

Use the online production artwork in:
- `CK/assets/concept/doctor_concepts.svg`
- `CK/assets/concept/clinic_layout.svg`
- `CK/assets/concept/cooking_mode.svg`
- `CK/assets/concept/props.svg`
- `CK/assets/concept/patient_npcs.svg`

The central visual rule is non-negotiable:

> The cooking area is the SAME consultation room transformed into a compact kitchen. Do not replace it with a restaurant, commercial kitchen, or unrelated location.

Do not publish or depend on private real-person source photographs. The public derived game art is sufficient visual reference.

## CHARACTER TASKS

### DR. SPEED
Create full-body game assets for:
- entrance,
- idle,
- prep,
- cut,
- cook,
- serve,
- ultimate.

Motion identity: energetic, fast tray/knife movement, playful snap timing. Ultimate = **閃電備料**.

### DR. HEAT
Same states.
Motion identity: calm, precise, wok-oriented, flame/seasoning flourish. Ultimate = **精準火候**.

### DR. STRATEGY
Same states.
Motion identity: clipboard/order-ticket/prescription gestures, analytical rhythm. Ultimate = **Craving 處方**.

The three entrances and ultimates MUST be visually different. Merely changing colors, speed, or text does not pass.

## PATIENT TASKS

For all six established patients, implement a minimal body animation state set:
- walk in,
- sit,
- order/react,
- eat,
- leave.

Keep existing portrait/CSS behavior as a fallback until body animations are verified online.

## AUDIO

Add production SFX/BGM only after animation integration is stable. Keep the current Web Audio procedural effects as fallback. Add independent master/music/SFX volume only if it can be done without rewriting the game architecture.

## ENGINEERING RULES

- Make the smallest targeted changes required.
- Do not refactor adjacent code just because it can be cleaner.
- Do not remove dead-looking code without proving it is unused and asking the PI if removal is not required.
- Do not introduce a framework or build system unless the current static architecture demonstrably blocks the milestone.
- Preserve GitHub static hosting compatibility.
- Prefer assets and CSS/JS that work from relative paths.
- Every change must have a visible or testable acceptance criterion.

## MANDATORY REGRESSION GATES

After each meaningful implementation batch:

```bash
cd CK
python tests/smoke_test.py
node --check src/data.js
node --check src/game.js
```

Then serve locally:

```bash
python -m http.server 8000
```

Manually verify at:
- 390×844
- 768×1024
- 1440×900

Required end-to-end checks:
1. all images load;
2. all three doctors are selectable;
3. doctor passive + Ultimate still work;
4. all six patients can appear;
5. prep/cut works;
6. four heat steps work;
7. toss works;
8. CRAVING 100% still fails;
9. successful order reaches score/result;
10. next patient starts without reload;
11. mute/audio controls remain functional;
12. online build has no 404 asset paths.

## COMMIT DISCIPLINE

Use small commits by concern, e.g.:
- `art: add doctor animation sprites`
- `feat: integrate doctor animation states`
- `art: add patient body sprites`
- `feat: animate patient visit lifecycle`
- `audio: add production sfx with fallback`
- `test: harden v0.4 regression gates`
- `docs: finalize v0.4 release handoff`

Do not merge to `main` unless explicitly instructed by the PI.

## STOP CONDITION

Do not declare v0.4 complete until all acceptance criteria in `FINAL_HANDOFF.md` pass. If any animation asset is missing, keep the current fallback and report the missing item explicitly rather than silently substituting a generic asset.

## FINAL REPORT FORMAT

Return:
- milestone status (`PASS`, `PASS_WITH_NOTES`, or `BLOCKED`),
- exact commit SHA,
- files changed,
- automated test results,
- manual viewport QA results,
- live play URL,
- live art URL,
- remaining blockers,
- next recommended milestone.