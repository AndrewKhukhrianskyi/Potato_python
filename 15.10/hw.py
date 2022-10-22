# Task 1 - Distance
speed, time = 1, 1 
while True:
    speed = int(input('SPEED: '))
    time = int(input('TIME: '))
    if speed < 0 or time < 0:
        break
    print(f'DISTANCE: {speed * time} km')

# Task 2 - By 2
from random import randint
number = randint(1000000, 9999999) 
while number > 1:
    number /= 2
    print(round(number,2))

# Task 3 - Count elements
word = input('Enter word: ')
element = input('Enter find element: ')
count = 0
for letter in word:
    if element == letter:
        count += 1

print(f'{element} in {word} meets {count} times!')