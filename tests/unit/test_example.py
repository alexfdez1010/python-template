"""Example unit tests.

These are simple examples to demonstrate testing patterns.
"""

import pytest


def test_basic_math():
    """Example: Test that 2 + 2 equals 4."""
    assert 2 + 2 == 4


def test_string_operations():
    """Example: Test string concatenation."""
    result = "Hello" + " " + "World"
    assert result == "Hello World"


def test_list_operations():
    """Example: Test list length."""
    my_list = [1, 2, 3, 4, 5]
    assert len(my_list) == 5


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (2, 2, 4),
        (5, 3, 8),
        (10, 20, 30),
    ],
)
def test_addition_parametrized(a, b, expected):
    """Example: Parametrized test for addition."""
    assert a + b == expected


def test_dictionary_operations():
    """Example: Test dictionary access."""
    data = {"name": "John", "age": 30}
    assert data["name"] == "John"
    assert data["age"] == 30
