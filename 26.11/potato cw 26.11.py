# Bad practice
def sum_numbers(num, num2,
                num3, num4):
    print(num + num2 + num3 + num4)

sum_numbers(1, 5, 6, 3)

# Good Practice
# * работает только внутри функций
# * преобразует переданные параметры в кортеж
def sum_numbers1(*numbers):
    #print(type(numbers))
    print(sum(numbers))

sum_numbers1(1, 5, 6, 3, 2, 2, 1,
             10, 12, 14, 15, 6, 3,
             5, 5, 5, 3, 4, 0, 1)

# ** преобразует переданные параметры в словарь
def data(**datas):
    print(datas)
    
# Выражение перед = делает выражение ключом,
# Выражение после = делает выражение значением
data(name='Bob', surname='Wilson',
     age=29, status = 'Married',
     date_birth = '10.08.1991')

# Обработка ошибок
# Exception (Исключение) - это ошибка, которая показывает что результат пошел не так как нужно
# try/except = if/else
# try - попытка
# Мы попадаем в except в случае некорректного поведения кода
# except без конкретики отлавливает ВСЕ ошибки
try:
    print(2/2)
except ZeroDivisionError: 
    print("Ахтунг! Ты делишь на 0.")
finally: # выполнится, не важно какое состояние
    print('END OF PROGRAM.')


def add_2(num, num2):
    try:
        print(num + num2)
    except TypeError:
        print('Возможно, вы не складываете числа...')

# Positive Test
add_2(2, 2)

# Negative Test
add_2(2, 'dog')

def vowels_consonants(string):
    string = string.lower()
    vowels_count = 'aeouiy'
    consonants_count = 'qwrtpsdfghjklzxcvbnm'
    vowels_amount, consonants_amount = 0, 0
    result = {'vowels' : None, 'consonants' : None}

    for vowel in vowels_count:
        vowels_amount += string.count(vowel)

    for consonant in consonants_count:
        consonants_amount += string.count(consonant)
    result['vowels'] = vowels_amount
    result['consonants'] = consonants_amount
    print(result)

vowels_consonants('hello, my name is Pavel')
    






