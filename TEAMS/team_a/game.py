from random import randint

def create_killer():
    def set_stat(abilities):
        stat_list = {}
        set_positive_stat = False
        set_negative_stat = False
        print(stat_list)
        for skill_name, description in stat_list.items():
            try:
                print(skill_name + ': ' + description)
                pos_skill = input('Выберите положительную черту из списка выше: ')
                set_positive_stat = True
                neg_skill = input('Выберите негативную черту из списка выше: ')
                set_negative_stat = False
                if pos_skill and neg_skill:
                    abilities.append(stat_list[pos_skill])
                    abilities.append(stat_list[neg_skill])
                    return abilities
            except KeyError:
                print('Несуществующий навык. Попробуйте выбрать снова! ')
                set_positive_stat = False
                set_negative_stat = False

        
    name = 'Aishi'
    _secret_name = 'Gaster'
    set_name = input('Меняем имя или нет? ').lower()
    if set_name == 'да':
        name = input('Введите новое имя: ')
        if name == _secret_name:
            while True:
                print('ERROR' * randint(1000, 10000))
    elif set_name == 'нет':
        print('Установлено имя Aishi')
    else:
        print('Error. Попробуйте снова.')
        
    set_abilities = input('Устанавливаем характеристики? Да\Нет: ').lower()
    abilities = []
    if set_abilities == "да":
        set_stat(abilities)
    elif set_abilities == 'нет':
        print("Пустые характеристики.")
        return name
    else:
        print("Error. Неизвестная команда.")

    return name, abilities

create_killer()
