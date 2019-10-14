import unittest
from unittest import mock
import math
import my_func


class TestTwoList(unittest.TestCase):

    def test_list_intersection(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(my_func.list_intersection(a, b), [1, 2, 3, 5, 8, 13])

    def test_count_an_element_in_str(self):

        string = 'I am a good developer.I am also a writer'
        self.assertEqual(my_func.count_an_element_in_str(string), 5)

    def test_int_to_base_of_three_true(self):
        nums = 27, 81, 3, 9
        for num in nums:
            with self.subTest(num=num):
                self.assertTrue(my_func.int_to_base_of_three(num))

    def test_int_to_base_of_three_false(self):
        nums = 4, 6, 12
        for num in nums:
            with self.subTest(num=num):
                self.assertFalse(my_func.int_to_base_of_three(num))

    def test_sum_of_digits(self):
        num = 43
        self.assertEqual(my_func.sum_of_digits(num), 7)

    def test_push_zeros_to_end(self):
        a = [0, 2, 0, 3, 0, 4, 6, 7, 10]
        b = [2, 3, 4, 6, 7, 10, 0, 0, 0]
        self.assertEqual(my_func.push_zeros_to_end(a), b)

    def test_is_arithmetic_progression(self):
        a = [5, 7, 9, 11]
        b = [5, 7, 9, 10, 11, 16]
        c = [5, 8, 11, 14]
        self.assertTrue(my_func.is_arithmetic_progression(a))
        self.assertFalse(my_func.is_arithmetic_progression(b))
        self.assertTrue(my_func.is_arithmetic_progression(c))

    def test_count_elements(self):
        list_int = [5, 3, 4, 3, 4]
        self.assertEqual(my_func.count_elements(list_int), 5)

    def test_find_missed_element(self):
        list_int = [1, 2, 3, 4, 6, 7, 8]
        self.assertEqual(my_func.find_missed_element(list_int), 5)

    def test_count_el_bef_tuple(self):
        list_int_tuple = [1, 2, 3, (1, 2), 3]
        self.assertEqual(my_func.count_el_bef_tuple(list_int_tuple), 3)

    def test_reverse_str(self):
        string = 'Hello World and Coders'
        self.assertEqual(my_func.reverse_str(string), 'sredoC dna dlroW olleH')

    def test_hours_minutes(self):
        num = 63
        num1 = 137
        self.assertEqual(my_func.hours_minutes(num), '1:3')
        self.assertEqual(my_func.hours_minutes(num1), '2:17')

    def test_find_longest_word(self):
        s = 'fun&!! time'
        s1 = 'I love dogs'
        self.assertEqual(my_func.find_longest_word(s), 'time')
        self.assertEqual(my_func.find_longest_word(s1), 'love')

    @mock.patch('builtins.input', return_value='My name is Michele')
    def test_revert_word_order(self, value):
        self.assertEqual(my_func.revert_word_order(), 'Michele is name My')

    @mock.patch('builtins.input', return_value=7)
    def test_fibonacci(self, value):
        self.assertEqual(my_func.fibonacci(), [1, 1, 2, 3, 5, 8, 13])

    def test_find_even(self):
        a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(my_func.find_even(a), [4, 16, 36, 64, 100])

    @mock.patch('builtins.input', return_value=4)
    def test_sum_of_int_range(self, value):
        self.assertEqual(my_func.sum_of_int_range(), 10)

    def test_find_factorial(self):
        num = 4
        fact_num = math.factorial(num)
        self.assertEqual(my_func.find_factorial(num), fact_num)

    def test_reorder_str_char(self):
        string = 'abcd'
        output = 'bcdE'
        self.assertEqual(my_func.reorder_str_char(string), output)

    def test_to_alphabet_order(self):
        string = 'edcba'
        output = 'abcde'
        self.assertEqual(my_func.to_alphabet_order(string), output)

    def test_compare_two_ints(self):
        num = 10
        num1 = 20
        num2 = 10
        self.assertEqual(my_func.compare_two_ints(num, num2), '-1')
        self.assertTrue(my_func.compare_two_ints(num, num2))
        self.assertFalse(my_func.compare_two_ints(num1, num2))


if __name__ == '__main__':
    unittest.main()
