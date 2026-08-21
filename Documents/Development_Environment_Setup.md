# Development environment setup

These instructions create one consistent Python environment for PHYS 441/541. Do
this before working on the Week 1 notebooks. Commands shown below work in a terminal
on macOS, Windows, and Linux unless a step says otherwise.

## 1. Install Git and Conda

Install:

- [Git](https://git-scm.com/downloads)
- [Miniforge](https://conda-forge.org/download/), the small Conda installer used for
  the course environment

After installing Miniforge, close and reopen your terminal. Check both programs:

```bash
git --version
conda --version
```

If `conda` is not found, use the Miniforge Prompt on Windows or follow the shell
initialization guidance shown by the installer.

## 2. Clone the course repository

In a terminal, move to the directory where you keep course work and run:

```bash
git clone https://github.com/brash99/phys441.git
cd phys441
```

The course repository is public, so cloning and pulling do not require a GitHub
credential. If GitHub authentication is needed for your own private repository,
use a browser-based sign-in through [GitHub CLI or Git Credential
Manager](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git).
Never place a personal access token in a clone URL or save one in this repository.

## 3. Create the course environment

From the repository root, run:

```bash
conda env create --file environment.yml
conda activate phys441
python scripts/verify_environment.py
```

The final command should report that all checks passed. The environment includes the
packages imported by the current Week 1–14 notebooks. Names such as `modsim`,
`P201_Functions`, `rk_functions`, `Sun`, and `ga` are course files stored beside the
notebooks, not packages to install from the internet.

To incorporate a later course update:

```bash
git pull --ff-only
conda env update --file environment.yml --prune
```

## 4. Run notebooks

The simplest option is JupyterLab:

```bash
conda activate phys441
jupyter lab
```

Your browser will open the notebook interface. Navigate to the appropriate directory
under `JupyterNotebooks/` and choose the `phys441` kernel if prompted. Stop the server
with `Ctrl+C` in the terminal.

## 5. Optional: use PyCharm

PyCharm is optional. Open the cloned `phys441` directory as an existing project, then
configure its Python interpreter as the existing Conda environment named `phys441`.
PyCharm can run local notebook cells using that interpreter; it is not necessary to
create a second environment.

JetBrains documents both [selecting an existing Conda
interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
and [working with Jupyter notebooks](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html).

## Troubleshooting

- **`conda: command not found`:** restart the terminal or use the Miniforge Prompt.
- **The `phys441` kernel is missing:** activate the environment and run
  `python -m ipykernel install --user --name phys441 --display-name "Python (phys441)"`.
- **A notebook cannot find a course-local module:** launch Jupyter from the repository
  root and run the notebook in its original directory.
- **Environment creation fails:** copy the complete error message before changing or
  installing packages manually; it identifies the operating-system or solver issue.
