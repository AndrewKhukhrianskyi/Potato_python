# Task 1 & 2 (Random Number and Random Phrase)
from tkinter import *
from random import randint, choice

def random_number():
    print(f'{randint(1, 100)} случайное число!')

def random_phrase():
    phrases = ['Мы берем советы каплями, а раздаем ведрами (Конфуций)',
               "Не все могут посмотреть в завтрашний день (Кличко)",
               "Запомни. Если твоего друга сбила машина, то он тебе не друг, потому что друзья НА ДОРОГЕ НЕ ВАЛЯЮТСЯ! (Ауф)"]
    print(choice(phrases))
root = Tk()
root.geometry('200x200')
button = Button(width = 30,
                height = 2,
                text = 'Рандомная цифра',
                command=random_number)
button2 = Button(width = 30,
                height = 2,
                text = 'Рандомная фраза',
                command=random_phrase)

widgets = [button,
           button2]

for widget in widgets:
    widget.pack(anchor = 'n')

root.mainloop()