import pytest

@pytest.mark.parametrize('start,finish,result', [(2,4,2), (3,5,2), (1,6,3)])
def test_task(start, finish, result):
    def solution(start, finish):
        n = finish - start
        return n // 3 + n % 3
    assert solution(start, finish) == result