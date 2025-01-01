"""
Unit test file.
"""

import time
import unittest
from pathlib import Path

import httpx  # type: ignore

from static_npm.npm_tool import NpmTool
from static_npm.paths import CACHE_DIR


def _get_tool_dir(tool: str) -> Path:
    return CACHE_DIR / tool


PORT = 8375


class MainTester(unittest.TestCase):
    """Main tester class."""

    def test_imports(self) -> None:
        """Test command line interface (CLI)."""
        live_server = NpmTool("live-server")
        live_server.install()
        proc = live_server.run([f"--port={PORT}", "--no-browser"])

        timeout = time.time() + 120
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
