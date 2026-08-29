# Copilot instructions for phys441

This repository holds course materials (Jupyter notebooks, scripts, and reference
documents) for PHYS 441 / PCSE 541 (Modeling and Simulation) at Christopher Newport
University. It is not a software library or application — there is no build, no
package to publish, and no application test suite.

## Environment setup and verification

- The canonical environment is defined in `environment.yml` (Conda, `python=3.12`,
  pinned scientific-Python stack: numpy 2.2, scipy 1.15, matplotlib 3.10, pandas 2.2,
  etc.). Create/update it with:
  ```bash
  conda env create --file environment.yml
  conda activate phys441
  ```
- `scripts/install_environment.py` is a pip-based alternative for people who already
  have a Python 3.12 environment. Its `REQUIRED_DISTRIBUTIONS` version ranges must
  stay synchronized with `environment.yml` — if you bump a package version in one,
  update the other.
- `scripts/verify_environment.py` is the closest thing to a test suite: it imports
  every required module and runs `pip check` to catch dependency-compatibility
  issues. Run it after any environment change:
  ```bash
  python scripts/verify_environment.py
  ```
  There is no per-module/single-test invocation — it always checks the full
  `REQUIRED_MODULES` list.

## Repository layout

- `JupyterNotebooks/Week1` … `Week14` (some combined as `Week7and8`, `Week9and10`):
  the current, numbered course sequence. **Unless an assignment says otherwise, this
  is the material to use/update** — treat it as the "current" content.
- `JupyterNotebooks/` also contains older, non-numbered subject folders (e.g. `CFD`,
  `Fitting`, `DataScience`, `General`) that are historical/reference examples, not
  part of the active course sequence.
- `JupyterNotebooks/CFD/CFDPython` and `JupyterNotebooks/Week12/genetic-algorithms`
  are third-party Git submodules (see `.gitmodules`), not needed for the standard
  Week 1–14 notebooks. Fetch them explicitly only if an assignment requires it:
  ```bash
  git submodule update --init
  ```
- `Documents/`: current syllabi and student-facing setup docs (see
  `Documents/Development_Environment_Setup.md` for the full onboarding walkthrough).
- `Assignments/`: assignment handouts and the final-project rubric (Word docs).
- `nmfp/`: a bundled third-party reference collection (C++/Fortran/Matlab numerical
  methods examples), unrelated to the Conda/Python environment above.

## Conventions specific to this repo

- Course notebooks import small same-directory helper modules by name (e.g.
  `modsim`, `P201_Functions`, `rk_functions`, `Sun`, `ga`). These are files stored
  beside the notebooks in the same week's folder, **not** pip/conda packages — don't
  try to install them, and when adding a notebook that needs one, place the helper
  `.py` file next to it.
- Never commit credentials, access tokens, or passwords in notebook cells, Git
  remote URLs, or any other file — this is called out explicitly in the README.
- Keep `environment.yml` and `scripts/install_environment.py` version pins in sync
  (see above) whenever a package version changes.
