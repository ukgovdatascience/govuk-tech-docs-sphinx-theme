# Contributing

We love contributions! We've compiled this documentation to help you understand our
contributing guidelines. If you still have questions, please [contact us][email] and
we'd be happy to help!

## Code of Conduct

Please read [`CODE_OF_CONDUCT.md`][code-of-conduct] before contributing.

## Getting started

To start contributing, first make sure your system meets these requirements:

1. Python 3.6.1+ installed
2. [`poetry` installed][poetry-install]

Then install the required Python packages, and [pre-commit hooks][pre-commit] using:

```shell
poetry run make dependencies
```

It is better to use the above make command, rather than `poetry install` and
`poetry run pre-commit install`, as the command will ensure your pre-commit hooks are
up-to-date with any changes made.

The pre-commit hooks are a security feature to ensure no secrets[^1], and large data
files, are accidentally committed into the repository. For more information about the
pre-commit hooks used in this repository, see the
[documentation][docs-pre-commit-hooks].

[^1]: [Only secrets of specific patterns are detected by the pre-commit
      hooks][docs-pre-commit-hooks-secrets-definition].

## Code conventions

We mainly follow [The GDS Way][gds-way] in our code conventions.

### Git and GitHub

We use Git to version control the source code; please read [The GDS Way][gds-way-git]
for further details, including information about writing good commit messages, using
`git rebase` for local branches, and `git merge --no-ff` for merges, as well as the
entry on `git push --force-with-lease` instead of `git push -f`.

If you want to modify the `.gitignore` files, see the template
[documentation][docs-updating-gitignore] for further details.

Our source code is stored on GitHub. Pull requests into `main` require at least one
approved review.

### Python

For Python code, we follow [The GDS Way Python style guide][gds-way-python] with a line
length of 88; the flake8 pre-commit hook should help with this!

### Markdown

Local links can be written as normal, but external links should be referenced at the
bottom of the Markdown file for clarity. For example:

```md
Use a local link to reference the [`README.md`](./README.md) file, but an external link
for [GOV.UK][gov-uk].

[gov-uk]: https://www.gov.uk/
```

We also try to wrap Markdown to a line length of 88 characters, but this is not
strictly enforced in all cases, for example with long hyperlinks.

## Testing

Tests are written using the [pytest][pytest] framework, with its configuration in the
`pyproject.toml` file. Note, only tests in the `tests` folder are executed. To run the
tests, execute the following command in your terminal:

```shell
pytest
```

### Code coverage

Code coverage of Python scripts is measured using the [`coverage`][coverage] Python
package; its configuration can be found in `pyproject.toml`. Note coverage only extends
to Python scripts in the `govuk_tech_docs_sphinx_theme` folder.

To run code coverage, and view it as an HTML report, execute the following command in
your terminal:

```shell
poetry run make coverage_html
```

The HTML report can be accessed at `htmlcov/index.html`.

## Documentation

We write our documentation in [MyST Markdown][myst] for use in Sphinx. This is mainly
stored in the `docs` folder, unless it's more appropriate to store it elsewhere, like
this file.

[Please read our guidance on how to write Sphinx
documentation][docs-write-sphinx-documentation], and build it into a searchable website.

[code-of-conduct]: ./CODE_OF_CONDUCT.md
[coverage]: https://coverage.readthedocs.io/
[docs-pre-commit-hooks]: ./pre_commit_hooks.md
[docs-pre-commit-hooks-secrets-definition]: ./pre_commit_hooks.md#definition-of-a-secret-according-to-detect-secrets
[docs-updating-gitignore]: ./updating_gitignore.md
[docs-write-sphinx-documentation]: ./writing_sphinx_documentation.md
[email]: mailto:gdsdatascience@digital.cabinet-office.gov.uk
[gds-way]: https://gds-way.cloudapps.digital/
[gds-way-git]: https://gds-way.cloudapps.digital/standards/source-code.html
[gds-way-python]: https://gds-way.cloudapps.digital/manuals/programming-languages/python/python.html#python-style-guide
[myst]: https://myst-parser.readthedocs.io/
[poetry-install]: https://python-poetry.org/docs/
[pre-commit]: https://pre-commit.com/
[pytest]: https://docs.pytest.org/
