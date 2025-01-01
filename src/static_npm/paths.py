from pathlib import Path

from appdirs import user_data_dir

CACHE_DIR = Path(user_data_dir("static-npm", "zackees"))
