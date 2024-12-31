import subprocess

from static_npm.ensure_npm_exists import Binaries, ensure_npm_exists
from static_npm.running_process import RunningProcess


class Npm:
    def __init__(self):
        self._binaries: Binaries | None = None

    @property
    def binaries(self) -> Binaries:
        if self._binaries is None:
            self._binaries = ensure_npm_exists()
        return self._binaries

    def run(self, cmd_list: list[str]) -> RunningProcess:
        npm_path = self.binaries.npm
        cmd_list = [str(npm_path)] + cmd_list
        cmd_str = subprocess.list2cmdline(cmd_list)
        print(f"Running: {cmd_str}")
        # subprocess.call(cmd_list, shell=True)
        proc = RunningProcess(cmd_str)
        return proc


if __name__ == "__main__":
    ensure_npm_exists()
