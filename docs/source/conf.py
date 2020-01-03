# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import re
# -- Project information -----------------------------------------------------
master_doc = 'index'
project = u'Data Science and Machine Learning basic course with Python'
slug = re.sub(r'\W+', '-', project.lower())
copyright = u'2020, Volodymyr Kovenko, Vitalii Shevchuk'
author = u'Volodymyr Kovenko, Vitalii Shevchuk'

# The full version, including alpha/beta/rc tags
release = '0.0.3'

pygments_style = 'sphinx'
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel',             
'sphinxmark',
'nbsphinx',
'sphinx.ext.mathjax',
'sphinx.ext.imgmath',
'sphinx.ext.mathbase']
sphinxmark_enable = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_title = 'DS/ML course'
html_logo = "logo/logo.png"
html_theme_options = {
    'logo_only': True
}
htmlhelp_basename = slug

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
