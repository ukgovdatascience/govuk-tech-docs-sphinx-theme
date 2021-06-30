# GOV.UK Tech Docs Sphinx Theme

A Sphinx theme to replicate the GOV.UK Tech Docs Template.

```{warning}

Where this documentation refers to the root folder we mean where this README.md is located.

```

## Getting started

The source code for this Sphinx theme is available at
[`https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme`][repository]. You
can use this for your own Sphinx documentation by following the steps below.

### Install the package

The latest released version can be installed from the [Python Package Index
(PyPI)][pypi]:

```shell
pip install govuk-tech-docs-sphinx-theme
```

### Amend your Sphinx `conf.py` configuration file

To use this Sphinx theme, modify your Sphinx `conf.py` configuration file as follows:

1. Add the theme in the list of `extensions`:
   ```python
   extensions = ["govuk_tech_docs_sphinx_theme"]
   ```
2. Make sure the `author`, and `project` variables reflect your organisation name, and
   project
3. Set `html_theme = "govuk_tech_docs_sphinx_theme"`
4. Set the `html_context` dictionary as follows:
   ```python
   html_context = {
       "github_url": None,                  # if using GitHub, set to the URL of your repository as a string
       "gitlab_url": None,                  # if using GitLab, set to the URL of your repository as a string
       "conf_py_path": "docs/",             # assuming your Sphinx folder is called `docs`
       "version": "main",                   # assuming `main` is your repository's default branch
       "accessibility": "accessibility.md"  # assuming your accessibility statement is at `docs/accessibility.md`
   }
   ```
5. Set the `html_theme_options` dictionary as follows:
   ```python
   html_theme_options = {
       "organisation": "",  # replace with your organisation's abbreviation (ideally) or name - long text may not look nice
       "phase": ""          # replace with an Agile project phase - see https://www.gov.uk/service-manual/agile-delivery
   }
   ```

Note, not all Sphinx configuration settings are currently supported by this theme —
[feel free to contribute to support other settings](#contributing)!

### Add an accessibility statement

````{note} Accessibility issues with Sphinx autodoc extension

With the Sphinx autodoc extension, you may find headers do not fit the content that
follows. This [fails the WCAG 2.1 success criterion 2.4.6 Headings and
Labels][wcag-2.1-2.4.6].

To resolve this, copy the entire `docs/_template` folder from this repository into
your Sphinx folder, and ensure your `conf.py` file contains:

```python
templates_path = ["_templates"]
```

````

All public sector bodies have to meet the [2018 accessibility
regulations][govuk-accessibility] unless exempt.

To add an accessibility statement, create a blank Markdown file in the root of your
Sphinx folder called `accessibility.md`. This folder is the same location as your
Sphinx `conf.py` configuration file. Add the following header to your new Markdown file:

```markdown
---
orphan: true
---
# Accessibility statement
```

followed by your accesibility statement. [Guidance on how to write an accessibility
statement can be found on GOV.UK][govuk-example-accessibility].

Next, in your Sphinx `conf.py` file, check that the `html_context` variable has this
file referenced, i.e.:

```python
html_context = {
    ...,
    "accessibility": "accessibility.md",
    ...
}
```

### Apply the theme's components

This theme should be compatible with most ReStructuredText syntax, and also includes
[components from the GOV.UK Design System][govuk-design]. [See the example
components page for further details][docs-example-components-rest].

[If you are using MyST to build Sphinx documentation using Markdown][myst], see
the [equivalent Markdown components page][docs-example-components-md].

## Troubleshooting

If you have difficulties with this theme, [please raise an issue][repository-issues] or
[contact us to report a problem][email].

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. [Additional third-party
component licences are stated in the `LICENSE`][license] file. The documentation is
© Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

[If you want to help us build, and improve `govuk-tech-docs-sphinx-theme`, view our
contributing guidelines][contributing].

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].

[contributing]: ./docs/contributor_guide/CONTRIBUTING.md
[docs-example-components-md]: ./docs/example_components/markdown.md
[docs-example-components-rest]: ./docs/example_components/restructuredtext.rst
[email]: mailto:gds-data-science@digital.cabinet-office.gov.uk
[govcookiecutter]: https://github.com/ukgovdatascience/govcookiecutter
[govuk-accessibility]: https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps
[govuk-design]: https://design-system.service.gov.uk/
[govuk-example-accessibility]: https://www.gov.uk/government/publications/sample-accessibility-statement/sample-accessibility-statement-for-a-fictional-public-sector-website
[license]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme/blob/main/LICENSE
[myst]: https://myst-parser.readthedocs.io/en/latest/
[pypi]: https://pypi.org/project/govuk-tech-docs-sphinx-theme/
[repository]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme
[repository-issues]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme/issues/new
[wcag-2.1-2.4.6]: https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels.html
