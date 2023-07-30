from flask import Flask, Blueprint, render_template, url_for
from . import character


main = Blueprint("main", __name__)


def create_app() -> Flask:
    app = Flask(__package__)
    app.register_blueprint(main)
    return app


@main.route("/")
def index() -> str:
    return render_template("index.html", content="Welcome")


@main.route("/stuff")
def stuff() -> str:
    filename = character.get_character_image_filename(
        "0", "headcircle", "faceneutral", "hairnancy", "hatwinter"
    )
    filename = url_for("static", filename=f"img/character/{filename}")
    desc = "this character"
    return f"<div><img src='{filename}' alt='{desc}'></div>"
