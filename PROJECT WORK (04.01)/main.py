'''
Main - это файл, через который производится запуск приложения
'''

from config import *

from tkinter import *

import tkinter.messagebox as mb
import re

def find_text():
    regex_pattern = regex_text_field.get(0.0, END).strip()
    if len(regex_pattern) == 0:
        mb.showerror(title='Ошибка!',
                     message='Введите регулярное выражение!')
    else:
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

def get_status_analyze():
    words = False,
    numbers = False,
    symbols = False
    if letters_var.get():
        words = True
    if numbers_var.get():
        numbers = True
    if symbols.get():
        symbols = True
    analyze_text(words, numbers, symbols)

def analyze_text(words = False,
                 numbers = False,
                 symbols = False,
                 language_status = 'en'):
    result = []
    text = text_field.get(0.0, END).strip()
    result_text = ''
    vowels_count = 0
    consonants_count = 0
    # Подсчет гласных букв будет здесь
    if language_status == 'en':
        vowels = 'aeouiy'
        if words:
            for elem in vowels:
                vowels_count += text.count(elem)
            result.append(vowels_count)
    # Подсчет согласных букв будет здесь
            consonants = 'qwrtpsdfghjklzxcvbnm'
            for elem in consonants:
                consonants_count += text.count(elem)
            result.append(consonants_count)
        else:
            result.append('Ignored')
    # Подсчет символов
        if symbols:
            result.append(len(text))
        else:
            result.append('Ignored')
    # Часто встречаемая гласная буква
        vowels_count_dictionary = {}
        if words:
            for vowel in vowels:
                vowels_count_dictionary[vowel] = text.count(vowel)
            maximum_value = max(vowels_count_dictionary.values())
            new_dictionary = {}
            for letter, number in vowels_count_dictionary.items():
                new_dictionary[number] = letter                      
            result.append(f'{new_dictionary[maximum_value]}({maximum_value})')
    # Часто встречаемая согласная буква
            consonants_count_dictionary = {}
            for consonant in consonants:
                consonants_count_dictionary[vowel] = text.count(consonant)
            maximum_value = max(consonants_count_dictionary.values())
            new_dictionary = {}
            for letter, number in consonants_count_dictionary.items():
                new_dictionary[number] = letter     
            result.append(f'{new_dictionary[maximum_value]}({maximum_value})')
        else:
            result.append('Ignored')
            result.append('Ignored')
    

    for res in range(len(ANALYZE_TEXT_LIST)):
        try:
            result_text += f'{ANALYZE_TEXT_LIST[res]}: {result[res]}\n'
        except IndexError:
            result_text += f'{ANALYZE_TEXT_LIST[res]}: None\n'

    result_text_field.insert(0.0, result_text)
    mb.showinfo(title='Сообщение',
                message='Результат записался в поле!')

    
    
    
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

analyze_button = Button(text = 'Отчет!',
                        width = BUTTON_WIDTH,
                        height = BUTTON_HEIGHT,
                        command = analyze_text)
letters_var = IntVar()
checkbox_letters = Checkbutton(text = 'Буквы',
                               variable = letters_var)
numbers_var = IntVar()
checkbox_numbers = Checkbutton(text = 'Числа',
                               variable = numbers_var)

symbols_var = IntVar()
checkbox_symbols = Checkbutton(text = 'Символы',
                               variable = symbols_var)

widgets = [regex_label, regex_text_field,
           label_text_field, text_field,
           result_label, result_text_field,
           clear_button, find_button, analyze_button,
           checkbox_letters, checkbox_numbers, checkbox_symbols]

for widget in widgets:
    widget.pack(anchor = 'n')


window.mainloop()

"""
TODO:
1. Найти баги в приложении
2. Отрефакторить код
3. Структурировать в понимаемый формат
"""
