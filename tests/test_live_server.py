"""
Unit test file.
"""

import unittest
from pathlib import Path

from static_npm.npm import Npm
from static_npm.npx import Npx
from static_npm.paths import CACHE_DIR


def _get_tool_dir(tool: str) -> Path:
    return CACHE_DIR / tool


class MainTester(unittest.TestCase):
    """Main tester class."""

    def test_imports(self) -> None:
        """Test command line interface (CLI)."""
        npm = Npm()
        npx = Npx()
        tool_dir = _get_tool_dir("live-server")
        npm.run(["install", "live-server", "--prefix", str(tool_dir)])
        proc = npx.run(["live-server", "--version", "--prefix", str(tool_dir)])
        rtn = proc.wait()
        stdout = proc.stdout
        self.assertEqual(0, rtn)
        self.assertIn("live-server", stdout)


if __name__ == "__main__":
    unittest.main()
