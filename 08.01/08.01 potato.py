from random import *
'''
#import random
#import random as rnd
# randint, choice,
num_1 = randint(1, 10) # создает случайное число от 1 до 10
num_2 = randint(1,10)
print(num_1)
print(num_2)
print(num_1 + num_2)

arr = [1,5,2,3,4]
# choice() выбирает случайным образом выражение из списка\кортежа\словаря
print('CHOICE: ')
print(choice(arr))

# random() создает абсолютно произвольное число
print(random())

# Task 1 - Hobby-dobby
random_number = randint(1, 6)
number = int(input('Enter a number: '))
if number == random_number:
    print(True)
else:
    print(False)
    print(random_number)

from time import sleep
sleep(2) # заставляем программу "спать"
print('2 секунды прошло')

# Task 2 - Sleeper
count = 10
while count != 0:
    print(count)
    count -= 1
    sleep(1)
'''
from os.path import exists
# Link: https://www.youtube.com/watch?v=hO40YIass5s
# exists() проверяет наличие файла\папки и тд
path = 'C:/Users/Вита/Desktop/code/ddd.py'
print(exists(path))

'''
HOMEWORK
1. Познакомиться с os (cсылка выше)
2. random(). Написать программу, которая будет генерировать
случайное число и проверять его четность\нечетность
3. time(). Написать программу, которая будет выводить текущее время
(НА ГУГЛЕНИЕ)
4. На повторение. Написать переводчик градусов (Цельсии\Фаренгейты\Кельвины)
'''
