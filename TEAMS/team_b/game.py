from random import randint

def create_character():
    def add_abilities(abilities):
        database_abilities = {"Ловкач" : ("Шанс уклонения увеличен", -5),
                              "Крепкий орешек" : ("Способность выдержать удар без потери здоровья.", -6),
                              "Атлет" : ("Шанс побега увеличен", -4),
                              "Богач" : ("Навык убеждения и подкупа увеличен", -4) ,
                              "Острый слух" : ("Навык восприятия и обезвреживания ловушек увеличен", -2),
                              "Смертник" : ("Вы ничего не боитесь и легко переносите урон, но можно очень быстро стать калекой.",
                                            0),
                              "Жирдяй" : ("Шанс побега уменьшен, также вы быстро устаете", 4),
                              "Забывчивость" : ("Навык восприятия и обезвреживания ловушек уменьшен. Есть шанс наткнуться на ту же ловушку.", 2),
                              "Пацифист" : ("Урон снижен в два раза", 10),
                              "Хронический простатит" : ("Все параметры снижены пятикратно.", 10),
                              "Астматик" : ("Вы не можете сбежать с поля боя.", 8)}
        
            
        # TODO - Удалять выбранный навык из базы
            
        number = 0
        while True:
            set_char = input('Добавляем характеристику? Да\Нет: ').lower()
            if set_char == 'да':
                print(database_abilities)
                set_ability = input("Введите навык:").capitalize()
                if set_ability in database_abilities:
                    abilities.append(set_ability)
                    number += database_abilities[set_ability][1]
                    database_abilities.pop(set_ability)
            elif set_char == 'нет':
                if number >= 0:
                    return abilities
                else:
                    print(number)
                    print("Выберите отрицательные навыки, чтобы сбалансировать персонажа.")
            
    name = 'Radga'
    set_name = input('Меняем имя? Да\Нет: ').lower()
    if set_name == "да":
        name = input('Введите новое имя вашего индуса: ')
    elif set_name == "нет":
        print("Установлено имя по умолчанию: Radga")
    else:
        print("Error. Неизвестная команда.")

    set_abilities = input('Устанавливаем характеристики? Да\Нет: ').lower()
    abilities = []
    if set_abilities == "да":
        add_abilities(abilities)
    elif set_abilities == 'нет':
        print("Пустые характеристики.")
        return name
    else:
        print("Error. Неизвестная команда.")

    return name, abilities

database_items = {'Название' : ["Повторяемое название", "Урон"],
                  'Нож' : ["Нож", 10],
                  }
hero = create_character()

stamina = 100
hp = 100
items = []
print(hero)

def fight_enemy(player, player_dmg, enemy_list):
    player_chance = 50
    enemy_name = []
    enemy_dmg = []
    enemy_chance = []
    enemy_hp = []
    for enemy_data in enemy_list:
        enemy_name.append(enemy_data[0]) # Name
        enemy_dmg.append(enemy_data[1]) # dmg
        enemy_chance.append(enemy_data[2]) # chance
        enemy_hp.append(enemy_data[3]) # hp

    while True:
        for enemy in range(len(enemy_list)):
            p_chance = randint(1, 100)
            if player_chance >= p_chance:
                if enemy_hp[enemy] <= 0:
                    pass
                else:
                    print("Удар по врагу!")
                    enemy_hp[enemy] -= player_dmg
            else:
                print("промах")
    # TODO - Написать функцию с главами 1-2
                
                
