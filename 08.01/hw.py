# Task 1 - random
from random import randint 
number = randint(1, 10000)

if number % 2 == 0:
    print(True)
else:
    print(False)

# Task 2 - time
import time
print('Current time is:', time.gmtime())

# Task 3 - Переводчик градусов: Фаренгейты, Цельсии и Кельвины
def temperature_converter(celsium_value = None,
                          farenheint_value = None,
                          kelvin_value = None):
    sub_value = 1.8
    farenheit_sub_value = 0.56
    if celsium_value is not None and farenheint_value is None and kelvin_value is None:
        print(f'Celsium to Farenheit: {(celsium_value * sub_value) + 32}')
        print(f'Celsium to Kelvin: {celsium_value + 273.15}')
    elif farenheint_value is not None and celsium_value is None and kelvin_value is None:
        print(f'Farenheit to Celsium: {(farenheint_value - 32) * sub_value}')
        print(f'Farenheit to Kelvin: {(farenheint_value - 32) * farenheit_sub_value + 273.15}')
    elif kelvin_value is not None and celsium_value is None and farenheint_value is None:
        print(f'Kelvin to Celsium: {kelvin_value - 273.15}')
        print(f'Kelvin to Farenheit: {(kelvin_value - 273.15) * sub_value+ 32}')
    else:
        print('Error!')

temperature_converter(10)