from flask import Flask, Blueprint, render_template, url_for, request
from dnd_character import Character, CLASSES
from . import character


main = Blueprint("main", __name__)


def create_app() -> Flask:
    app = Flask(__package__)
    app.register_blueprint(main)
    return app


@main.route("/")
def index() -> str:
    return render_template("index.html")


@main.route("/data", methods=["POST"])
def get_data() -> str:
    return render_template(
        "data.html",
        character_data=dict(
            Character(
                name=str(request.form["name"]),
                level=int(request.form["level"]),
                classs=CLASSES[str(request.form["class"])],
            )
        ),
    )


@main.route("/image")
def get_image() -> str:
    filename = character.get_character_image_filename(
        "0", "headcircle", "faceneutral", "hairnancy", "hatwinter"
    )
    filename = url_for("static", filename=f"img/character/{filename}")
    desc = "this character"
    return f"<div><img src='{filename}' alt='{desc}'></div>"
