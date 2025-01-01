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
from pathlib import Path
from static_npm.npm import Npm
from static_npm.npx import Npx
from static_npm.paths import CACHE_DIR

def _get_tool_dir(tool: str) -> Path:
    return CACHE_DIR / tool

npm = Npm()
npx = Npx()
tool_dir = _get_tool_dir("live-server")
npm.run(["install", "live-server", "--prefix", str(tool_dir)])
proc = npx.run(["live-server", "--version", "--prefix", str(tool_dir)])
rtn = proc.wait()
stdout = proc.stdout
assert 0 == rtn
assert "live-server" in stdout
```


# Examples

```python
        npm = Npm()
        npx = Npx()
        tool_dir = _get_tool_dir("live-server")
        npm.run(["install", "live-server", "--prefix", str(tool_dir)])
        proc = npx.run(["live-server", "--version", "--prefix", str(tool_dir)])
        rtn = proc.wait()
        stdout = proc.stdout
        self.assertEqual(0, rtn)
        self.assertIn("live-server", stdout)
```

To develop software, run `. ./activate.sh`

# Windows

This environment requires you to use `git-bash`.

# Linting

Run `./lint.sh` to find linting errors using `pylint`, `flake8` and `mypy`.


