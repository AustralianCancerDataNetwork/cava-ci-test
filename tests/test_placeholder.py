"""Smoke test to confirm the package is importable and the test suite runs."""


def test_import() -> None:
    import cava_ci_test  # noqa: F401


def test_placeholder() -> None:
    assert 1 + 1 == 2
