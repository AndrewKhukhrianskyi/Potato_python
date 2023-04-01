'''
Main - это файл, через который производится запуск приложения
'''

from config import *

from tkinter import *

import tkinter.messagebox as mb
import re

def find_text():
    regex_pattern = regex_text_field.get(0.0, END).strip()
    text = text_field.get(0.0, END).strip()

    result = re.findall(rf'{regex_pattern}', text)

    result_text_field.delete(0.0, END)
    result_text_field.insert(0.0, str(result))

    mb.showinfo(title='Результат',
                message = "Данные найдены!")

def clear_data():
    ask_message = mb.askyesno(title='Вопрос',
                              message = "Уверены, что хотите очистить данные?")
    if ask_message:
        widgets = [text_field,
                   result_text_field]
        for widget in widgets:
            widget.delete(0.0, END)

        mb.showinfo(title = 'Окно',
                    message = 'Данные удалены!')
# UI часть

window = Tk()

window.resizable(RESIZABLE_STATUS_WIDTH,
                 RESIZABLE_STATUS_HEIGHT)

window.geometry(f'{WIDTH}x{HEIGHT}')

window.title(TITLE)

regex_label = Label(width = LABEL_WIDTH,
                    text = 'Напишите регулярное выражение ниже:')

regex_text_field = Text(width = TEXT_ENTRY_WIDTH,
                        height = TEXT_ENTRY_HEIGHT)

label_text_field = Label(width = LABEL_WIDTH,
                          text = 'Напишите текст снизу:')

text_field = Text(width = TEXT_WIDTH,
                  height = TEXT_HEIGHT)

result_label = Label(width = LABEL_WIDTH,
                     text = 'Результат:')

result_text_field = Text(width = TEXT_WIDTH,
                         height = TEXT_HEIGHT + 10)

clear_button = Button(text = 'Очистить!',
                      width = BUTTON_WIDTH,
                      height = BUTTON_HEIGHT,
                      command = clear_data)

find_button = Button (text = 'Найти!',
                      width = BUTTON_WIDTH,
                      height = BUTTON_HEIGHT,
                      command = find_text)

widgets = [regex_label, regex_text_field,
           label_text_field, text_field,
           result_label, result_text_field,
           clear_button, find_button]

for widget in widgets:
    widget.pack(anchor = 'n')

window.mainloop()