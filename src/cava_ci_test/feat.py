def add(x: int, y: int) -> int:
    """Add two integers. Dummy feature for testing CI/CD pipelines."""
    return x + y

def subtract(x: int, y: int) -> int:
    """Subtract two integers. Dummy feature for testing CI/CD pipelines."""
    return x - y

def multiply(x: int, y: int) -> int:
    """Multiply two integers. Dummy feature for testing CI/CD pipelines."""
    return x * y

def divide(x: int, y: int) -> float:
    # add error on purpose so we can see the fix bit
    return x / y