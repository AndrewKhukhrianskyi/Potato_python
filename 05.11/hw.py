# Task 1 - KeyError
d = {1 : 'a', 2 : 'b'}
# KeyError here
#print(d[3])

# Task 2 - Make dictionary
keys = ['name', 'surname']
values = ['Ivan', 'Ivanov']
result = {}
for val in range(len(values)):
    result[keys[val]] = values[val]
print(result)