# `docs` folder

All documentation for the project should be included in this folder in either
reStructuredText or Markdown files, with acceptable formatting for Sphinx.

To build the documentation, run the `docs` command [from `Makefile` using the `make`
utility at the top-level of this Git repository][docs-makefile].

```shell
poetry run make docs
```

[Guidance on how to write Sphinx documentation is supplied in the contributor
guide][writing-sphinx-documentation].

[docs-makefile]: ../docs/structure/README.md#makefile
[writing-sphinx-documentation]: ../docs/contributor_guide/writing_sphinx_documentation.md
