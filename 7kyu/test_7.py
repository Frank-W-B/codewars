import unittest
import max_len_diff


class TestMaxLength(unittest.TestCase):
   def test_mxdiflg(self):
        s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
        s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        correct_result = 13
        result = max_len_diff.mxdiflg(s1,s2)
        self.assertEqual(result, correct_result)

if __name__ == '__main__':
    unittest.main()
        

