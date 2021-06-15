# Development of the `govuk-tech-docs-sphinx-theme`

[This theme was designed to complement `govcookiecutter`][govcookiecutter] to provide a
standardised [GOV.UK Tech Docs-style theme][govuk-tech-docs] that leverages the power
of [Sphinx, a Python document generator][sphinx]. This enables users to build and
deploy documentation as a searchable website, whether that is locally on their machine
or elsewhere, such as on GitHub Pages.

```{note} This theme is not an exact replica of GOV.UK Tech Docs template!

As bugs/discrepancies are discovered, the theme will be improved and updated - we are
"TDD"-ing to completeness.

In this case, most of the testing is done by visual inspection of the built theme,
rather than formal test scripts; [use the example component pages to help with
testing!][docs-example-components]

This theme is based on commit [`1fb26fc`][current-version] of the
[GOV.UK Tech Docs template][govuk-tech-docs].

```

The theme was developed by taking a build of the GOV.UK Tech Docs template, splitting
it out into an acceptable Sphinx layout. Sphinx blocks were then applied to the
appropriate areas of the HTML code. By default, the template CSS and JavaScript files
supersede the inbuilt Sphinx ones, aside from a few cases (e.g. search).

If you discover any bugs, and/or discrepancies, [please raise a GitHub issue][issue] on
our repository ([check out our contributing guidelines][contributing], and [code of
conduct][code-of-conduct] first).

If you also want to contribute to the solution, please do raise a pull request too! The
following sections will hopefully assist with fixing any bugs. Consider [reading the
Sphinx documentation on templating][sphinx-templating], and [documentation on using
Jinja templating][jinja]. For new or existing [GOV.UK Design System
components][govuk-design-system], [read the Sphinx extension development
documentation][sphinx-extension].

## Comparing with GOV.UK Tech Docs template

[The theme was built by from a specific version of the GOV.UK Tech Docs
template][current-version], and amending all HTML files to use relative paths for all
assets (CSS, JavaScript, images, etc.).

This repository contains an automated way to get the latest version of the template,
and amend the paths on a Unix-based machine:

```{note} For comparison purposes only

Given the amount of changes, this process is more for comparison purposes to improve
the theme, rather than rebuilding it from scratch.

For example, breaking changes between the template and the theme include [updating the
vendor JavaScript files][commit-update-js], and the use of Sphinx's search engine.

You can also use the [GOV.UK Developer Docs][govuk-dev-docs] or [the GDS Way][gds-way]
for comparison, although they are both slightly different to the template.

```

1. [Install ./jq][jq]
2. [Install the requirements for the GOV.UK Tech Docs template][govuk-tech-docs], but
   stop before creating a new project
3. Open your terminal at the root of this repository, and run the
   `build_alphagov_tech_docs_template.sh` shell script
   ```shell
   sh build_alphagov_tech_docs_template.sh
   ```

This builds the latest version of the template in the untracked folder
`source/alphagov-tech-docs-template/build`.

## Fixing missing attributes and classes with jQuery

If you notice missing attributes and/or classes in the HTML, use jQuery to inject these
attributes or classes at the correct location. Changes should be made in
`src/govuk_tech_docs_sphinx_theme/static/javascripts/theme.js`.

For example, to prevent Sphinx autosummary from using a 10%:90% split for summary
tables, the `style` attribute of all `col` tags are set to have a 50% width by this
code:

```javascript
$(function() {
  $('table.longtable > colgroup').find('col').each(function() {
    $(this).css('width', '50%');
  });
});
```
The `'table.longtable > colgroup'` line ensures only `table` tags with a `longtable`
class with a nested `colgroup` tag are used to find nested `col` tags.

## Fixing missing styles with CSS

As Sphinx blocks were injected directly into the built GOV.UK Tech Docs template,
Sphinx will sometimes inject more HTML tags and classes. This can then break any styles
that a conditional, say on the order of tags and/or classes.

If you identify a situation where this occurs, [find out what the affected style should
look like](#comparing-with-govuk-tech-docs-template). Open
`src/govuk_tech_docs_sphinx_theme/static/stylesheets/manifest.css`, and find the
incorrectly applied style. Identify the problem, then copy the relevant styles from
`mainfest.css` to `src/govuk_tech_docs_sphinx_theme/static/stylesheets/theme.css`,
making the relevant changes to apply the style to the theme.

For example, page titles have a specific format in the GOV.UK Tech Docs template.
However, they rely on a tag having a `technical-documentation` class, with a nested
`h1` tag (or a tag with a `govuk-heading-xl` class) in `manifest.css`.

```css
.technical-documentation > h1, .govuk-heading-xl {
  color: #0b0c0c;
  font-family: "GDS Transport", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: 700;
  font-size: 32px;
  font-size: 2rem;
  line-height: 1.09375;
  display: block;
  margin-top: 0;
  margin-bottom: 30px; }
```

However, Sphinx injects a `section` before the first heading (page title), so the above
CSS is amended in `theme.css` to:

```css
.technical-documentation > section > h1, .govuk-heading-xl {
  color: #0b0c0c;
  font-family: "GDS Transport", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: 700;
  font-size: 32px;
  font-size: 2rem;
  line-height: 1.09375;
  display: block;
  margin-top: 0;
  margin-bottom: 30px; }
```

Other relevant, and amended page title CSS also exist in `theme.css` exist, but have
not been reproduced here for brevity.

## GOV.UK Design System components

Some, but not all, GOV.UK Design System components have been included in this theme. To
add additional ones, [read the Sphinx documentation on extensions][sphinx-extension],
and take a look at the existing ones in the
`src/govuk_tech_docs_sphinx_theme/components` folder.

Note new components must be added as directives in the `setup` function of
`src/govuk_tech_docs_sphinx_theme/__init__.py`.

[code-of-conduct]: ./CODE_OF_CONDUCT.md
[commit-update-js]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme/commit/f78f0d74ba0d82e45a993b4bb40aa1e3d8d34643
[contributing]: ./CONTRIBUTING.md
[current-version]: https://github.com/alphagov/tech-docs-template/tree/1fb26fcf3a8605fe4734fdfbdf9dfc180f1fe3f7
[docs-example-components]: ../example_components/README.md
[gds-way]: https://gds-way.cloudapps.digital/
[govcookiecutter]: https://github.com/ukgovdatascience/govcookiecutter
[govuk-design-system]: https://design-system.service.gov.uk/
[govuk-dev-docs]: https://docs.publishing.service.gov.uk/
[govuk-tech-docs]: https://github.com/alphagov/tech-docs-template
[issue]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme/issues/new
[jinja]: https://jinja.palletsprojects.com/
[jq]: https://stedolan.github.io/jq/
[sphinx]: https://www.sphinx-doc.org/en/master/
[sphinx-extension]: https://www.sphinx-doc.org/en/master/extdev/index.html
[sphinx-templating]: https://www.sphinx-doc.org/en/master/templating.html
