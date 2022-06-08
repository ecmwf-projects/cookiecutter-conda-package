import {{ cookiecutter.project_slug }}


def test_import() -> None:
    assert {{ cookiecutter.project_slug }}.__version__ != "999"
