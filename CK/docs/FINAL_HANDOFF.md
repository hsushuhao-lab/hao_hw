# CK Final Handoff — v0.4 Character Animation & Deployment QA

## Status

**MILESTONE v0.4 ACCEPTED / FULL-BODY ANIMATIONS INTEGRATED / SMOKE TEST PASS**

The project has advanced from v0.3 Production Slice to **v0.4 Character Animation & Deployment QA** without altering the v0.3 core loop. The game remains a zero-dependency static web application fully deployable via GitHub Pages and raw.githack.

## Completed in v0.4

1. **Doctor Full-Body Animation Suite (21 SVG assets)**:
   - Full-body character vector art for DR. SPEED, DR. HEAT, and DR. STRATEGY across 7 states:
     - `entrance` (dynamic character-unique arrival)
     - `idle` (breathing, ready stance)
     - `prep` (ingredient preparation)
     - `cut` (rhythmic knife chopping)
     - `cook` (wok stirring and heat mastery)
     - `serve` (plate presentation)
     - `ultimate` (character-unique signature VFX: 閃電備料 lightning, 精準火候 roaring flame inferno & target reticle, Craving 處方 glowing clinical Rx seal).
   - The three entrances and ultimates are visually distinct in motion, effects, and iconography.

2. **Patient NPC Full-Body Lifecycle Suite (30 SVG assets)**:
   - Complete 5-state lifecycle for all six established patient archetypes:
     - 焦慮上班族 (Office Worker)
     - 熬夜學生 (Student)
     - 長班司機 (Driver)
     - 熱情阿姨 (Auntie)
     - 安靜青年 (Quiet Youth)
     - 熟客 (Repeat Patron)
   - Lifecycle states: `walk_in` → `sit` → `order` → `eat` → `leave`.
   - Existing portrait elements and CSS bounce animations preserved as guaranteed fallback.

3. **Stage & Gameplay Integration**:
   - `doctorStage` and `patientStage` full-body visual layers added within `clinicStage`.
   - Dynamic synchronization with gameplay phases (selection, order acceptance, prep, cut challenge, wok heat steps, wok toss, ultimate activation, serving, eating, result, and departure).

4. **Production Audio & Volume Mixer**:
   - Web Audio polyphonic synthesizer engine with layered audio nodes:
     - Multi-harmonic sound design for knife chopping, wok sizzle, flame flare, order printer ticket, porcelain serving bell, and ultimate fanfare.
     - Interactive clinic-kitchen procedural BGM groove.
     - Independent volume mixer: Master Volume, BGM Volume, SFX Volume, and BGM Play/Pause controls.
     - Fallback Web Audio synth kept active if any node failure occurs.

5. **Hardened Regression Gates**:
   - `smoke_test.py` now verifies 69 files (including all 21 doctor SVGs, all 30 patient SVGs, DOM IDs, functions, and Node syntax).

## Frozen Decisions & Rules

The next agent must NOT:
- add a second recipe (the recipe remains Mapo Tofu),
- add multiplayer or complex hospital maps,
- rewrite the state model or remove SVG/CSS fallbacks,
- turn the clinic into a generic restaurant (Same Clinic, Different Mode).

## Acceptance Criteria Checklist

- [x] v0.3 core loop regression baseline completely preserved.
- [x] All 21 doctor state assets load without 404s.
- [x] All 30 patient state assets load without 404s.
- [x] Doctors are distinguishable by motion, props, and signature ultimates.
- [x] All six patients execute walk_in → sit → order → eat → leave.
- [x] Prep, cut, 4 wok heats, wok toss, and serve mini-games work as expected.
- [x] CRAVING >= 100% failure path remains functional.
- [x] Audio mixer with independent volume controls and procedural BGM works without external audio files.
- [x] Responsive layout validated across 390×844 (mobile), 768×1024 (tablet), and 1440×900 (desktop).

## QA Commands

From `CK/`:

```bash
python tests/smoke_test.py
python -m http.server 8000
node --check src/data.js
node --check src/game.js
```

## Links

- Play: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html
- Art: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art.html
- GitHub: https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK