# Task 1 - Pwd
tries = 3
correct_pwd = 'admin'
for step in range(3):
    pwd = input('Enter password: ')
    if pwd == correct_pwd:
        print('WELCOME!')
        break
else:
    print('BLOCKED!')

# Task 2 - Count element
word = input('Enter word: ')
count_element = input('Element: ')
count = 0
for letter in word:
    if letter == count_element:
        count += 1

print(f'Element {count_element} meets {count} times!')

# Task 3 - Check pwd
correct_pwd = 'admin'
correct_login = 'user'
while True:
    login = input('Enter username: ')
    pwd = input('Enter pwd: ')
    # Case 1 - All correct
    if login == correct_login and pwd == correct_pwd:
        print('WELCOME!')
        break
    # Case 2 - Incorrect login
    elif login != correct_login and pwd == correct_pwd:
        print('Incorrect login!')
    # Case 3 - Incorrect pwd
    elif login == correct_login and pwd != correct_pwd:
        print('Incorrect pwd!')
    # Case 4 - All wrong
    else:
        print('ALL WRONG!')