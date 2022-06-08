# cookiecutter-conda-package

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
- Makefile
- gitignore

Planned:

- make Docker image
- auto template update via cruft
- keep environment files up-to-date
- add documentation skeleton (with sphinx / myst?)
- publish on PyPI on release
- add testing `main` on selected dependencies

## Usage

For best experience create and keep the project up-to-date with cruft:

```
conda install -c conda-forge cruft
cruft create https://github.com/bopen/cookiecutter-conda-package
```

then answer the configuration questions or accept the defaults when in doubt.

Setup the environment and git pre-commit hooks:

```
git init
git add .
git commit -m "Initial commit of the package boilerplate"
make conda-env-update
pre-commit install
```

To test the setup install the package and run pre-commit and pytest:

```
pip install -e .
make
```

## License

```
Copyright 2022, European Centre for Medium-Range Weather Forecasts (ECMWF).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
