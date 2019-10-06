import math
import string



a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
some_str = 'I am a good developer. I am also a writer'
int_list = [0,2,0,4,0,7,10]
l = [5, 3, 4, 3, 4]
l1 = [1,2,3,4,6,7,8]

def func_1(a, b):
    return list(set(a) & set(b))


def func_2(string):
    return string.count('a')

def func_3(num, _pow=3):
    flag = False
    for i in range(num):
        if i ** _pow == num:
            flag = True
            break
    return flag

def func_4(num):
    if len(str(num)) > 1:
        num = str(sum([int(i) for i in str(num)]))
        if len(num) > 1:
            return func_4(num)
        else:
            return int(num)
    else:
        return num

def func_5(sqc: list):
    sqc.sort(key=lambda i: i == 0)
    return sqc

def func_6(sqnc: list):
    start = sqnc[0]
    step = sqnc[1] - sqnc[0]
    stop = sqnc[-1]
    return list(range(start, stop+1, step)) == sqnc

def func_7(l):
    for i in l:
        if l.count(i) == 1:
            return i

def func_8(l):
    contr_list = list(range(l[0], l[-1]+1))
    return list(set(contr_list) ^ set(l))[0]

def func_9(l):
    count = 0
    for i in l:
        if isinstance(i, tuple):
            break
        else:
            count += 1
    return count

def func_10(s):
    return s[::-1]

def func_11(num):
    return f'{num // 60}:{num % 60}'

def func_12(s):
    s = "".join((char if char.isalpha() else " ") for char in s).split()
    return max(s, key=len)

def func_13(s):
    return ' '.join(s.split()[::-1])

def func_14(num):
    a = 0
    b = 1
    fib_list = []
    if num <= 1:
        return 1
    for i in range(num):
        a, b = b, a+b
        fib_list.append(a)

    return fib_list

def func_15(n: list):
    return [i for i in n if i % 2 == 0]

def func_16(rang: int):
    sum_of_range = 0
    for i in range(1, rang+1):
        sum_of_range += i
    return sum_of_range

def func_17(num):
    return math.factorial(num)

def func_18(s: str):
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


def func_19(s: str):
    return ''.join(sorted(list(s)))

def func_20(num, num1):
    if num < num1:
        return True
    elif num > num1:
        return False
    else:
        return '1'

print(1 ** (1./3.))