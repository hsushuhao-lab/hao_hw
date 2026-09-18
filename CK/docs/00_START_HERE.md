# CK — START HERE

This is the canonical handoff entry for **Craving Kitchen (CK) v0.4.2 Art Closeout**.

## Read in this order

1. `../README.md` — overview, live links, current milestone.
2. `FINAL_HANDOFF.md` — closeout status, art governance, declared limitations.
3. `MASTER_AGENT_PROMPT.md` — execution prompt for the next AGENT.
4. `SCENE_AND_GAME_FLOW.md` — frozen gameplay/state flow.
5. `ONLINE_ASSET_INDEX.md` — canonical and fallback asset map.
6. `ART_BIBLE.md` — approved visual rules.
7. `GDD.md` — gameplay design.
8. `../PROGRESS.md` — milestone history.

## Repository

- Repository: `hsushuhao-lab/hao_hw`
- Branch: `ck-game`
- Project root: `CK/`
- Current milestone: `v0.4.2 Art Closeout`
- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`

## Canonical visual source of truth

Only these five files have production visual authority:

```text
../assets/art_direction/source_of_truth/
  doctor_concepts.avif
  clinic_layout.avif
  cooking_mode.avif
  props_station.avif
  patient_npcs.avif
```

Do not substitute older JPEG, WebP or SVG files when judging art direction.

Legacy files under `assets/art/`, `assets/concept/`, `assets/portraits/`, and `assets/characters/` remain fallback/programmatic assets only.

## Non-negotiable visual rule

**Same Clinic, Different Flavors.**

The same outpatient consultation room transforms into a compact mapo-tofu cooking workstation. It must not become a generic restaurant or commercial kitchen.

## Current limitation

The runtime now follows the correct art direction, but purpose-built transparent doctor/patient/prop production assets are a v0.5 task. Until those replacements are verified, concept-sheet bridging and legacy state-machine fallbacks remain intentionally available.

## Public repository boundary

Only derived game artwork and code are public. Original private source photographs are not required by the runtime.
