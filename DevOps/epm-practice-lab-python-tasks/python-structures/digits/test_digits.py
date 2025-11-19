import pytest
from digits import sum_digits

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (5, 5),
        (321, 6),
        (12345, 15),
        (999, 27),
    ],
)
def test_sum_digits(n, expected):
    assert sum_digits(n) == expected

def test_negative_raises():
    with pytest.raises(ValueError):
        sum_digits(-1)

