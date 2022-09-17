# Data types
# Strings
# Simple part
# Строки - это любые слова, символы, чилса взятые в кавычки
# Пример: "Hello, World!", '12345'
# Неправильно: "Hello' - Error!!!
# Известные свойства:
# Конкатенация (склеивание): 'a' + 'b' = 'ab' (Example)
# Повторение: 'a' * 3 = 'aaa' (Example)
# Hard part
# Строки - это набор однострочных строковых объектов
# Все что есть Python - это объект (Мао Цзе Дун 440 г. до н.э)
# "Собака"
#  012345 -> Читаем слева-направо
#      -1 -> Читаем справа-налево
# Индексация - это порядок элементов строки. Индекс - это номер по порядку
# "....."
# "Вечера на хуторе близ диканьки"
# Обращение по индексу: строка[индекс]
from turtle import title


string = 'Home'
print(string[1])
print(string[-4])
#print(string[6]) # IndexError - невозможно найти значение по индексу
# Slice - срезы
# Срез - это излвеченный элемент динамического объекта (строки, списка и тд.)
# Срез - это вырезание символов из строки
# Вырезание элементов: строка[start:end]
# start - откуда режем, end - до куда режем (не включая последний элемент)
# строка[start:] - учитываются все элементы со start и дальше
word = "Собака"
print(word[0] + word[-2] + word[1:3] + word[4:])
# строка[-1::] - элементы будут читаться справа налево
print(word[::-1])
# Методы (функции) - набор действий, который применяется к объекту (А.К.А строке)
# Применение методов: строка.метод(...)
# строка.replace(заменяемый элемент, новый элемент)
# .replace() - это метод, позволяющий заменить элемент строки
# .find(), .rfind()
# После применения методов к строке результат будет сохраняться НОВЫМ значением
string = "Пиратss"
correct_string = string.replace('s', '')
print(correct_string)
print(string)
long_text = 'gsdfgfdsdbfdbvcbvxbngfxbdxgfbhgfxbgfxbvzvxdfhfcgncfbncgfnhcncbnbmbvdogjtrhgfnghmhjvkgfhjkghli;lk,hjjhdg'
find_dog = long_text.find('dog')
print(find_dog)
print(long_text[find_dog:find_dog + 3])
find_cat = long_text.find('cat')
print(find_cat)
# cтрока.count(элемент)
# Task 1 - Скороговорка
task= "шла саша по шоссе и сосала сушку"
task2 = task.count ("а")

print (task2)
# Task 2 - Перевертыш
stroka= "не собака"
print (stroka [:: -1])

# Task 3 - Каждое слово с большой буквы
nestroka="кто ето прочитал тот ... а дальше додумайте сами"
print (nestroka.title())
# Task 4 - Upper, Lower, Swapcase
string = 'БаГет'
print(string.upper())
print(string.lower())
print(string.swapcase())
