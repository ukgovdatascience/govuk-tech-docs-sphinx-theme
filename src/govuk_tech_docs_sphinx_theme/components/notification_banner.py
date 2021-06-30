from docutils import nodes
from docutils.parsers.rst import Directive
from typing import List


class NotificationBanner(Directive):
    """Create a notification banner based on the GOV.UK Design System.

    The `notification banner`_ is based on the GOV.UK Design System, excluding the `id`
    attributes. Some attributes are generated using JavaScript in the `theme.js` file.

    Returns:
        A `nodes.Element` object containing the compiled notification banner.

    .. _notification banner:
        https://design-system.service.gov.uk/components/notification-banner/

    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self) -> List[nodes.Element]:
        """Create a notification banner based on the GOV.UK Design System."""

        # Assert there is content in the directive
        self.assert_has_content()

        # Create a heading containing the required argument of the directive, and
        # compile this within a `<div>` tag
        notification_title = (
            f'<h2 class="govuk-notification-banner__title" '
            f'id="govuk-notification-banner-title">{self.arguments[0]}</h2>'
        )
        notification_header = nodes.raw(
            "",
            notification_title,
            format="html",
            classes=["govuk-notification-banner__header"],
        )

        # Render the content within a `<p>` tag, parsing the actual text
        # TODO: Issue with parsing nested content using the correct class
        notification_heading = nodes.paragraph(
            # classes=["govuk-notification-banner__heading"]
        )
        self.state.nested_parse(self.content, self.content_offset, notification_heading)

        # Combine `notification_heading` inside a `<div>` tag
        notification_content = nodes.container(
            classes=["govuk-notification-banner__content"]
        )
        notification_content += notification_heading

        # Combine `notification_header`, and `notification_content` inside a `<div>` tag
        notification_node = nodes.container(classes=["govuk-notification-banner"])
        notification_node += [notification_header, notification_content]

        return [notification_node]
