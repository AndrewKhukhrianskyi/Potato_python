'''
# Функцию принято называть глаголом
def add_2():
    # Читаемость определяется вложенностью
    number = int(input('Введи число: '))
    print(number * 2)

# Для вызова функции нужно обратиться по ее имени
add_2()

# Аргументы - параметры, которые нужны для работы ф-и
# def ...(аргумент, аргумент2, ...,)

print('FUNCTION 2')
def add_2(number):
    print(number * 2)

add_2(5)

n = int(input('Введи число: '))

add_2(n)

# potato_team = [1,2,3,4,5,6,7,8]
'''
import random
# Аргументы по умолчанию - это параметры которые задаются по умолчанию (дефолтные выражения)
# def ...(аргумент = ...)
def add_2(number = 1):
    print(number * 2)

# Ошибки при работе с функциями
# Функция работает с тем числом аргументов, которые ей передаются
def say_hello(name):
    print(f"Привет, {name}!")


#say_hello() # Error
#say_hello("Иван", "Иванов") # Error
def say_hello(name = 'Blank',
              surname = 'Blank'):
    print(f"Welcome, {name} {surname}!")

# В функции можно изменять конкретный параметр по умолчанию
# say_hello(name = "Адам", surname = 'Милошевич')

def add_two(number, number2):
    print(number + number2)

def set_square_perimeter(square_line):
    print(square_line * 4)

# "Мой дорогой товарищ!" -> "Мой"
def find_first_word(sentence):
    # .find()
    space = sentence.find(' ')
    print(sentence[0:space])

    # .split()
    sentence = sentence.split() # ['Мой', "дорогой"...]
    print(sentence[0])


team_list = [1,2,3,4,5,6,7,8]
print(random.shuffle(
print(result[0:3])
print(result[4:])






