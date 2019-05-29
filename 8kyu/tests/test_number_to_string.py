import unittest
import number_to_string as n2s

class TestNumbertoString(unittest.TestCase):
    def test_number_to_string(self):
        self.assertEqual(n2s.number_to_string(67), '67')
        self.assertEqual(n2s.number_to_string(12.3), '12.3')


if __name__ == '__main__':
    unittest.main()
