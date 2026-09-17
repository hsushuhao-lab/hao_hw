# CK — START HERE

This is the canonical handoff entry for **Craving Kitchen (CK) v0.4.1 Corrected Art Build**.

## Read in this order

1. `../README.md` — project overview, live links, current milestone.
2. `FINAL_HANDOFF.md` — current status, corrected art governance, remaining blockers.
3. `MASTER_AGENT_PROMPT.md` — execution prompt for the next AGENT.
4. `SCENE_AND_GAME_FLOW.md` — gameplay/state flow.
5. `ONLINE_ASSET_INDEX.md` — canonical and fallback asset map.
6. `ART_BIBLE.md` — approved visual rules.
7. `GDD.md` — gameplay design.
8. `../PROGRESS.md` — milestone history.

## Repository

- Repository: `hsushuhao-lab/hao_hw`
- Branch: `ck-game`
- Project root: `CK/`
- Current milestone: `v0.4.1 Corrected Art Build`
- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`

## Canonical visual source of truth

Only these five files have production visual authority:

```text
../assets/art_direction/source_of_truth/
  doctor_concepts.webp
  clinic_layout.webp
  cooking_mode.webp
  props_station.webp
  patient_npcs.webp
```

Do not substitute older JPEG or SVG files when judging art direction.

Legacy files under `assets/concept/`, `assets/portraits/`, and `assets/characters/` remain fallback/programmatic assets only.

## Non-negotiable visual rule

**Same Clinic, Different Flavors.**

The same outpatient consultation room transforms into a compact mapo-tofu cooking workstation. It must not become a generic restaurant or commercial kitchen.

## Important correction

Earlier v0.4 documentation overstated the production status of the SVG character assets. v0.4.1 supersedes that claim: the approved concept sheets are canonical; legacy SVGs are placeholders/fallbacks until proper production character/prop assets are created.

## Public repository boundary

Only derived game artwork is public. Original source photographs of real people remain outside the public repository.
