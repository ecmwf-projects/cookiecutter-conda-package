# cookiecutter-conda-package

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

Template for Python packages based on Conda.

This package is developed to ease development of ECMWF packages, but it is intended to
be more generic.

## Features

Alpha stage:

- pre-commit hooks
  - various linters
  - black + isort
- version with setuptools-scm-git
- copyright + Apache v2.0 license
- GitHub Actions
  - unit-tests
  - pre-commit
  - integration-tests
  - build package & publish on PyPI
- Makefile
- gitignore
- make Docker image
- auto template update via cruft

Planned:

- keep environment files up-to-date
- add documentation skeleton (with sphinx / myst?)
- add testing `main` on selected dependencies

## Usage

For best experience create a new conda environment (e.g. DEVELOP) with Python 3.10,
cruft and make, then create the package:

```
conda create -n DEVELOP -c conda-forge python=3.10 cruft make
conda activate DEVELOP
cruft create https://github.com/ecmwf-projects/cookiecutter-conda-package
```

answer the configuration questions or accept the defaults when in doubt.

Create the git repo and add the pre-commit git hooks:

```
git init
git add .
git commit -m "Initial commit of the package boilerplate"
```

Attach an empty remote repository and push the skeleton package:

```
git remote add origin git@github.com:ORGANISATION/PROJECT_NAME.git
git push --set-upstream origin main
```

To setup the package and its dependecies run:

```
make conda-env-update
pre-commit install
pip install -e .
```

Finally to run pre-commit, pytest, and mypy on the newly created package run:

```
make
```

To update the boilerplate to the latest template execute:

```
make template-update
```

## License

```
(C) Copyright 2022 ECMWF.

This software is licensed under the terms of the Apache Licence Version 2.0
which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
In applying this licence, ECMWF does not waive the privileges and immunities
granted to it by virtue of its status as an intergovernmental organisation
nor does it submit to any jurisdiction.
```
