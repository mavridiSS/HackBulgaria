import math


def count_words(arr):
    return {word: arr.count(word) for word in arr}
print(count_words(["apple", "banana", "apple", "pie"]))


def unique_words_count(arr):
    return len([ch for ch in count_words(arr).items()])
print(unique_words_count(["HELLO!"] * 10))


def nan_expand(times):
    NaN = "Not a "
    result = NaN * times
    result += "NaN"
    return result
print(nan_expand(3))


def iterations_of_nan_expand(expanded):
    return expanded.count("Not a")
print(iterations_of_nan_expand(
    'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))


def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


def is_prime(n):
    return sum_of_divisors(n) == n + 1


def dividors(n):
    return [x for x in range(2, n / 2 + 1) if n % x == 0]


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


def divide_count(n, k):
    times = 0
    while n != 1 and n % k == 0:
        times += 1
        n = n // k
    return times


def prime_factorization(n):
    prime = 2
    result = []
    while n > 1:
        times = divide_count(n, prime)
        if times != 0:
            result.append((prime, times))
            n = n // prime ** times
        prime = next_prime(prime)
    return result
print(prime_factorization(356))


def prime_factorization2(n):
    prime_numbers = [3, 5]
    result = []
    for prime in prime_numbers:
        if n > 1:
            times = divide_count(n, prime)
            if times != 0:
                result.append((prime, times))
                n = n // prime ** times
    return result
print(prime_factorization2(45))


def take_same(arr):
    same = arr[0]
    result = [same]
    n = len(arr)
    index = 1
    while index < n and arr[index] == same:
        result.append(arr[index])
        index += 1
    return result


def find_equals(arr):
    result = []
    while len(arr) > 0:
        curr_group = take_same(arr)
        result.append(curr_group)
        arr = arr[len(curr_group):]
    return result
print(find_equals([1, 1, 1, 2, 3]))


def max_consecutive(items):
    return len(max(find_equals(items)))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def groupby(func, seq):
    g = func
    groupby_dict = {}
    key_list = list(set([g(x) for x in seq]))
    value_list = []
    index = 0
    n = len(key_list)
    for numb in seq:
        while index < n:
            if g(numb) == key_list[index]:
                value_list.append(numb)
                groupby_dict[key_list[index]] = value_list
            index += 1
    return groupby_dict
print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))


def prepare_meal(number):
    result = ""
    factorized_number = prime_factorization2(number)
    if factorized_number == []:
        return result
    for pair in factorized_number:
        if pair[0] == 3:
            result += "spam " * pair[1]
        if pair[0] == 5 and result != "":
            result += "and " + "eggs " * pair[1]
        elif pair[0] == 5:
            result += "eggs " * pair[1]
    return result
print(prepare_meal(45*25))


def is_an_bn(word):
    index = 0
    an_counter = 0
    bn_counter = 0
    while index < len(word):
        if word[index] == 'a':
            an_counter += 1
        index += 1
    word_sliced = word[an_counter:]
    index1 = 0
    while index1 < len(word_sliced):
        if word_sliced[index1] == 'b':
            bn_counter += 1
        index1 += 1
    if an_counter == bn_counter and an_counter + bn_counter == len(word):
        return True
    return False
print(is_an_bn("aaabbbaaabbb"))
