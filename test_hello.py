import pytest
from hello import hello_world, add_numbers, factorial, is_palindrome

def test_hello_world():
    assert "CI/CD Test Successful" in hello_world()

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0.5, 0.5) == 1.0

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("python") is False
    assert is_palindrome("") is True