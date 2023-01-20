from tkinter import *
from random import randint, choice


root = Tk()
number_1, number_2 = 500, 500
screen_name = 'Окно'
# Task 1 - Set Title Name
root.title(screen_name)
# Task 2 - Set title size
root.geometry(f'{number_1}x{number_2}')
# Task 3 - NO RESIZE
root.resizable(False, False)
root.mainloop()