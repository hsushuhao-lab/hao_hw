# CK Asset Hierarchy — v0.4.1

## Canonical visual source of truth

Use only:

```text
art_direction/source_of_truth/
  doctor_concepts.webp
  clinic_layout.webp
  cooking_mode.webp
  props_station.webp
  patient_npcs.webp
```

These files define the approved art direction for all new work.

## Legacy fallback assets

The following directories remain for gameplay compatibility and state references, but they are **not production-final art**:

```text
concept/
portraits/
characters/doctors/
characters/patients/
```

Older `art/*.jpg` and older `art_direction/source_of_truth/*.jpg` are deprecated copies from the incorrect art pass and must not be used for new work.

## Next production structure

New approved production assets should be added under:

```text
production/
  characters/doctors/
  characters/patients/
  environments/
  ingredients/
  props/
  ui/
  vfx/
```

Do not replace working fallbacks until new production assets are visually reviewed and regression-tested.
