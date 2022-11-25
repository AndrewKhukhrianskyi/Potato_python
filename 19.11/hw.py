# Task 1 - Zero counter
from random import randint

random_number = randint(10000, 99999)

def count_zero(number):
    list_number = list(str(number))
    zero_count = 0

    for digit in list_number:
        if digit == '0':
            zero_count += 1
    print(f'Число {number} содержит {zero_count} нулей!') 


# Task 2 - Calculator
def calc(num, num2, operation):
    if operation == '+':
        print(num + num2)
    elif operation == '-':
        print(num - num2)
    elif operation == '*':
        print(num * num2)
    elif operation == '//':
        print(num // num2)
    else:
        print('Ошибка! Неизвестная операция')

count_zero(random_number)
calc(5, 2, '+')
calc(5, 2, '-')
calc(5, 2, '*')
calc(5, 2, '//')