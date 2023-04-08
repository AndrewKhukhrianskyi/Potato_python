'''
Config - это конфигурационный файл,
для сохранения постоянных выражений (например, названия приложения)

Правила оформления:
Все переменные начинаются С Больших букв полностью, например TITLE = ...
'''

# Параметры окна

TITLE = 'Анализатор текста V 1.0.0'
WIDTH = 500
HEIGHT = 800

RESIZABLE_STATUS_WIDTH = False
RESIZABLE_STATUS_HEIGHT = False

BUTTON_WIDTH = 10
BUTTON_HEIGHT = 1

TEXT_WIDTH = 50
TEXT_HEIGHT = 15

TEXT_ENTRY_WIDTH = 50
TEXT_ENTRY_HEIGHT = 1

LABEL_WIDTH = 50

# Работа с текстом
ANALYZE_TEXT_LIST = ["Кол-во гласных букв:",
                     "Кол-во согласных букв:",
                     "Кол-во символов:",
                     "Часто встречаемая буква:",
                     "Редко встречаемая буква:",
                     "Не встречаемая буква:",
                     "Кол-во чисел:",
                     "Среднее арифметическое по кол-ву текста:"]

LANGUAGE_RU ='абвгдеёжзийклмнопрстюфхцчшщьъэюя'
LANGUAGE_UA = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
LANGUAGE_EN = 'abcdefghijklmnopqrstuvwxyz'

