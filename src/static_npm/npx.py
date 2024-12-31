from static_npm.ensure_npm_exists import LATEST, Binaries, ensure_npm_exists
from static_npm.running_process import RunningProcess


class Npx:
    def __init__(self, version: str = LATEST):
        self._binaries: Binaries | None = None
        self.version = version

    @property
    def binaries(self) -> Binaries:
        if self._binaries is None:
            self._binaries = ensure_npm_exists(self.version)
        return self._binaries

    @property
    def path(self) -> str:
        return str(self.binaries.npx)

    def run(self, cmd_list: list[str], echo=True) -> RunningProcess:
        npx_path = self.binaries.npx
        cmd_list = [str(npx_path)] + cmd_list
        proc = RunningProcess(cmd_list, echo=echo)
        return proc
