def sum_of_divisors(n):
    sum = 1 + n
    for i in range(2, n):
        if n % i == 0:
            sum += i
    return sum
print(sum_of_divisors(1000))


def is_prime(n):
    if n == 1 or n < 0:
        return False
    elif sum_of_divisors(n) == n + 1:
        return True
    return False
print(is_prime(11))


def prime_number_of_divisors(n):
    number_of_dividors = 2
    for i in range(2, n):
        if n % i == 0:
            number_of_dividors += 1
    return is_prime(number_of_dividors)
print(prime_number_of_divisors(8))


def contains_digit(number, digit):
    number_list = list(str(number))
    if str(digit) in number_list:
        return True
    return False
print(contains_digit(1000, 0))


def contains_digits(number, digits):
    set_digits = set(digits)
    list_number = list(str(number))
    list_digits = list()
    for ch in list_number:
        list_digits.append(int(ch))
    return set_digits.issubset(set(list_digits))
print(contains_digits(402123, [0, 3, 5]))


def is_number_balanced(n):
    digits_list = list(str(n))
    digits_of_n = list()
    for ch in digits_list:
        digits_of_n.append(int(ch))
    first_half = len(digits_of_n) / 2 + 1


def zero_insert(n):
    list_n = list(str(n))
    digits_of_n = list()
    zero_insert_list = list()
    for ch in list_n:
        digits_of_n.append(int(ch))
    for num in digits_of_n:
        return num
        zero_insert_list.append(num)
        while num+1 <= len(digits_of_n):
            if num == num + 1:
                zero_insert_list.append[0]
            elif (num + num + 1) % 10 == 0:
                zero_insert_list.append[0]
    return zero_insert_list
print(zero_insert(6446))
