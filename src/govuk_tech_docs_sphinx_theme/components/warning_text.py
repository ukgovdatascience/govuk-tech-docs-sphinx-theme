from docutils import nodes
from docutils.parsers.rst import Directive
from typing import List


class WarningText(Directive):
    """Create warning text based on the GOV.UK Design System.

    The `warning text`_ is based on the GOV.UK Design System, excluding the `id`
    attributes. Some attributes are generated using JavaScript in the `theme.js` file.

    Returns:
        A `nodes.Element` object containing the compiled warning text.

    .. _warning text:
        https://design-system.service.gov.uk/components/warning-text/

    """

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self) -> List[nodes.Element]:
        """Create warning text based on the GOV.UK Design System."""

        # Assert there is content in the directive, and compile this as text, parsing
        # any content
        # TODO: `nodes.raw` does not render reST - need to find a way to do this!
        self.assert_has_content()
        warning_message = nodes.raw(format="html")
        self.state.nested_parse(self.content, self.content_offset, warning_message)

        # Add the assistive warning label, and combine with `warning_message` inside a
        # `<strong>` tag
        warning_assistive = nodes.inline(
            text="Warning", classes=["govuk-warning-text__assistive"]
        )
        warning_text = nodes.strong(classes=["govuk-warning-text__text"])
        warning_text += [warning_assistive, warning_message]

        # Add the warning icon, and then combine with `warning_text` in a `<div>` tag
        warning_icon = nodes.inline(text="!", classes=["govuk-warning-text__icon"])
        warning_node = nodes.container(classes=["govuk-warning-text"])
        warning_node += [warning_icon, warning_text]

        return [warning_node]
