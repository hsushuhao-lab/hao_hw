import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

canonical_art = [
    'assets/art_direction/source_of_truth/doctor_concepts.webp',
    'assets/art_direction/source_of_truth/clinic_layout.webp',
    'assets/art_direction/source_of_truth/cooking_mode.webp',
    'assets/art_direction/source_of_truth/props_station.webp',
    'assets/art_direction/source_of_truth/patient_npcs.webp',
]

base_required = [
    'index.html', 'styles.css', 'art-direction.css',
    'src/game.js', 'src/data.js', 'src/art-direction.js',
    'art-original.html', 'README.md', 'PROGRESS.md',
    'docs/00_START_HERE.md', 'docs/FINAL_HANDOFF.md',
    'docs/MASTER_AGENT_PROMPT.md', 'docs/ART_BIBLE.md',
    'docs/ONLINE_ASSET_INDEX.md', 'docs/RELEASE_MANIFEST.md',
]

# Legacy state assets remain compatibility fallbacks, not art authority.
doctor_ids = ['doctor_speed', 'doctor_heat', 'doctor_strategy']
doctor_states = ['entrance', 'idle', 'prep', 'cut', 'cook', 'serve', 'ultimate']
legacy_doctor_assets = [
    f'assets/characters/doctors/{d}_{s}.svg'
    for d in doctor_ids
    for s in doctor_states
]

patient_ids = [
    'patient_office', 'patient_student', 'patient_driver',
    'patient_auntie', 'patient_quiet', 'patient_repeat'
]
patient_states = ['walk_in', 'sit', 'order', 'eat', 'leave']
legacy_patient_assets = [
    f'assets/characters/patients/{p}_{s}.svg'
    for p in patient_ids
    for s in patient_states
]

required = base_required + canonical_art + legacy_doctor_assets + legacy_patient_assets
missing = [p for p in required if not (ROOT / p).exists()]
assert not missing, f'Missing required files: {missing}'

# Canonical art must be real substantial raster assets, not tiny placeholders.
for rel in canonical_art:
    size = (ROOT / rel).stat().st_size
    assert size > 100_000, f'Canonical art unexpectedly small: {rel} ({size} bytes)'

html = (ROOT / 'index.html').read_text(encoding='utf-8')
css = (ROOT / 'art-direction.css').read_text(encoding='utf-8')
js = (ROOT / 'src/game.js').read_text(encoding='utf-8')
art_js = (ROOT / 'src/art-direction.js').read_text(encoding='utf-8')
data = (ROOT / 'src/data.js').read_text(encoding='utf-8')
readme = (ROOT / 'README.md').read_text(encoding='utf-8')

for token in [
    'Craving Kitchen', 'src/game.js', 'src/art-direction.js',
    'doctorCards', 'ingredientGrid', 'cutActionBtn', 'ultimateBtn',
    'tossActionBtn', 'doctorPresence', 'doctorStage', 'patientStage',
    'audioSettingsPanel'
]:
    assert token in html, f'index.html missing token: {token}'

for token in [
    'acceptOrder', 'pickIngredient', 'startCutChallenge', 'cutAction',
    'cookAction', 'startTossChallenge', 'tossAction', 'useUltimate',
    'serve', 'failOrder', 'setDoctorAnimation', 'setPatientAnimation'
]:
    assert token in js, f'game.js missing function/token: {token}'

for rel in canonical_art:
    filename = Path(rel).name
    assert filename in art_js or filename in css or filename in readme, (
        f'Canonical art is not referenced by runtime/docs: {filename}'
    )

for forbidden in [
    "clinic: 'assets/art/clinic_layout.jpg'",
    "cooking: 'assets/art/cooking_mode.jpg'",
    "doctors: 'assets/art/doctor_concepts.jpg'",
    "patients: 'assets/art/patient_npcs.jpg'",
]:
    assert forbidden not in art_js, f'Old wrong runtime art path still active: {forbidden}'

for token in [
    'approved-doctor-portrait',
    'source_of_truth/doctor_concepts.webp',
    'source_of_truth/patient_npcs.webp',
    'source_of_truth/cooking_mode.webp',
]:
    assert token in css or token in art_js, f'Approved art bridge missing token: {token}'

for token in ['DR. SPEED', 'DR. HEAT', 'DR. STRATEGY', 'patients', 'cookSteps']:
    assert token in data, f'data.js missing content: {token}'

assert 'v0.4.1' in readme, 'README does not identify corrected art build'
assert 'source_of_truth' in readme, 'README does not declare canonical art path'

try:
    for path in ['src/data.js', 'src/game.js', 'src/art-direction.js']:
        res = subprocess.run(['node', '--check', path], cwd=ROOT, capture_output=True, text=True)
        assert res.returncode == 0, f'node --check {path} failed: {res.stderr}'
except FileNotFoundError:
    pass

print(
    'CK smoke test: PASS '
    f'(canonical art={len(canonical_art)}, legacy doctor fallbacks={len(legacy_doctor_assets)}, '
    f'legacy patient fallbacks={len(legacy_patient_assets)})'
)
