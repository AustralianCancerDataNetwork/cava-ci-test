"""Smoke test to confirm the package is importable and the test suite runs."""


def test_import() -> None:
    import cava_ci_test  # noqa: F401


def test_placeholder() -> None:
    assert 1 + 1 == 2

def test_add() -> None:
    from cava_ci_test import add as add_func
    assert add_func(2, 3) == 5