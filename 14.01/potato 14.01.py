from tkinter import *
from random import randint, choice

def generate_random_numbers():
    number_1 = randint(200, 500)
    number_2 = randint(200, 500)
    return number_1, number_2

def generate_window_name():
    names = ['Плюшка', 'Крендель', 'Окурок']
    return choice(names)
# Для работы с tkinter нужно прописать команду
root = Tk()
# .geometry позволяет работать с окнами приложения
# Параметры передаются в виде: "axb"
# a - ширина, b - высота
number_1, number_2 = generate_random_numbers()
screen_name = generate_window_name()
root.title(screen_name)
root.geometry(f'{number_1}x{number_2}')
# resizable позволяет блоикровать размер окна
# 1е выражение - по горизонтали, 2е выраж. - по вертикали
root.resizable(False, True)
# mainloop позволяет повторно использовать приложение
root.mainloop()

# Task - Kg to pnd
def kg_to_pnds():
    kg = int(input('KG: '))
    print(f'POUNDS: {kg * 2.205}')

kg_to_pnds()
'''
1. Почитать о Tkinter и параметрах окна
    - geometry()
    - Tk()
    - resizable()
    - title()
2. Написать программу, которая будет создавать окно
размером 500х500
3. Поменяйте название экрана
4. Запретите изменять размеры окна
'''
