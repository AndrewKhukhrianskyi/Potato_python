# Task 1 - Modify code
from tkinter import *
from random import randint
import tkinter.messagebox as mb
'''
def get_data():
    name = text_name.get(0.0, END).strip().title()
    age = text_age.get(0.0, END).strip()
    if len(name) == 0 or len(age) == 0:
        mb.showerror(title='Error!',
                     message='Поля пустые!')
    elif not name.isalpha():
        mb.showerror(title = 'Error!',
                     message = 'Имя содержит не буквенные символы!')
    elif not age.isdigit():
        mb.showerror(title = 'Error!',
                     message = 'Возраст содержит не числовые символы!')
    elif int(age) > 100:
        mb.showerror(title='Error!',
                     message="Шо ты тут забыл, дедуля? Иди в шахматы играй!")
    elif len(name) > 20:
        mb.showerror(title='Error',
                     message="Ты шо? Казах? Имя не может быть таким длинным!")
    print(name, age)

root = Tk()

root.geometry("300x300")
root.resizable(False, False)

name_label = Label(width = 15,
                   text = 'Введите имя:')
text_name = Text(width = 15,
                 height = 1)
age_label = Label(width = 15,
                  text = 'Возраст:')
text_age = Text(width = 15,
                height = 1)
button = Button(width = 8,
                height = 2,
                text = 'Save!',
                command = get_data)

widgets = [name_label, text_name, age_label, text_age, button]

for widget in widgets:
    widget.pack(anchor='n')
    
root.mainloop()
'''
# Task 2 - Random number app
def generate_random_number():
    number = str(randint(1, 100))
    mb.showinfo(title='Инфо',
                message=f'Рандомное число: {number}')

root = Tk()

root.geometry("100x100")
root.resizable(False, False)

button = Button(width = 8,
                height = 2,
                text = 'Рандом!',
                command = generate_random_number)

button.pack(anchor='n')
root.mainloop()
