from palindrome import is_palindrome

def test_palindrome_true():
    assert is_palindrome('asghjyt')

def test_palindrome_false():
    assert not is_palindrome('asertd')
