# CK Online Asset Index — v0.4.1 Corrected Art Build

All public game-art assets are committed to GitHub under the `ck-game` branch. Original source photographs of real people are intentionally **not** published; only derived game artwork is public.

## 1. Canonical production visual source of truth

These five files have the highest visual authority in the project:

| Asset | GitHub path | Purpose |
|---|---|---|
| Playable doctors | `assets/art_direction/source_of_truth/doctor_concepts.webp` | DR. SPEED / DR. HEAT / DR. STRATEGY appearance, props, mood |
| Clinic layout | `assets/art_direction/source_of_truth/clinic_layout.webp` | consultation room structure before transformation |
| Cooking mode | `assets/art_direction/source_of_truth/cooking_mode.webp` | same clinic transformed into compact mapo-tofu cooking mode |
| Props & station | `assets/art_direction/source_of_truth/props_station.webp` | ingredients, wok, tools, order slips, prescription motifs |
| Patient NPCs | `assets/art_direction/source_of_truth/patient_npcs.webp` | six patient archetypes, clothing, expressions, order identity |

Online review:

`https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`

## 2. Runtime visual bridge

`src/art-direction.js` and `art-direction.css` force the visible online build to use the canonical WebP sheets.

Current bridge usage:

- Hero → `cooking_mode.webp`
- Clinic stage → `clinic_layout.webp`
- Cooking stage → `cooking_mode.webp`
- Doctor cards / doctor presence / visible doctor stage → cropped presentation from `doctor_concepts.webp`
- Patient card / visible patient stage → cropped presentation from `patient_npcs.webp`
- Art gallery → all five canonical sheets

This bridge is temporary until transparent production sprites are created.

## 3. Legacy fallback assets — NOT production-final art

### Legacy concept SVGs

```text
assets/concept/doctor_concepts.svg
assets/concept/clinic_layout.svg
assets/concept/cooking_mode.svg
assets/concept/props.svg
assets/concept/patient_npcs.svg
```

### Legacy portrait SVGs

Doctors:

```text
assets/portraits/doctor_speed.svg
assets/portraits/doctor_heat.svg
assets/portraits/doctor_strategy.svg
```

Patients:

```text
assets/portraits/patient_office.svg
assets/portraits/patient_student.svg
assets/portraits/patient_driver.svg
assets/portraits/patient_auntie.svg
assets/portraits/patient_quiet.svg
assets/portraits/patient_repeat.svg
```

### Legacy doctor animation state SVGs

`assets/characters/doctors/` contains 21 files across:

- entrance
- idle
- prep
- cut
- cook
- serve
- ultimate

### Legacy patient lifecycle SVGs

`assets/characters/patients/` contains 30 files across:

- walk_in
- sit
- order
- eat
- leave

These assets remain for fallback and state-machine compatibility only. They must not override the canonical concept-sheet identities.

## 4. Deprecated duplicate raster assets

Older files under `assets/art/*.jpg` and the older `source_of_truth/*.jpg` were part of the incorrect art pass. They are deprecated and must not be used for new work.

New work must reference the WebP files listed in section 1.

## 5. Next production asset structure

Target paths for v0.5:

```text
assets/production/
  characters/doctors/
  characters/patients/
  environments/
  ingredients/
  props/
  ui/
  vfx/
```

Production sprites should be derived visually from the canonical sheets, not from the legacy SVG style.

## Online viewing

- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`
- Repository: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`

## Public/private boundary

Public GitHub contains only derived game artwork and code. Original real-person source photographs remain outside the public repository unless separately approved for redistribution.
