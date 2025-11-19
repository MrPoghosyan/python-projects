"""
Calculate n!. n! = 1 * 2 * 3 * … * (n-1) * n,  0! = 1. n >= 0.
"""

def factorial(n: int) -> int:
    """Return factorial of a non-negative integer ''n''.
    Args:
        n: non-negative integer
    Returns:
        n! as int
    Raises:
        ValueError: if n is negative"""

    if n < 0:
        raise ValueError("n must be non-negative")
    result =1
    # Multipiy from 2 to n inclusive (1 is neutral)
    for i in range(2, n + 1):
        result *= i
    return result

def main() -> None:
    """Factorial calculation."""
    # Read integer from stdin and print its factorial.
    # Read input, strip whitespace, convert to int
    n = int(input().strip())
    print(factorial(n))


if __name__ == "__main__":
    main()
