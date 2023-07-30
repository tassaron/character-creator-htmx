# Character Creator using htmx

A little example app created to try out [htmx](https://htmx.org/docs/). Create a character image using a few attributes like hair, body shape, and facial expression. Also generate some basic D&D character details using my library [dnd-character](https://github.com/tassaron/dnd-character)

## Installation on Ubuntu Server 22.04

1. Create a virtual env, activate it.
  `sudo apt install python3-venv; python3 -m venv env; source env/bin/activate`
1. Install this package: `pip install .`
1. [Download htmx.min.js](https://htmx.org/docs/#download-a-copy) and move it to `/api/static/js`
1. Use `FLASK_APP=api.run flask run` for Flask's built-in local development server.
1. Use the `uwsgi.sh` shell script to run a development uWSGI server (connect to `0.0.0.0:5000`).
1. See the [readme inside `/install`](install/README.md) for help with setting up a production server.

## Upgrading

1. Stop running server
1. `git pull` the new code
1. Activate the venv and `pip install .`

## Inkscape SVGs

`character.svg` is an Inkscape SVG with layers. I toggle the visibility of layers and export to PNGs which go into `app/static/img/character` for use in the actual app.

## Development stuff

- use `black` for auto-formatting of code
- use `pytest` to run test suite
- use `mypy --strict api` for fun
