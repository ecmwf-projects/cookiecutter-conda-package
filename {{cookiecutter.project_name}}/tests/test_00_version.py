import {{ cookiecutter.project_slug }}


def test_version() -> None:
    assert {{ cookiecutter.project_slug }}.__version__ != "999"
