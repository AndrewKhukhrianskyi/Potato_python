# .keys(), .values(), .items()
# .keys() - достает ключи из словаря
k = {1 : 'a', 2 : 'b', 3 : 'c'}
keys = k.keys()# создает "недосписок"

print(list(keys))

# .values() - достает значения из словаря
values = k.values() # создает "недосписок"
print(list(values))

# Если не указывать значение - создаст пустоту

# В обычном случае создания словаря без значий = error
#d = {1 : , 2: , 3:}
#print(d)
d = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'v', 'dog', 'user')
d2 = None
# fromkeys() - создает словарь из двух сущностей 
result = dict.fromkeys(d, d2)
count = 0
# .items() - достает выражение в виде двух отдельных значений (отдельно ключ и отдельно значение)
# Удобно применять в циклах
for key, value in result.items():
    result[key] = count
    count += 1

print(f"RESULT: {result}")


# Task 1 - Id generator
arr = ['username', 'age', 'name', 'surname', 'middlename', 'ID', 'Card Number']
data = ['user123', 15, 'Vlad', 'Mikhno', 'Ivanovich', '00001', '5169 1001 1001 1001']
result = {}

for info in range(len(data)):
    result[arr[info]] = data[info]

print(result)

# Task 1 - Id generator (MOD)
arr = []
data = []
result = {}


while True:
    ask = input('Напишите ваш ключ: ') # Здесь лежит ключ
    if ask == 'exit':
        break
    ask2 = input('Значение: ') # Тут лежит значение
    result[ask] = ask2 # На этом этапе добавляем новое выражение в словарь
    print(result)
