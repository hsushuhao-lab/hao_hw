# CK — Asset Manifest v0.4.2

## Canonical approved art

The following five AVIF files are the only production visual authority:

| File | Purpose |
|---|---|
| `assets/art_direction/source_of_truth/doctor_concepts.avif` | DR. SPEED / DR. HEAT / DR. STRATEGY identity, clothing, props, brushwork |
| `assets/art_direction/source_of_truth/clinic_layout.avif` | outpatient consultation-room spatial baseline |
| `assets/art_direction/source_of_truth/cooking_mode.avif` | same clinic transformed into Cooking Mode |
| `assets/art_direction/source_of_truth/props_station.avif` | mapo-tofu ingredients, tools, station, order/prescription language |
| `assets/art_direction/source_of_truth/patient_npcs.avif` | six patient NPC archetypes and visual identity |

## Runtime integration

Canonical art is bound by:

- `src/art-direction.js`
- `art-direction.css`
- `art-original.html`

The runtime must not use `assets/art/*.jpg` as visual authority.

## Legacy / fallback assets

These files remain for state-machine compatibility and emergency fallback only:

```text
assets/concept/*.svg
assets/portraits/*.svg
assets/characters/doctors/*.svg
assets/characters/patients/*.svg
```

They are not production-final art.

## Legacy state counts

Doctors: 3 × 7 states = 21 SVG fallbacks.

`entrance / idle / prep / cut / cook / serve / ultimate`

Patients: 6 × 5 states = 30 SVG fallbacks.

`walk_in / sit / order / eat / leave`

## Still missing for production v0.5

- purpose-built transparent full-body doctor sprites derived from `doctor_concepts.avif`
- fail/victory states for each doctor
- purpose-built patient lifecycle sprites derived from `patient_npcs.avif`
- transparent ingredient/prop cutouts derived from `props_station.avif`
- final character animation pass
- production VFX polish

Audio is already represented by procedural Web Audio/BGM and is not the current art blocker.

## Visual governance

**Same Clinic, Different Flavors.** The clinic remains recognizable in Cooking Mode. New assets must visually trace back to the five canonical sheets and must not introduce a new unrelated style.
