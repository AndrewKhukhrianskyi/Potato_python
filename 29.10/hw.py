# Task 1 - Сумма чисел

string = 'jgdfsl ;ghlkd fsjh o 5 ei;sghsero 68 r jlkhs;elrl kjyh ;oster u 869 e'
arr = []
for num in string.split():
    if num.is_numeric():
        arr.append(int(num))

print(sum(arr))

# Task 2 - Кол-во цифр в числе
from random import randint
number = randint(100, 1000000)
print(f'Number: {number}')
print(f'Amount of digits: {len(str(number))}')

# Task 3 - Acceptable pwd (pt 2)
password = 'something'
if len(password) > 6 and not password.replace(' ', '').isalpha():
    print(True)
else:
    print(False)

# Task 4 - Acceptable pwd (pt 3)
if len(password) > 6 and not password.replace(' ', '').isalpha() and not password.isnumeric():
    print(True)
else:
    print(False)

# Task 5 - Goes Right After
word = 'some word'
first = 'o'
last = 'm'

index = word.find(first)
if word[index] == last:
    print(True)
else:
    print(False)

# Task 6 - Three Words
sentence = 'Some right here'.split()
count = 0
words = sentence.split()

for word in range(0, len(words), 1):
    if words[word].isalpha():
        count += 1
        if count == 3:
            print(True)
            break
    else:
        count = 0

if count < 3:
    print(False)

# Task 7 - Acceptable pwd (pt 3)
if 6 < len(password) > 9 and not password.replace(' ', '').isalpha():
    print(True)
else:
    print(False)

# Task 8 - Marker
text = "one two <three> four"
start = '<'
end = '>'
start_index = text.find(start)
end_index = text.find(end)
word = text[start_index + 1:end_index]
if len(word) == 0:
    print('')
else:
    print(word)