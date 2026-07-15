"""Smoke test to confirm the package is importable and the test suite runs."""


def test_import() -> None:
    import cava_ci_test  # noqa: F401


def test_placeholder() -> None:
    assert 1 + 1 == 2

def test_add() -> None:
    from cava_ci_test import add
    assert add(2, 3) == 5

def test_subtract() -> None:
    from cava_ci_test import subtract
    assert subtract(5, 3) == 2

def test_multiply() -> None:
    from cava_ci_test import multiply
    assert multiply(2, 3) == 6
