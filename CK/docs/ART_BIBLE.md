# CK — Approved Art Bible v0.4.1

## Status

**APPROVED VISUAL SOURCE OF TRUTH — CORRECTED 2026-09-17**

The following five WebP sheets are the highest-priority visual references for all future CK work:

```text
assets/art_direction/source_of_truth/
  doctor_concepts.webp
  clinic_layout.webp
  cooking_mode.webp
  props_station.webp
  patient_npcs.webp
```

They supersede the older compressed JPEG copies and all legacy SVG interpretations.

Legacy SVG characters/environments remain gameplay fallback assets only. They are **not** the final production art direction.

## Core Direction

CK is a **stylized 2.5D arcade illustration** game: warm, bright, semi-realistic, friendly, humorous, and visually polished. It should feel like an indie cooking-management game occurring inside a psychiatric outpatient clinic.

Core phrase: **Same Clinic, Different Flavors.**

The visual joke works only if Cooking Mode still clearly reads as the same clinic. Do not redesign the room into a generic restaurant or commercial kitchen.

## Palette

- Deep navy — titles, strong UI anchors, medical professionalism.
- Warm cream / paper white — cards, clinic surfaces, order slips.
- Soft sky blue — calm clinic information states.
- Warm yellow — sticky notes, selection, positive feedback.
- Chili red / flame orange — wok heat, cooking energy, craving pressure.
- Fresh scallion green — focus, completion, ingredient freshness.

## Presentation Language

Use the same visual language as the approved sheets:

- rounded white cards
- handwritten-note feeling
- sticky notes / labels
- order tickets
- recipe prescription sheets
- soft drop shadows
- navy headings with warm yellow accents
- bright clinic background
- warm cooking highlights

Production UI copy must use real HTML/CSS text. Do not depend on AI-generated pseudo-text baked into artwork.

## Doctors

### DR. SPEED

- friendly, energetic, extroverted
- transparent/light glasses
- bowl/chopsticks/fast-prep identity
- quick, springy, playful motion language
- Ultimate: lightning-fast prep

### DR. HEAT

- calm, centered, precise
- blue shirt under white coat
- wok / spice / flame identity
- controlled, stable, confident motion language
- Ultimate: precision heat

### DR. STRATEGY

- analytical, composed
- round glasses + pale-green mask element
- clipboard / recipe prescription identity
- deliberate, tactical motion language
- Ultimate: craving prescription / order management

Future production character art should preserve consistent anatomy, face identity, clothing, glasses, hairstyle, coat length, and props across:

`entrance / idle / prep / cut / cook / serve / ultimate / fail / victory`

## Patient NPCs

Approved archetypes:

1. The Anxious Office Worker
2. The Tired Student
3. The Chain-Smoking Driver
4. The Cheerful Auntie
5. The Quiet Young Adult
6. The Repeat Visitor

Each patient must remain recognizable by silhouette and clothing, not facial details alone.

Gameplay states:

`walk in / sit / order / eat / leave`

Avoid repeated glamorized smoking imagery. Craving should be conveyed mainly through restlessness, fidgeting, pocket-checking, expression, pacing, and the CRAVING meter.

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

Use `props_station.webp` as the authority for:

- tofu
- minced pork
- doubanjiang
- fermented black beans
- garlic
- scallion
- chili
- Sichuan pepper
- rice
- wok
- ladle
- spatula
- knife
- chopping board
- portable stove
- order slips
- recipe prescription

Production interaction assets should use consistent 3/4 perspective, transparent background, unified lighting, and high one-glance recognizability.

## Camera

- Main gameplay — slightly elevated 3/4 front perspective.
- Dialogue/order — medium character card / portrait presentation.
- Heat/toss feedback — short close-up or VFX emphasis without losing clinic context.

## Runtime bridge

Until transparent production sprites are available, the web build may crop visible doctor/patient imagery directly from the approved concept sheets. This is preferable to showing the visually inconsistent legacy SVGs.

## Do / Don't

### DO

- keep clinic identity visible
- use the five WebP sheets as the highest visual authority
- maintain warm semi-realistic illustrated look
- make UI feel like notes, prescriptions, labels, and tickets
- use real web text for final labels and copy

### DON'T

- convert the room into a generic restaurant
- treat legacy SVGs as production-final art
- revert runtime to old `assets/art/*.jpg`
- introduce unrelated anime/chibi styles that break consistency
- use generated misspelled text as final UI
- add a second recipe before the first dish reaches production-quality visual polish
