import unittest
import remove_anchor as ra

class TestRemoveAnchor(unittest.TestCase):
    def test_remove_anchor(self):
        url1 = "www.codewars.com#about"
        url2 = "www.codewars.com/katas/?page=1#about"
        url3 = "www.codewars.com/katas/"
        ans1 = "www.codewars.com"
        ans2 = "www.codewars.com/katas/?page=1"
        ans3 = "www.codewars.com/katas/"
        self.assertEqual(ra.remove_url_anchor(url1), ans1)
        self.assertEqual(ra.remove_url_anchor(url2), ans2)
        self.assertEqual(ra.remove_url_anchor(url3), ans3)

if __name__ == '__main__':
    unittest.main()        

