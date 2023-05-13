import pytest

from random import randint

@pytest.fixture # Метка, определяющая фикстуру
def add_one():
    return 1

@pytest.fixture
def generate_numbers():
    mass = [randint(-1000, 1000) for elem in range(randint(10, 100))]
    return mass

@pytest.fixture
def generate_number():
    return randint(1, 10)
