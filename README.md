# GOV.UK Tech Docs Sphinx Theme

A Sphinx theme to replicate the GOV.UK Tech Docs Template.

> ℹ️ Where this documentation refers to the **root folder** we mean where this README.md is located.

## Getting started

The source code for this Sphinx theme is available at
[`https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme`][repository]. You can use this for your own Sphinx
documentation by following the steps below.

### Install the package

The latest released version can be installed from the [Python Package Index (PyPI)][pypi]:

```shell
pip install govuk-tech-docs-sphinx-theme
```

Alternatively, you can install the bleeding edge version directly from this repository using https or ssh:

```shell
pip install -e git+https://git@github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme#egg=govuk_tech_docs_sphinx_theme
pip install -e git+ssh://git@github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme#egg=govuk_tech_docs_sphinx_theme
```

or a specific branch, say `example-branch` like so:

```shell
pip install -e git+https://git@github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme.git@example-branch#egg=govuk_tech_docs_sphinx_theme
pip install -e git+ssh://git@github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme.git@example-branch#egg=govuk_tech_docs_sphinx_theme
```


### Amend your Sphinx `conf.py` configuration file

To use this Sphinx theme, modify your Sphinx `conf.py` configuration file as follows:

1. Add the theme in the list of `extensions`:
   ```python
   extensions = ["govuk_tech_docs_sphinx_theme"]
   ```
2. Make sure the `author`, and `project` variables reflect your organisation name, and project
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

Note, note all Sphinx configuration settings are currently supported by this theme - feel free to
[contribute](#contributing)!

### Add an accessibility statement

All public sector bodies have to meet the 2018 accessibility regulations unless exempt; see
[here][govuk-accessibility] for further details.

To add an accessibility statement, create a blank Markdown file in the root of your Sphinx folder called
`accessibility.md`; this is the same location as your Sphinx `conf.py` configuration file. Add the following header to
your new Markdown file:

```markdown
---
orphan: true
---
# Accessibility statement
```

followed by your accesibility statement; guidance on how to write one can be found on
[GOV.UK][govuk-example-accessibility].

Next, in your Sphinx `conf.py` file, check that the `html_context` variable has this file referenced, i.e.:

```python
html_context = {
    ...,
    "accessibility": "accessibility.md",
    ...
}
```

### Apply the theme's components

This theme should be compatible with most ReStructuredText syntax, and also includes some
[GOV.UK Design System][govuk-design] components. See the [example components][docs-example-components-rest] page for
further details.

If you are using [MyST-Parser][myst] to build Sphinx documentation using Markdown, see the equivalent components page
[here][docs-example-components-md].

## Troubleshooting

If you have difficulties with this theme, please raise an [issue][repository-issues] or [contact us][email].

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers both the codebase and any sample
code in the documentation. Additional third-party component licences are stated in the [`LICENSE`][license] file. The
documentation is © Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

If you want to help us build, and improve `govuk-tech-docs-sphinx-theme`, view our
[contributing guidelines][contributing].

## Acknowledgements

This project structure is based on the [`govcookiecutter`][govcookiecutter] template project.

[contributing]: ./docs/contributor_guide/CONTRIBUTING.md
[docs-example-components-md]: ./docs/example_components/markdown.md
[docs-example-components-rest]: ./docs/example_components/restructuredtext.rst
[docs-loading-environment-variables]: docs/contributor_guide/loading_environment_variables.md
[email]: mailto:gds-data-science@digital.cabinet-office.gov.uk
[govcookiecutter]: https://github.com/ukgovdatascience/govcookiecutter
[govuk-accessibility]: https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps
[govuk-design]: https://design-system.service.gov.uk/
[govuk-example-accessibility]: https://www.gov.uk/government/publications/sample-accessibility-statement/sample-accessibility-statement-for-a-fictional-public-sector-website
[license]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme/blob/main/LICENSE
[myst]: https://myst-parser.readthedocs.io/en/latest/
[pre-commit]: https://pre-commit.com/
[pypi]: https://pypi.org/project/govuk-tech-docs-sphinx-theme/
[repository]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme
[repository-issues]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme/issues/new
[sphinx-quickstart]: https://www.sphinx-doc.org/en/master/usage/quickstart.html#setting-up-the-documentation-sources
