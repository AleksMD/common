import pytest
import my_func


class TestMyFuncModule:

    def test_list_intersection(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        assert my_func.list_intersection(a, b) == [1, 2, 3, 5, 8, 13]

    @pytest.mark.parametrize('any_string, expected_output',
                             [('I am a good developer.I am also a writer', 5)])
    def test_count_an_element_in_str(self, any_string, expected_output):
        assert my_func.count_an_element_in_str(any_string) == expected_output

    @pytest.mark.parametrize('num, result', [((3, 9, 27, 81), True),
                                             ((4, 19, 6, 5), False)])
    def test_int_to_base_of_three(self, num, result):
        for n in num:
            assert my_func.int_to_base_of_three(n) == result

    @pytest.mark.parametrize('num, result', [(43, 7), (193, 4), (225, 9)])
    def test_sum_of_digits(self, num, result):
        assert my_func.sum_of_digits(num) == result

    @pytest.mark.parametrize('list_of_int, result',
                             [([0, 2, 0, 3, 0, 4, 6, 7, 10],
                              [2, 3, 4, 6, 7, 10, 0, 0, 0])])
    def test_push_zeros_to_end(self, list_of_int, result):
        assert my_func.push_zeros_to_end(list_of_int) == result

    @pytest.mark.parametrize('list_of_int, result',
                             [([5, 7, 9, 11], True),
                              ([5, 7, 9, 10, 11, 16], False),
                              ([5, 8, 11, 14], True)])
    def test_is_arithmetic_progression(self, list_of_int, result):
        assert my_func.is_arithmetic_progression(list_of_int) == result

    @pytest.mark.parametrize('list_of_items, result',
                             [
                              ([5, 3, 4, 3, 4], 5),
                              (['a', 'b', 'a', 'c', 'c'], 'b')
                               ])
    def test_count_elements(self, list_of_items, result):
        assert my_func.count_elements(list_of_items) == result

    @pytest.mark.parametrize('list_of_int, result',
                             [([1, 2, 3, 4, 6, 7, 8], 5),
                              ([1, 3, 5, 6], 2)])
    def test_find_missed_element(self, list_of_int, result):
        assert my_func.find_missed_element(list_of_int) == result

    @pytest.mark.parametrize('list_of_items, result',
                             [([1, 2, 3, (1, 2), 3], 3),
                              ([1, 2, 3, 4, ('a', 'b')], 4)])
    def test_count_el_bef_tuple(self, list_of_items, result):
        assert my_func.count_el_bef_tuple(list_of_items) == result

    @pytest.mark.parametrize('string, result', [('Hello World and Coders',
                                                 'sredoC dna dlroW olleH'),
                                                ('Another one string.',
                                                 '.gnirts eno rehtonA')])
    def test_reverse_str(self, string, result):
        assert my_func.reverse_str(string) == result
