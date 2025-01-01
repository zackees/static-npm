"""
Unit test file.
"""

from pathlib import Path

from static_npm.npm import Npm
from static_npm.npx import Npx
from static_npm.paths import CACHE_DIR
from static_npm.running_process import RunningProcess


def _get_tool_dir(tool: str) -> Path:
    return CACHE_DIR / tool


class NpmTool:
    """Installs a single use npm tool and allows you to run it."""

    def __init__(self, tool: str) -> None:
        self.tool = tool
        self.tool_dir = _get_tool_dir(tool)
        self.install_attempt = False

    def install(self) -> None:
        npm = Npm()
        self.tool_dir.mkdir(exist_ok=True, parents=True)
        npm.run(["install", self.tool, "--prefix", str(self.tool_dir)])
        self.install_attempt = True

    def run(self, args: list[str]) -> RunningProcess:
        if not self.install_attempt:
            self.install()
        npx = Npx()
        proc = npx.run(["--prefix", str(self.tool_dir), self.tool, *args])
        return proc
