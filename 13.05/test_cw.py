import pytest

# Название фикстуры пишется в тесте
# Сначала запускается фикстура, а потом - тест
@pytest.mark.parametrize('number, result',[(1, 2), (4, 5), (7, 8)])
def test_add_one(add_one, number, result): 
    one = add_one # будет лежать 1
    assert number == result

# flaky - плавающий
# Бывают баги, когда не понятно, каким образом они работают
def test_sum(generate_numbers):
    summa = sum(generate_numbers)
    assert summa > 0

def test_gen_num(generate_number):
    number = generate_number
    if number % 2 == 0:
        assert True
    else:
        assert False

'''
1. Почитать о фикстурах:
https://docs.pytest.org/en/7.1.x/how-to/fixtures.html
2. Почитать о yield (*)
https://realpython.com/introduction-to-python-generators/
3. Написать фикстуру, которая будет создавать пароль и логин
4. Написать тест, который будет выводить assert True, если длина пароля между 8 и 16 символами
'''
