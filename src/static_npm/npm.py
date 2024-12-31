import os
from pathlib import Path

from static_npm.ensure_npm_exists import LATEST, Binaries, ensure_npm_exists
from static_npm.running_process import RunningProcess


class Npm:
    def __init__(self, version: str = LATEST):
        self._binaries: Binaries | None = None
        self.version = version

    @property
    def binaries(self) -> Binaries:
        if self._binaries is None:
            self._binaries = ensure_npm_exists(self.version)
        return self._binaries

    @property
    def path(self) -> Path:
        return Path(self.binaries.npm)

    def run(self, cmd_list: list[str], echo=True) -> RunningProcess:
        npm_path = self.binaries.npm
        cmd_list = [str(npm_path)] + cmd_list
        proc = RunningProcess(cmd_list, echo=echo)
        return proc

    def run_tool(
        self, tool_name: str, cmd_list: list[str] | None = None, echo=True
    ) -> RunningProcess:
        cmd_list = cmd_list or []

        start_path = self.binaries.npm.parent

        # walk path to find tool

        # os.walk
        tool_path: Path | None = None
        file_founds: list[str] = []

        for root, _, files in os.walk(start_path):
            if tool_name in files:
                file_founds.append(root)
                tool_path = Path(root) / tool_name
                break

        if tool_path is None:
            print("File not found in path")
            print("Files found:")
            for file_found in file_founds:
                print(file_found)
            raise FileNotFoundError(f"Could not find {tool_name} in {start_path}")

        print(f"Tool path: {tool_path}")
        if not tool_path.exists():
            path = self.binaries.npm.parent
            tool_path = path / tool_name
            if not tool_path.exists():
                raise FileNotFoundError(
                    f"Could not find {tool_name} in {self.binaries.npm} or {path}"
                )
        cmd_list = [str(tool_path)] + cmd_list
        proc = RunningProcess(cmd_list, echo=echo)
        return proc
