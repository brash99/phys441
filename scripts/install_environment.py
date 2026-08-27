"""Install the Python packages required by the current course notebooks.

Run this script with the Python interpreter that should own the packages::

    python scripts/install_environment.py

The Conda environment in ``environment.yml`` remains the preferred setup. This
installer is a pip-based alternative for an existing Python 3.12 environment.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


# Keep these compatible-release ranges synchronized with environment.yml.
# The upper bounds prevent pip from silently combining packages from different
# release series, as happened with SciPy 1.15 and NumPy 2.5.
REQUIRED_DISTRIBUTIONS = (
    "numpy>=2.2,<2.3",
    "scipy>=1.15,<1.16",
    "matplotlib>=3.10,<3.11",
    "pandas>=2.2,<2.3",
    "lxml>=5.3,<5.4",
    "sympy>=1.13,<1.14",
    "statsmodels>=0.14,<0.15",
    "scikit-learn>=1.6,<1.7",
    "astropy>=7.0,<7.1",
    "ipywidgets>=8.1,<8.2",
    "tqdm>=4.67,<4.68",
    "jupyterlab>=4.3,<4.4",
    "notebook>=7.3,<7.4",
    "ipykernel>=6.29,<6.30",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show what would be installed without changing the environment",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if sys.version_info[:2] != (3, 12):
        print(
            "This course environment requires Python 3.12; "
            f"the active interpreter is Python {sys.version_info.major}."
            f"{sys.version_info.minor} ({sys.executable}).",
            file=sys.stderr,
        )
        return 2

    command = [
        sys.executable,
        "-m",
        "pip",
        "install",
        *REQUIRED_DISTRIBUTIONS,
    ]

    print(f"Using Python {sys.version.split()[0]} at {sys.executable}")
    if args.dry_run:
        print("Would install the following compatible package ranges:")
        for requirement in REQUIRED_DISTRIBUTIONS:
            print(f"  {requirement}")
        return 0

    install = subprocess.run(command, check=False)
    if install.returncode != 0:
        print("\nPackage installation failed; see the pip output above.", file=sys.stderr)
        return install.returncode

    verifier = Path(__file__).with_name("verify_environment.py")
    print("\nInstallation finished; verifying the resulting environment...")
    return subprocess.run([sys.executable, str(verifier)], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
