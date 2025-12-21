import re

def is_palindrome(text: str) -> bool:
    clean = "".join(char.lower() for char in text if char.isalnum())
    return clean == clean[::-1]

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n cannot be negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def count_vowels(text: str) -> int:
    return sum(1 for char in text.lower() if char in "yaeiouąęó")

def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Discount out of range")
    return float(price * (1 - discount))

def flatten_list(nested_list: list) -> list:
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def word_frequencies(text: str) -> dict:
    words = re.findall(r'\w+', text.lower())
    if not words:
        return {}
    return {word: words.count(word) for word in set(words)}

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True