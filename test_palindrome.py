from palindrome import is_palindrome

def test_palindrome_true():
    assert is_palindrome('racecar')

def test_palindrome_false():
    assert not is_palindrome('asertd')
