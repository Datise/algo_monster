import unittest

from bts import BTSSolutions


class TestBTSVarities(unittest.TestCase):
    def test_first_match(self):
        result = BTSSolutions().first_match_in_arr([1,2,2,3,3,4,5,6,7,7,8], 2)
        self.assertEqual(result, 1)

    def test_only_one(self):
        result = BTSSolutions().first_match_in_arr([1], 1)
        self.assertEqual(result, 0)

    def test_only_three(self):
        result = BTSSolutions().first_match_in_arr([1,5,5], 5)
        self.assertEqual(result, 1)

    def test_missing(self):
        result = BTSSolutions().first_match_in_arr([2,3,4,5], 7)
        self.assertEqual(result, -1)

    # peak of mountain
    def test_peak_of_mtn(self):
        result = BTSSolutions().peak_of_mtn([2,3,4,5,4,3,2,1])
        self.assertEqual(result, 3)

    def test_peak_high_num(self):
        result = BTSSolutions().peak_of_mtn([0, 10, 3, 2, 1, 0])
        self.assertEqual(result, 1)

    def test_peak_low_count(self):
        result = BTSSolutions().peak_of_mtn([0, 10, 0])
        self.assertEqual(result, 1)
        
    # sqrt estimate
    def test_sqrt_estimate(self):
        result = BTSSolutions().sqrt_estimate(8)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()