import os
from flask import Flask, Blueprint, render_template, url_for, request
from dnd_character import Character, CLASSES, __version__
from . import character


try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


main = Blueprint("main", __name__)


class MyFlask(Flask):
    def add_url_rule(self, rule, *args, **kwargs):
        return super().add_url_rule(os.getenv("ROOT_DIR", "") + rule, *args, **kwargs)


def create_app() -> MyFlask:
    app = MyFlask(__package__)
    app.register_blueprint(main)
    return app


@main.route("/")
def index() -> str:
    return render_template("index.html", dep_version=__version__)


@main.route("/data", methods=["POST"])
def get_data() -> str:
    if request.form["class"]:
        classs = CLASSES[str(request.form["class"])]
    else:
        classs = None
    return render_template(
        "data.html",
        character_data=dict(
            Character(
                name=str(request.form["name"]),
                level=int(request.form["level"]),
                classs=classs,
            )
        ),
        dep_version=__version__,
    )


@main.route("/image", methods=["POST"])
def get_image() -> str:
    keys = ["body", "head", "face", "hair", "hat"]
    filename = character.get_character_image_filename(
        *[f"{key if key != 'body' else ''}{request.form[key]}" for key in keys]
    )
    filename = url_for("static", filename=f"img/character/{filename}")
    desc = "this character"
    return f"<div id='character-image'><img src='{filename}' alt='{desc}'></div>"
