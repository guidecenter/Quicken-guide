# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'How to Login to Your Quicken Account?'
copyright = '2025, Download Quicken Now'
author = 'Download Quicken Now'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Use a clean, readable theme
html_theme = 'alabaster'  # You can switch to 'sphinx_rtd_theme' if installed

# Title shown in the browser tab and on top of HTML pages
html_title = "How to Login to Your Quicken Account?"

# Shorter version of the title (optional)
html_short_title = "Login to Quicken"

# Favicon file (optional — place favicon.ico in _static/)
html_favicon = 'favicon.ico'

# Static files like CSS, JS, images
html_static_path = ['_static']

# Allow raw HTML in .rst files
raw_enabled = True
html_allow_unsafe = True

# Hide "View page source" link
html_show_sourcelink = False

# Theme-specific options
html_theme_options = {
    'show_powered_by': False,
    'sidebar_width': '220px',
    'page_width': '1020px',
    'font_family': 'Georgia, serif',
}

# -- Custom CSS (optional) ---------------------------------------------------
# Uncomment and create _static/custom.css to style your docs
# html_css_files = [
#     'custom.css',
# ]
