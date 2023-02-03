from tkinter import *

def clear_text():
    text_field.delete(0.0, END)

def save_text():
    text = text_field.get(0.0, END)
    print(f'Saved text: {text}')

root = Tk()

root.geometry('200x200')

text_field = Text(width = 50,
                  height = 5)
button = Button(width = 8,
                height = 2,
                text = 'Clear text!',
                command = clear_text)
button2 = Button(width = 8,
                 height = 2,
                 text = 'Save text!',
                 command = save_text)

widgets = [text_field, button, button2]

for widget in widgets:
    widget.pack(anchor='n')

root.mainloop()