import unittest
import remove_first_last_character as rflc


class TestRemoveFirstLastCharacter(unittest.TestCase):
    # Test cases
    # "1,2,3"      =>  "2"
    # "1,2,3,4"    =>  "2 3"
    # "1,2,3,4,5"  =>  "2 3 4"
    # ""     =>  Null
    # "1"    =>  Null
    # "1,2"  =>  Null

    def test_remove_first_last_character(self):
        self.assertEqual(rflc.remove_first_and_last_char("1,2,3"), "2")
        self.assertEqual(rflc.remove_first_and_last_char("1,2,3,4"), "2 3")
        self.assertEqual(rflc.remove_first_and_last_char("1,2,3,4,5"), "2 3 4")
        self.assertEqual(rflc.remove_first_and_last_char(""), None)
        self.assertEqual(rflc.remove_first_and_last_char("1"), None)
        self.assertEqual(rflc.remove_first_and_last_char("1, 2"), None)


if __name__ == "__main__":
    unittest.main()
