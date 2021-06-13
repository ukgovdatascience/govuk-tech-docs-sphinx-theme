from govuk_tech_docs_sphinx_theme import add_js_files
from pathlib import Path
from typing import List
from unittest.mock import MagicMock, call
import pytest

# Define the input file path list for the test case
args_test_add_js_files = [
    [Path("hello/world.js")],
    [Path("foo/bar.js")],
    [Path("hello/world.js"), Path("foo/bar.js")],
]


@pytest.mark.parametrize("test_input_files", args_test_add_js_files)
class TestAddJsFiles:
    def test_calls_add_js_file_correctly(self, test_input_files: List[Path]) -> None:
        """Test that the `Sphinx.add_js_file` method is called correctly."""

        # Mock the `app`
        test_input_app = MagicMock()

        # Execute the function, and assert the `add_js_file` method is called correctly
        add_js_files(test_input_app, test_input_files)
        assert test_input_app.add_js_file.call_count == len(test_input_files)
        test_input_app.add_js_file.assert_has_calls(
            [call(a) for a in test_input_files], any_order=False
        )
