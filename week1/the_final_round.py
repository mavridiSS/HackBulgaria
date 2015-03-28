import math


def count_words(arr):
    return {word: arr.count(word) for word in arr}


def unique_words_count(arr):
    return len([ch for ch in count_words(arr).items()])


def nan_expand(times):
    result = ""
    if times > 0:
        NaN = "Not a "
        result = NaN * times
        result += "NaN"
    return result


def iterations_of_nan_expand(expanded):
    nan_table = {}
    n = len(expanded)

    current_index = 0

    while True:
        current_expand = nan_expand(current_index)
        nan_table[current_expand] = current_index

        if len(current_expand) > n:
            break

    if expanded in nan_table:
        return nan_table[expanded]

    return False


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


def take_same(arr):
    same = arr[0]
    result = [same]
    n = len(arr)
    index = 1
    while index < n and arr[index] == same:
        result.append(arr[index])
        index += 1
    return result


def group(arr):
    result = []
    while len(arr) > 0:
        curr_group = take_same(arr)
        result.append(curr_group)
        arr = arr[len(curr_group):]
    return result


def max_consecutive(items):
    return len(max(group(items)))


def groupby(func, seq):
    g = func
    groupby_dict = {}
    key_list = list(set([g(x) for x in seq]))
    result = list()
    for key in key_list:
        for element in seq:
            if g(element) == key:
                result.append(element)
        groupby_dict[key] = result
        result = list()
    return groupby_dict


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


def reduce_file_path(path):
    splitted = [ch for ch in path.split("/") if ch != '.' and ch != ""]
    n = len(splitted) - 1
    result = list()
    while n >= 0:
        if splitted[n] == "..":
            result = splitted[0:n-1]
            n -= 2
        else:
            result.insert(0, splitted[n])
            n -= 1
    if result == list():
        return "/"
    else:
        result.insert(0, "")
        return "/".join(result)


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


def sum_digits(n):
    result = 0
    while n > 0:
        result += n % 10
        n = n / 10
    return result


def is_credit_card_valid(n):
    list_numbers = [int(i) for i in str(n)]
    index = 1
    while index < len(list_numbers):
        list_numbers[index] = list_numbers[index] * 2
        index += 2
    return sum(sum_digits(i) for i in list_numbers) % 10 == 0


def goldbach(n):
    result = list()
    curr_prime = 2
    while curr_prime <= n / 2:
        if is_prime(n - curr_prime):
            result.append((curr_prime, n - curr_prime))
        curr_prime = next_prime(curr_prime)
    return result


def magic_square(matrix):
    result = list()
    index_element = 0
    n = len(matrix)
    for row in matrix:
        result.append(sum(row))
    while index_element < n:
        result.append(sum([matrix[index][index_element]
                      for index in range(n)]))
        index_element += 1
    result.append(sum([matrix[index][index]
                  for index in range(n)]))
    result.append(sum([matrix[index][n - index - 1]
                  for index in range(n)]))
    return all([x == (n * (n ** 2 + 1)) / 2
                for x in result])


def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def dayofweek(y, m, d):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m < 3
    return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7


def friday_years(start, end):
    result = 0
    for year in range(start, end + 1):
        if leap_year(year):
            if dayofweek(year, 1, 1) == 5 or dayofweek(year, 1, 2) == 5:
                result += 1
        if not leap_year(year):
            if dayofweek(year, 1, 1) == 5:
                result += 1
    return result
