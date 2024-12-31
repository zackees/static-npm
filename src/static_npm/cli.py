"""
Main entry point.
"""

import argparse

from static_npm.node import Node
from static_npm.npm import Npm
from static_npm.npx import Npx
from static_npm.prog_exec import run


def parse_args() -> tuple[argparse.Namespace, list[str]]:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="npm static binary")
    return parser.parse_known_args()


def main_npm() -> int:
    """Main entry point for the template_python_cmd package."""
    return run(Npm())


def main_node() -> int:
    return run(Node())


def main_npx() -> int:
    return run(Npx())


def npm_tool() -> tuple[int, str]:
    """Main entry point for the template_python_cmd package."""
    parser = argparse.ArgumentParser(description="npm static binary")
    parser.add_argument("tool", help="Tool to run")
    parser.add_argument("--echo", action="store_true", help="Echo command")
    args, other_args = parser.parse_known_args()
    npm = Npm()
    proc = npm.run_tool(args.tool, other_args, echo=args.echo)
    rtn = proc.wait()
    return rtn, proc.stdout
