import unittest
import string_to_number as s2n


class TestNumbertoString(unittest.TestCase):
    def test_string_to_number(self):
        self.assertEqual(s2n.string_to_number("1234"), 1234)
        self.assertEqual(s2n.string_to_number("103"), 103)
        self.assertEqual(s2n.string_to_number("80002351"), 80002351)

if __name__ == '__main__':
    unittest.main()
