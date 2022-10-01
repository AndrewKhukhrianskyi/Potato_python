# DRY - Don't Repeat Yourself (Не повторяйся)
# Циклы - это повторение одного и того же действия
# 1й - это циклы, которые работют бесконечно или при определенных условиях
# while - пока
# Вариант бесконечного цикла
from time import sleep # ставит программу на "паузу"
from random import randint # Создает случайное число
'''
while True:
    print('a')

# Вариант конечного цикла при определенных условиях
# while = if
count = 10
while count > 0:
    print(count)
    count -= 1

# break - останавливает работу цикла
count = 0
while True:
    count += 1
    sleep(1)
    print(count)
    if count >= 3:
        break

# Цикл while будет работать пока условие истинно (True)!
while False:
    print('a')

print(randint(1,10)) # randint создает случайное число

score_1 = 0
score_2 = 0
while True:
    if score_1 == 5 and score_1 > score_2 or score_2 == 5 and score_1 < score_2:
        print(f'Player 1: {score_1}')
        print(f'Player 2: {score_2}')
        break
    player_1 = randint(1,6)
    player_2 = randint(1,6)
    if player_1 > player_2:
        print(f'Player 1 win! Value: {player_1}')
        print(f'Player 2 lose! Value: {player_2}')
        score_1 += 1
    elif player_1 < player_2:
        print(f'Player 2 win! Value: {player_2}')
        print(f'Player 1 lose! Value: {player_1}')
        score_2 += 1
    else:
        print(f'Equal! {player_1} - {player_2}')


# Цикл while может зависеть от изменяемого в нем значения
step = ''
while step != 'exit':
    step = input('Enter step: ')
    print(f"Вы сделали шаг {step}")

# a = 10000000
# b = 1
# a / b = c
# c < 1
a = 100
b = 2
while True:
    c = a / b
    b += 1
    print(c)
    if c < 1:
        print(b)
        break
'''
card = True
while card:
    operation = input('Введите операцию: ').capitalize()
    if operation == 'Withdraw':
        print('Средства забраны')
    elif operation == 'Info':
        print('Информация о счете')
    else:
        print('Либо вы вышли либо некорректно ввели команду')
        card = False
