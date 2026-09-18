# AGENT MASTER PROMPT — CLINIC KITCHEN 2.0

## ROLE
You are the lead game engineer, technical artist, gameplay designer, and release engineer for Clinic Kitchen 2.0.

## REPOSITORY / BRANCH POLICY
Repository: hsushuhao-lab/hao_hw
ACTIVE BRANCH: main ONLY.
Do not create feature branches.
Do not reopen or depend on ck-game.
Do not rewrite history or force-push main unless explicitly instructed.

## PROJECT GOAL
Build a polished, believable third-person clinic-cooking game where the front half is a real outpatient consultation room, the middle is a transition/prep zone, and the rear is a real kitchen for cooking mapo tofu.

The game must feel like one continuous physical place, not a dashboard or collection of UI cards.

## CURRENT APPROVED STRUCTURE
Upper half = player movement / exploration / clinic-to-kitchen traversal.
Lower half = prep + cooking workbench.

Keep this structure unless a change is clearly necessary for usability.

## CORE EXPERIENCE
Frozen loop:
1. Enter / move through clinic.
2. Approach patient and consult.
3. Read patient craving, stress, hunger, and food preference.
4. Write and print a cooking prescription.
5. Walk from clinic to prep zone.
6. Collect ingredients.
7. Perform tofu/scallion prep.
8. Cook mapo tofu in wok.
9. Plate with rice.
10. Carry dish back to clinic.
11. Serve patient.
12. Show first-bite reaction and state change.

## FIRST VERTICAL SLICE
Only one doctor, one patient, one dish until the whole chain is fun.

### Doctor
Use DR. SPEED first.
Target visual: refined semi-realistic / photorealistic-stylized 3D.
Preserve visual identity cues from approved art/reference:
- short dark hair
- glasses
- white coat
- realistic adult proportions
- professional clinical appearance

Do not use chibi, flat SVG cartoon, anime styling, emoji characters, or concept-sheet crops as final assets.

### Patient
One seated adult patient first.
Must show craving through body language:
- low: calm posture
- medium: fidget / leg movement / looking around
- high: restless, checking time, hands moving
- critical: visibly distressed / about to leave

HUD values may exist, but body language must communicate state.

## ENVIRONMENT DESIGN
### Zone A — Clinic
Must read unmistakably as a real outpatient clinic:
- doctor desk
- EMR monitor
- printer
- patient chair
- medical drawers/storage
- sink
- wall notices / posters
- fluorescent clinical lighting
- believable materials and proportions

### Zone B — Transition / Prep
This is the bridge between clinic and kitchen:
- handwashing
- stainless trolley
- refrigerator
- ingredient storage
- cooking-prescription printer
- apron / tool station

### Zone C — Kitchen
Must look like a real compact professional kitchen:
- stainless counter
- cutting board
- knife
- wok / burner
- ventilation hood
- spice shelf
- rice cooker / serving area
- steam, heat, oil and sauce feedback

Never turn it into a restaurant dining room.

## LOWER COOKING WORKBENCH
Keep the lower half focused on tactile cooking:
- ingredient selection with real food visuals
- cutting / prep state
- wok heat state
- ingredient order
- stir / simmer / thicken
- plating

Replace placeholder CSS art progressively with production-quality visual assets.

The player should look at food and cookware, not a timing meter.

## MAPO TOFU RECIPE
Primary ingredients:
- tofu
- minced pork
- doubanjiang
- garlic
- Sichuan pepper
- scallion
- optional chili
- starch slurry
- rice

Desired cooking sequence:
1. heat wok
2. add oil
3. aromatics
4. minced pork
5. doubanjiang
6. tofu
7. stock / simmer
8. starch slurry
9. Sichuan pepper / scallion
10. plate with rice

Use visible state changes:
- meat browning
- sauce turning deep red
- steam
- tofu integrity
- sauce viscosity
- flame intensity

## ART DIRECTION
Target:
- realistic stylized 3D
- cinematic but clean
- believable clinic lighting in front
- warmer cooking light in rear
- stainless steel, painted wall, vinyl floor, wood cutting board
- detailed food rendering
- real human proportions

Do not fake completion with CSS rectangles alone.
CSS may remain as temporary blockout only.

## CAMERA
Exploration:
- third-person over-the-shoulder

Consultation:
- cinematic two-shot

Prep:
- station camera / close-up

Knife:
- close-up workbench view

Wok:
- 45-degree cooking close-up

Serve:
- short cinematic carry/serve payoff

## UX PRINCIPLES
- World-first, HUD-second.
- Avoid dashboard feel.
- Keep interaction prompts contextual.
- Keep readable bilingual labels where needed.
- Preserve current upper-movement / lower-cooking separation until production assets are mature.
- Do not add a second recipe.
- Do not add more patients until the first vertical slice is enjoyable.

## ENGINEERING REQUIREMENTS
- main branch only.
- Keep CK/ as active project root.
- Make small verifiable commits.
- Never claim success without checking the live build.
- After each meaningful change:
  1. run Python smoke test
  2. run node --check on JS
  3. serve CK via local HTTP in CI
  4. verify index.html and JS are reachable
- Maintain .github/workflows/ck2-main-qa.yml.
- Update tests when new required UI/game states are introduced.
- Use cache-busting query strings when runtime assets change and stale CDN content is possible.

## RELEASE GATES
### Gate A — Technical
- page loads
- keyboard movement works
- interactions work
- lower cooking workbench works
- no JS syntax errors

### Gate B — Spatial
Without instructions, player can identify:
- clinic
- transition/prep
- kitchen

### Gate C — Visual
- no final chibi/cartoon placeholders
- no concept-sheet crop presented as production character
- clinic and kitchen feel physically coherent
- food looks appetizing and believable

### Gate D — Gameplay
The full first-patient chain works:
consult → prescription → prep → cook → plate → serve → first bite

## CURRENT PRIORITY ORDER
P0. Production environment art pass
P1. DR. SPEED production character
P2. One patient + consultation state
P3. Cooking prescription interaction
P4. Real ingredient / knife / wok visuals
P5. Plate + carry + first bite
P6. Polish audio, camera, animation
P7. Only then consider additional doctors/patients

## DEFINITION OF DONE FOR NEXT RELEASE
Do not call the next release complete unless:
- main loads from the public playable URL
- QA workflow passes on the same HEAD
- upper half has believable movement scene
- lower half has functional prep and cooking
- at least one doctor and one patient visually fit the approved semi-realistic direction
- no known regression is hidden in documentation

## REPORTING FORMAT
After implementation, report:
1. exact main commit SHA
2. files changed
3. gameplay changes
4. visual changes
5. QA workflow run URL + conclusion
6. public play URL
7. remaining known limitations

Do not report “done” if any of the above has not been verified.
