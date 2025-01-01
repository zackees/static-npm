"""
Main entry point.
"""

import argparse

from static_npm.node import Node
from static_npm.npm import Npm
from static_npm.npm_tool import NpmTool
from static_npm.npx import Npx
from static_npm.prog_exec import run


def parse_args() -> tuple[argparse.Namespace, list[str]]:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="npm static binary")
    return parser.parse_known_args()


def main_npm() -> int:
    """Main entry point for the template_python_cmd package."""
    try:
        return run(Npm())
    except KeyboardInterrupt:
        return 1


def main_node() -> int:
    try:
        return run(Node())
    except KeyboardInterrupt:
        return 1


def main_npx() -> int:
    try:
        return run(Npx())
    except KeyboardInterrupt:
        return 1


def main_npm_tool() -> int:
    _, args = parse_args()
    try:
        proc = NpmTool(args[0]).run(args[1:])
        return proc.wait()
    except KeyboardInterrupt:
        return 1
