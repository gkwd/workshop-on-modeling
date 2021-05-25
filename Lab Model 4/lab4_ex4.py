PLAYER = {'name': 'player', 'health': 120, 'damage': 30, 'armor': 1.2}
ENEMY = {'name': 'enemy', 'health': 100, 'damage': 50, 'armor': 1.2}

PLAYER['name'] = input('Введите имя первого участника: ')
ENEMY['name'] = input('Введите имя второго участника: ')

def log_char(character):
    for char, value in character.items():
        print(char, value)
    print('\n')

def compute_damage(damage, armor):
    return damage / armor

def attack(atacker, defender):
    defender['health'] -= compute_damage( atacker['damage'], defender['armor'])

round = 1

log_char(PLAYER)
log_char(ENEMY)

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