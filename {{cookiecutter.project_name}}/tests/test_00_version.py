import {{ cookiecutter.repo_name }}


def test_version() -> None:
    assert {{ cookiecutter.repo_name }}.__version__ != "999"
