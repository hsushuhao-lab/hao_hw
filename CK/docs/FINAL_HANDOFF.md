# CK Final Handoff — v0.4.1 Corrected Art Build

## Status

**PASS_WITH_NOTES — CORRECTED CANONICAL ART IS ONLINE / GAMEPLAY REMAINS PLAYABLE / PRODUCTION CHARACTER ASSETS STILL PENDING**

This document supersedes the earlier v0.4 handoff that incorrectly treated the legacy SVG character suite as production-final art.

## What was wrong

The previous build had an art-governance mismatch:

- the approved five concept sheets existed conceptually,
- but runtime still loaded older `assets/art/*.jpg` and SVG placeholders,
- documentation described the SVG animation suite too strongly,
- the online game therefore did not visually match the approved Craving Kitchen art direction.

## What v0.4.1 corrected

The canonical art is now published at:

```text
assets/art_direction/source_of_truth/
  doctor_concepts.webp
  clinic_layout.webp
  cooking_mode.webp
  props_station.webp
  patient_npcs.webp
```

`src/art-direction.js` and `art-direction.css` now bind the visible game shell to those approved WebP sheets:

- Hero → approved Cooking Mode.
- Clinic / Cooking stage → approved environment sheets.
- Doctor selection / presence / visible stage layer → approved doctor sheet.
- Patient card / visible stage layer → approved patient sheet.
- Art Gallery → approved five sheets.

Legacy SVGs are retained only to preserve compatibility with the existing state machine and as fallback assets.

## Frozen gameplay baseline

`doctor select → patient enter → order → clinic transforms → prep/cut → four heat judgements → final toss → serve → patient eat → result → patient leave → next patient`

Failure remains `CRAVING >= 100%`.

No second recipe is authorized for this milestone.

## Art rules

1. **Same Clinic, Different Flavors.**
2. The room remains recognizably the same outpatient clinic.
3. Approved five WebP sheets have higher authority than every old JPEG/SVG.
4. Legacy SVGs cannot be called production-final art.
5. UI text should remain real HTML/CSS text rather than generated text baked into final assets.

## What is still not production-final

- Transparent full-body doctor sprites derived from the approved character identity.
- Production patient body sprites derived from the approved NPC sheet.
- Individually cut transparent ingredients/props from the approved prop sheet.
- Final animation pass using those production assets.

The current approved-sheet sprite cropping is an intentional bridge so the visible game no longer uses the wrong art direction.

## QA commands

From `CK/`:

```bash
python tests/smoke_test.py
node --check src/data.js
node --check src/game.js
node --check src/art-direction.js
python -m http.server 8000
```

## Links

- Play: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html
- Approved art: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html
- GitHub: https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK

## Next milestone

**v0.5 Production Asset Extraction & Animation Pass**

Priority order:

1. one doctor production vertical slice,
2. remaining two doctors,
3. six patient bodies,
4. ingredient/prop cutouts,
5. animation/VFX polish,
6. only then consider content expansion.
