'''
# Home Work
print('Hello world!')
# Examples
print('a' + 'b' + 'c')
print(2 + 3)
print(2 + 3 * 6 - 4)
# +, -, *, /
print('Result is - ', 2 + 2 * 2, 'hello', 'my', 'friend')
# //, **, %
print(10 // 2)
print(5 // 2)
print(9 ** 2)
print(4 ** 3)
print(5 % 2)
print(16 % 2)
# Variables (Переменные)
# имя_переменной = значение
number = 5
number_even = 4

print(number * number_even * number)
# Задача со скидкой
money = 1000
sweater_price = 100
pants_price = 200
shoes_price = 100
pants_discount = pants_price * 0.1 # Скидка

# Переопределение
pants_price = pants_price - pants_discount
print("Кол-во денег:")
print(money - sweater_price - (pants_price * 2) - shoes_price)

# input('Комментарий для ввода данных: ')
username = input('Введите имя пользователя: ')
print("Добро пожаловать,", username + '!')

# Задача с выводом данных
name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
middle_name = input('Введите отчество: ')
print("Ваше имя", name)
print("Ваша фамилия", surname)
print("Ваше отчество", middle_name)

# input - нюансы
number = input('Number 1: ')
number_2 = input('Number 2: ')
print(number + number_2)

# int() - Integer (Целое число)
print(int('4') + int('6'))

# input - int(input(...))
number = int(input('Number 1: '))
number_2 = int(input('Number 2: '))
print(number + number_2)
'''
# float() - Float (Дробное число (десятичное))
print(float('2') + float('3'))
