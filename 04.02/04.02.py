from tkinter import *
from random import choice
from time import sleep

root = Tk()
root.geometry('200x200')

def change_random_color():
    colors = ['red', 'green',
              'black', 'brown',
              'pink', 'cyan',
              'blue', 'yellow']
    # config позволяет изменять структуру сущестующего виджета
    label.config(bg = choice(colors))

def get_data():
    text_list = []
    widgets = [text_name,
               text_surname,
               text_age]
    for widget in widgets:
        text = widget.get(0.0, END)
        text_list.append(text.strip())
    print(text_list)
'''
label = Label(width = 10,
              height = 2,
              bg = 'blue')
button = Button(width = 8,
                height = 2,
                command = change_random_color,
                text = 'Click!')
'''
# Модифицировать код для задачи 4 нужно отсюда
name_label = Label(width = 10,
                   height = 1,
                   text = 'Ваше имя')
text_name = Text(width = 10,
                 height = 1)

surname_label = Label(width = 20,
                   height = 1,
                   text = 'Ваша фамилия')
text_surname = Text(width = 10,
                    height = 1)

age_label = Label(width = 20,
                   height = 1,
                   text = 'Возраст')
text_age = Text(width = 10,
                height = 1)

button = Button(width = 5,
                height = 2,
                text = 'Click!',
                command = get_data)

widgets = [name_label, text_name,
           surname_label, text_surname,
           age_label, text_age, button]
for widget in widgets:
    widget.pack(anchor = 'n')

root.mainloop()

'''
HW 04.02
1. Почитать о Label: https://sites.google.com/comp-sc.if.ua/python-easy/tkinter/віджети/label
2. Почитать о создании файлов: https://istories.media/workshops/2021/01/29/vvedenie-v-python-chast-11-rabota-s-failami/
3. Умный блокнот. Напишите приложение, которое будет создавать файл и сохранять записанные данные из блокнота
4. Модифицируйте задачу с классной работы таким образом, чтобы введенные данные с анкеты сохранялись в файле
'''
