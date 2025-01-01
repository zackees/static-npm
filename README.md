# static-npm

Downloads and runs `npm`, `npx` and `node` through static binary downloads.

[![Linting](https://github.com/zackees/static-npm/actions/workflows/lint.yml/badge.svg)](https://github.com/zackees/static-npm/actions/workflows/lint.yml)
[![MacOS_Tests](https://github.com/zackees/static-npm/actions/workflows/test_macos.yml/badge.svg)](https://github.com/zackees/static-npm/actions/workflows/test_macos.yml)
[![Ubuntu_Tests](https://github.com/zackees/static-npm/actions/workflows/test_ubuntu.yml/badge.svg)](https://github.com/zackees/static-npm/actions/workflows/test_ubuntu.yml)
[![Win_Tests](https://github.com/zackees/static-npm/actions/workflows/test_win.yml/badge.svg)](https://github.com/zackees/static-npm/actions/workflows/test_win.yml)

# Install

`pip install static-npm`

# Cmds

```bash
# Get the versions of all tools
static-npm --version
static-node --version
static-npx --version

# Install live-server
static-npm install -g live-server
```

# Api

```python
from static_npm import Npm, Node, Npx
npm = Npm()
print(f"npm path: {npm.path}")
proc = npm.run(["--version"])
proc.wait()
assert "10.9.0" in proc.stdout
```


# Examples

```python
import unittest
from static_npm.npm import Npm

class MainTester(unittest.TestCase):
    """Main tester class."""

    def test_npm_run_version(self) -> None:
        """Test command line interface (CLI)."""
        npm = Npm()
        proc = npm.run(["--version"])
        rtn = proc.wait()
        version = proc.stdout
        print(f"Version: {version}")
        self.assertIn("10.9.0", version)
        self.assertEqual(0, rtn)
        self.assertEqual(npm.binaries.npm.exists(), True)


if __name__ == "__main__":
    unittest.main()
```

To develop software, run `. ./activate.sh`

# Windows

This environment requires you to use `git-bash`.

# Linting

Run `./lint.sh` to find linting errors using `pylint`, `flake8` and `mypy`.


