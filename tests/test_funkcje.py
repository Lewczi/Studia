import pytest
from funkcje_do_testow.funkcje import (
    is_palindrome,
    count_vowels,
    word_frequencies,
    calculate_discount,
    flatten_list,
    fibonacci,
    is_prime
)

def test_is_palindrome():
    assert is_palindrome("kajak") is True
    assert is_palindrome("Kobyła ma mały bok") is True
    assert is_palindrome("python") is False
    assert is_palindrome("") is True

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_count_vowels():
    assert count_vowels("Python") == 2
    assert count_vowels("AEIOU") == 5   
    assert count_vowels("bcd") == 0
    assert count_vowels("") == 0
    assert count_vowels("Próba żółwia") == 5

def test_calculate_discount():
    assert calculate_discount(100, 0.2) == 80.0
    assert calculate_discount(200, 1) == 0.0
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)

def test_flatten_list():
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert flatten_list([]) == []

def test_word_frequencies():
    wynik = word_frequencies("To be or not to be")
    assert wynik["to"] == 2
    assert wynik["be"] == 2
    assert word_frequencies("") == {}

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(4) is False
    assert is_prime(97) is True