# """
# Домашнее задание №1
# Функции и структуры данных
# """
def power_numbers(*numbers):
    newlist = []
    for item in numbers:
        newlist.append(item ** 2)
    print(newlist)
    return(newlist)

# """
#     функция, которая принимает N целых чисел,
#     и возвращает список квадратов этих чисел
# power_numbers(1, 2, 5, 7)
#     <<< [1, 4, 25, 49]
#     """

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(x):
    if x == 1:
        n = False
    elif x == 2:
        n = True
    i = 2
    while i < x:
        if x % i == 0:
            n = False
            break
        i += 1
        if i == x:
            n = True
    return(n)

def filter_numbers(number_list, filter_type):
    if filter_type == ODD:
        return [number for number in number_list if number % 2 != 0]
    if filter_type == EVEN:
        return [number for number in number_list if number % 2 == 0]
    if filter_type == PRIME:
        return [number for number in number_list if is_prime(number) == True]

# print(filter_numbers ([2, 3, 4, 5, 7], ODD))
# print(filter_numbers([2, 3, 4, 5], EVEN))
# print(filter_numbers([1, 2, 11, 13, 23, 24, 45], PRIME))
    # """
    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа
    # (выбор производится передачей дополнительного аргумента)


    # <<< [1, 3]
    #
    # <<< [2, 4]
    # """
