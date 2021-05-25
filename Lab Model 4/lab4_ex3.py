PLAYER = {'name': 'player', 'health': 120, 'damage': 30}
ENEMY = {'name': 'enemy', 'health': 100, 'damage': 50}

PLAYER['name'] = input('Введите имя первого участника: ')
ENEMY['name'] = input('Введите имя второго участника: ')


def attack(atacker, defender):
    defender['health'] -= atacker['damage']

round = 1
while PLAYER['health'] > 0 and ENEMY['health'] > 0:
    print(f'Текущий раунд {round}')
    if round % 2 == 0:
        print(f'Атакует {PLAYER["name"]}')
        attack(PLAYER, ENEMY)
    else:
        print(f'Атакует {ENEMY["name"]}')
        attack(ENEMY, PLAYER)
    print(f'Количество здоровья у участников: \n {PLAYER["name"]} = {PLAYER["health"]} \n {ENEMY["name"]} = {ENEMY["health"]} \n')
    round += 1

if PLAYER['health'] > 0 and ENEMY['health'] <= 0:
    print(f'Победитель состязания {PLAYER["name"]}!')
elif ENEMY['health'] > 0 and PLAYER['health'] <= 0:
    print(f'Победитель состязания {ENEMY["name"]}!')
else:
    print('Ничья')