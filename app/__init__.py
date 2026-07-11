import datetime
import os

from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

from app.data import (
    ABOUT,
    BANNER_MESSAGES,
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

mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])


def _context(**extra):
    """Shared template context for every page."""
    return {
        "profile": PROFILE,
        "pages": PAGES,
        "banner_messages": BANNER_MESSAGES,
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


@app.route("/hobbies/")
def hobbies():
    return render_template(
        "hobbies.html",
        title=f"Hobbies · {PROFILE['name']}",
        hobbies=HOBBIES,
        **_context(),
    )


@app.route("/projects/")
def projects():
    return render_template(
        "projects.html",
        title=f"Projects · {PROFILE['name']}",
        projects=PROJECTS,
        **_context(),
    )


@app.route("/travel/")
def travel():
    return render_template(
        "travel.html",
        title=f"Travel Map · {PROFILE['name']}",
        locations=TRAVEL_LOCATIONS,
        **_context(),
    )


@app.route("/timeline/")
def timeline():
    return render_template(
        "timeline.html",
        title="Timeline",
        **_context(),
    )


@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form["name"]
    email = request.form["email"]
    content = request.form["content"]
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/api/timeline_post/<int:post_id>", methods=["DELETE"])
def delete_time_line_post(post_id):
    post = TimelinePost.get_by_id(post_id)
    post.delete_instance()
    return {"message": f"Timeline post {post_id} deleted"}
