from tkinter import *
from random import choice, randint

import tkinter.messagebox as mb

# Task 1 - Switch color
'''
COLORS = 'red', 'green', 'blue', 'white', 'cyan'
def change_color():
    ask = mb.askyesno(title = 'Вопрос',
                      message = 'Уверены, что хотите поменять цвет окна?')
    # Если нажмем "Да" -> Будет True, иначе - False
    if ask: # ask == True
        window['bg'] = choice(COLORS)
        mb.showinfo(title='Результат',
                    message = 'Цвет поменялся!')
    else:
        mb.showinfo(title = 'Результат',
                    message = 'Цвет не поменялся!')
'''

# Task 2 - Blackjack

def blackjack():
    count_player = 0
    count_pc = randint(10, 21)
    while True:
        ask = mb.askyesno(title = 'Вопрос',
                          message = "Тянем карту?")
        if ask:
            count_player += randint(1, 6)
            mb.showinfo(title='Сообщение',
                        message=f'Счет: {count_player}')
        else:
            break
    if count_player < count_pc or count_player > 21:
        mb.showerror(title = "Поражение!",
                     message = "Вы проиграли!")
    elif count_player == count_pc:
        mb.showinfo(title = "Ничья!",
                    message = "Ничья!")
    else:
        mb.showinfo(title = "Победа!",
                    message = "Вы победили!")
    mb.showinfo(title = "Результат!",
                message = f"Игрок: {count_player}, РС: {count_pc}")
    """
    1. Цикл, который будет работать, пока игрок не нажмет кнопку НЕТ (DONE)
    2. Внутри цикла, если игрок нажал ДА -> добавить случайное число от 1 до 6 (DONE)
    3. Внутри цикла, если игрок нажал НЕТ -> break (DONE)
    4. Сгенерировать компьютеру случайное число от 6 до 21 (DONE)
    5. Сделать сравнение
    """
window = Tk()

window.geometry('100x100')
window.resizable(False, False)
button = Button(text = 'Start!',
                width = 8,
                height = 1,
                command=blackjack)

button.pack(anchor='n')

"""
HW
1. Почитать об окнах: https://docs.python.org/3/library/tkinter.messagebox.html
2. Решить задачу на повторение: https://www.codewars.com/kata/56530b444e831334c0000020
3. Форма регистрации. Написать приложение, которое будет сохранять информацию о пользователе (Имя, Фамилия, Дата)
и предлагать пользователю сохранить информацию в файле (Вы уверены что хотите сохранить данные?). Если
да -> сохранить в файле save.txt иначе -> не сохранять
"""



