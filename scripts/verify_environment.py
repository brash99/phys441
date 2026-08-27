"""Smoke-test the Python packages required by the current course notebooks."""

from __future__ import annotations

import importlib
import platform
import subprocess
import sys


REQUIRED_MODULES = (
    "astropy",
    "ipywidgets",
    "lxml",
    "matplotlib",
    "numpy",
    "pandas",
    "scipy",
    "sklearn",
    "statsmodels",
    "sympy",
    "tqdm",
)


def main() -> int:
    print(f"Python {platform.python_version()} ({sys.executable})")
    failures: list[str] = []

    for module_name in REQUIRED_MODULES:
        try:
            module = importlib.import_module(module_name)
        except Exception as exc:  # report broken binary installs as well as missing ones
            failures.append(f"{module_name}: {type(exc).__name__}: {exc}")
            continue

        version = getattr(module, "__version__", "version unavailable")
        print(f"[import ok] {module_name} {version}")

    # Importing a package is not sufficient evidence that the environment is
    # consistent. For example, SciPy can import while warning that the installed
    # NumPy version lies outside its supported range. ``pip check`` evaluates the
    # dependency metadata for every installed distribution and catches that case.
    dependency_check = subprocess.run(
        [sys.executable, "-m", "pip", "check"],
        capture_output=True,
        text=True,
        check=False,
    )
    if dependency_check.returncode == 0:
        print("[ok] installed package requirements are mutually compatible")
    else:
        details = "\n".join(
            part.strip()
            for part in (dependency_check.stdout, dependency_check.stderr)
            if part.strip()
        )
        failures.append(f"dependency compatibility:\n{details}")

    if failures:
        print("\nEnvironment verification failed:", file=sys.stderr)
        for failure in failures:
            print(f"[error] {failure}", file=sys.stderr)
        return 1

    print("\nAll PHYS 441/541 environment checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
