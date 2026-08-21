# PHYS 441/541: Modeling and Simulation

Course materials for PHYS 441 and PHYS 541 at Christopher Newport University,
Fall 2026.

## Start here

1. Follow the [development-environment setup](Documents/Development_Environment_Setup.md).
2. Create the course environment from [`environment.yml`](environment.yml).
3. Run `python scripts/verify_environment.py` with that environment active.
4. Begin with the notebooks in [`JupyterNotebooks/Week1`](JupyterNotebooks/Week1).

## Repository map

- `Documents/`: current syllabi and student-facing course documents
- `Assignments/`: assignment handouts and the final-project rubric
- `JupyterNotebooks/Week*`: the current sequence of course notebooks
- `JupyterNotebooks/`: additional examples and reference material
- `environment.yml`: the shared Python environment for current course notebooks

The repository also contains older examples and third-party reference material. Unless
an assignment says otherwise, use the numbered `Week*` directories as the current
course sequence.

## Keeping your copy current

If you cloned this repository directly, update it from the repository root with:

```bash
git pull --ff-only
conda env update --file environment.yml --prune
```

Activate the environment again after updating:

```bash
conda activate phys441
```

Do not put passwords, access tokens, API keys, or other credentials in notebook cells,
Git remote URLs, or committed files.
