// Approved visual source-of-truth bridge. Keeps gameplay logic untouched.
const ART = {
  clinic: 'assets/art/clinic_layout.jpg',
  cooking: 'assets/art/cooking_mode.jpg',
  doctors: 'assets/art/doctor_concepts.jpg',
  props: 'assets/art/props.jpg',
  patients: 'assets/art/patient_npcs.jpg'
};

function normalizeStageArt(img) {
  if (!img) return;
  const src = img.getAttribute('src') || '';
  if (src.includes('clinic_layout')) img.src = ART.clinic;
  if (src.includes('cooking_mode')) img.src = ART.cooking;
}

function applyApprovedArt() {
  const stage = document.getElementById('stageArt');
  normalizeStageArt(stage);
  if (stage) {
    new MutationObserver(() => normalizeStageArt(stage)).observe(stage, { attributes: true, attributeFilter: ['src'] });
  }

  const gallery = document.querySelectorAll('#artGallery figure img');
  const sources = [ART.doctors, ART.clinic, ART.cooking, ART.props, ART.patients];
  gallery.forEach((img, i) => { if (sources[i]) img.src = sources[i]; });

  const eyebrow = document.querySelector('.topbar .eyebrow');
  if (eyebrow) eyebrow.textContent = 'CK v0.4 · APPROVED ART DIRECTION';

  document.documentElement.dataset.artDirection = 'approved-2026-09-17';
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', applyApprovedArt, { once: true });
} else {
  applyApprovedArt();
}
