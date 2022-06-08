PROJECT := {{ cookiecutter.project_slug }}
CONDA := conda
CONDAFLAGS :=

default: qa test

qa:
	pre-commit run --all-files

test:
	python -m pytest -vv

type-check:
	python -m mypy --strict .

conda-env-update:
	$(CONDA) env update $(CONDAFLAGS) -f environment.yml
