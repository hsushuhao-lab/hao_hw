# MASTER AGENT PROMPT — Craving Kitchen v0.5 Production Asset Pass

You are taking over **Craving Kitchen (CK)** from the corrected v0.4.1 art build. Work directly from the repository and preserve existing gameplay behavior.

## REPOSITORY

- Repository: `hsushuhao-lab/hao_hw`
- Branch: `ck-game`
- Project root: `CK/`
- Play build: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`

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
10. `CK/src/art-direction.js`
11. `CK/tests/smoke_test.py`

## GOAL

Advance CK from the corrected art bridge to a **production-quality character/prop asset slice** without breaking the established loop.

The loop is frozen:

`doctor select → patient enter → order → clinic transforms → prep/cut → four heat judgements → final toss → serve → patient eat → result → patient leave → next patient`

Failure remains `CRAVING >= 100%`.

Do not add a second recipe.

## ONLY APPROVED VISUAL SOURCE OF TRUTH

These five WebP files override every older JPEG, SVG concept sheet, portrait, animation asset, or interpretation:

```text
CK/assets/art_direction/source_of_truth/
  doctor_concepts.webp
  clinic_layout.webp
  cooking_mode.webp
  props_station.webp
  patient_npcs.webp
```

Treat them as the highest-priority authority for:

- character identity
- patient identity
- environment
- props
- UI language
- palette
- mood
- framing
- presentation

Legacy files under `assets/concept/`, `assets/characters/`, `assets/portraits/`, and `assets/art/*.jpg` are **fallback / deprecated assets only**.

Do not call those legacy assets production-final.

## VISUAL RULE

> **Same Clinic, Different Flavors.**

The cooking area is the same consultation room transformed into a compact mapo-tofu station.

Do not replace it with a restaurant, commercial kitchen, fantasy kitchen, cafe, or unrelated location.

Target environment balance: roughly **70% clinic identity / 30% cooking intervention**.

## CURRENT RUNTIME BRIDGE

The current online build intentionally crops visible doctor/patient imagery from the canonical concept sheets through:

- `CK/src/art-direction.js`
- `CK/art-direction.css`

This bridge fixed the previous wrong-art problem. Preserve it until a production replacement is verified online.

Never remove a working fallback before its replacement passes QA.

## PRODUCTION TASK ORDER

### P0 — DR. SPEED vertical slice

Create production art derived from the approved doctor sheet for:

- entrance
- idle
- prep
- cut
- cook
- serve
- ultimate
- fail
- victory

Requirements:

- same face identity across every pose
- same transparent/light glasses
- same hairstyle
- same white coat and inner clothing identity
- recognizable bowl/chopsticks / fast-prep motif
- transparent background
- consistent canvas and scale
- no baked pseudo-text

Integrate only after visual review.

### P1 — DR. HEAT / DR. STRATEGY

Repeat after DR. SPEED style is locked.

DR. HEAT identity:

- blue shirt
- centered / precise
- wok / spice / flame focus

DR. STRATEGY identity:

- round glasses
- pale-green mask element
- clipboard / recipe prescription focus

The three entrances and ultimates must be visually different. Color swaps alone do not pass.

### P2 — six patient production sets

Use the approved patient sheet:

1. The Anxious Office Worker
2. The Tired Student
3. The Chain-Smoking Driver
4. The Cheerful Auntie
5. The Quiet Young Adult
6. The Repeat Visitor

Each requires:

- walk in
- sit
- order/react
- eat
- leave

Characters must remain recognizable by silhouette/clothing, not face alone.

Avoid repeated glamorized smoking imagery; convey craving primarily via fidgeting, restlessness, pacing, expression, and CRAVING UI.

### P3 — ingredient / prop extraction

Use `props_station.webp` as authority.

Create transparent production interaction assets for:

- tofu
- minced pork
- doubanjiang
- fermented black beans
- garlic
- scallion
- chili
- Sichuan pepper
- rice
- wok
- ladle
- spatula
- knife
- chopping board
- portable stove
- order slips
- recipe prescription

Use consistent 3/4 perspective and unified lighting.

## ENGINEERING RULES

- Preserve existing gameplay state flow.
- Make the smallest targeted changes required.
- Do not refactor adjacent code unless required for this milestone.
- Do not add a framework/build system unless static hosting is demonstrably blocked.
- Preserve relative-path static hosting compatibility.
- Do not reintroduce old art paths into visible runtime.
- Do not use generated text baked into final UI assets.

## REQUIRED REGRESSION GATES

After each meaningful batch:

```bash
cd CK
python tests/smoke_test.py
node --check src/data.js
node --check src/game.js
node --check src/art-direction.js
```

Then serve locally:

```bash
python -m http.server 8000
```

Manual QA:

- 390×844
- 768×1024
- 1440×900

Required checks:

1. all five canonical WebP assets load;
2. hero uses approved Cooking Mode art;
3. clinic stage resolves to approved Clinic Layout;
4. cooking stage resolves to approved Cooking Mode;
5. all three doctors remain selectable;
6. all six patients can appear;
7. passive + Ultimate mechanics still work;
8. prep/cut works;
9. four heat steps work;
10. toss works;
11. CRAVING 100% still fails;
12. successful order reaches result;
13. next patient starts without reload;
14. audio controls remain functional;
15. online build has no 404s;
16. no visible component silently falls back to the old wrong art direction.

## COMMIT DISCIPLINE

Use small commits by concern, for example:

- `art: add DR SPEED production state set`
- `feat: integrate approved DR SPEED sprites`
- `art: add remaining approved doctor sprites`
- `art: add approved patient lifecycle assets`
- `art: extract approved mapo tofu props`
- `test: harden canonical art regression gates`
- `docs: finalize v0.5 production asset handoff`

Do not merge to `main` unless explicitly instructed by the PI.

## STOP CONDITION

Do not declare v0.5 complete while visible gameplay still depends primarily on concept-sheet cropping or legacy SVGs.

If a production asset is missing, keep the corrected v0.4.1 bridge and report the missing item explicitly.

## FINAL REPORT FORMAT

Return:

- milestone status (`PASS`, `PASS_WITH_NOTES`, or `BLOCKED`)
- exact commit SHA
- files changed
- canonical art files verified
- automated test results
- manual viewport QA results
- live play URL
- live approved-art URL
- remaining concept-sheet bridge elements
- remaining legacy fallback assets
- blockers
- next recommended milestone
