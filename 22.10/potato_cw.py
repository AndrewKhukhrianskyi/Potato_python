# Lists (Списки\Maссивы)
# Динамические объекты (Типы данных), Коллекции
# Как создать список?
# Списки - контейнеры для хранения данных
l = [1, 2, 3]
print(l)
l = ['a', 'b', 'c']
print(l)
l = [True, None, [], 'a', 'b', 1.245]
print(l)
# Свойства списков
arr1 = ['abc']
arr2 = ['cde']
# Списки можно соединять
print(arr1 + arr2)
# .append()
massive = []
# add number
massive.append(2)
print(massive)

# Задача 1 - сумма чисел
arr = [1, 2, 3, 4, 5]
count = 0
print(arr)
# Применение цикла
for num in arr: # num = взятое число из arr
    count += num
    print(count)

# Задача 2 - фильтрация чисел
arr = [4, 2, 3, 4, 5, 6, 0 ,1, 11, 2]
# Создать пустой список
arr2 = []
# Создаем цикл-переборщик
# Elem - Число взятое из списка arr
for elem in arr:
    if elem % 2 == 0: # Четное
        # добавляем в список arr2
        arr2.append(elem)
print(arr2)

# Задача 3
mass = [4, 2, 5, 6, 22, 1, 0, 9, 2]
# .sort()
mass.sort()
print(mass)
# .reverse()
mass.reverse()
print(mass)

    


