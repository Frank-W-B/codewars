import unittest
import count_divisible_numbers as cdn

class TestDivisibleNumbers(unittest.TestCase):
    def test_count_divisible_numbers(self):
        self.assertEqual(cdn.divisible_count(6, 11, 2), 3)
        self.assertEqual(cdn.divisible_count(101,9999999999999999999999999999999999999999999,11), 909090909090909090909090909090909090909081)

if __name__ == '__main__':
    unittest.main()
