from tkinter import *
from random import randint

import tkinter.messagebox as mb

def more_or_less():
    def generate_number():
        player_number = int(text_field.get(0.0, END).strip())
        pc_number = randint(1, 100)
        if player_number > pc_number:
            mb.showinfo(title = 'Результат!',
                        message = f'Игрок: {player_number}, PC: {pc_number}. Игрок победил!')
        elif player_number == pc_number:
            mb.showinfo(title = 'Результат!',
                        message = f'Игрок: {player_number}, PC: {pc_number}. Ничья!')
        else:
            mb.showinfo(title = 'Результат!',
                        message = f'Игрок: {player_number}, PC: {pc_number}. PC победил!')
    more_window = Toplevel()
    more_window.geometry('300x150')
    more_window.resizable(False, False)
    more_window.title('Больше\меньше')

    label = Label(more_window,
                  width=20,
                  text = 'Введите число ниже')
    text_field = Text(more_window,
                      width = 10,
                      height = 1)
    button = Button(more_window,
                    width=5,
                    height=2,
                    text = 'Click!',
                    command=generate_number)
    widgets = [label, text_field, button]
    for widget in widgets:
        widget.pack(anchor='n')
    

def blackjack():
    card_score = 0

    def show_results():
        player_score, pc_score = [], []

        cards = int(text.get(0.0, END).strip())

        for card in range(cards):
            player_score.append(randint(1, 6))
        
        for card in range(randint(3, 6)):
            pc_score.append(randint(1, 6))

        mb.showinfo(title='Результат!',
                    message=f'Карты игрока: {player_score}, PC: {pc_score}')
        
    blackjack_window = Toplevel()
    blackjack_window.title('Игра в 21')
    blackjack_window.geometry('300x150')
    blackjack_window.resizable(False, False)

    
    label = Label(blackjack_window,
                  width = 40,
                  height = 1,
                  text='Введите кол-во карт, которые хотите взять')
    
    text = Text(blackjack_window,
                width=15,
                height=1)
    
    button = Button(blackjack_window,
                    width=8,
                    height=1,
                    text='CLICK!',
                    command=show_results)
    
    widgets = [label, text, button]

    for widget in widgets:
        widget.pack(anchor='n')

def show_help():
    help_window = Toplevel()
    help_window.geometry('300x150')
    help_window.resizable(False, False)
    help_window.title('Справка')
    text = Label(help_window,
                 width = 15, 
                 height= 1,
                 text = 'Окно о помощи!')
    text.pack(anchor='n')

window = Tk()
window.geometry('300x150')
window.resizable(False, False)
window.title('Главное окно')

btn1 = Button(text='Больше\меньше',
              width = 15,
              height = 1,
              command=more_or_less)
btn2 = Button(text='Игра в 21',
              width = 15,
              height = 1,
              command=blackjack)
btn3 = Button(text='Справка',
              width = 15,
              height = 1,
              command=show_help)

widgets = [btn1, btn2, btn3]
for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()
