import pytest

from palindrome_pse_review import is_palindrome

def test_is_palindrome_racecar_returns_true():
    s = 'racecar'
    result = is_palindrome(s)
    assert result == True

def test_invalid_input_returns_false():
    s = 787
    with pytest.raises(TypeError):
        is_palindrome(s)

def test_nonis_palindrome_input_returns_false():
    s = "cookie run"
    result = is_palindrome(s)
    assert result == False

def test_function_returns_true():
    s = "kayak"
    assert is_palindrome(s) == True

def test_function_returns_false():
    s = "donut"
    assert is_palindrome(s) == False

def test_accepts_empty_string():
    assert is_palindrome("") == True
    
def test_accepts_space_and_exclamations():
    s = "   !!  k a y    !!a!k"
    assert is_palindrome(s) == True

def test_raises_type_error():
    with pytest.raises(TypeError):  # why does this pass when we return a string??
        is_palindrome([])