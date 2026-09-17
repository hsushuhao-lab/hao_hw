# CK — Approved Art Bible v0.4

## Status

**APPROVED VISUAL SOURCE OF TRUTH — 2026-09-17**

The following five sheets are the highest-priority visual references for all future CK work:

```text
assets/art_direction/source_of_truth/
  doctor_concepts.jpg
  clinic_layout.jpg
  cooking_mode.jpg
  props_station.jpg
  patient_npcs.jpg
```

Legacy SVG characters and environments are gameplay placeholders/fallbacks only. They are not the final production art direction.

## Core Direction

CK is a **stylized 2.5D arcade illustration** game: warm, bright, semi-realistic, friendly, and humorous. It should feel like a polished indie cooking-management game occurring inside a psychiatric outpatient clinic.

Core phrase: **Same Clinic, Different Flavors.**

The joke works only if Cooking Mode still clearly looks like the same clinic. Do not redesign the room into a generic restaurant or commercial kitchen.

## Palette

- Deep navy: titles, strong UI anchors, medical professionalism.
- Warm cream / paper white: cards, clinic surfaces, order slips.
- Soft sky blue: clinic information, calm UI states.
- Warm yellow: sticky-note emphasis, selection, positive feedback.
- Chili red / flame orange: heat, wok, craving pressure.
- Fresh scallion green: focus, completion, ingredients.

## UI Language

Use the same presentation language as the approved concept sheets:

- rounded white cards
- handwritten-note feeling
- sticky notes / labels
- order tickets
- recipe prescription sheets
- soft drop shadows
- navy headings with warm yellow accents
- clean white/cream clinic background

UI text must be real HTML/CSS text. Do not bake generated pseudo-text into production UI assets.

## Doctors

### DR. SPEED
- friendly, energetic, extroverted
- transparent/light glasses
- bowl/chopsticks/fast-prep visual identity
- motion language: quick, springy, playful
- Ultimate: lightning-fast prep

### DR. HEAT
- calm, centered, precise
- blue shirt under white coat
- wok / spice / flame identity
- motion language: controlled, stable, confident
- Ultimate: precision heat

### DR. STRATEGY
- analytical, composed
- round glasses + pale green mask element
- clipboard / recipe prescription identity
- motion language: deliberate, tactical
- Ultimate: craving prescription / order management

Production character art should include consistent proportions and the following states: entrance, idle, prep, cut, cook, serve, ultimate, fail, victory.

## Patient NPCs

Approved archetypes:

1. The Anxious Office Worker
2. The Tired Student
3. The Chain-Smoking Driver
4. The Cheerful Auntie
5. The Quiet Young Adult
6. The Repeat Visitor

Each patient must be recognizable by silhouette and clothing, not facial details alone. Gameplay states: walk in, sit, order, eat, leave.

Avoid glamorizing smoking in repeated gameplay imagery. Craving should be conveyed primarily through fidgeting, restlessness, pocket-checking, expression, motion, and the CRAVING meter.

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
- open floor space → portable wok station

Target visual balance: **at least ~70% still reads as clinic; cooking elements invade the clinic rather than replacing it.**

## Props / Ingredients

Use the approved prop sheet as the source of truth for tofu, minced pork, doubanjiang, fermented black beans, garlic, scallion, chili, Sichuan pepper, rice, wok, ladle, spatula, knife, chopping board, portable stove, order slips, and recipe prescription.

Production ingredient assets should use a consistent 3/4 perspective, transparent background, unified lighting, and high one-glance recognizability.

## Camera

- Main gameplay: slightly elevated 3/4 front perspective.
- Dialogue/order: medium character card / portrait presentation.
- Heat/toss feedback: short close-up or VFX emphasis without losing clinic context.

## Do / Don't

### DO
- keep clinic identity visible
- use approved five sheets as visual authority
- maintain warm semi-realistic illustrated look
- make UI look like notes, prescriptions and tickets
- use real web text for labels and copy

### DON'T
- convert the room into a generic restaurant
- treat legacy SVGs as production-final art
- add unrelated anime/chibi styles that break consistency
- use generated misspelled text as final UI
- add a second recipe before the first dish reaches production-quality visual polish
