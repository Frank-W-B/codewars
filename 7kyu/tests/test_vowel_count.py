import unittest
import vowel_count as vc


class TestVowelCount(unittest.TestCase):
    def test_vowel_count(self):
        self.assertEqual(vc.get_count('Every rose has its thorn.'), 7)
        self.assertEqual(vc.get_count('Xyzzy'), 0)


if __name__ == '__main__':
    unittest.main()
