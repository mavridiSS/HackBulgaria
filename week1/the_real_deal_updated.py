def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])
print(sum_of_divisors(7))


def is_prime(n):
    return sum_of_divisors(n) == n + 1
print(is_prime(-11))


def prime_number_of_divisors(n):
    return is_prime(len([x for x in range(1, n + 1) if n % x == 0]))
print(prime_number_of_divisors(7))


def to_digits(n):
    return [int(x) for x in str(n)]
print(to_digits(1231))


def contains_digit(number, digit):
    return digit in to_digits(number)
print(contains_digit(1000, 0))


def contains_digits(number, digits):
    return set(digits).issubset(set(to_digits(number)))
print(contains_digits(402123, [0, 3, 4]))


def is_number_balanced(n):
    number_list = to_digits(n)
    half = len(number_list) // 2
    if len(number_list) % 2 == 0:
        return (sum(number_list[0:half]) ==
                sum(number_list[half:len(number_list)]))
    return (sum(number_list[0:half]) ==
            sum(number_list[half + 1:len(number_list)]))
print(is_number_balanced(1238033))


def count_substrings(haystack, needle):
    return haystack.count(needle)
print(count_substrings("babababa", "baba"))


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0

    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit

    return result


def zero_insert(n):
    result = []
    digits = to_digits(n)

    start = 0
    end = len(digits)

    while start < end - 1:
        x = digits[start]
        y = digits[start + 1]

        result.append(x)

        if (x + y) % 10 == 0 or x == y:
            result.append(0)

        start += 1

    result.append(digits[start])

    return to_number(result)
print(zero_insert(6446))


def sum_matrix(m):
    return sum([num for i in m for num in i])
print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
