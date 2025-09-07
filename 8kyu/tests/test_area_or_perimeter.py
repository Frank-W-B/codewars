import unittest
import area_or_perimiter as ap


class TestAreaOrPerimiter(unittest.TestCase):
    # 6, 10 --> 32
    # 3, 3 --> 9
    def test_area_or_perimiter(self):
        self.assertEqual(ap.area_or_perimeter(6, 10), 32)
        self.assertEqual(ap.area_or_perimeter(3, 3), 9)


if __name__ == '__main__':
    unittest.main()
