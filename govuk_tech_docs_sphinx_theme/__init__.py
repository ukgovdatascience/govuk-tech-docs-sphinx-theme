import os


def setup(app):
    app.add_html_theme("govuk_tech_docs_sphinx_theme", os.path.abspath(os.path.dirname(__file__)))
