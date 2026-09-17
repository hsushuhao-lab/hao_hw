# Craving Kitchen — Development Progress

## v0.3 — Production Slice

Status: **COMPLETE / PLAYABLE**

Frozen gameplay baseline:

`doctor select → patient enter → order → clinic transforms → prep/cut → four heat judgements → final toss → serve → patient eat → result → patient leave → next patient`

Failure remains `CRAVING >= 100%`.

Implemented gameplay:

- 3 selectable doctors with different passives and Ultimates.
- 6 patient archetypes and order preferences.
- prep / cut timing.
- four-step wok heat timing.
- final toss timing.
- CRAVING / FOCUS.
- score / streak.
- Web Audio SFX + procedural BGM + mixer.

## v0.4 — Legacy Character Animation Pass

Historical status: **FUNCTIONALLY COMPLETE, ART STATUS SUPERSEDED**

This milestone added 21 doctor SVG state assets and 30 patient SVG lifecycle assets. They remain useful as programmatic fallback assets and state-machine references, but they are **not production-final art**.

## v0.4.1 — Art Correction

Historical status: **CORRECTIVE BUILD**

The major defect was identified: approved concept art existed, but the visible runtime still depended on the wrong `assets/art/*.jpg` / legacy SVG visual language. Runtime art binding was corrected and moved to `assets/art_direction/source_of_truth/`.

## v0.4.2 — Art Closeout

Status: **CLOSEOUT READY / CANONICAL ART ONLINE / RUNTIME BOUND**

### Canonical art authority

```text
assets/art_direction/source_of_truth/
  doctor_concepts.avif
  clinic_layout.avif
  cooking_mode.avif
  props_station.avif
  patient_npcs.avif
```

### Closeout completed

- runtime bridge points directly to the five canonical AVIF sheets.
- visible CSS layers point to canonical Cooking Mode / doctor / patient art.
- approved-art gallery points only to canonical AVIF assets.
- README, Art Bible, Online Asset Index and AGENT prompt use the same source-of-truth paths.
- regression gate checks canonical AVIF assets rather than obsolete WebP/JPEG paths.
- old `assets/art/*.jpg`, `assets/concept/*.svg`, `assets/characters/*.svg`, and `assets/portraits/*.svg` are explicitly downgraded to legacy/fallback status.
- `Same Clinic, Different Flavors` is frozen as the environment rule.
- second recipe remains out of scope.

### Known limitations carried forward

- current doctor/patient gameplay presentation still uses concept-sheet cropping plus legacy state-machine fallbacks; purpose-built transparent production sprites are not yet complete.
- individual ingredient/prop cutouts are not yet extracted.
- legacy SVG files remain in the repository for compatibility and must not be mistaken for approved production art.

These limitations define v0.5 work; they do not invalidate the v0.4.2 art closeout.

## Next milestone — v0.5 Production Asset Extraction & Animation

Priority:

1. DR. SPEED production sprite vertical slice.
2. lock character consistency after visual review.
3. DR. HEAT + DR. STRATEGY production sprites.
4. six patient production body sets.
5. transparent ingredient / prop assets from `props_station.avif`.
6. animation / VFX polish and responsive QA.

Do not add a second recipe until the first dish reaches production-quality visual polish.

## Online URLs

- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`
- Repository: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`
