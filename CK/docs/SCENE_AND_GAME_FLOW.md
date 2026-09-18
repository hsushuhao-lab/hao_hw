# CK Scene & Game Flow

## Core fantasy

A normal outpatient visit abruptly becomes an arcade mapo-tofu cooking challenge when a patient's craving rises. The player controls one of three doctors, completes the order in the same consultation room, and tries to finish before CRAVING reaches 100%.

## Scene flow

`BOOT / TITLE`
→ `NORMAL CLINIC`
→ `DOCTOR SELECT`
→ `PATIENT ENTER`
→ `ORDER`
→ `COOKING MODE TRANSFORM`
→ `PREP`
→ `CUT TIMING (tofu/scallion when required)`
→ `WOK HEAT ×4`
→ `FINAL TOSS`
→ `SERVE`
→ `PATIENT EAT`
→ `RESULT`
→ `PATIENT LEAVE`
→ next patient

Failure path: at any active order state, `CRAVING >= 100%` → order failed → result → next patient.

## Playable doctors

### DR. SPEED / 快刀醫師
- Passive: strongest prep Focus gain.
- Ultimate: **閃電備料** — instantly completes one missing ingredient and gives Focus.
- Animation identity for v0.4: rapid hand movement, tray slide, energetic entrance.

### DR. HEAT / 火候醫師
- Passive: larger perfect-heat tolerance.
- Ultimate: **精準火候** — next heat judgement is guaranteed Perfect.
- Animation identity: calm wok control, deliberate seasoning, flame flourish.

### DR. STRATEGY / 處方醫師
- Passive: slower CRAVING rise.
- Ultimate: **Craving 處方** — immediately reduces CRAVING and restores Focus.
- Animation identity: order clipboard, deliberate prescription gesture, UI/order-ticket motif.

## Patients

Six established archetypes only for this milestone:
1. 焦慮上班族
2. 熬夜學生
3. 長班司機
4. 熱情阿姨
5. 安靜青年
6. 熟客

Do not add more patients until the six have body animation states.

## Gameplay resources

### CRAVING
- Primary failure pressure.
- Rises while the player is handling an order.
- Wrong ingredients/misses can raise it faster.
- At 100% the order fails.

### FOCUS
- Positive execution resource / feedback.
- Correct prep and successful timing raise it.
- Used primarily as a performance indicator; do not redesign into a complex economy in v0.4.

## Visual transformation rule

Clinic Mode and Cooking Mode must visibly be **the same room**. Preserve recognizable anchors:
- doctor desk/computer,
- printer/order ticket station,
- drawer cabinet → ingredient/spice storage,
- sink/wash area,
- patient chair/serving lane.

## v0.4 acceptance flow

A full successful run must visibly demonstrate:
1. doctor entrance,
2. patient walk-in and sit,
3. order event,
4. room transformation,
5. doctor prep animation,
6. doctor cook animation,
7. serve animation,
8. patient eat animation,
9. patient leave animation,
10. next patient loads without page refresh.