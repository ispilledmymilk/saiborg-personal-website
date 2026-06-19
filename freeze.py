"""Generate a static build of the portfolio for GitHub Pages."""

import os
from pathlib import Path

from flask_frozen import Freezer

from app import app

BASE_URL = os.environ.get(
    "FREEZER_BASE_URL",
    "https://ispilledmymilk.github.io/saiborg-personal-website",
)

build_dir = Path(__file__).resolve().parent / "build"

app.config["FREEZER_DESTINATION"] = str(build_dir)
app.config["FREEZER_BASE_URL"] = BASE_URL
app.config["FREEZER_IGNORE_MIMETYPE_WARNINGS"] = True

os.environ.setdefault("URL", BASE_URL.replace("https://", ""))

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
