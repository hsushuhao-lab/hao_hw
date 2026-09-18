# R2 Materials / Delivery Manifest

## On this repository main
- CK/index.html, CK/styles.css, CK/r2-fixes.css, CK/src/main.js: 2D prototype.
- CK/tests/smoke_test.py: DOM/local-resource/syntax checks.
- CK/tests/browser_qa.py: 24 real Chromium behavior/layout checks.
- .github/workflows/ck2-main-qa.yml: HTTP-served browser verification with screenshots and source hashes.
- CK/docs/AGENT_PROMPT.md and R2_MIGRATION.md: updated handoff and explicit limitations.

## In the separately delivered R2 source package (NOT uploaded here)
- 7 exact full-resolution original PNG concept boards.
- 7 viewing JPEG previews (up to 1200 px).
- 6 historical candidate WebP rasters, explicitly not production models.
- assets/manifest.json: exact bytes, SHA-256, dimensions, formats, roles.
- art-review.html: reference gallery, not the game renderer.
- tools/verify_assets.py: full image decode and checksum verification.
- tools/publish_main.py: main-only private target publishing via the user's authorized local GitHub CLI.
- complete design specification, privacy policy, browser evidence and migration notes.

## Private/history package (not for public GitHub)
Real-person reference photographs, old ZIP deliveries, historical QA and superseded documents. This package must not be part of the public source tree or public deployment.

## Explicit status
Production 3D models: 0. New repository clinic-kitchen-2: unavailable to the connected app at the latest check (404); not claimed as created or published. Existing main receives only the runtime fix/tests/text handoff in this push. No private images or large binary artwork are included in this commit.
