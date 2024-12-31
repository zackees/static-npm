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
        tool_path = self.binaries.npm.parent / "node_modules" / ".bin" / tool_name
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
