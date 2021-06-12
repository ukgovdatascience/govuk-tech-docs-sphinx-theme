# GOV.UK Tech Docs Sphinx Theme

A Sphinx theme to replicate the GOV.UK Tech Docs Template.

> ℹ️ Where this documentation refers to the **root folder** we mean where this README.md is located.

## Getting started

The source code for this Sphinx theme is available at
[`https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme`][repository]. You can use this for your own Sphinx
documentation by:

1. [Installing Sphinx][sphinx-quickstart] (if you haven't already)
2. [Installing this theme](#install-the-package)
3. [Amending your Sphinx `conf.py` configuration file](#amend-your-sphinx-confpy-configuration-file)
4. [Adding an accessibility statement](#add-an-accessibility-statement)

### Install the package

The latest released version can be installed from the [Python Package Index (PyPI)][pypi]:

```shell
pip install govuk-tech-docs-sphinx-theme
```

Alternatively, you can install the bleeding edge version directly from this repository using https:

```shell
pip install -e git+https://git@github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme#egg=govuk_tech_docs_sphinx_theme
```

or using ssh:

```shell
pip install -e git+ssh://git@github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme#egg=govuk_tech_docs_sphinx_theme
```

### Amend your Sphinx `conf.py` configuration file

To use this Sphinx theme, modify your Sphinx `conf.py` configuration file to resemble the example one found
[here][example-conf], filling in any placeholders, and adding other settings as required.

Note, note all Sphinx configuration settings are currently supported by this theme - feel free to
[contribute](#contributing)!

### Add an accessibility statement

All public sector bodies have to meet the 2018 accessibility regulations unless exempt; see
[here][govuk-accessibility] for further details.

To add an accessibility statement, copy the example Markdown template
[`example_accesibility.md`][example-accessibility] to the root of your Sphinx folder - this is the same location as
your Sphinx `conf.py` configuration file. Add your accessibility statement; guidance can be found on
[GOV.UK][govuk-example-accessibility].

Next, in your Sphinx `conf.py` file, amend the `accessibility` value of the `html_context` to reference the filename of
your accessibility statement.

## Troubleshooting

If you have difficulties with this theme, please raise an [issue][repository-issues] or [contact us][email].

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers both the codebase and any sample
code in the documentation. Additional third-party component licences are stated in the `LICENSE` file. The
documentation is © Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

If you want to help us build, and improve `govuk-tech-docs-sphinx-theme`, view our
[contributing guidelines][contributing].

## Acknowledgements

This project structure is based on the [`govcookiecutter`][govcookiecutter] template project.

[contributing]: ./CONTRIBUTING.md
[email]: mailto:gds-data-science@digital.cabinet-office.gov.uk
[example-accessibility]: ./example_accessibility.md
[example-conf]: ./example_conf.py
[govcookiecutter]: https://github.com/ukgovdatascience/govcookiecutter
[govuk-accessibility]: https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps
[govuk-example-accessibility]: https://www.gov.uk/government/publications/sample-accessibility-statement/sample-accessibility-statement-for-a-fictional-public-sector-website
[docs-loading-environment-variables]: docs/contributor_guide/loading_environment_variables.md
[pre-commit]: https://pre-commit.com/
[pypi]: https://pypi.org/project/govuk-tech-docs-sphinx-theme/
[repository]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme
[repository-issues]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme/issues/new
[sphinx-quickstart]: https://www.sphinx-doc.org/en/master/usage/quickstart.html#setting-up-the-documentation-sources
