from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    'index.html', 'styles.css', 'src/game.js', 'src/data.js',
    'assets/concept/doctor_concepts.svg',
    'assets/concept/clinic_layout.svg',
    'assets/concept/cooking_mode.svg',
    'assets/concept/props.svg',
    'assets/concept/patient_npcs.svg',
]

missing = [p for p in required if not (ROOT / p).exists()]
assert not missing, f'Missing required files: {missing}'

html = (ROOT / 'index.html').read_text(encoding='utf-8')
js = (ROOT / 'src/game.js').read_text(encoding='utf-8')
data = (ROOT / 'src/data.js').read_text(encoding='utf-8')

for token in ['Craving Kitchen', 'src/game.js', 'doctorCards', 'ingredientGrid']:
    assert token in html, f'index.html missing token: {token}'

for token in ['acceptOrder', 'pickIngredient', 'cookAction', 'serve', 'failOrder']:
    assert token in js, f'game.js missing function/token: {token}'

for token in ['DR. SPEED', 'DR. HEAT', 'DR. STRATEGY', 'patients', 'cookSteps']:
    assert token in data, f'data.js missing content: {token}'

print('CK smoke test: PASS')
