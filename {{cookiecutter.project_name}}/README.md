# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Quick Start

Install in your current environment:

```
pip install git+https://github.com/spark-cleantech/{{ cookiecutter.project_name }}
```

Run in Python:

```python
>>> import {{ cookiecutter.repo_name }}

```

## Use in a dedicated environment

This is recommended for large packages. Clone the repository and create
an isolated environment :

```
git clone https://github.com/spark-cleantech/{{ cookiecutter.project_name }}.git
cd {{ cookiecutter.project_name }}
conda env create -n {{ cookiecutter.repo_name }}-env -f environment.yml
conda activate {{ cookiecutter.repo_name }}-env
pip install -e .         # install in editable mode
```

Run in Python:

```python
>>> import spy
```

## Workflow for Developers/contributors

Clone the repository :

```
git clone https://github.com/spark-cleantech/{{ cookiecutter.project_name }}.git
cd {{ cookiecutter.project_name }}
```

For best experience create a new conda environment (e.g. {{ cookiecutter.repo_name }}-env) with Python 3.11:

```
conda create -n {{ cookiecutter.repo_name }}-env -c conda-forge python=3.11 -y
conda activate {{ cookiecutter.repo_name }}-env
```

Before pushing to GitHub, run the following commands:

1. Update conda environment: `make conda-env-update`
1. Install this package in editable mode: `pip install -e .`
1. (optional) Sync with the latest [template](https://github.com/spark-cleantech/package-template) : `make template-update`
1. (optional) Run quality assurance checks (code linting): `make qa`
1. (optional) Run tests: `make unit-tests`
1. (optional) Run the static type checker: `make type-check`
1. (optional) Build the documentation (see [Sphinx tutorial](https://www.sphinx-doc.org/en/master/tutorial/)): `make docs-build`

If using Windows, `make` is not available by default. Either install it
([for instance with Chocolatey](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)),
or open the [Makefile](./Makefile) and execute the lines therein manually.

## License

```
Copyright (C) Spark Cleantech SAS (SIREN 909736068) - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Erwan Pannier <erwan.pannier@spark-cleantech.eu>, March 2024
```
