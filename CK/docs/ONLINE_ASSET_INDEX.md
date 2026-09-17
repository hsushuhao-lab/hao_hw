# CK Online Asset Index — v0.4.2 Art Closeout

All public CK assets are committed to the `ck-game` branch. The five canonical AVIF sheets below are the **only production visual authority**.

## Canonical approved art

| Asset | GitHub path | Role |
|---|---|---|
| Playable doctors | `assets/art_direction/source_of_truth/doctor_concepts.avif` | 3 playable doctor identities, clothing, props, brushwork |
| Clinic layout | `assets/art_direction/source_of_truth/clinic_layout.avif` | consultation-room spatial baseline |
| Cooking mode | `assets/art_direction/source_of_truth/cooking_mode.avif` | same clinic transformed into mapo-tofu cooking mode |
| Props & station | `assets/art_direction/source_of_truth/props_station.avif` | ingredients, utensils, wok station, order/prescription language |
| Patient NPCs | `assets/art_direction/source_of_truth/patient_npcs.avif` | six patient archetypes and visual identities |

## Runtime binding

The live build references the canonical assets through:

- `src/art-direction.js`
- `art-direction.css`
- `art-original.html`

The live build must never fall back to `assets/art/*.jpg` as its visual authority.

## Legacy compatibility assets

The following folders remain because the existing gameplay/animation state machine still uses them as compatibility fallbacks:

```text
assets/concept/
assets/portraits/
assets/characters/doctors/
assets/characters/patients/
```

They are **not production-final art** and should be progressively replaced by new assets derived from the five canonical sheets.

### Legacy doctor states

3 doctors × 7 states = 21 SVG fallbacks:

`entrance / idle / prep / cut / cook / serve / ultimate`

### Legacy patient lifecycle states

6 patients × 5 states = 30 SVG fallbacks:

`walk_in / sit / order / eat / leave`

## Approved visual identity

**Same Clinic, Different Flavors.**

Cooking Mode keeps the consultation room recognizable. Monitor → order screen; printer → ticket printer; drawers → spice cabinet; desk → prep/plating counter; wash area → ingredient washing; open floor → portable wok station.

## Deprecated paths

Older `assets/art/*.jpg`, `source_of_truth/*.jpg`, and obsolete WebP references are deprecated. They must not be used for new production work.

## Online viewing

- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`
- Play build: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- GitHub source: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`

## Public/private boundary

The public repository contains derived game artwork and code. Original private source photographs are not required by the runtime and are not part of the public release.
