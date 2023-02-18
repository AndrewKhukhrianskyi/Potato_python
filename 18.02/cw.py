from random import randint

from tkinter import *

import tkinter.messagebox as mb

def convert_to_numbers():
    text = message_field.get(0.0, END).strip().upper()
    database = {'A' : '01,', 'B' : '02,', 'C' : '03,',
                'D' : '04,', 'E' : '05,', 'F' : '06,',
                'G' : '07,', 'H' : '08,', 'H' : '09,', 'J' : '10,',
                'K' : '11,', 'L' : '12,', 'M' : '13,',
                'N' : '14,', 'O' : '15,', 'P' : '16,',
                'Q' : '17,', 'R' : '18,', 'S' : '19,',
                'T' : '20,', 'U' : '21,', 'V' : '22,',
                'W' : '23,', 'X' : '24,', 'Y' : '25,',
                'Z' : '26,'}
    for symbol, number in database.items():
        text = text.replace(symbol, number)

    mb.showinfo('Сообщение', 'Данные зашифрованы в числа!')

    file = open('cipher.txt', 'w')
    file.write('Result:\n' + text)
    file.close()

    mb.showinfo('Сообщение', 'Файл с шифром сообщением был создан!')
    
def convert_to_text():
    text = message_field.get(0.0, END).strip().upper()
    database = {'A' : '01,', 'B' : '02,', 'C' : '03,',
                'D' : '04,', 'E' : '05,', 'F' : '06,',
                'G' : '07,', 'H' : '08,', 'H' : '09,', 'J' : '10,',
                'K' : '11,', 'L' : '12,', 'M' : '13,',
                'N' : '14,', 'O' : '15,', 'P' : '16,',
                'Q' : '17,', 'R' : '18,', 'S' : '19,',
                'T' : '20,', 'U' : '21,', 'V' : '22,',
                'W' : '23,', 'X' : '24,', 'Y' : '25,',
                'Z' : '26,'}
    database = dict(zip(database.values(), database.keys()))
    
    for number, symbol in database.items():
        text = text.replace(number, symbol)

    mb.showinfo('Сообщение', 'Данные дешифрованы в текст!')

    file = open('decipher.txt', 'w')
    file.write('Result:\n' + text)
    file.close()

    mb.showinfo('Сообщение', 'Файл с расшифрованным сообщеним был создан!')

window = Tk()

window.geometry('500x500')
window.resizable(False, False)

label_text = Label(width = 20,
                   text = 'Enter your text below:')
message_field = Text(width = 50,
                     height = 20)
cipher_button = Button(width = 8,
                       height = 2,
                       text = 'Crypt!',
                       command = convert_to_numbers)
decrypt_button = Button(width = 8,
                       height = 2,
                       text = 'Decrypt!',
                       command = convert_to_text)
label_text.pack(anchor = 'w')
widgets = [message_field, cipher_button, decrypt_button]

for widget in widgets:
    widget.pack(anchor = 'n')

window.mainloop()
