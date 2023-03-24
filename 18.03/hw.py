from tkinter import *

import tkinter.messagebox as mb

# Task 1 - Fields
'''
def save_data():
    save_msg = mb.askyesno(title='Question',
                           message='Do you want to save this data?')
    fields = [name_field, surname_field, age_field]
    # Достаем текст из полей и сразу добавляем их в список
    text_list = [widget.get(0.0, END) for widget in fields] 
    if save_msg:
        file = open('Potato_python\\18.03\\save.txt', 'w')
        for elem in text_list:
            file.write(elem)
        mb.showinfo(title='Saved!',
                    message='Data was saved!')
        file.close()

        
        

window = Tk()
window.geometry('300x300')
window.resizable(False, False)

label_name = Label(text='Enter your name below:',
                   width=20)
name_field = Text(width=20,
                  height=1)

label_surname = Label(text='Enter your surname below:',
                      width=20)
surname_field = Text(width=20,
                     height=1)

label_age = Label(text='Enter your age below:',
                  width=20)

age_field = Text(width=20,
                 height=1)

button = Button(text='Save!',
                width = 8,
                height = 1,
                command=save_data)

widgets = [label_name, name_field,
           label_surname, surname_field,
           label_age, age_field,
           button]

for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()
'''

# Task 2 - XX & XY

def check_chromosomes(string):
    return 'girl' if string[-1] == 'X' else 'boy'

print(check_chromosomes('XYYXYXYXYXYYXXYXYX'))