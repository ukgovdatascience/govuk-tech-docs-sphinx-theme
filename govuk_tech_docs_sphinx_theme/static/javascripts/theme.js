// Sets `sphinx.ext.autosummary` table columns to 50%:50%, which looks nicer
$(function() {
  $('table.longtable.table.autosummary > colgroup').find('col').each(function() {
    $(this).css('width', '50%');
  });
});
