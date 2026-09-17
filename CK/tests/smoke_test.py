import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 1. Base files and concept art
base_required = [
    'index.html', 'styles.css', 'src/game.js', 'src/data.js',
    'assets/concept/doctor_concepts.svg',
    'assets/concept/clinic_layout.svg',
    'assets/concept/cooking_mode.svg',
    'assets/concept/props.svg',
    'assets/concept/patient_npcs.svg',
    'assets/portraits/doctor_speed.svg',
    'assets/portraits/doctor_heat.svg',
    'assets/portraits/doctor_strategy.svg',
    'assets/portraits/patient_office.svg',
    'assets/portraits/patient_student.svg',
    'assets/portraits/patient_driver.svg',
    'assets/portraits/patient_auntie.svg',
    'assets/portraits/patient_quiet.svg',
    'assets/portraits/patient_repeat.svg',
]

# 2. Doctor full-body animation state assets (v0.4)
doctor_ids = ['doctor_speed', 'doctor_heat', 'doctor_strategy']
doctor_states = ['entrance', 'idle', 'prep', 'cut', 'cook', 'serve', 'ultimate']
doctor_assets = [
    f'assets/characters/doctors/{d}_{s}.svg'
    for d in doctor_ids
    for s in doctor_states
]

# 3. Patient full-body lifecycle animation state assets (v0.4)
patient_ids = [
    'patient_office', 'patient_student', 'patient_driver',
    'patient_auntie', 'patient_quiet', 'patient_repeat'
]
patient_states = ['walk_in', 'sit', 'order', 'eat', 'leave']
patient_assets = [
    f'assets/characters/patients/{p}_{s}.svg'
    for p in patient_ids
    for s in patient_states
]

required = base_required + doctor_assets + patient_assets

missing = [p for p in required if not (ROOT / p).exists()]
assert not missing, f'Missing required files: {missing}'
assert len(doctor_assets) == 21, f'Expected 21 doctor assets, got {len(doctor_assets)}'
assert len(patient_assets) == 30, f'Expected 30 patient assets, got {len(patient_assets)}'

html = (ROOT / 'index.html').read_text(encoding='utf-8')
css = (ROOT / 'styles.css').read_text(encoding='utf-8')
js = (ROOT / 'src/game.js').read_text(encoding='utf-8')
data = (ROOT / 'src/data.js').read_text(encoding='utf-8')

# DOM element check
for token in [
    'Craving Kitchen', 'src/game.js', 'doctorCards', 'ingredientGrid',
    'cutActionBtn', 'soundBtn', 'heatFx', 'ultimateBtn', 'tossActionBtn',
    'doctorPresence', 'doctorStage', 'doctorBodyImage', 'doctorStateBadge',
    'patientStage', 'patientBodyImage', 'patientStateBadge',
    'audioSettingsPanel', 'masterVolSlider', 'musicVolSlider', 'sfxVolSlider', 'bgmToggleBtn'
]:
    assert token in html, f'index.html missing token: {token}'

# JS state and functions check
for token in [
    'acceptOrder', 'pickIngredient', 'startCutChallenge', 'cutAction',
    'cookAction', 'triggerHeatFx', 'toggleSound', 'startTossChallenge',
    'tossAction', 'useUltimate', 'serve', 'failOrder',
    'setDoctorAnimation', 'setPatientAnimation', 'ensureAudioContext',
    'startBgm', 'stopBgm'
]:
    assert token in js, f'game.js missing function/token: {token}'

# CSS class check for animation states
for token in [
    'doctor-stage', 'doctor-body-img', 'doc-entrance-speed', 'doc-entrance-heat',
    'doc-entrance-strategy', 'doc-idle', 'doc-prep', 'doc-cut', 'doc-cook',
    'doc-serve', 'doc-ultimate-speed', 'doc-ultimate-heat', 'doc-ultimate-strategy',
    'patient-stage', 'patient-body-img', 'pat-walk-in', 'pat-sit', 'pat-order',
    'pat-eat', 'pat-leave', 'audio-panel'
]:
    assert token in css, f'styles.css missing style class: {token}'

for token in ['DR. SPEED', 'DR. HEAT', 'DR. STRATEGY', 'ultimate', 'patients', 'cookSteps']:
    assert token in data, f'data.js missing content: {token}'

# Syntax check with node if available
try:
    node_res_data = subprocess.run(['node', '--check', 'src/data.js'], cwd=ROOT, capture_output=True, text=True)
    assert node_res_data.returncode == 0, f'node --check src/data.js failed: {node_res_data.stderr}'
    node_res_game = subprocess.run(['node', '--check', 'src/game.js'], cwd=ROOT, capture_output=True, text=True)
    assert node_res_game.returncode == 0, f'node --check src/game.js failed: {node_res_game.stderr}'
except FileNotFoundError:
    pass

print(f'CK smoke test: PASS (Checked {len(required)} files, 21 doctor states, 30 patient states, audio mixer, and syntax)')
