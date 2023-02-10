# Task 1 - Умный блокнот
from tkinter import *
from random import choice
from time import sleep

def save_data():
    text_data = text.get(0.0, END)
    file = open('save_data', 'w')
    file.write(text_data.strip())
    file.close()
root = Tk()
root.geometry('200x200')

label = Label(width=20,
              text='Введите текст внизу:')
text = Text(width=20,
            height=5)
save_button = Button(width=8,
                     height=2,
                     text='Сохранить',
                     command=save_data)

widgets = [label, text, save_button]

for widget in widgets:
    widget.pack(anchor='n')

root.mainloop()