from tkinter import *
import tkinter.messagebox as mb
'''
#showinfo, showwarning
def open_error():
    mb.showerror(title = 'Оповещение',
                message = 'Вау. Сообщение.')
def open_info():
    mb.showinfo(title = 'Инфо',
                message = 'Инфо!')

def open_warning():
    mb.showwarning(title = 'Предупреждение',
                   message = "Предупреждение!")

root = Tk()
root.geometry('200x200')

button = Button(width = 8,
                height = 2,
                text = 'Click!',
                command = open_error)
button2 = Button(width = 12,
                height = 2,
                text = 'Info!',
                command = open_info)
button3 = Button(width = 8,
                height = 2,
                text = 'Warning!',
                command = open_warning)
widgets = [button, button2, button3]
for btn in widgets:
    btn.pack(anchor='n')
'''
def get_data():
    name = text_name.get(0.0, END).strip().title()
    age = text_age.get(0.0, END).strip()
    if not name.isalpha():
        mb.showerror(title = 'Error!',
                     message = 'Имя содержит не буквенные символы!')
    if not age.isdigit():
        mb.showerror(title = 'Error!',
                     message = 'Возраст содержит не числовые символы!')
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
Homework 11.02
1. Почитать о Messagebox (Tkinter)
2. Модифицировать код из классной работы, добавив следующие проверки:
    - Возраст не может быть больше 100 лет;
    - Имя не может быть длинее 20 символов;
    - Поля не могут быть пустыми.
3. На повторение. Написать приложение, которое будет выводить случайное число в messagebox
'''
