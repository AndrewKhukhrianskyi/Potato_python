from random import randint

def create_killer():
    def set_stat(abilities):
        stat_list = {"Меткая: увеличивает шанс попадания" : 5,
                     "Социальный хамелеон: подстраиваетесь под окружение и людей" : 5,
                     "Плохое зрение: уменьшает шанс попадания, а также негативно влияет на некоторые действия в событиях": -5,
                     "Социофоб: Тяжело общаться с людьми" : -5}
        set_positive_stat = False
        set_negative_stat = False
        print(list(stat_list.keys()))
        while True:
            try:
                pos_skill = input('Выберите положительную черту из списка выше: ').capitalize()
                set_positive_stat = True
                neg_skill = input('Выберите негативную черту из списка выше: ').capitalize()
                set_negative_stat = True
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


def get_perks(perk):
    database_perks = {'Отравитель: Шанс отравления увеличен' : 10,
                      "Штрафник: Шанс забить жертву в бою голыми руками увеличен" : 5,
                      "Хитман: Получить все ачивки по убийствам" : 20,
                      "Разорванная селезенка: Получить критическую неудачу при сопротивлении жертвы": -5,
                      "Болевые точки: Критический шанс на убийство одним ударом увеличен" : 5,
                      "Гладиатор: Шанс убийства оппонента в бою увеличивается в два раза" : 20,
                      "Морда кирпичом: Шанс убеждения увеличен" : 5,
                      "Неудачник: Вы никого не убили и вам почему-то не везет..": -50,
                      "Призрак Спарты: Вы остаетесь в здравом психическом состоянии." : 0}
    return database[perk]

def fight(killer_hp, hero, enemy_count, enemy_hp, enemy_dmg, item_list):
    crit_chance = 5
    player_hit_chance = 50
    while killer_hp > 0 and enemy_hp > 0:
            p_chance = randint(1, 100)
            c_chance = randint(1, 100)
            if player_hit_chance >= p_chance:
                if crit_chance >= c_chance:
                    print('Жертва пала замертво...')
                    return killer_hp, hero, item_list
                enemy_hp[enemy] -= player_dmg
            else:
                print("промах")
    if killer_hp < 0:
        return 'Game Over'
    elif enemy_hp < 0:
        print("После долгой борьбы жертва была убита...")
        return killer_hp, hero, item_list

# TODO - наисать главу 1 в виде функции
    
hero = create_killer()
hp = 100
psychical_mood = 0
items = []

