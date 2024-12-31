from pathlib import Path

from static_npm.ensure_npm_exists import LATEST, Binaries, ensure_npm_exists
from static_npm.running_process import RunningProcess


class Node:
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
        node_path = self.binaries.node
        cmd_list = [str(node_path)] + cmd_list
        proc = RunningProcess(cmd_list, echo=echo)
        return proc
