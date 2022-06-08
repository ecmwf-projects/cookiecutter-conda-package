PROJECT = {{ cookiecutter.project_slug }}

default: qa test

qa:
	pre-commit run --all-files

test:
	python -m pytest -vv

conda-env-update:
	conda env update -f environment.yml