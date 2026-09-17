# CK Deployment

## Immediate playable preview

https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html

This URL serves the exact static files from the `ck-game` branch and requires no build step.

## Intended GitHub Pages URL

https://hsushuhao-lab.github.io/hao_hw/CK/

To activate the GitHub-native URL, open repository **Settings → Pages** and choose a branch publishing source that contains `CK/` (or configure GitHub Actions Pages deployment). The connector used for this project can edit repository content but cannot change repository Pages administration settings.

## Deployment requirements

- Static hosting only.
- Keep relative paths.
- Do not introduce a bundler unless needed.
- Smoke test must pass before deployment.
- `index.html`, `styles.css`, `src/`, `assets/` must stay together.
