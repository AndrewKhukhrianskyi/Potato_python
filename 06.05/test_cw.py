# Служебные метки
# @pytest.mark.служебная метка
import pytest

# skip - пропускает тест
@pytest.mark.skip
def test_smth():
    assert True

# skipif - пропускает тест при определенных условиях
import sys

@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_smth2():
    assert True

# parametrize позволяет вставить данные в тест
@pytest.mark.parametrize(('num','num2'), [(1, 2), (5, 9), (0, -1), (-1, -1), (25, 24)])
def test_add(num, num2):
    assert num + num2 > 0

@pytest.mark.parametrize(('num', 'num2', 'num3', 'perimeter'), [(1, 2, 4, 7),
                                                               (5, 12, 13, 30),
                                                               (8, 4, 2, 14)])
@pytest.mark.perimeter
def test_perimeter(num, num2, num3, perimeter):
    assert num + num2 + num3 == perimeter

'''
HW 06.05
1. Почитать о фикстурах:
https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=fixture#pytest.fixture
2. Почитать о служебных метках (skip, skipif, parametrize):
https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=pytest%20mark#pytest.Mark
3. Решить задачу и протестировать ее:
https://www.codewars.com/kata/62c93765cef6f10030dfa92b
'''


                                                           
