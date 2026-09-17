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
  phase: 'idle',
  active: false,
  heatHits: []
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
  $('acceptOrderBtn').disabled = false;
  $('orderPanel').classList.remove('is-disabled');
  newPatient();
  setStatus(`已選擇 ${state.doctor.subtitle}`);
}

function randomPatient() {
  return patients[Math.floor(Math.random() * patients.length)];
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

  $('patientImage').src = state.patient.portrait;
  $('patientName').textContent = state.patient.name;
  $('patientLine').textContent = state.patient.line;
  $('orderNumber').textContent = String(state.orderNo).padStart(3, '0');
  $('orderHeadline').textContent = `${state.patient.order.spice} · ${state.patient.order.modifier}`;
  $('orderDetails').textContent = `${state.patient.order.rice}｜必要材料 ${state.required.length} 種`;
  $('acceptOrderBtn').disabled = false;
  $('acceptOrderBtn').textContent = '接單';
  $('workstation').classList.add('is-hidden');
  $('stageArt').src = 'assets/concept/clinic_layout.svg';
  updateMeters();
  renderIngredients();
  setPhase('prep', false);
}

function acceptOrder() {
  if (!state.doctor || !state.patient) return;
  state.active = true;
  state.phase = 'prep';
  $('acceptOrderBtn').disabled = true;
  $('acceptOrderBtn').textContent = '料理中';
  $('workstation').classList.remove('is-hidden');
  $('stageArt').src = 'assets/concept/cooking_mode.svg';
  setStatus('備料中');
  startCravingTimer();
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
  if (!state.active || state.phase !== 'prep') return;
  const btn = ingredientGrid.querySelector(`[data-ingredient="${id}"]`);
  if (state.required.includes(id)) {
    if (!state.prepped.has(id)) {
      state.prepped.add(id);
      btn.classList.add('is-done');
      state.focus = clamp(state.focus + (state.doctor?.prepFocusBonus ?? 4), 0, 100);
      state.craving = clamp(state.craving - 2, 0, 100);
    }
  } else {
    state.craving = clamp(state.craving + 6, 0, 100);
    state.focus = clamp(state.focus - 6, 0, 100);
    btn.animate([{transform:'translateX(0)'},{transform:'translateX(-5px)'},{transform:'translateX(5px)'},{transform:'translateX(0)'}],{duration:220});
  }
  updatePrepStatus();
  updateMeters();
  if (state.prepped.size === state.required.length) enterCookPhase();
}

function updatePrepStatus() {
  $('prepStatus').textContent = `${state.prepped.size} / ${state.required.length}`;
}

function enterCookPhase() {
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

function cookAction() {
  if (!state.active || state.phase !== 'cook') return;
  const tolerance = state.doctor?.heatTolerance ?? 0;
  const low = 40 - tolerance / 2;
  const high = 60 + tolerance / 2;
  const hit = state.heatPosition >= low && state.heatPosition <= high;
  state.heatHits.push(hit);
  if (hit) {
    state.focus = clamp(state.focus + 12, 0, 100);
    state.craving = clamp(state.craving - 4, 0, 100);
  } else {
    state.focus = clamp(state.focus - 8, 0, 100);
    state.craving = clamp(state.craving + 4, 0, 100);
  }
  state.cookStep += 1;
  updateMeters();
  $('cookStatus').textContent = `${state.cookStep} / ${cookSteps.length}`;
  if (state.cookStep >= cookSteps.length) {
    clearInterval(state.heatTimer);
    enterServePhase();
    return;
  }
  $('cookInstruction').textContent = `步驟 ${state.cookStep + 1}：${cookSteps[state.cookStep]}`;
  $('cookActionBtn').textContent = `火候到位 → ${cookSteps[state.cookStep]}`;
}

function enterServePhase() {
  state.phase = 'serve';
  setPhase('serve', true);
  const goodHeat = state.heatHits.filter(Boolean).length;
  $('serveSummary').innerHTML = `
    <div class="summary-chip"><span>材料</span><strong>${state.prepped.size}/${state.required.length}</strong></div>
    <div class="summary-chip"><span>火候</span><strong>${goodHeat}/${cookSteps.length}</strong></div>
    <div class="summary-chip"><span>Craving</span><strong>${Math.round(state.craving)}%</strong></div>
  `;
  setStatus('等待上菜');
}

function serve() {
  if (!state.active || state.phase !== 'serve') return;
  state.active = false;
  stopTimers();
  const heatScore = state.heatHits.filter(Boolean).length * 25;
  const cravingScore = Math.max(0, 100 - Math.round(state.craving));
  const focusScore = Math.round(state.focus * 0.6);
  const earned = 80 + heatScore + cravingScore + focusScore;
  state.score += earned;
  state.done += 1;
  state.streak += 1;
  state.bestStreak = Math.max(state.bestStreak, state.streak);
  $('resultTitle').textContent = `${state.patient.name}：成功撐過這一波！`;
  $('resultText').textContent = `完成 ${state.patient.order.spice} 麻婆豆腐。火候成功 ${state.heatHits.filter(Boolean).length}/${cookSteps.length} 次，結束時 craving ${Math.round(state.craving)}%。`;
  $('resultScore').textContent = `+${earned} pts`;
  $('resultModal').classList.remove('is-hidden');
  updateStats();
}

function failOrder() {
  state.active = false;
  stopTimers();
  state.streak = 0;
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

function setStatus(text) { $('statusText').textContent = text; }
function clamp(n,min,max) { return Math.max(min,Math.min(max,n)); }
function stopTimers() { clearInterval(state.cravingTimer); clearInterval(state.heatTimer); }

$('startBtn').addEventListener('click', () => {
  $('heroTitle').textContent = 'CRAVING 72%';
  $('heroText').textContent = '診間進入 Cooking Mode。選一位醫師接下第一張訂單。';
  $('game').classList.remove('is-hidden');
  $('game').scrollIntoView({behavior:'smooth', block:'start'});
  setStatus('等待角色選擇');
});
$('acceptOrderBtn').addEventListener('click', acceptOrder);
$('cookActionBtn').addEventListener('click', cookAction);
$('serveBtn').addEventListener('click', serve);
$('nextPatientBtn').addEventListener('click', nextPatient);
$('artBtn').addEventListener('click', () => $('artGallery').classList.toggle('is-hidden'));
$('closeArtBtn').addEventListener('click', () => $('artGallery').classList.add('is-hidden'));

window.addEventListener('beforeunload', stopTimers);
renderDoctors();
updateStats();
