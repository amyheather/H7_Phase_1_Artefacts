import random

# TASK 3

def attack_target(player_str, enemy_hp, enemy_def):
    random_atk_modifier = random.randint(-5,5)
    attack_value = player_str + random_atk_modifier
    missed = False

    if attack_value > enemy_def:
        enemy_hp -= (attack_value - enemy_def)
        if enemy_hp < 0:
            enemy_hp = 0
    else:
        missed = True

    return enemy_hp, missed, attack_value

def defend(player_hp, player_def, enemy_str):
    random_def_modifier = random.randint(-5,5)
    defense_value = player_def + random_def_modifier
    missed = False

    if defense_value < enemy_str:
        player_hp -= (enemy_str - defense_value)
        if player_hp < 0:
            player_hp = 0
    else:
        missed = True

    return player_hp, missed, defense_value

def enter_name(character_type):
    name = input(f"What is the name of the {character_type}? ")
    return name

def display_hp(player_name, player_hp, enemy_name, enemy_hp):
    print (f"{player_name} has {player_hp}HP")
    print (f"{enemy_name} has {enemy_hp}HP")

def display_attack_status(attacker, victim, atk_val, def_val):
    print (f"{attacker} attacked {victim} with a power of {atk_val}.")
    print (f"{victim} defended {def_val} points of the attack")

def display_character_defeat(victor, victim):
    print (f"{victim} has been defeated by {victor}")

player_hp = 100
player_str = 50
player_def = 27

enemy_hp = 100
enemy_str = 30
enemy_def = 47

player_name = enter_name("player")
enemy_name = enter_name("enemy")

while True:
    display_hp(
        player_name=player_name,
        player_hp=player_hp,
        enemy_name=enemy_name,
        enemy_hp=enemy_hp
    )

    enemy_hp, missed, atk_val = attack_target(
        player_str=player_str,
        enemy_hp=enemy_hp,
        enemy_def=enemy_def
    )

    display_attack_status(player_name, enemy_name, atk_val, enemy_def)

    if missed:
        print (f"!!{player_name} MISSED!!")

    if enemy_hp == 0:
        display_character_defeat(player_name, enemy_name)
        break

    player_hp, missed, def_val = defend(
        player_hp = player_hp,
        player_def = player_def,
        enemy_str=enemy_str
    )

    display_attack_status(enemy_name, player_name, enemy_str, def_val)

    if missed:
        print (f"!!{enemy_name} MISSED!!")

    if player_hp == 0:
        display_character_defeat(enemy_name, player_name)
        break

