
# Task 1 - Check number
number = int(input('Enter a number: '))
if number > 0:
    print('+')
elif number < 0:
    print('-')
else:
    print('0')

# Task 2 - BMI 
width = int(input('Enter mass: '))
height = int(input('Enter height '))
index = width / height ** 2
if 16.5 < index < 25:
    print('OK')
else:
    print('Error')

# Task 3 - Swapcase
word = input('Enter a word: ')
print(word.swapcase())

# Task 4 - Random index from string
from random import randint
word = input('Word: ')
index = randint(0, len(word) - 1)
if index % 2 == 0:
    print(word[index])
else:
    print('odd string index')
