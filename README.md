# PHYS 441 / PCSE 541: Modeling and Simulation

Course materials for PHYS 441 and PCSE 541 at Christopher Newport University,
Fall 2026.

## Start here

1. Follow the [development-environment setup](Documents/Development_Environment_Setup.md).
2. Create the course environment from [`environment.yml`](environment.yml). If you
   already have a Python 3.12 environment that you want to use, the pip-based
   [`scripts/install_environment.py`](scripts/install_environment.py) is an alternative.
3. Run `python scripts/verify_environment.py` with that environment active. The
   pip-based installer runs this verification automatically.
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

Two third-party reference collections are stored as Git submodules and are not needed
for the standard Week 1–14 notebooks. If an assignment asks you to use them, download
them from the repository root with:

```bash
git submodule update --init
```

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
