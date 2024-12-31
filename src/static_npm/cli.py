"""
Main entry point.
"""

import argparse
import sys

from static_npm.npm import Npm


def parse_args() -> tuple[argparse.Namespace, list[str]]:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="npm static binary")
    return parser.parse_known_args()


def main() -> int:
    """Main entry point for the template_python_cmd package."""
    _, unknown = parse_args()
    npm = Npm()
    proc = npm.run(unknown)
    rtn = proc.wait()
    return rtn


if __name__ == "__main__":
    sys.exit(main())
