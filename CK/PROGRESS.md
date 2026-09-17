# Craving Kitchen — Development Progress

## v0.3 — Production Slice

Status: **COMPLETE / PLAYABLE**

Established gameplay baseline:

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

Historical status: **FUNCTIONALLY COMPLETE, BUT ART STATUS SUPERSEDED**

This milestone added 21 doctor SVG state assets and 30 patient SVG lifecycle assets. They remain useful as programmatic fallback assets and state-machine references.

However, they are **not production-final art**. The earlier documentation that called them production art is superseded by v0.4.1.

## v0.4.1 — Corrected Art Build

Status: **PASS_WITH_NOTES / CORRECTED CANONICAL ART ONLINE**

Reason for corrective milestone:

- the approved visual designs were not actually driving the runtime,
- old JPEG/SVG assets remained visible,
- the online game therefore did not match the approved Craving Kitchen look.

### Corrected canonical art

```text
assets/art_direction/source_of_truth/
  doctor_concepts.webp
  clinic_layout.webp
  cooking_mode.webp
  props_station.webp
  patient_npcs.webp
```

### Completed corrections

- published all five approved concept sheets as WebP.
- Hero now uses approved Cooking Mode art.
- runtime stage normalizer now resolves clinic/cooking scenes to canonical WebP assets.
- doctor selection, doctor presence, and visible doctor stage use the approved doctor sheet rather than visible legacy SVG art.
- patient card and visible patient stage use the approved patient NPC sheet.
- in-game art gallery now resolves to the five canonical sheets.
- `art-original.html` rebuilt as the canonical online art review page.
- Art Bible, handoff documents, asset index, release manifest, and AGENT instructions are being normalized around the corrected source of truth.

### Remaining limitations

- current doctor/patient gameplay art is cropped from the approved concept sheets rather than purpose-built transparent production sprites.
- individual ingredient/prop cutouts are not yet extracted.
- legacy SVGs still exist in the repository for fallback/state compatibility.

These are known limitations, not blockers for the corrected art-direction milestone.

## Next milestone — v0.5 Production Asset Extraction & Animation

Priority:

1. DR. SPEED production sprite vertical slice.
2. DR. HEAT + DR. STRATEGY production sprites.
3. six patient production body sets.
4. transparent ingredient/prop assets.
5. animation/VFX polish.
6. final responsive QA.

Do not add a second recipe until the first dish reaches production-quality visual polish.

## Online URLs

- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`
- Repository: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`
