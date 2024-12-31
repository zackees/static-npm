"""
Main entry point.
"""

import argparse

from static_npm.node import Node
from static_npm.npm import Npm
from static_npm.npx import Npx


def parse_args() -> tuple[argparse.Namespace, list[str]]:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="npm static binary")
    return parser.parse_known_args()


def run(prog: Npm | Npx | Node) -> int:
    """Main entry point for the template_python_cmd package."""
    _, unknown = parse_args()
    proc = prog.run(unknown)
    rtn = proc.wait()
    return rtn
