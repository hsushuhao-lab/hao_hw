import { doctors, ingredients, patients, cookSteps } from './data.js';

const $ = (id) => document.getElementById(id);
const state = {
  doctor: null,
  patient: null,
  orderNo: 1,
  craving: 0,
  focus: 0,
  score: 0,
  done: 0,
  streak: 0,
  bestStreak: 0,
  required: [],
  prepped: new Set(),
  cookStep: 0,
  heatPosition: 0,
  heatDirection: 1,
  heatTimer: null,
  cravingTimer: null,
  cutTimer: null,
  cutChallenge: null,
  phase: 'idle',
  active: false,
  heatHits: [],
  soundEnabled: true,
  audioCtx: null,
  skillUsed: false,
  guaranteedHeat: false,
  tossTimer: null,
  tossPosition: 4,
  tossDirection: 1,
  tossHit: null
};

const doctorCards = $('doctorCards');
const ingredientGrid = $('ingredientGrid');

function renderDoctors() {
  doctorCards.innerHTML = doctors.map(d => `
    <button class="doctor-card" data-doctor="${d.id}" type="button">
      <img src="${d.portrait}" alt="${d.subtitle}" />
      <span><strong>${d.name}</strong><small>${d.subtitle}<br>${d.bonusText}</small></span>
    </button>
  `).join('');
  doctorCards.querySelectorAll('.doctor-card').forEach(btn => {
    btn.addEventListener('click', () => selectDoctor(btn.dataset.doctor));
  });
}

function selectDoctor(id) {
  state.doctor = doctors.find(d => d.id === id);
  document.querySelectorAll('.doctor-card').forEach(el => el.classList.toggle('is-selected', el.dataset.doctor === id));
  $('doctorBonus').textContent = state.doctor.bonusText;
  $('skillName').textContent = state.doctor.ultimate.name;
  $('skillDesc').textContent = state.doctor.ultimate.desc;
  $('doctorPresenceImage').src = state.doctor.portrait;
  $('doctorPresenceName').textContent = state.doctor.subtitle;
  $('doctorPresence').classList.remove('is-hidden','is-arriving');
  void $('doctorPresence').offsetWidth;
  $('doctorPresence').classList.add('is-arriving');
  $('acceptOrderBtn').disabled = false;
  $('orderPanel').classList.remove('is-disabled');
  sound('select');
  newPatient();
  setStatus(`已選擇 ${state.doctor.subtitle}`);
}

function randomPatient() {
  return patients[Math.floor(Math.random() * patients.length)];
}

function animatePatient(className) {
  const card = $('patientCard');
  card.classList.remove('is-entering','is-leaving','is-eating');
  void card.offsetWidth;
  card.classList.add(className);
  if (className === 'is-entering') setTimeout(() => card.classList.remove(className), 500);
  if (className === 'is-eating') setTimeout(() => card.classList.remove(className), 800);
}

function newPatient() {
  stopTimers();
  state.patient = randomPatient();
  state.craving = 34 + Math.floor(Math.random() * 11);
  state.focus = 24;
  state.required = [...state.patient.order.required];
  state.prepped = new Set();
  state.cookStep = 0;
  state.heatHits = [];
  state.phase = 'order';
  state.active = false;
  state.cutChallenge = null;
  state.skillUsed = false;
  state.guaranteedHeat = false;
  state.tossHit = null;

  $('patientImage').src = state.patient.portrait;
  $('patientName').textContent = state.patient.name;
  $('patientLine').textContent = state.patient.line;
  $('orderNumber').textContent = String(state.orderNo).padStart(3, '0');
  $('orderHeadline').textContent = `${state.patient.order.spice} · ${state.patient.order.modifier}`;
  $('orderDetails').textContent = `${state.patient.order.rice}｜必要材料 ${state.required.length} 種`;
  $('acceptOrderBtn').disabled = false;
  $('acceptOrderBtn').textContent = '接單';
  $('workstation').classList.add('is-hidden');
  $('tossChallenge').classList.add('is-hidden');
  $('cookActionBtn').classList.remove('is-hidden');
  updateUltimateButton(false);
  $('cutChallenge').classList.add('is-hidden');
  ingredientGrid.classList.remove('is-locked');
  $('stageArt').src = 'assets/concept/clinic_layout.svg';
  updateMeters();
  renderIngredients();
  setPhase('prep', false);
  animatePatient('is-entering');
  sound('ticket');
}

function acceptOrder() {
  if (!state.doctor || !state.patient) return;
  state.active = true;
  state.phase = 'prep';
  $('acceptOrderBtn').disabled = true;
  $('acceptOrderBtn').textContent = '料理中';
  $('workstation').classList.remove('is-hidden');
  $('stageArt').src = 'assets/concept/cooking_mode.svg';
  flashScene();
  sound('start');
  setStatus('備料中');
  updateUltimateButton(true);
  startCravingTimer();
}

function flashScene() {
  const el = $('sceneFlash');
  el.classList.remove('is-active');
  void el.offsetWidth;
  el.classList.add('is-active');
  setTimeout(() => el.classList.remove('is-active'), 520);
}

function startCravingTimer() {
  clearInterval(state.cravingTimer);
  state.cravingTimer = setInterval(() => {
    if (!state.active) return;
    const base = 1.25 * (state.doctor?.timeSlow ?? 1);
    state.craving = clamp(state.craving + base, 0, 100);
    state.focus = clamp(state.focus - 0.3, 0, 100);
    updateMeters();
    if (state.craving >= 100) failOrder();
  }, 1000);
}

function renderIngredients() {
  ingredientGrid.innerHTML = ingredients.map(i => `
    <button class="ingredient-btn" data-ingredient="${i.id}" type="button">
      <span>${i.icon}</span>${i.label}
    </button>
  `).join('');
  ingredientGrid.querySelectorAll('.ingredient-btn').forEach(btn => {
    btn.addEventListener('click', () => pickIngredient(btn.dataset.ingredient));
  });
  updatePrepStatus();
}

function pickIngredient(id) {
  if (!state.active || state.phase !== 'prep' || state.cutChallenge) return;
  const btn = ingredientGrid.querySelector(`[data-ingredient="${id}"]`);
  if (state.required.includes(id)) {
    if (state.prepped.has(id)) return;
    if (id === 'tofu' || id === 'scallion') {
      startCutChallenge(id);
      return;
    }
    completePrepIngredient(id);
  } else {
    state.craving = clamp(state.craving + 6, 0, 100);
    state.focus = clamp(state.focus - 6, 0, 100);
    sound('wrong');
    btn.animate([{transform:'translateX(0)'},{transform:'translateX(-5px)'},{transform:'translateX(5px)'},{transform:'translateX(0)'}],{duration:220});
  }
  updatePrepStatus();
  updateMeters();
  maybeFinishPrep();
}

function completePrepIngredient(id, extraFocus = 0) {
  const btn = ingredientGrid.querySelector(`[data-ingredient="${id}"]`);
  state.prepped.add(id);
  btn?.classList.add('is-done');
  state.focus = clamp(state.focus + (state.doctor?.prepFocusBonus ?? 4) + extraFocus, 0, 100);
  state.craving = clamp(state.craving - 2, 0, 100);
  sound('prep');
}

function startCutChallenge(id) {
  clearInterval(state.cutTimer);
  state.cutChallenge = { id, attempts: 0, hits: 0, position: 4, direction: 1 };
  $('cutLabel').textContent = id === 'tofu' ? '切豆腐：保持完整方塊' : '切青蔥：節奏切配';
  $('cutStatus').textContent = '0 / 3';
  $('cutChallenge').classList.remove('is-hidden');
  ingredientGrid.classList.add('is-locked');
  state.cutTimer = setInterval(() => {
    const c = state.cutChallenge;
    if (!c) return;
    const speed = state.doctor?.id === 'speed' ? 1.7 : 2.15;
    c.position += c.direction * speed;
    if (c.position >= 98) c.direction = -1;
    if (c.position <= 2) c.direction = 1;
    $('cutCursor').style.left = `${c.position}%`;
  }, 26);
}

function cutAction() {
  const c = state.cutChallenge;
  if (!state.active || state.phase !== 'prep' || !c) return;
  const tolerance = state.doctor?.id === 'speed' ? 14 : 0;
  const hit = c.position >= 40 - tolerance / 2 && c.position <= 60 + tolerance / 2;
  c.attempts += 1;
  if (hit) {
    c.hits += 1;
    state.focus = clamp(state.focus + 5, 0, 100);
    state.craving = clamp(state.craving - 2, 0, 100);
    sound('cutGood');
  } else {
    state.focus = clamp(state.focus - 3, 0, 100);
    state.craving = clamp(state.craving + 4, 0, 100);
    sound('wrong');
  }
  $('cutStatus').textContent = `${c.attempts} / 3 · Perfect ${c.hits}`;
  updateMeters();
  if (c.attempts < 3) return;

  clearInterval(state.cutTimer);
  const { id, hits } = c;
  state.cutChallenge = null;
  completePrepIngredient(id, hits * 2);
  $('cutChallenge').classList.add('is-hidden');
  ingredientGrid.classList.remove('is-locked');
  updatePrepStatus();
  updateMeters();
  maybeFinishPrep();
}

function maybeFinishPrep() {
  if (state.prepped.size === state.required.length) enterCookPhase();
}

function updatePrepStatus() {
  $('prepStatus').textContent = `${state.prepped.size} / ${state.required.length}`;
}

function enterCookPhase() {
  clearInterval(state.cutTimer);
  state.cutChallenge = null;
  $('cutChallenge').classList.add('is-hidden');
  ingredientGrid.classList.remove('is-locked');
  state.phase = 'cook';
  setPhase('cook', true);
  $('cookInstruction').textContent = `步驟 1：${cookSteps[0]}`;
  $('cookStatus').textContent = `0 / ${cookSteps.length}`;
  $('cookActionBtn').textContent = `火候到位 → ${cookSteps[0]}`;
  setStatus('烹調中');
  startHeatMeter();
}

function setPhase(phase, enable=true) {
  ['prep','cook','serve'].forEach(p => {
    $(`${p}Phase`).classList.toggle('is-hidden', p !== phase);
    const tab = document.querySelector(`[data-phase="${p}"]`);
    tab.classList.toggle('is-active', p === phase);
    if (enable && p === phase) tab.disabled = false;
  });
}

function startHeatMeter() {
  clearInterval(state.heatTimer);
  state.heatPosition = 4;
  state.heatDirection = 1;
  state.heatTimer = setInterval(() => {
    state.heatPosition += state.heatDirection * 2.2;
    if (state.heatPosition >= 98) state.heatDirection = -1;
    if (state.heatPosition <= 2) state.heatDirection = 1;
    $('heatCursor').style.left = `${state.heatPosition}%`;
  }, 26);
}

function triggerHeatFx() {
  const fx = $('heatFx');
  fx.classList.remove('is-active');
  void fx.offsetWidth;
  fx.classList.add('is-active');
  setTimeout(() => fx.classList.remove('is-active'), 600);
}

function cookAction() {
  if (!state.active || state.phase !== 'cook') return;
  const tolerance = state.doctor?.heatTolerance ?? 0;
  const low = 40 - tolerance / 2;
  const high = 60 + tolerance / 2;
  const hit = state.guaranteedHeat || (state.heatPosition >= low && state.heatPosition <= high);
  if (state.guaranteedHeat) state.guaranteedHeat = false;
  state.heatHits.push(hit);
  if (hit) {
    state.focus = clamp(state.focus + 12, 0, 100);
    state.craving = clamp(state.craving - 4, 0, 100);
    triggerHeatFx();
    sound('perfect');
  } else {
    state.focus = clamp(state.focus - 8, 0, 100);
    state.craving = clamp(state.craving + 4, 0, 100);
    sound('wrong');
  }
  state.cookStep += 1;
  updateMeters();
  $('cookStatus').textContent = `${state.cookStep} / ${cookSteps.length}`;
  if (state.cookStep >= cookSteps.length) {
    clearInterval(state.heatTimer);
    startTossChallenge();
    return;
  }
  $('cookInstruction').textContent = `步驟 ${state.cookStep + 1}：${cookSteps[state.cookStep]}`;
  $('cookActionBtn').textContent = `火候到位 → ${cookSteps[state.cookStep]}`;
}

function startTossChallenge() {
  state.phase = 'cook';
  state.tossPosition = 4;
  state.tossDirection = 1;
  $('cookInstruction').textContent = '最後收尾：甩鍋讓醬汁均勻包覆豆腐';
  $('cookActionBtn').classList.add('is-hidden');
  $('tossChallenge').classList.remove('is-hidden');
  $('tossStatus').textContent = '瞄準中央 PERFECT 區';
  clearInterval(state.tossTimer);
  state.tossTimer = setInterval(() => {
    state.tossPosition += state.tossDirection * 2.55;
    if (state.tossPosition >= 98) state.tossDirection = -1;
    if (state.tossPosition <= 2) state.tossDirection = 1;
    $('tossCursor').style.left = `${state.tossPosition}%`;
  }, 24);
  setStatus('甩鍋收尾');
}

function tossAction() {
  if (!state.active || state.phase !== 'cook' || $('tossChallenge').classList.contains('is-hidden')) return;
  const tolerance = state.doctor?.id === 'speed' ? 4 : state.doctor?.id === 'heat' ? 8 : 0;
  const hit = state.tossPosition >= 44 - tolerance / 2 && state.tossPosition <= 56 + tolerance / 2;
  state.tossHit = hit;
  clearInterval(state.tossTimer);
  if (hit) {
    state.focus = clamp(state.focus + 12, 0, 100);
    state.craving = clamp(state.craving - 6, 0, 100);
    $('tossStatus').textContent = 'PERFECT TOSS!';
    triggerHeatFx();
    sound('toss');
  } else {
    state.focus = clamp(state.focus - 4, 0, 100);
    state.craving = clamp(state.craving + 3, 0, 100);
    $('tossStatus').textContent = '收尾完成';
    sound('wrong');
  }
  updateMeters();
  setTimeout(enterServePhase, 420);
}

function updateUltimateButton(active) {
  const btn = $('ultimateBtn');
  const ready = Boolean(active && state.doctor && !state.skillUsed && state.active);
  btn.disabled = !ready;
  btn.textContent = state.skillUsed ? '已使用' : state.doctor ? state.doctor.ultimate.name : 'ULTIMATE';
  btn.classList.toggle('is-ready', ready);
}

function useUltimate() {
  if (!state.active || !state.doctor || state.skillUsed) return;
  state.skillUsed = true;
  if (state.doctor.id === 'speed') {
    const remaining = state.required.find(id => !state.prepped.has(id));
    if (remaining) {
      if (state.cutChallenge) {
        clearInterval(state.cutTimer);
        state.cutChallenge = null;
        $('cutChallenge').classList.add('is-hidden');
        ingredientGrid.classList.remove('is-locked');
      }
      completePrepIngredient(remaining, 8);
      updatePrepStatus();
      maybeFinishPrep();
    } else {
      state.focus = clamp(state.focus + 12, 0, 100);
    }
  } else if (state.doctor.id === 'heat') {
    state.guaranteedHeat = true;
    state.focus = clamp(state.focus + 6, 0, 100);
  } else {
    state.craving = clamp(state.craving - 18, 0, 100);
    state.focus = clamp(state.focus + 10, 0, 100);
  }
  updateMeters();
  updateUltimateButton(false);
  flashScene();
  sound('ultimate');
}

function enterServePhase() {
  state.phase = 'serve';
  setPhase('serve', true);
  const goodHeat = state.heatHits.filter(Boolean).length;
  $('serveSummary').innerHTML = `
    <div class="summary-chip"><span>材料</span><strong>${state.prepped.size}/${state.required.length}</strong></div>
    <div class="summary-chip"><span>火候</span><strong>${goodHeat}/${cookSteps.length}</strong></div>
    <div class="summary-chip"><span>甩鍋</span><strong>${state.tossHit ? 'PERFECT' : 'OK'}</strong></div>
    <div class="summary-chip"><span>Craving</span><strong>${Math.round(state.craving)}%</strong></div>
  `;
  setStatus('等待上菜');
}

function serve() {
  if (!state.active || state.phase !== 'serve') return;
  state.active = false;
  stopTimers();
  animatePatient('is-eating');
  sound('serve');
  const heatScore = state.heatHits.filter(Boolean).length * 25;
  const cravingScore = Math.max(0, 100 - Math.round(state.craving));
  const focusScore = Math.round(state.focus * 0.6);
  const tossScore = state.tossHit ? 35 : 10;
  const earned = 80 + heatScore + tossScore + cravingScore + focusScore;
  state.score += earned;
  state.done += 1;
  state.streak += 1;
  state.bestStreak = Math.max(state.bestStreak, state.streak);
  $('resultTitle').textContent = `${state.patient.name}：成功撐過這一波！`;
  $('resultText').textContent = `完成 ${state.patient.order.spice} 麻婆豆腐。火候成功 ${state.heatHits.filter(Boolean).length}/${cookSteps.length} 次，甩鍋 ${state.tossHit ? 'Perfect' : '完成'}，結束時 craving ${Math.round(state.craving)}%。`;
  $('resultScore').textContent = `+${earned} pts`;
  setStatus('病人用餐中');
  setTimeout(() => animatePatient('is-leaving'), 760);
  setTimeout(() => $('resultModal').classList.remove('is-hidden'), 1060);
  updateStats();
}

function failOrder() {
  state.active = false;
  stopTimers();
  state.streak = 0;
  sound('fail');
  $('resultTitle').textContent = 'Craving 爆表';
  $('resultText').textContent = '這次出餐來不及。下一位病人會重新開始；遊戲設定不代表實際戒菸治療方式。';
  $('resultScore').textContent = '+0 pts';
  $('resultModal').classList.remove('is-hidden');
  updateStats();
}

function nextPatient() {
  $('resultModal').classList.add('is-hidden');
  state.orderNo += 1;
  newPatient();
}

function updateMeters() {
  $('cravingBar').style.width = `${state.craving}%`;
  $('focusBar').style.width = `${state.focus}%`;
  $('cravingText').textContent = `${Math.round(state.craving)}%`;
  $('focusText').textContent = `${Math.round(state.focus)}%`;
}

function updateStats() {
  $('scorePill').textContent = `${state.score} pts`;
  $('ordersDone').textContent = state.done;
  $('bestStreak').textContent = state.bestStreak;
}

function sound(kind) {
  if (!state.soundEnabled) return;
  try {
    state.audioCtx ??= new (window.AudioContext || window.webkitAudioContext)();
    const ctx = state.audioCtx;
    const now = ctx.currentTime;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    const settings = {
      select:[440,.045,'sine'], ticket:[660,.06,'square'], start:[220,.11,'sawtooth'],
      prep:[520,.045,'sine'], cutGood:[760,.04,'square'], perfect:[880,.11,'sine'],
      wrong:[150,.09,'square'], toss:[980,.08,'triangle'], ultimate:[720,.16,'sawtooth'], serve:[1040,.12,'sine'], fail:[110,.25,'sawtooth']
    }[kind] ?? [440,.05,'sine'];
    osc.type = settings[2];
    osc.frequency.setValueAtTime(settings[0], now);
    if (kind === 'perfect') osc.frequency.exponentialRampToValueAtTime(1320, now + settings[1]);
    gain.gain.setValueAtTime(.055, now);
    gain.gain.exponentialRampToValueAtTime(.0001, now + settings[1]);
    osc.connect(gain).connect(ctx.destination);
    osc.start(now); osc.stop(now + settings[1]);
  } catch (_) { /* sound is optional */ }
}

function toggleSound() {
  state.soundEnabled = !state.soundEnabled;
  $('soundBtn').textContent = `音效：${state.soundEnabled ? '開' : '關'}`;
  $('soundBtn').setAttribute('aria-pressed', String(state.soundEnabled));
  if (state.soundEnabled) sound('select');
}

function setStatus(text) { $('statusText').textContent = text; }
function clamp(n,min,max) { return Math.max(min,Math.min(max,n)); }
function stopTimers() {
  clearInterval(state.cravingTimer);
  clearInterval(state.heatTimer);
  clearInterval(state.cutTimer);
  clearInterval(state.tossTimer);
}

$('startBtn').addEventListener('click', () => {
  $('heroTitle').textContent = 'CRAVING 72%';
  $('heroText').textContent = '診間進入 Cooking Mode。選一位醫師接下第一張訂單。';
  flashScene();
  sound('start');
  $('game').classList.remove('is-hidden');
  $('game').scrollIntoView({behavior:'smooth', block:'start'});
  setStatus('等待角色選擇');
});
$('acceptOrderBtn').addEventListener('click', acceptOrder);
$('cutActionBtn').addEventListener('click', cutAction);
$('cookActionBtn').addEventListener('click', cookAction);
$('tossActionBtn').addEventListener('click', tossAction);
$('ultimateBtn').addEventListener('click', useUltimate);
$('serveBtn').addEventListener('click', serve);
$('nextPatientBtn').addEventListener('click', nextPatient);
$('soundBtn').addEventListener('click', toggleSound);
$('artBtn').addEventListener('click', () => $('artGallery').classList.toggle('is-hidden'));
$('closeArtBtn').addEventListener('click', () => $('artGallery').classList.add('is-hidden'));

window.addEventListener('keydown', (event) => {
  if (event.repeat) return;
  if (event.code === 'KeyU') { useUltimate(); return; }
  if (event.code !== 'Space') return;
  const tag = document.activeElement?.tagName;
  if (tag === 'BUTTON') return;
  event.preventDefault();
  if (state.cutChallenge) cutAction();
  else if (!$('tossChallenge').classList.contains('is-hidden') && state.phase === 'cook') tossAction();
  else if (state.phase === 'cook') cookAction();
});

window.addEventListener('beforeunload', stopTimers);
renderDoctors();
updateStats();
