from tkinter import *
'''
def open_window():
    top_level_window = Toplevel()
    top_level_window.geometry('300x300')
    top_level_window.title('Доп окно')
    top_level_window.resizable(False, False)
    top_level_window['bg'] = 'red'
    entry = Label(top_level_window,
                  width = 20,
                  text = "Это доп окно")
    # Нужно дать понять В КАКОМ окне нужно запаковывать
    entry.pack(anchor = 'n')
    top_level_window.after(5000, lambda: top_level_window.destroy())

window = Tk()

window.title('Основное окно')
window.resizable(False, False)
window.geometry('300x300')


button = Button(width = 8,
                height = 1,
                text = 'Click!',
                command = open_window)

button.pack(anchor = 'n')

window.mainloop()
'''

# Шифр Виженера
from tkinter import *
from itertools import cycle

import tkinter.messagebox as mb

# Константы
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# Функция шифровки
def encode_vijn():
    text = text_field.get(0.0, END).strip().lower()
    keytext = key_field.get(0.0, END).strip()
    f = lambda arg: ALPHABET[(ALPHABET.index(arg[0])+ALPHABET.index(arg[1])%26)%26]
    crypt_file = open('crypt.txt', 'w')
    crypt_file.write(''.join(map(f, zip(text, cycle(keytext)))))
    crypt_file.close()
    mb.showinfo(title = 'Окно',
                message = "Данные зашифрованы!")

# Функция дешифровки
def decode_vijn():
    text = text_field.get(0.0, END).strip().lower()
    keytext = key_field.get(0.0, END).strip()
    f = lambda arg: ALPHABET[ALPHABET.index(arg[0])-ALPHABET.index(arg[1])%26]
    decrypt_file = open('decrypt.txt', 'w')
    decrypt_file.write(''.join(map(f, zip(coded_text, cycle(keytext)))))
    decrypt_file.close()
    mb.showinfo(title = 'Окно',
                message = "Данные дешифрованы!")

# Инструкиця по применению
def show_help():
    pass
window = Tk()

# Параметры окна
window.geometry('300x300')
window.resizable(False, False)
window.title('Шифр Виженера')

# Графические элементы (поля, кнопки и тп.)
label = Label(width = 40,
              text = 'Введите текст или шифротекст ниже:')
text_field = Text(width = 20,
                  height = 1)
label_2 = Label(width = 40,
                text = 'Введите ключ для зашифровки\расшифровки:')
key_field = Text(width = 20,
                 height = 1)
crypt_button = Button(text = 'Зашифровать!',
                      width = 12,
                      height = 1,
                      command = encode_vijn)
decrypt_button = Button(text = 'Расшифровать!',
                        width = 12,
                        height = 1,
                        command = decode_vijn)
help_button = Button(text = "Справка",
                     width = 12,
                     height = 1,
                     command = show_help)
widgets = [label, text_field,
           label_2, key_field,
           crypt_button, decrypt_button,
           help_button]

for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()

'''
HW
1. Почитать о Toplevel
2. Написать приложение-игру в котором будут 3 кнопки под программы
    "Игра больше-меньше" - Игрок пишет число до 100 и если у компьютера число больше - компьютер победил
    иначе - победил игрок
    21 - Миниигра, где игрок набирает число до 21. Если у игрока перебор - он проигрывает. Тянуть можно числа от
    1 до 6 в случайном порядке. Компьютер тоже набирает параллельно карты. Если получает больше значения чем
    компьютер - побеждает компьютер, иначе - побеждает игрок. Если у обоих игроков перебор, побеждает тот, у
    кого перебор по числам ближе к 21 (т.е у кого меньше перебор по очкам, тот и победил)
    Справка - окно с информацией по тем играм, которые есть.
'''

