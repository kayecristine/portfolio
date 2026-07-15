# AGENTS.md — Developer Portfolio & Resume Generator Guidelines
> Project-specific AI coding guidelines for the Personal Developer Portfolio site.
> Inherits universal rules from `/Users/kctolentino/workspace/agents.md`.

---

## 🛠️ Project Stack & Architecture
- **Frontend / Website:** Static HTML5 (`index.html`), Vanilla CSS (`style.css`), and Vanilla JavaScript (`script.js`).
- **Automation / Scripting:** Python 3 (`build_resume.py`) for generating or processing resume assets (`Resume_Kaye Cristine Tolentino (v2).pdf`).
- **Environment:** Uses local Python virtual environment (`.venv/`).

---

## 🧪 Verification & Workflow
- **Frontend Changes:** Verify visual layout, responsive breakpoints, and animations by opening `index.html` in a browser or running a local static server (`python3 -m http.server`).
- **Script Changes:** Run `python3 build_resume.py` (within `.venv`) to verify script correctness without raising syntax or runtime exceptions.
- **Aesthetic Standards:** Maintain modern, clean typography, intentional whitespace, smooth hover micro-animations, and bespoke developer styling. Avoid generic bootstrap templates.
