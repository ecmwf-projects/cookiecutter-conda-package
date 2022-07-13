import my_package


def test_version() -> None:
    assert my_package.__version__ != "999"
