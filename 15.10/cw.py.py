# КАК НЕ НАДО ДЕЛАТЬ!!!!!
word = 'cat'
# len() - подсчет кол-ва символов в строке
#for elem in range(len(word)):
 #   print(word[elem])
# Как надо делать!!!!
#for elem in word:
#    print(elem)

#ЗАДАЧА - перевернуть строку без примене-
#ния reverse & [::-1]
new_word = ''
for elem in range(len(word) - 1, -1, -1):
    new_word += word[elem]
print(new_word)

# Вложенность цикла
for i in range(10):
    for j in range(10):
        print(i, '-', j)
