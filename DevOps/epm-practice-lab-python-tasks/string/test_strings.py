import pytest
from strings import is_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcba", True),
        ("test", False),
        ("Aba", True),  # case insensitive
        ("", True),     # empty string
        ("a", True),    # single char
        ("abccba", True),
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected

