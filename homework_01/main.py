# """
# Домашнее задание №1
# Функции и структуры данных
# """
def power_numbers(*numbers):
    newlist = []
    for item in numbers:
        newlist.append(item ** 2)
    print(newlist)
power_numbers(1, 2, 5, 7)
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
        n = 0
    elif x == 2:
        n = 1
    i = 2
    while i < x:
        if x % i == 0:
            n = 0
            break
        i += 1
        if i == x:
            n = 1
    return(n)

def filter_numbers():
    if filter_type == ODD:
        print([number for number in number_list if number % 2 != 0])
    if filter_type == EVEN:
        print([number for number in number_list if number % 2 == 0])
    if filter_type == PRIME:
        is_prime()
        for item in number_list:
            if item in is_prime() == 1:
                print(item)

# filter_numbers([1, 2, 24, 45], PRIME)
    # """
    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа
    # (выбор производится передачей дополнительного аргумента)
    #
    filter_numbers([1, 2, 3], ODD)
    # <<< [1, 3]
    filter_numbers([2, 3, 4, 5], EVEN)
    # <<< [2, 4]
    # """
