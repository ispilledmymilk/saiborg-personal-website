import os

from flask import Flask, render_template
from dotenv import load_dotenv

from app.data import (
    ABOUT,
    EDUCATION,
    EXPERIENCES,
    HOBBIES,
    PAGES,
    PROFILE,
    PROJECTS,
    TRAVEL_LOCATIONS,
)

load_dotenv()
app = Flask(__name__)


def _context(**extra):
    """Shared template context for every page."""
    return {
        "profile": PROFILE,
        "pages": PAGES,
        "url": os.getenv("URL", "localhost:5000"),
        **extra,
    }


@app.route("/")
def index():
    return render_template(
        "index.html",
        title=f"{PROFILE['name']} · Portfolio",
        about=ABOUT,
        experiences=EXPERIENCES,
        education=EDUCATION,
        **_context(),
    )


@app.route("/hobbies")
def hobbies():
    return render_template(
        "hobbies.html",
        title=f"Hobbies · {PROFILE['name']}",
        hobbies=HOBBIES,
        **_context(),
    )


@app.route("/projects")
def projects():
    return render_template(
        "projects.html",
        title=f"Projects · {PROFILE['name']}",
        projects=PROJECTS,
        **_context(),
    )


@app.route("/travel")
def travel():
    return render_template(
        "travel.html",
        title=f"Travel Map · {PROFILE['name']}",
        locations=TRAVEL_LOCATIONS,
        **_context(),
    )
