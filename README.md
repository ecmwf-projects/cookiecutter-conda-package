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
  - pre-commit
  - integration-tests
  - build package & publish on PyPI
- Makefile
- gitignore
- make Docker image
- auto template update via cruft
- add documentation skeleton (with sphinx / myst)

Planned:

- keep environment files up-to-date
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
Copyright 2022, European Union.

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
