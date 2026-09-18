# CK Final Handoff — v0.4.2 Art Closeout

## Status

**PASS_WITH_NOTES — CANONICAL ART ONLINE / RUNTIME BOUND / GAMEPLAY PLAYABLE / PURPOSE-BUILT PRODUCTION SPRITES STILL PENDING**

This handoff supersedes all earlier documents that treated legacy SVG assets as production-final art or referenced obsolete JPEG/WebP source-of-truth paths.

## What was corrected

The project previously had an art-governance mismatch: approved concept art existed, but runtime and documentation still allowed older `assets/art/*.jpg` and SVG placeholders to dominate the visible game.

v0.4.2 closes that mismatch by using one canonical visual authority everywhere.

## Canonical visual source of truth

```text
assets/art_direction/source_of_truth/
  doctor_concepts.avif
  clinic_layout.avif
  cooking_mode.avif
  props_station.avif
  patient_npcs.avif
```

`src/art-direction.js`, `art-direction.css`, `art-original.html`, README, Art Bible, Online Asset Index and the regression test all resolve to the same AVIF authority.

Visible mapping:

- Hero → approved Cooking Mode.
- Clinic stage → approved Clinic Layout.
- Cooking stage → approved Cooking Mode.
- Doctor selection / presence / visible stage → approved doctor sheet bridge.
- Patient card / visible stage → approved patient sheet bridge.
- Art gallery → five canonical sheets.

## Frozen gameplay baseline

`doctor select → patient enter → order → clinic transforms → prep/cut → four heat judgements → final toss → serve → patient eat → result → patient leave → next patient`

Failure remains `CRAVING >= 100%`.

No second recipe is authorized during this closeout.

## Art rules

1. **Same Clinic, Different Flavors.**
2. Cooking Mode must still read as the same outpatient clinic.
3. The five canonical AVIF sheets outrank every older JPEG/WebP/SVG interpretation.
4. `assets/art/`, `assets/concept/`, `assets/characters/`, and `assets/portraits/` are fallback/deprecated visual sources only.
5. UI copy remains real HTML/CSS text; baked generated pseudo-text is not final UI.
6. New character and prop assets must be visually traceable to the canonical sheets.

## Known limitations carried to v0.5

- Transparent full-body doctor production sprites are not yet complete.
- Production patient body sets are not yet complete.
- Individual transparent ingredient / prop cutouts are not yet extracted.
- Current visible doctor/patient presentation uses concept-sheet bridging while legacy state assets remain for compatibility.

These are declared limitations, not hidden regressions.

## Regression gate

From `CK/`:

```bash
python tests/smoke_test.py
node --check src/data.js
node --check src/game.js
node --check src/art-direction.js
python -m http.server 8000
```

Manual review targets: `390×844`, `768×1024`, `1440×900`.

## Links

- Play: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html
- Approved art: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html
- GitHub: https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK

## Next milestone

**v0.5 Production Asset Extraction & Animation Pass**

Priority:

1. DR. SPEED production vertical slice.
2. visual consistency review and lock.
3. DR. HEAT + DR. STRATEGY.
4. six patient body sets.
5. ingredient/prop cutouts from `props_station.avif`.
6. animation/VFX and responsive QA.

Do not expand to a second recipe before this production-art pass is complete.
