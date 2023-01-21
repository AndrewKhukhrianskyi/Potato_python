from tkinter import *
from random import choice
# При работе с command ф-я принимает никаких аргументов
"""
# Task 1 - Достигатор
def you_fool():
    random_words = ['Дурачок', 'Голова', 'Семен-семеныч!']
    print(f'Достижение получено: {choice(random_words)}')
    
root = Tk()
button = Button(width = 15,
                height = 2,
                text = 'Тыкни на меня!',
                command = you_fool)
button2 = Button(width = 15,
                height = 2,
                text = 'Тыкни на меня!12')
button3 = Button(width = 15,
                height = 2,
                text = 'Тыкни на меня!33')
root.geometry('400x400')

# .pack() позволяет прикрепить кнопку
# свойство anchor работает со сторонами свет
# n - север,s - юг, w - запад, e - восток
widgets = [button, button2, button3]
for widget in widgets:
    widget.pack(anchor = 'n')
root.mainloop()
"""
# Task 2 - Калькулятор
def add():
    number = int(input('Число 1: '))
    number2 = int(input('Число 2: '))
    print(number + number2)
def multiply():
    number = int(input('Число 1: '))
    number2 = int(input('Число 2: '))
    print(number * number2)

def divide():
    number = int(input('Число 1: '))
    number2 = int(input('Число 2: '))
    print(number // number2)

def minus():
    number = int(input('Число 1: '))
    number2 = int(input('Число 2: '))
    print(number - number2)

root = Tk()
root.geometry('400x400')
button = Button(width = 15,
                height = 2,
                text = 'Сложить',
                command = add)
button2 = Button(width = 15,
                height = 2,
                text = 'Умножить',
                command = multiply)
button3 = Button(width = 15,
                height = 2,
                text = 'Деление',
                command = divide)
button4 = Button(width = 15,
                height = 2,
                text = 'Вычитание',
                command = minus)
buttons = [button, button2, button3, button4]
for btn in buttons:
    btn.pack(anchor='n')

'''
Homework 21.01
1. Почитать о виджетах
2. Познакомиться с виджетом Button
3. Написать приложение, которое будет выводить случайное число
4. Написать приложение, которое будет выводить цитаты великих людей 
'''
