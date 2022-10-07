# Task 1 - Odd\Even
entry = ''
while True:
    entry = input('Continue? (Yes/No): ')
    if entry == 'No':
        break
    number = int(input('Number: '))
    if number % 2 == 0:
        print(f'Number {number} is even')
    else:
        print(f'Number {number} is odd')

# Task 2 - ATM
card = True
money = int(input('Количество денег: '))
while card:
    operation = input('Введите операцию: ').capitalize()
    if operation == 'Withdraw':
        value = int(input('Введите сумму съема средств: '))
        if money <= 0:
            print("Нехватка денег!")
            card = False
        else:
            money -= value
        print('Средства забраны')
    elif operation == 'Info':
        print('Информация о счете')
        print(f'Кол-во денег на карте: {money}')
    else:
        print('Либо вы вышли либо некорректно ввели команду')
        card = False

# Task 3 - isupper\islower()
while True:
    word = input('Enter word: ')
    if word == 'exit': 
        break
    if word.isupper():
        print(True)
    elif word.islower():
        print(False)