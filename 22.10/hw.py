# Task 1 - Multiply
a = int(input('Number 1: '))
b = int(input('Number 2: '))

print(f'{a} * {b} = {a * b}')

# Task 2 - Acceptable pwd
pwd = input('Enter pwd')

if len(pwd) > 6:
    print(True)
else:
    print(False)

# Task 3 - Backward string

word = input('Enter any word')

# Case 1 - [::-1]
print(f'Reverse version (V 1.0): {word[::-1]}')

# Case 2 - ''.join(reversed(word))
result = ''.join(reversed(word))
print(f'Reverse version (V 1.0): {result}')

# Task 4 - Is even

number = int(input('Number: '))
print(number % 2) # True or False

# Task 5 - First word
string = input('Enter any string here: ')
space = string.find(' ')
print(f'First word is: {string[0:space]}')

# Task 6 - FizzBuzz
number = int(input('Enter number: '))

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')

# Task 7 - Correct Sentence
string = input('Enter any word without dot in the end of the word: ')
print(string.capitalize() + '.')

# Task 8 - Number length
from random import randint
number = randint(10000,100000)
print(f'Amount digits in number {number}: {len(str(number))}')

# Task 9 - Max digits
number = int(input('Enter any number: '))
arr = []
for digit in str(number):
    arr.append(int(digit))

print(f'ARRAY: {arr}')
print(f'MAX VALUE FROM ARRAY: {max(arr)}')

# Task 10 - Find Zeros
digit = '1010101000100100010100010010010'
zeroes_amount = 0
for dig in digit:
    if dig != 0:
        zeroes_amount = 0
    else:
        zeroes_amount += 1

print(f'Zeroes: {zeroes_amount}')
