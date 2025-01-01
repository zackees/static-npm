"""
Unit test file.
"""

import time
import unittest
from pathlib import Path

import httpx  # type: ignore

from static_npm.npm import Npm
from static_npm.npx import Npx
from static_npm.paths import CACHE_DIR


def _get_tool_dir(tool: str) -> Path:
    return CACHE_DIR / tool


PORT = 8375


class MainTester(unittest.TestCase):
    """Main tester class."""

    def test_imports(self) -> None:
        """Test command line interface (CLI)."""
        npm = Npm()
        npx = Npx()
        tool_dir = _get_tool_dir("live-server")
        npm.run(["install", "live-server", "--prefix", str(tool_dir)])
        proc = npx.run(
            ["--prefix", str(tool_dir), "live-server", f"--port={PORT}", "--no-browser"]
        )

        timeout = time.time() + 60
        while time.time() < timeout:
            try:
                response = httpx.get(f"http://localhost:{PORT}")
                if response.status_code == 200:
                    break
            except httpx.ConnectError:
                pass
            time.sleep(1)
        else:
            self.fail("Server did not start.")

        proc.terminate()


if __name__ == "__main__":
    unittest.main()
