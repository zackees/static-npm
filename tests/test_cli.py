"""
Unit test file.
"""

import os
import unittest

COMMAND = "static-npm --version"


class MainTester(unittest.TestCase):
    """Main tester class."""

    def test_cli_tools(self) -> None:
        """Test command line interface (CLI)."""
        rtn = os.system("static-npm --version")
        self.assertEqual(0, rtn)
        rtn = os.system("static-npm --version")
        self.assertEqual(0, rtn)
        rtn = os.system("static-npm --version")
        self.assertEqual(0, rtn)
        rtn = os.system("static-npm-tool live-server --version")
        self.assertEqual(0, rtn)


if __name__ == "__main__":
    unittest.main()
