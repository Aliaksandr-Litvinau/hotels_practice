from typing import List
import unittest


# ЗАДАЧА 2
def get_divisors(n):
    """
    Функция для нахождения всех делителей числа.
    """
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


def find_common_divisors(numbers):
    """
    Функция находит общие делители для всех чисел в массиве.
    """
    if not numbers:
        return []
    # Находим общие делители для всех чисел
    common_divisors = set(get_divisors(numbers[0]))
    for num in numbers[1:]:
        common_divisors.intersection_update(get_divisors(num))
    return sorted(common_divisors)


class TestFindCommonDivisors(unittest.TestCase):
   def test_empty_list(self):
       self.assertEqual(find_common_divisors([]), [])

   def test_single_number(self):
       self.assertEqual(find_common_divisors([42]), [1, 2, 3, 6, 7, 14, 21, 42])

   def test_multiple_numbers(self):
       self.assertEqual(find_common_divisors([42, 12, 18]), [1, 2, 3, 6])
       self.assertEqual(find_common_divisors([10, 15, 20]), [1, 5])
       self.assertEqual(find_common_divisors([24, 36, 48]), [1, 2, 3, 4, 6, 12])

if __name__ == "__main__":
   unittest.main()
