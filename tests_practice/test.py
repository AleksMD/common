import unittest
from unittest import mock
import math
from my_func import func_1, func_2, func_3, func_4, func_5, func_6, func_7, \
    func_8, func_9, func_10, func_11, func_12, func_13, func_14, func_15, \
    func_16, func_17, func_18, func_19, func_20


class TestTwoList(unittest.TestCase):

    def test_func_1(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(func_1(a, b), [1, 2, 3, 5, 8, 13])

    def test_func_2(self):

        string = 'I am a good developer.I am also a writer'
        self.assertEqual(func_2(string), 5)

    def test_func_3_true(self):
        nums = 27, 81, 3, 9
        for num in nums:
            with self.subTest(num=num):
                self.assertTrue(func_3(num))

    def test_func_3_false(self):
        nums = 4, 6, 12
        for num in nums:
            with self.subTest(num=num):
                self.assertFalse(func_3(num))

    def test_func_4(self):
        num = 43
        self.assertEqual(func_4(num), 7)

    def test_func_5(self):
        a = [0, 2, 0, 3, 0, 4, 6, 7, 10]
        b = [2, 3, 4, 6, 7, 10, 0, 0, 0]
        self.assertEqual(func_5(a), b)

    def test_func_6(self):
        a = [5, 7, 9, 11]
        b = [5, 7, 9, 10, 11, 16]
        c = [5, 8, 11, 14]
        self.assertTrue(func_6(a))
        self.assertFalse(func_6(b))
        self.assertTrue(func_6(c))

    def test_func_7(self):
        list_int = [5, 3, 4, 3, 4]
        self.assertEqual(func_7(list_int), 5)

    def test_func_8(self):
        list_int = [1, 2, 3, 4, 6, 7, 8]
        self.assertEqual(func_8(list_int), 5)

    def test_func_9(self):
        list_int_tuple = [1, 2, 3, (1, 2), 3]
        self.assertEqual(func_9(list_int_tuple), 3)

    def test_func_10(self):
        string = 'Hello World and Coders'
        self.assertEqual(func_10(string), 'sredoC dna dlroW olleH')

    def test_func_11(self):
        num = 63
        num1 = 137
        self.assertEqual(func_11(num), '1:3')
        self.assertEqual(func_11(num1), '2:17')

    def test_func_12(self):
        s = 'fun&!! time'
        s1 = 'I love dogs'
        self.assertEqual(func_12(s), 'time')
        self.assertEqual(func_12(s1), 'love')

    @mock.patch('builtins.input', return_value='My name is Michele')
    def test_func_13(self, value):
        self.assertEqual(func_13(), 'Michele is name My')

    @mock.patch('builtins.input', return_value=7)
    def test_func_14(self, value):
        self.assertEqual(func_14(), [1, 1, 2, 3, 5, 8, 13])

    def test_func_15(self):
        a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(func_15(a), [4, 16, 36, 64, 100])

    @mock.patch('builtins.input', return_value=4)
    def test_func_16(self, value):
        self.assertEqual(func_16(), 10)

    def test_func_17(self):
        num = 4
        fact_num = math.factorial(num)
        self.assertEqual(func_17(num), fact_num)

    def test_func_18(self):
        string = 'abcd'
        output = 'bcdE'
        self.assertEqual(func_18(string), output)

    def test_func_19(self):
        string = 'edcba'
        output = 'abcde'
        self.assertEqual(func_19(string), output)

    def test_func_20(self):
        num = 10
        num1 = 20
        num2 = 10
        self.assertEqual(func_20(num, num2), '1')
        self.assertTrue(func_20(num, num1))
        self.assertFalse(func_20(num1, num))


if __name__ == '__main__':
    unittest.main()
