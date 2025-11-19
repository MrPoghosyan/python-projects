import pytest

from loop import factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial_values(n, expected):
    assert factorial(n) == expected


def test_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)

