from functools import partial
from govuk_tech_docs_sphinx_theme.components.notification_banner import (
    NotificationBanner,
)
from govuk_tech_docs_sphinx_theme.components.warning_text import WarningText
from pathlib import Path
from typing import List

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError

__all__ = ["add_js_files", "setup", "NotificationBanner", "WarningText"]

try:
    __version__ = version(__package__)
except PackageNotFoundError:
    __version__ = "unknown"

# Define a `Path` object to the `static/javascripts` folder
DIR_STATIC = Path(__file__).parent.joinpath("static")
DIR_JAVASCRIPTS = DIR_STATIC.joinpath("javascripts")

# Define a list of JavaScript files to not include across all pages
EXCLUDE_JAVASCRIPT_FILES = [DIR_JAVASCRIPTS.joinpath("searchtools.js")]

# Get the file paths to the JavaScript files of interest
JAVASCRIPT_FILES = sorted(
    [
        j.relative_to(DIR_STATIC).as_posix()
        for j in DIR_JAVASCRIPTS.rglob("*.js")
        if j not in EXCLUDE_JAVASCRIPT_FILES
    ]
)


def add_js_files(app, files: List[Path]) -> None:
    """Add a list of JavaScript files to the ``script_files`` configuration variable of
    the theme.

    Args:
        app: A ``sphinx.application.Sphinx`` object.
        files: A list of ``Path`` objects routed to JavaScript files of interest.

    Returns:
        None

    """
    _ = [app.add_js_file(j) for j in files]


def setup(app) -> None:
    """Set up function for the Sphinx theme.

    Args:
        app: A ``sphinx.application.Sphinx`` object.

    Returns:
        None

    """

    # Register the HTML theme
    app.add_html_theme(
        "govuk_tech_docs_sphinx_theme", Path.resolve(Path(__file__).parent)
    )

    # Import required JavaScript files on build
    app.connect("builder-inited", partial(add_js_files, files=JAVASCRIPT_FILES))

    # Add GOV.UK Design System components
    app.add_directive("warning", WarningText)
    app.add_directive("note", NotificationBanner)
