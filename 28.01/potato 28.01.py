from tkinter import *
from random import choice
'''
def add_some_text():
    text = 'Волк, не тот кто волк а тот кто не волк'
    text_field.insert(1.0, text)

def get_text():
    text = text_field.get(2.0, END)
    print(f'Text: {text}')

def add_smart_text():
    text_list = ['Что-то',
                 'Stop!',
                 'Remark!']
    text_field.insert(0.0, choice(text_list))
root = Tk()

root.geometry('200x200')

# Entry
#field = Entry(width = 20)
# Text
text_field = Text(width = 50,
                  height = 5)
button = Button(width = 5,
                height = 2,
                text = 'Start!',
                command = add_some_text)
button2 = Button(width = 5,
                 height = 2,
                 text = 'Get text!',
                 command = get_text)
button3 = Button(width = 8,
                 height = 2,
                 text = 'Smart Text!',
                 command = add_smart_text)
#field.pack(anchor='n')
text_field.pack(anchor='n')
button.pack(anchor='n')
button2.pack(anchor = 'n')
button3.pack(anchor = 'n')
root.mainloop()
'''

# Task - Площадь равнобедренного треугольника
def triangle_square():
    side = int(input('Side: '))
    height = int(input('Height: '))
    print(0.5 * (side * height))

'''
28.01 HW
1. Почитать об Entry & Text
2. Описать различия между ними
3. Написать программу-блокнот, в которой можно будет
    - Стереть введенный текст
    - "Сохранить" введенный текст в переменную
'''
