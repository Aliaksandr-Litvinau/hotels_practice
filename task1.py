import unittest


# ЗАДАЧА 1
def convert_to_string(num: int) -> str:
    """
    Функция принимает целое число и возвращает строку с этим числом и словом
    'компьютер' в правильной форме множественного числа.
    """
    last_digit = num % 10
    if last_digit == 1 and num % 100 != 11:
        plural_form = "компьютер"
    elif 2 <= last_digit <= 4 and (num % 100 < 10 or num % 100 >= 20):
        plural_form = "компьютера"
    else:
        plural_form = "компьютеров"
    return f"{num} {plural_form}"


class TestConvertToString(unittest.TestCase):
    def test_singular(self):
        self.assertEqual(convert_to_string(1), "1 компьютер")
        self.assertEqual(convert_to_string(21), "21 компьютер")
        self.assertEqual(convert_to_string(101), "101 компьютер")

    def test_plural_2_4(self):
        self.assertEqual(convert_to_string(2), "2 компьютера")
        self.assertEqual(convert_to_string(3), "3 компьютера")
        self.assertEqual(convert_to_string(4), "4 компьютера")
        self.assertEqual(convert_to_string(22), "22 компьютера")
        self.assertEqual(convert_to_string(33), "33 компьютера")
        self.assertEqual(convert_to_string(44), "44 компьютера")

    def test_plural_other(self):
        self.assertEqual(convert_to_string(5), "5 компьютеров")
        self.assertEqual(convert_to_string(10), "10 компьютеров")
        self.assertEqual(convert_to_string(15), "15 компьютеров")
        self.assertEqual(convert_to_string(20), "20 компьютеров")
        self.assertEqual(convert_to_string(25), "25 компьютеров")
        self.assertEqual(convert_to_string(100), "100 компьютеров")


if __name__ == "__main__":
   unittest.main()
