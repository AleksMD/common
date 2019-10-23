import math
import string


def list_intersection(a: list, b: list) -> list:
    """
        The function finds and returns common values from two lists
    :param a: any list
    :param b: any list
    :return: list with common values from list 'a' and list 'b'
    """
    return list(set(a) & set(b))


def count_an_element_in_str(any_str: str) -> int:
    """
        Counts symbol in a given string
    :param any_str: string instance where to count
    :return: count of an element to be found
    """
    return any_str.count('a')


def int_to_base_of_three(num: int) -> bool:
    """
    Finds if a given integer is logarithm with base of 3
    :param num: Integer to be tested
    :return: True or False
    """
    x = math.log(num, 3)
    return int(x) == x


def sum_of_digits(num: int) -> int:
    """
    Adds all digits from given number(e.g. 123 -> 6)
    :param num: given integer
    :return: sum of digits(in int format)
    """
    if len(str(num)) > 1:
        num = str(sum([int(i) for i in str(num)]))
        if len(num) > 1:
            return sum_of_digits(int(num))
        else:
            return int(num)
    else:
        return num


def push_zeros_to_end(sqnc: list) -> list:
    """
    Sorts a given list in order to place all zeros to the end of list
    :param sqnc: Given list
    :return: Sorted list
    """
    sqnc.sort(key=lambda i: i == 0)
    return sqnc


def is_arithmetic_progression(sqnc: list) -> bool:
    """
    Checks if  integers in a given list are in arithmetic progression
    :param sqnc: list with integers
    :return: True or False
    """
    start = sqnc[0]
    step = sqnc[1] - sqnc[0]
    stop = sqnc[-1]
    return list(range(start, stop+1, step)) == sqnc


def count_elements(l: list):
    """
    Counts all elements in  a given list and returns the one has been met
        less times.
    :param l: Given list
    :return: Element of list
    """
    for i in l:
        if l.count(i) == 1:
            return i


def find_missed_element(l: list) -> int:
    """
    Finds a missed element in a list of integers
        if the latter seems to be ordered
    :param l: List of integers
    :return: Missed elements
    """
    contr_list = list(range(l[0], l[-1]+1))
    return list(set(contr_list) ^ set(l))[0]


def count_el_bef_tuple(l: list) -> int:
    """
    Iterates through a given list and counts elements
        unless meet a tuple object
    :param l: Given list
    :return: Number of elements before tuple has been met
    """
    count = 0
    for i in l:
        if isinstance(i, tuple):
            break
        else:
            count += 1
    return count


def reverse_str(s: str) -> str:
    """
    Returns a given string in a reversed order.
    :param s: Given string
    :return: Reversed variant of given string
    """
    return s[::-1]


def hours_minutes(num: int) -> str:
    """
    Converts a given integer(minutes) to a string with hours, minutes and colon
        as a delimiter between them(e.g. 67 minutes -> '1:07')
    :param num: Minutes as integer
    :return: Hours and minutes as a string
    """
    return f'{num // 60}:{num % 60}'


def find_longest_word(s: str) -> str:
    """
    Choses the very first longest word in a given string. Non ascii letters
        and signs are not taken into account.
    :param s: Given string
    :return: The very first longest word.
    """
    s = "".join((char if char.isalpha() else " ") for char in s).split()
    return max(s, key=len)


def revert_word_order() -> str:
    """
    Asks user to enter any string and then reverts it
    :return: String in reverse order
    """
    user_str = input('Please, type some words: ')
    return ' '.join(user_str.split()[::-1])


def fibonacci() -> list:
    """
    Ask user to enter any number and then calculates fibonacci numbers till
    entered number
    :return: List with fibonacci sequence
    """
    user_num = int(input('Please, enter any number: '))
    a = 0
    b = 1
    fib_list = []
    if user_num <= 1:
        return [1]
    for i in range(user_num):
        a, b = b, a+b
        fib_list.append(a)

    return fib_list


def find_even(n: list) -> list:
    """
    Finds all even numbers in a given list and returns a new list with
        those numbers
    :param n: List with all numbers
    :return: List with even numbers
    """
    return [i for i in n if i % 2 == 0]


def sum_of_int_range() -> int:
    """
    Asks user to enter any number and then calculates a sum of all numbers in
        a range from 0 to the entered number
    :return: Sum of range in int format
    """
    input_num = int(input('Enter any number: '))
    sum_of_range = 0
    for i in range(1, input_num+1):
        sum_of_range += i
    return sum_of_range


def find_factorial(num: int) -> int:
    """
    Calculates and returns a factorial of a given number
    :param num: An integers which factorial should be found
    :return: Factorial of an given integer
    """
    return math.factorial(num)


def reorder_str_char(s: str) -> str:
    """
    Converts a given string in a way where all characters should be replaced
        with those one which possess next position in ascii letters order.
        If a new character is going to be a vowel, it should be an upper.
        The output string will not contain punctuation signs.
    :param s: String to be reordered
    :return: New string
    """
    vowels = 'aeiou'
    alphabet_dict = dict(enumerate(string.ascii_lowercase))
    normal_reversed_dict = {v: k+1 for k, v in alphabet_dict.items()}
    result = ''
    for char in s:
        char = alphabet_dict[normal_reversed_dict[char]]
        if char in vowels:
            result += char.upper()
        else:
            result += char
    return result


def to_alphabet_order(s: str) -> str:
    """
    Sort a given string according to the alphabet.
    :param s: String to be ordered
    :return: New string
    """
    return ''.join(sorted(list(s)))


def compare_two_ints(num: int, num1: int) -> 'True, False or -1':
    """
    Compares two numbers.
        If numbers are equal it returns string -1;
        elif number 1 less then number 2 it returns True;
        else (number 1 is greater than number 2) it returns False.
    :param num:
    :param num1:
    :return:
    """
    if num < num1:
        return True
    elif num > num1:
        return False
    else:
        return '-1'
