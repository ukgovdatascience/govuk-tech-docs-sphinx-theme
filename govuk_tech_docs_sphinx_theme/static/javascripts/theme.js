// Sets `sphinx.ext.autosummary` table columns to 50%:50%, which looks nicer
$(function() {
  $('table.longtable.table.autosummary > colgroup, table.longtable > colgroup').find('col').each(function() {
    $(this).css('width', '50%');
  });
});

// Sets the correct link for the anchored heading icon
$(function() {
  $('section').find('h1.anchored-heading, h2.anchored-heading, h3.anchored-heading, h4.anchored-heading, h5.anchored-heading, h6.anchored-heading').each(function() {
    $(this).find('a.anchored-heading__icon').attr('href', '#' + $(this).parents('section').attr('id'));
  });
});

// Sets the `aria-hidden` attribute for the GOV.UK Design System warning text, and allows for multiline text. This is
// generated using the `warning` directive created using the `WarningText` class
$(function() {
    $('div.govuk-warning-text.docutils.container').each(function() {
        $(this).find('span.govuk-warning-text__icon').attr('aria-hidden', 'true');
        $(this).find('strong.govuk-warning-text__text').css('white-space', 'pre-wrap');
    });
});
