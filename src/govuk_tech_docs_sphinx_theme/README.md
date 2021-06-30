# `govuk_tech_docs_sphinx_theme` package overview

All functions for this project, should be stored in this folder. All tests should be
stored in the `tests` folder, which is two-level above this folder in the main project
directory.

Feel free to create/rename/delete these folders as required, as they will not be
necessary for each and every project.

It is strongly suggested that you import functions in the
`govuk_tech_docs_sphinx_theme` `__init__.py` script. You should also try to use
absolute imports in this script whenever possible. Relative imports are not
discouraged, but can be an issue for projects where the directory structure is likely
to change. See [PEP 328 for details on absolute imports][pep-328].

[pep-328]: https://www.python.org/dev/peps/pep-0328/
