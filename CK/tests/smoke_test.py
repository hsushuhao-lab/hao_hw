import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# v0.4.2 canonical approved art. These are the only production art authority files.
canonical_art = [
    'assets/art_direction/source_of_truth/doctor_concepts.avif',
    'assets/art_direction/source_of_truth/clinic_layout.avif',
    'assets/art_direction/source_of_truth/cooking_mode.avif',
    'assets/art_direction/source_of_truth/props_station.avif',
    'assets/art_direction/source_of_truth/patient_npcs.avif',
]

base_required = [
    'index.html', 'styles.css', 'art-direction.css',
    'src/game.js', 'src/data.js', 'src/art-direction.js',
    'art-original.html', 'README.md', 'PROGRESS.md',
    'docs/00_START_HERE.md', 'docs/FINAL_HANDOFF.md',
    'docs/MASTER_AGENT_PROMPT.md', 'docs/ART_BIBLE.md',
    'docs/ONLINE_ASSET_INDEX.md', 'docs/RELEASE_MANIFEST.md',
]

# Legacy animation/state art remains compatibility fallback only.
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

# Guard against zero-byte/truncated placeholders. AVIF compression can be compact,
# so the gate checks a conservative minimum rather than an arbitrary 100 KB threshold.
for rel in canonical_art:
    size = (ROOT / rel).stat().st_size
    assert size > 3_000, f'Canonical art unexpectedly small/truncated: {rel} ({size} bytes)'

html = (ROOT / 'index.html').read_text(encoding='utf-8')
css = (ROOT / 'art-direction.css').read_text(encoding='utf-8')
js = (ROOT / 'src/game.js').read_text(encoding='utf-8')
art_js = (ROOT / 'src/art-direction.js').read_text(encoding='utf-8')
data = (ROOT / 'src/data.js').read_text(encoding='utf-8')
readme = (ROOT / 'README.md').read_text(encoding='utf-8')
art_gallery = (ROOT / 'art-original.html').read_text(encoding='utf-8')
art_bible = (ROOT / 'docs/ART_BIBLE.md').read_text(encoding='utf-8')

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
    assert (
        filename in art_js or filename in css or filename in art_gallery or filename in readme
    ), f'Canonical art is not referenced by runtime/gallery/docs: {filename}'

# Old wrong JPG bridge must never become active again.
for forbidden in [
    "assets/art/clinic_layout.jpg",
    "assets/art/cooking_mode.jpg",
    "assets/art/doctor_concepts.jpg",
    "assets/art/props.jpg",
    "assets/art/patient_npcs.jpg",
]:
    assert forbidden not in art_js, f'Old runtime art path still active: {forbidden}'
    assert forbidden not in css, f'Old CSS art path still active: {forbidden}'

for token in [
    'source_of_truth/doctor_concepts.avif',
    'source_of_truth/patient_npcs.avif',
    'source_of_truth/cooking_mode.avif',
]:
    assert token in css or token in art_js, f'Approved art runtime bridge missing: {token}'

for filename in [
    'doctor_concepts.avif', 'clinic_layout.avif', 'cooking_mode.avif',
    'props_station.avif', 'patient_npcs.avif'
]:
    assert filename in art_gallery, f'Art gallery is not canonical: {filename}'
    assert filename in art_bible, f'Art Bible is not canonical: {filename}'

for token in ['DR. SPEED', 'DR. HEAT', 'DR. STRATEGY', 'patients', 'cookSteps']:
    assert token in data, f'data.js missing content: {token}'

assert 'v0.4.2' in readme, 'README does not identify the art-closeout build'
assert 'source_of_truth' in readme, 'README does not declare canonical art path'
assert '*.avif' in readme or '.avif' in readme, 'README still points to an obsolete raster format'

try:
    for path in ['src/data.js', 'src/game.js', 'src/art-direction.js']:
        res = subprocess.run(['node', '--check', path], cwd=ROOT, capture_output=True, text=True)
        assert res.returncode == 0, f'node --check {path} failed: {res.stderr}'
except FileNotFoundError:
    pass

print(
    'CK smoke test: PASS '
    f'(canonical AVIF art={len(canonical_art)}, legacy doctor fallbacks={len(legacy_doctor_assets)}, '
    f'legacy patient fallbacks={len(legacy_patient_assets)})'
)
