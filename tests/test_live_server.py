"""
Unit test file.
"""

import unittest

from static_npm.cli import npm_tool
from static_npm.npm import Npm


class MainTester(unittest.TestCase):
    """Main tester class."""

    def test_imports(self) -> None:
        """Test command line interface (CLI)."""
        npm = Npm()
        npm.run(["install", "-g", "live-server"])
        rtn, stdout = npm_tool("live-server", ["--version"])
        self.assertEqual(0, rtn)
        print(stdout)

        print()


if __name__ == "__main__":
    unittest.main()
