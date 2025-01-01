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

    def global_bin_path(self) -> Path:
        return Path(self.run(["root", "-g"]).stdout.strip())

    def global_prefix_path(self) -> Path:
        return Path(self.run(["prefix", "-g"]).stdout.strip())

    def run(self, cmd_list: list[str], echo=True) -> RunningProcess:
        npm_path = self.binaries.npm
        cmd_list = [str(npm_path)] + cmd_list
        proc = RunningProcess(cmd_list, echo=echo)
        return proc

    def run_tool(
        self, tool_name: str, cmd_list: list[str] | None = None, echo=True
    ) -> RunningProcess:
        cmd_list = cmd_list or []
        global_path = self.global_prefix_path()
        print(f"Global path: {global_path}")
        tool_path: Path = global_path / tool_name
        if not tool_path.exists():
            raise FileNotFoundError(f"Could not find {tool_name} in {global_path}")
        cmd_list = [str(tool_path)] + cmd_list
        proc = RunningProcess(cmd_list, echo=echo)
        return proc
