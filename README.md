# Spark Package Template

This package is developed to ease development of Spark-Cleantech packages

## Features

Alpha stage:

- pre-commit hooks
  - various linters
  - ruff
- version with setuptools-scm-git
- copyright license
- GitHub Actions
  - unit-tests (py3.11)
  - pre-commit
  - integration-tests
  - build documentation
  - static type check
- Makefile
- gitignore
- auto template update via cruft
- add documentation skeleton (with sphinx / myst)

Planned:

- keep environment files up-to-date

## Usage

For best experience create a new conda environment (e.g. `MY_PACKAGE`) with Python 3.11,
cruft and make, then create the package:

```
conda create -n MY_PACKAGE -c conda-forge python=3.11 cruft make
conda activate MY_PACKAGE
cruft create https://github.com/spark-cleantech.eu/package-template
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
git branch -M main
git remote add origin git@github.com:spark-cleantech/MY_PACKAGE.git
git push --set-upstream origin main
```

To setup the package and its dependecies run:

```
make conda-env-update
conda activate MY_PACKAGE
pre-commit install
pip install -e . --no-deps
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
Copyright (C) Spark Cleantech SAS (SIREN 909736068) - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Erwan Pannier <erwan.pannier@spark-cleantech.eu>, March 2024
```

## Credits

Originally based on Cookiecutter template at https://github.com/ecmwf-projects/cookiecutter-conda-package,
distributed under Apache Licence. Licence was changed after the fork. 