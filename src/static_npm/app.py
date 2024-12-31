import platform
from pathlib import Path

from appdirs import user_data_dir
from download import download

CACHE_DIR = Path(user_data_dir("static-npm", "zackees"))

BASE_URL = "https://github.com/zackees/static-npm/raw/refs/heads/main/npm"

BINARIES_22_12_0 = {
    "darwin": {
        "arm64": f"{BASE_URL}/node-v22.12.0-darwin-arm64.tar.gz",
        "x64": f"{BASE_URL}/node-v22.12.0-darwin-x64.tar.gz",
    },
    "linux": {
        "arm64": f"{BASE_URL}/node-v22.12.0-linux-arm64.tar.xz",
        "armv7l": f"{BASE_URL}/node-v22.12.0-linux-armv7l.tar.xz",
        "x64": f"{BASE_URL}/node-v22.12.0-linux-x64.tar.xz",
    },
    "windows": {
        "x64": f"{BASE_URL}/node-v22.12.0-win-x64.zip",
    },
}

VERSION_BINARIES = {
    "22.12.0": BINARIES_22_12_0,
}


def get_bin_url(version: str, platform: str, arch: str) -> str:
    return VERSION_BINARIES[version][platform][arch]


def get_default(version: str) -> str:
    """Gets the binary URL for the current platform and architecture.

    Args:
        version: The node version to get (e.g. "22.12.0")

    Returns:
        The URL for the appropriate binary

    Raises:
        KeyError: If the platform/architecture combination is not supported
    """
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Map system names to our platform keys
    if system == "darwin":
        platform_key = "darwin"
    elif system == "linux":
        platform_key = "linux"
    elif system == "windows":
        platform_key = "windows"
    else:
        raise KeyError(f"Unsupported platform: {system}")

    # Map CPU architectures to our arch keys
    if machine in ("x86_64", "amd64"):
        arch_key = "x64"
    elif machine == "arm64":
        arch_key = "arm64"
    elif machine == "armv7l":
        arch_key = "armv7l"
    else:
        raise KeyError(f"Unsupported architecture: {machine}")

    return get_bin_url(version, platform_key, arch_key)


def download_windows_binary():
    print("Downloading Windows binary...")
    src = get_default("22.12.0")
    name = Path(src).name
    dst = CACHE_DIR / name
    print(f"dst: {dst}")
    download(src, str(dst))
    print("Download complete.")


if __name__ == "__main__":
    download_windows_binary()
