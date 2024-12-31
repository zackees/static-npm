"""
Unit test file.
"""

import unittest

from static_npm.npm import Npm


class MainTester(unittest.TestCase):
    """Main tester class."""

    def test_npm_run_version(self) -> None:
        """Test command line interface (CLI)."""
        npm = Npm()
        proc = npm.run(["--version"])
        rtn = proc.wait()
        self.assertEqual(0, rtn)
        self.assertEqual(npm.binaries.npm.exists(), True)


if __name__ == "__main__":
    unittest.main()
