"""Sphinx configuration."""
project = "Arneso Poetry Publish Test"
author = "Arne Sørli"
copyright = "2022, Arne Sørli"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
