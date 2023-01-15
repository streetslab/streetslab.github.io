"""Sphinx build configuration.

For more details: https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Project information ---------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Streets Lab"

author = "Aaron Streets"
copyright = f"2023, {author}"

# -- General configuration -------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "myst_parser",
    "sphinx_immaterial",
    "sphinx_design",
]

myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "amsmath",
]

# -- Options for HTML output -----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_immaterial"
html_title = "Streets Lab"
html_logo = None
html_theme_options = {
    "repo_name": "Streets Lab",
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "black",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            }
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "black",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            }
        },
    ],
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        "navigation.sections",
        "navigation.top",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
    ],
    "toc_title_is_page_title": True,
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

# -- Options for Autodoc --------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

autodoc_member_order = "bysource"
autodoc_preserve_defaults = True

# Keep the type hints outside the function signature, and nudge toward adding
# descriptions for all type annotated arguments.
autodoc_typehints = "description"

# Don't show the class signature with the class name.
autodoc_class_signature = "separated"

# -- Options for intersphinx ----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# -- Options for TODOs -------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True
