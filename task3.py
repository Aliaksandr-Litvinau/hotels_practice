from typing import List
import unittest


def is_prime(num: int) -> bool:
    """
    Функция для проверки, является ли число простым.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes_in_range(start: int, end: int) -> List[int]:
    """
    Функция для нахождения всех простых чисел в заданном диапазоне.
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


class TestFindPrimesInRange(unittest.TestCase):
    def test_primes_in_range(self):
        self.assertEqual(find_primes_in_range(11, 20), [11, 13, 17, 19])
        self.assertEqual(find_primes_in_range(1, 10), [2, 3, 5, 7])
        self.assertEqual(find_primes_in_range(20, 30), [23, 29])
        self.assertEqual(find_primes_in_range(30, 40), [31, 37])


if __name__ == "__main__":
   unittest.main()
