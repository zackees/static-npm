from pathlib import Path

from appdirs import user_data_dir
from download import download

CACHE_DIR = Path(user_data_dir("static-npm", "zackees"))


WINDOWS_BINARY = "https://github.com/zackees/static-npm/raw/refs/heads/main/npm/node-v22.12.0-win-x64.zip"


def download_windows_binary():
    print("Downloading Windows binary...")
    dst = CACHE_DIR / "node-v22.12.0-win-x64.zip"
    download(WINDOWS_BINARY, str(dst))
    print("Download complete.")


if __name__ == "__main__":
    download_windows_binary()
