import pytest

def test_increment(): # Все должно начинаться с test
    def increment(n):
        return n + 2 
    
    assert increment(3) == 5

# В одном тестовом файле можно писать
# несколько тестовых функций

@pytest.mark.call_test
def test_a():
    assert True
    
@pytest.mark.call_test
def test_b():
    assert True
    
@pytest.mark.call_test
def test_c():
    assert True
    
@pytest.mark.add
def test_add():
    from random import randint
    def add(a, b):
        return a + b
    for expect in range(10):
        a = randint(1, 10)
        b = randint(1, 10)
        assert add(a, b) > 0

# для проверки запуска конкретного теста нужно:
'''
1. pytest название файла::функция
2. метка (@pytest.mark.) -> pytest название файла -m метка
'''

# Служебные метки (@pytest.mark...)
# parametrize, skip, skipif
"""
1. Найти информацию о служебных метках
2. Написать тест, который будет проверять четность и нечетность чисел
Если числа нечетные -> assert True
3. Написать метку skipif, если оба числа будут либо нечетными, либо
меньше нуля
4. Написать метку parametrize с разными данными
5. Написать тест, который будет проверять выражение на палиндром
(берется текст)
"""
