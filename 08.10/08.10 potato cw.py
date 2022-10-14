from time import sleep # sleep заставляет программу поспать

# Dynamic object (Динамический тип данных)
# Строка
word = 'text'
# letter работает внутри цикла и сохраняет последниий результат
for letter in word:
    sleep(2) # Сон на 2 секунды
    print(letter)

# Range case (Конструкция range)
for number in range(0,10):
    print(number)
print('RANGE CASE #2')
# Range case 2
for number in range(5):# range(0, 5)
    print(number)

# Range case 3
print('STEP')
for number in range(0, 10, 2):
    print(number)

# len(obj) - подсчитывает кол-во символов в динамическом obj
print(len('dog'))

word = 'dog'
for index in range(len(word)): # BAD PRACTICE
    print(word[index])

# Task 1 - range minus
print('TASK #1')
for elem in range(10, 0, -1):
    print(elem)

# Task 2 - odd symbols word (Четные буквы по индексу)
print('TASK #2')
word = input('Введите слово: ')
word_length = len(word)
for letter in range(0, word_length, 2):
    print(word[letter])

# Цикл в цикле
for index in range(5):
    print(f'INDEX: {index}')
    for sub_index in range(5):
        print(f'SUBINDEX: {sub_index}')

