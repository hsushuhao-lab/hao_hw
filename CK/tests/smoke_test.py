import pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
for p in ['index.html','styles.css','src/main.js','README.md','docs/CK2_REBUILD_PLAN.md']:
    assert (ROOT/p).exists(), p
html=(ROOT/'index.html').read_text(encoding='utf-8')
js=(ROOT/'src/main.js').read_text(encoding='utf-8')
for t in ['CLINIC KITCHEN 2.0','id="player"','CLINIC','PREP','KITCHEN','src/main.js','id="cookingDeck"','id="cutBtn"','id="heatBtn"','id="plateBtn"']:
    assert t in html,t
for t in ['keydown','requestAnimationFrame','nearProp','WASD','foodButtons','cookLog','stirBtn','plateBtn']:
    assert t in js,t
print('CK2 M0 smoke test: PASS')
