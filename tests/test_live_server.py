"""
Unit test file.
"""

import unittest

from static_npm.npm import Npm


class MainTester(unittest.TestCase):
    """Main tester class."""

    def test_imports(self) -> None:
        """Test command line interface (CLI)."""
        npm = Npm()
        npm.run(["install", "-g", "live-server"])
        proc = npm.run_tool("live-server", ["--version"])
        rtn, stdout = proc.wait(), proc.stdout
        self.assertEqual(0, rtn)
        self.assertIn("live-server", stdout)


if __name__ == "__main__":
    unittest.main()
