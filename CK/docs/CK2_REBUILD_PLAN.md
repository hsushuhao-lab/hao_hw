# CK 2.0 — Clinic Kitchen Rebuild Plan

## Status
**ACTIVE REBUILD — TEXT DESIGN LOCKED / FIRST SHELL UPDATE PUBLISHED**

This version abandons the old “dashboard timing mini-game” presentation and rebuilds CK around a believable continuous space and physical task flow.

## Product definition
Third-person 3D clinic-cooking simulation / mission management.

The player must physically move through one connected environment:
**Clinic → Transition/Prep → Kitchen → back to Clinic**.

## Vertical slice goal
One playable doctor, one patient, one bowl of mapo tofu, fully playable from consultation to first bite.

## Frozen loop
1. Patient enters clinic.
2. Player approaches and starts consultation.
3. Gather craving/stress/hunger/preferences.
4. Write recipe prescription.
5. Print and carry order.
6. Walk through transition/prep area.
7. Open storage/fridge and collect ingredients.
8. Knife-work on tofu/scallion.
9. Cook mapo tofu in a wok using visual/audio food feedback.
10. Plate rice and tofu.
11. Carry tray back to clinic.
12. Serve.
13. Patient takes first bite.
14. Reaction + score + state change.

## Environment
### Zone A — Clinic
Doctor desk, monitor, printer, patient chair, examination equipment, drawers, sink, fluorescent lighting.

### Zone B — Transition / Prep
Handwashing, stainless prep trolley, refrigerator, ingredient storage, prescription/order printer, apron/tool station.

### Zone C — Kitchen
Compact but real cooking line: stove, wok, chopping board, steel counter, spice rack, rice station, ventilation.

The kitchen must remain visibly connected to the clinic. It is not a restaurant.

## Character art
Target: refined semi-realistic / photorealistic-stylized 3D.
No chibi, flat SVG, emoji, anime-style production characters.

Doctor identity must preserve hairstyle, glasses, coat, inner clothing and recognizable silhouette from approved references.

## Interaction philosophy
The player should look at the world, not at meters.

HUD is secondary. Primary feedback comes from:
- patient fidgeting/restlessness;
- visible ingredients in hand;
- tofu size and breakage;
- wok color, steam, flame and sauce viscosity;
- sound of oil, meat, doubanjiang and starch slurry;
- patient facial reaction.

## First implementation milestone
**M1 — DR. SPEED vertical slice**
- third-person locomotion shell
- one clinic-patient interaction
- recipe prescription UI
- one complete ingredient pickup sequence
- tofu cutting
- full wok cooking sequence
- tray carry
- first-bite payoff

No second patient and no second recipe until M1 is fun.
