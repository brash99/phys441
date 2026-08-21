"""Smoke-test the Python packages required by the current course notebooks."""

from __future__ import annotations

import importlib
import platform
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
        print(f"[ok] {module_name} {version}")

    if failures:
        print("\nEnvironment verification failed:", file=sys.stderr)
        for failure in failures:
            print(f"[error] {failure}", file=sys.stderr)
        return 1

    print("\nAll PHYS 441/541 environment checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
