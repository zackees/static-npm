"""
Unit test file.
"""

import unittest

from static_npm.npm import Npm
from static_npm.npx import Npx


class MainTester(unittest.TestCase):
    """Main tester class."""

    def test_imports(self) -> None:
        """Test command line interface (CLI)."""
        npm = Npm()
        npx = Npx()
        npm.run(["install", "live-server"])
        proc = npx.run(["live-server", "--version"])
        rtn = proc.wait()
        stdout = proc.stdout
        self.assertEqual(0, rtn)
        self.assertIn("live-server", stdout)


if __name__ == "__main__":
    unittest.main()
