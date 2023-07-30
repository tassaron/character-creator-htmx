from setuptools import setup, find_packages
from api.__init__ import __version__, __author__

setup(
    name="character-creator-htmx",
    version=__version__,
    author=__author__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "uwsgi",
        "flask",
        "python-dotenv",
        "dnd_character==23.7.29",
        "pillow",
    ],
)
