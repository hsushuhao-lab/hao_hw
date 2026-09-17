# MASTER AGENT PROMPT — Craving Kitchen v0.4 Art Alignment

You are taking over **Craving Kitchen (CK)** from an already playable build. Work directly from the repository and preserve existing behavior.

## REPOSITORY

- Repository: `hsushuhao-lab/hao_hw`
- Branch: `ck-game`
- Project root: `CK/`
- Play build: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved concept art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`

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

Advance CK from the current playable build to a **production-quality art-aligned slice** without breaking the established gameplay loop.

The established loop is:

`doctor select → patient enter → order → clinic transforms → prep/cut → four heat judgements → final toss → serve → patient eat → result → patient leave → next patient`

Failure remains `CRAVING >= 100%`.

## APPROVED VISUAL SOURCE OF TRUTH

These five files override every older SVG concept sheet and every older interpretation of the art direction:

```text
CK/assets/art_direction/source_of_truth/
  doctor_concepts.jpg
  clinic_layout.jpg
  cooking_mode.jpg
  props_station.jpg
  patient_npcs.jpg
```

Treat them as the highest-priority visual authority for characters, environment, props, UI language, palette, mood, framing and presentation.

Legacy files under `assets/concept/`, `assets/characters/`, and `assets/portraits/` are **placeholder/fallback gameplay assets only** unless explicitly promoted later. Do not mistake them for production-final art.

The central visual rule is non-negotiable:

> **Same Clinic, Different Flavors.** The cooking area is the SAME consultation room transformed into a compact mapo-tofu station.

Do not replace it with a restaurant, commercial kitchen, fantasy kitchen, cafe, or unrelated location.

## VISUAL STYLE

Target style:

- stylized 2.5D arcade illustration
- warm, bright, clean, semi-realistic
- polished indie cooking-management game
- clinic white / cream / sky blue base
- navy typography and anchors
- warm yellow sticky-note accents
- chili red / flame orange cooking emphasis
- scallion green positive/focus emphasis
- rounded cards, recipe prescriptions, order tickets, handwritten-note motifs

All production UI copy must use real HTML/CSS text. Never bake AI-generated pseudo-text or misspelled text into final UI assets.

## DOCTOR PRODUCTION TASKS

### DR. SPEED
Visual identity: friendly, energetic, bowl/chopsticks, quick-prep motion.
Required states: entrance, idle, prep, cut, cook, serve, ultimate, fail, victory.
Ultimate: **閃電備料**.

### DR. HEAT
Visual identity: calm, precise, blue shirt, wok/spice/flame focus.
Required states: entrance, idle, prep, cut, cook, serve, ultimate, fail, victory.
Ultimate: **精準火候**.

### DR. STRATEGY
Visual identity: analytical, round glasses, pale-green mask element, clipboard / recipe prescription.
Required states: entrance, idle, prep, cut, cook, serve, ultimate, fail, victory.
Ultimate: **Craving 處方**.

The three entrances and ultimates MUST be visually different. Color swaps alone do not pass.

## PATIENT PRODUCTION TASKS

Use the approved NPC sheet for these six archetypes:

1. The Anxious Office Worker
2. The Tired Student
3. The Chain-Smoking Driver
4. The Cheerful Auntie
5. The Quiet Young Adult
6. The Repeat Visitor

Each must be recognizable by silhouette/clothing, not face alone.
Required states: walk in, sit, order/react, eat, leave.

Avoid repeated glamorized smoking imagery. Convey craving primarily through restlessness, fidgeting, pocket-checking, expression, pacing and the CRAVING meter.

## ENVIRONMENT TASKS

The room must remain visibly clinical. Preserve:

- doctor desk
- patient seat
- printer/storage
- wash area
- cabinets
- clinic lighting
- white walls
- doorway

Cooking Mode converts existing objects:

- monitor → order screen
- printer → order ticket printer
- drawers → spice cabinet
- desk → prep/plating counter
- wash area → ingredient wash station
- open floor → portable wok station

Target visual balance: roughly 70% clinic identity, 30% cooking intervention.

## PROP TASKS

Use `props_station.jpg` as the source for tofu, minced pork, doubanjiang, fermented black beans, garlic, scallion, chili, Sichuan pepper, rice, wok, ladle, spatula, knife, chopping board, portable stove, order slips and recipe prescription.

Create production interaction assets with consistent 3/4 perspective, transparent background, unified lighting and immediate recognizability.

## ENGINEERING RULES

- Preserve existing gameplay state flow.
- Make the smallest targeted changes required.
- Do not refactor adjacent code unless necessary for the milestone.
- Do not add a second recipe.
- Do not introduce a framework/build system unless static hosting is demonstrably blocked.
- Preserve relative-path static hosting compatibility.
- Keep fallbacks until production replacements are verified online.

## MANDATORY REGRESSION GATES

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

Manual QA at:
- 390×844
- 768×1024
- 1440×900

Required end-to-end checks:
1. approved hero/background art loads;
2. clinic stage uses approved clinic layout;
3. cooking transition uses approved cooking mode art;
4. all three doctors remain selectable;
5. passive + Ultimate mechanics still work;
6. all six patients can appear;
7. prep/cut works;
8. four heat steps work;
9. toss works;
10. CRAVING 100% still fails;
11. successful order reaches score/result;
12. next patient starts without reload;
13. mute/audio controls remain functional;
14. online build has no 404 asset paths.

## COMMIT DISCIPLINE

Use small commits by concern, e.g.:
- `art: add approved doctor production sprites`
- `art: split approved ingredient assets`
- `feat: integrate doctor state art`
- `feat: integrate patient lifecycle art`
- `style: align ui with approved art bible`
- `test: harden art-alignment regression gates`
- `docs: finalize production art handoff`

Do not merge to `main` unless explicitly instructed by the PI.

## STOP CONDITION

Do not declare the production art pass complete while the visible gameplay still reads primarily as placeholder SVG art. If a production asset is missing, keep the fallback and report it explicitly.

## FINAL REPORT FORMAT

Return:
- milestone status (`PASS`, `PASS_WITH_NOTES`, or `BLOCKED`),
- exact commit SHA,
- files changed,
- automated test results,
- manual viewport QA results,
- live play URL,
- live approved-art URL,
- remaining placeholder assets,
- remaining blockers,
- next recommended milestone.
