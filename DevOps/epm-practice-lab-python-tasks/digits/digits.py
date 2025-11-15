"""
Find sum of n-integer digits. n >= 0.
"""

def sum_digits(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    return sum(int(digit) for digit in str(n))

def main() -> None:
    """Sum of number digits."""
    n = int(input().strip())
    print(sum_digits(n))


if __name__ == "__main__":
    main()
