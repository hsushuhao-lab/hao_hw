# CK — Approved Art Bible v0.4.2

## Status

**FINAL VISUAL SOURCE OF TRUTH — 2026-09-17 ART CLOSEOUT**

The following five AVIF sheets are the highest-priority visual references for all future CK work:

```text
assets/art_direction/source_of_truth/
  doctor_concepts.avif
  clinic_layout.avif
  cooking_mode.avif
  props_station.avif
  patient_npcs.avif
```

They supersede every older compressed JPEG copy and every legacy SVG interpretation.

Legacy SVG characters, portraits and environment assets remain compatibility fallbacks only. They are **not production-final art**.

## Core Direction

CK is a **stylized 2.5D arcade illustration** game: warm, bright, semi-realistic, friendly, humorous, and polished. The world is a psychiatric outpatient consultation room that unexpectedly becomes a mapo-tofu cooking station.

Core phrase: **Same Clinic, Different Flavors.**

The joke only works if Cooking Mode clearly remains the same clinic. Never redesign the room into a generic restaurant, cafe, fantasy kitchen, or commercial kitchen.

## Palette

- Deep navy — titles, UI anchors, medical professionalism.
- Warm cream / paper white — cards, clinic surfaces, prescriptions, order slips.
- Soft sky blue — clinic information and calm states.
- Warm yellow — sticky-note emphasis, selection, positive feedback.
- Chili red / flame orange — heat, cooking energy, craving pressure.
- Scallion green — focus, completion, ingredient freshness.

## Presentation Language

Use the same visual language as the canonical sheets:

- rounded white cards
- handwritten-note feeling
- sticky notes / labels
- order tickets
- recipe prescription sheets
- soft drop shadows
- navy headings with warm yellow accents
- bright clinic ambient light
- warm cooking highlights

Production UI copy must be real HTML/CSS text. Do not use baked-in AI pseudo-text as final UI.

## Doctors

### DR. SPEED
- friendly, energetic, extroverted
- transparent/light glasses
- bowl/chopsticks/fast-prep identity
- quick, springy, playful motion
- Ultimate: 閃電備料

### DR. HEAT
- calm, centered, precise
- blue shirt under white coat
- wok / spice / flame identity
- controlled, stable, confident motion
- Ultimate: 精準火候

### DR. STRATEGY
- analytical, composed
- round glasses + pale green mask element
- clipboard / recipe prescription identity
- deliberate, tactical motion
- Ultimate: Craving 處方

Production character art should maintain consistent face, body proportions, clothing, eyewear and hairstyle across entrance, idle, prep, cut, cook, serve, ultimate, fail and victory states.

## Patient NPCs

Approved archetypes:

1. The Anxious Office Worker
2. The Tired Student
3. The Chain-Smoking Driver
4. The Cheerful Auntie
5. The Quiet Young Adult
6. The Repeat Visitor

Each patient must be recognizable by silhouette and clothing, not facial details alone. Gameplay states: walk in, sit, order/react, eat, leave.

Avoid repeated glamorized smoking imagery. Convey craving mainly through fidgeting, restlessness, pocket-checking, expression, pacing and the CRAVING meter.

## Environment

The original clinic remains the structural base:

- doctor desk
- patient seat
- printer / storage
- wash area
- cabinets
- clinic lighting
- white walls
- doorway

Cooking Mode transforms existing clinic objects rather than replacing them:

- monitor → order screen
- printer → order ticket printer
- drawers → spice cabinet
- desk → prep / plating counter
- wash area → ingredient wash station
- open floor → portable wok station

Target balance: **at least ~70% clinic identity, ~30% cooking intervention**.

## Props / Ingredients

Use `props_station.avif` as the authority for tofu, minced pork, doubanjiang, fermented black beans, garlic, scallion, chili, Sichuan pepper, rice, wok, ladle, spatula, knife, chopping board, portable stove, order slips and recipe prescription.

Production interaction assets should use a consistent 3/4 perspective, transparent background, unified lighting and one-glance recognizability.

## Camera

- Main gameplay: slightly elevated 3/4 front perspective.
- Dialogue/order: medium character card / portrait presentation.
- Heat/toss feedback: short close-up or VFX emphasis without losing clinic context.

## Governance

Runtime and gallery must directly reference `assets/art_direction/source_of_truth/*.avif`.

The following folders are legacy/fallback only:

```text
assets/art/
assets/concept/
assets/characters/
assets/portraits/
```

An AGENT may use them for compatibility while production replacements are missing, but may not cite them as art authority.

## Do / Don't

### DO
- keep clinic identity visible
- use the five canonical sheets as visual authority
- maintain warm semi-realistic illustrated look
- make UI resemble notes, prescriptions and tickets
- use real web text for labels and copy
- verify every new production asset visually against the canonical sheets

### DON'T
- convert the room into a generic restaurant
- treat legacy SVGs as production-final art
- introduce unrelated anime/chibi/flat-vector styles
- use generated misspelled text as final UI
- add a second recipe before the first dish reaches production-quality visual polish
