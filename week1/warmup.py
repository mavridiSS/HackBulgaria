def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)    # see below
        a, b = b, a + b
    return result
print(fibonacci(5))


def sum_of_digits(n):
    if n < 0:
        n = n * -1
    result = 0
    while n > 0:
        result += n % 10
        n = n // 10
    return result
print(sum_of_digits(-10))


def fact_digits(n):
    result = 0
    while n > 0:
        result += factorial(n % 10)
        n = n // 10
    return result
print(fact_digits(999))


def palindrome(obj):
    obj = str(obj)
    if obj == obj[::-1]:
        return True
    return False
print(palindrome(121))


def to_digits(n):
    return list(str(n))
print(to_digits(123))


def to_list(n):
    return list(str(n))
print(to_list(2222))


def to_number(digits):
    str1 = ''.join(str(numb) for numb in digits)
    return int(str1)
print(to_number([9, 9, 9, 9, 9]))


def count_vowels(str):
    vowels_list = list("aeiouy")
    counter = 0
    for ch in str.lower():
        if ch in vowels_list:
            counter += 1
    return counter
print(count_vowels("Python"))


def count_consonants(str):
    consonants_list = list("bcdfghjklmnpqrstvwxz")
    counter = 0
    for ch in str.lower():
        if ch in consonants_list:
            counter += 1
    return counter
print(count_consonants("Python"))


def char_histogram(string):
    my_dict = {}
    for ch in string:
        my_dict[ch] = string.count(ch)
    return my_dict
print(char_histogram("AAAAaaa!!!"))


def p_score(n):
    n_reversed = int(str(n)[::-1])
    if palindrome(n):
        return 1
    return 1 + p_score(n + n_reversed)
print(p_score(48))


def is_increasing(seq):
    if seq == sorted(seq):
        return True
    return False
print(is_increasing([5, 6, 8]))


def is_decreasing(seq):
    if seq == sorted(seq, reverse=True):
        return True
    return False
print(is_decreasing([5, 6, 8]))


def next_hack(n):
    bin_number = "{0:b}".format(n)
    bin_in_string = str(int(bin_number))
    if palindrome(bin_number) and bin_in_string.count("1") % 2 != 0:
        return n
    return next_hack(n + 1)
print(next_hack(10))
