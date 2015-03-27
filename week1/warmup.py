def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    result = []
    a, b = 1, 1
    result.append(b)
    while len(result) < n:
        result.append(b)
        a, b = b, a + b
    return result


def sum_of_digits(n):
    if n < 0:
        n = n * -1
    result = 0
    while n > 0:
        result += n % 10
        n = n // 10
    return result


def fact_digits(n):
    result = 0
    while n > 0:
        result += factorial(n % 10)
        n = n // 10
    return result


def palindrome(obj):
    obj = str(obj)
    if obj == obj[::-1]:
        return True
    return False


def to_digits(n):
    return list(str(n))


def to_number(digits):
    str1 = ''.join(str(numb) for numb in digits)
    return int(str1)


def fib_number(n):
    return to_number(fibonacci(n))


def count_vowels(str):
    vowels_list = list("aeiouy")
    counter = 0
    for ch in str.lower():
        if ch in vowels_list:
            counter += 1
    return counter


def count_consonants(str):
    consonants_list = list("bcdfghjklmnpqrstvwxz")
    counter = 0
    for ch in str.lower():
        if ch in consonants_list:
            counter += 1
    return counter


def char_histogram(string):
    my_dict = {}
    for ch in string:
        my_dict[ch] = string.count(ch)
    return my_dict


def p_score(n):
    n_reversed = int(str(n)[::-1])
    if palindrome(n):
        return 1
    return 1 + p_score(n + n_reversed)


def is_increasing(seq):
    if seq == sorted(seq):
        return True
    return False


def is_decreasing(seq):
    if seq == sorted(seq, reverse=True):
        return True
    return False


def next_hack(n):
    n = n + 1
    bin_number = "{0:b}".format(n)
    bin_in_string = str(int(bin_number))
    if palindrome(bin_number) and bin_in_string.count("1") % 2 != 0:
            return n
    return next_hack(n)
