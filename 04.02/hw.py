# Task 1 - Умный блокнот
from tkinter import *
from random import choice
from time import sleep

def save_data():
    text_data = text.get(0.0, END)
    file = open('save_data.txt', 'w')
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

"""
# Task 2 - Анкета

def save_data_blank():
    text_fields = [text_name, text_surname,
               text_age]
    database_list = ['name', 'surname', 'age']
    result = {}
    for value in range(len(database_list)):
        sub_data = text_fields[value].get(0.0, END).strip()
        result[database_list[value]] = sub_data
    blank_file = open('blank.txt', 'w')
    blank_file.write(str(result))
    blank_file.close()
    
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

button = Button(width = 8,
                height = 2,
                text = 'Сохранить!',
                command = save_data_blank)

widgets = [name_label, text_name,
           surname_label, text_surname,
           age_label, text_age, button]
for widget in widgets:
    widget.pack(anchor = 'n')
"""
root.mainloop()
