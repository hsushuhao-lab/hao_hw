// CK approved-art runtime bridge — corrected canonical asset pass, 2026-09-17.
// Gameplay logic remains in game.js. This file only replaces visible placeholder art.

const ART_ROOT = 'assets/art_direction/source_of_truth';
const ART = {
  clinic: `${ART_ROOT}/clinic_layout.webp`,
  cooking: `${ART_ROOT}/cooking_mode.webp`,
  doctors: `${ART_ROOT}/doctor_concepts.webp`,
  props: `${ART_ROOT}/props_station.webp`,
  patients: `${ART_ROOT}/patient_npcs.webp`
};

const DOCTOR_IDS = ['speed', 'heat', 'strategy'];
const PATIENT_IDS = ['office', 'student', 'driver', 'auntie', 'quiet', 'repeat'];

function parseId(src, ids) {
  return ids.find(id => src.includes(`_${id}`) || src.includes(`-${id}`) || src.includes(`/${id}`)) || null;
}

function canonicalizeStage(img) {
  if (!img) return;
  const src = img.getAttribute('src') || '';
  if (src.includes('clinic_layout') && src !== ART.clinic) img.src = ART.clinic;
  if (src.includes('cooking_mode') && src !== ART.cooking) img.src = ART.cooking;
}

function decorateDoctorCards() {
  document.querySelectorAll('.doctor-card').forEach(card => {
    const id = card.dataset.doctor;
    if (!DOCTOR_IDS.includes(id)) return;
    const legacy = card.querySelector('img');
    legacy?.classList.add('legacy-approved-hidden');
    if (!card.querySelector('.approved-doctor-portrait')) {
      const art = document.createElement('span');
      art.className = `approved-doctor-portrait approved-doctor-${id}`;
      art.setAttribute('role', 'img');
      art.setAttribute('aria-label', card.querySelector('strong')?.textContent || id);
      card.prepend(art);
    }
    card.addEventListener('click', () => {
      const presence = document.getElementById('doctorPresence');
      if (presence) presence.dataset.doctor = id;
      const stage = document.getElementById('doctorStage');
      if (stage) stage.dataset.doctor = id;
    });
  });
}

function syncDoctorPresence() {
  const img = document.getElementById('doctorPresenceImage');
  const box = document.getElementById('doctorPresence');
  if (!img || !box) return;
  img.classList.add('legacy-approved-hidden');
  const id = parseId(img.getAttribute('src') || '', DOCTOR_IDS);
  if (id) box.dataset.doctor = id;
}

function syncDoctorStage() {
  const img = document.getElementById('doctorBodyImage');
  const stage = document.getElementById('doctorStage');
  if (!img || !stage) return;
  img.classList.add('legacy-approved-hidden');
  const src = img.getAttribute('src') || '';
  const id = parseId(src, DOCTOR_IDS);
  if (id) stage.dataset.doctor = id;
  const stateMatch = src.match(/_(entrance|idle|prep|cut|cook|serve|ultimate)\.svg$/);
  if (stateMatch) stage.dataset.state = stateMatch[1];
}

function syncPatientCard() {
  const img = document.getElementById('patientImage');
  const card = document.getElementById('patientCard');
  if (!img || !card) return;
  img.classList.add('legacy-approved-hidden');
  const id = parseId(img.getAttribute('src') || '', PATIENT_IDS);
  if (id) card.dataset.patient = id;
}

function syncPatientStage() {
  const img = document.getElementById('patientBodyImage');
  const stage = document.getElementById('patientStage');
  if (!img || !stage) return;
  img.classList.add('legacy-approved-hidden');
  const src = img.getAttribute('src') || '';
  const id = parseId(src, PATIENT_IDS);
  if (id) stage.dataset.patient = id;
  const stateMatch = src.match(/_(walk_in|sit|order|eat|leave)\.svg$/);
  if (stateMatch) stage.dataset.state = stateMatch[1];
}

function bindObserver(el, callback) {
  if (!el) return;
  new MutationObserver(callback).observe(el, { attributes: true, attributeFilter: ['src', 'class'] });
}

function applyApprovedArt() {
  const stage = document.getElementById('stageArt');
  canonicalizeStage(stage);
  bindObserver(stage, () => canonicalizeStage(stage));

  decorateDoctorCards();
  syncDoctorPresence();
  syncDoctorStage();
  syncPatientCard();
  syncPatientStage();

  bindObserver(document.getElementById('doctorPresenceImage'), syncDoctorPresence);
  bindObserver(document.getElementById('doctorBodyImage'), syncDoctorStage);
  bindObserver(document.getElementById('patientImage'), syncPatientCard);
  bindObserver(document.getElementById('patientBodyImage'), syncPatientStage);

  const gallery = document.querySelectorAll('#artGallery figure img');
  [ART.doctors, ART.clinic, ART.cooking, ART.props, ART.patients].forEach((src, i) => {
    if (gallery[i]) gallery[i].src = src;
  });

  const eyebrow = document.querySelector('.topbar .eyebrow');
  if (eyebrow) eyebrow.textContent = 'CK v0.4.1 · CORRECTED APPROVED ART';

  document.documentElement.dataset.artDirection = 'approved-corrected-2026-09-17';
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', applyApprovedArt, { once: true });
} else {
  applyApprovedArt();
}
