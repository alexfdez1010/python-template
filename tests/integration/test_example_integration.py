"""Example integration tests.

These tests demonstrate integration testing patterns without mocks.
"""


def test_multiple_operations():
    """Example: Test multiple operations together."""
    result = 10 + 5
    result = result * 2
    result = result - 10
    assert result == 20


def test_string_and_list_integration():
    """Example: Test string and list operations together."""
    words = ["Hello", "World"]
    sentence = " ".join(words)
    assert sentence == "Hello World"
    assert len(sentence) == 11


def test_data_processing():
    """Example: Test processing a list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    assert total == 15
    assert average == 3.0


def test_nested_data_structures():
    """Example: Test working with nested data."""
    users = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
    ]
    
    # Get all scores
    scores = [user["score"] for user in users]
    assert len(scores) == 3
    assert max(scores) == 92
    assert min(scores) == 78
