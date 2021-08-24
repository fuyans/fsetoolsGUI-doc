# -*- coding: utf-8 -*-
import os
import datetime

# Minimum version, enforced by sphinx
needs_sphinx = '3.2.0'

# -- Project information -----------------------------------------------------

project = 'SFEPRAPY'
author = 'Yan Fu'
copyright = f'2017-{datetime.datetime.now().strftime("%Y")}, {author}'
version = '0.8.1'
# release = '1'
language = 'en'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "numpydoc",
    "recommonmark",
    "jupyter_sphinx",
    "nbsphinx",
    "sphinx.ext.mathjax"
]

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_sidebars = {
    "contributing": ["search-field", "custom-template"],
    "changelog": [],
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = os.path.join('_static', 'sfeprapy-logo.png')
html_favicon = os.path.join('_static', 'logo_1_32x32.ico')

html_theme_options = {
    "logo_link": "index",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/fsepy/sfeprapy",
            "icon": "fab fa-github-square",
        },
    ],
    "favicons": [
        {
            "rel": os.path.join('logo_1_16x16.ico'),
            "sizes": "16x16",
            "href": os.path.join('logo_1_16x16.ico'),
        },
        {
            "rel": os.path.join('logo_1_32x32.ico'),
            "sizes": "32x32",
            "href": os.path.join('logo_1_32x32.ico'),
        },
    ],
    "collapse_navigation": True,
    "navigation_depth": 2,
    "show_prev_next": True,
    "use_edit_page_button": True,
    "navbar_end": ["navbar-icon-links.html", "search-field.html"],
    "search_bar_text": "Search documentation ...",
    "show_toc_level": 1,
}

html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise interprise
    "github_user": "fuyans",
    "github_repo": "sfeprapy-doc",
    "github_version": "dev",
    "doc_path": "source/",
}
