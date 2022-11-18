# Task 1 - Filters
string = input('Введи строку: ').split() # разбиваем введенный результат на ['...', '...', '...']
# Значения разбиваются по пробелам
result_dict = {}
for identificator in range(len(string)):
    if string[identificator].isdigit():
        result_dict[identificator] = int(string[identificator])
print(result_dict)

# Task 2 - Filters (Mod)
values = list(result_dict.values())
print(f'MAXIMUM VALUE: {max(values)}')
print(f'AVERAGE VALUE: {sum(values) // len(values)}')