import random
import time

# Function to enter the name of a character, given a provided character type
def enter_name(character_type):
    name = input(f"What is the name of the {character_type}? ")
    return name

# Function to display the current player and enemy HP levels
def display_hp(player_name, player_hp, enemy_name, enemy_hp):
    print (f"{player_name} has {player_hp}HP")
    print (f"{enemy_name} has {enemy_hp}HP")

# Function to display who attacked who and with what strength, and how many
# points of the attack were defended
def display_attack_status(attacker, victim, atk_val, def_val):
    print (f"{attacker} attacked {victim} with a power of {atk_val}.")
    print (f"{victim} defended {def_val} points of the attack")

# Function to display a victory / defeat message, based on a given victor and
# victim
def display_character_defeat(victor, victim):
    print (f"{victim} has been defeated by {victor}")

# Function to attack an enemy, given a player strength, enemy healh points and
# enemy defence level
def attack_enemy(player_str, enemy_hp, enemy_def):
    # Randomly pick an attack modifier
    random_atk_modifier = random.randint(-5,5)

    # Calculate the attack value as player strength modified by the random
    # modifier value
    attack_value = player_str + random_atk_modifier

    # Set up boolean to store if the attack missed, defaulting to False
    missed = False

    # If the attack value exceeds the enemy's defence, then reduce the enemy's
    # HP by the amount above the enemy's defence level.
    if attack_value > enemy_def:
        enemy_hp -= (attack_value - enemy_def)
        # If the enemy HP is now less than 0, set it to 0
        if enemy_hp < 0:
            enemy_hp = 0
    # If the attack value doesn't exceed the enemy's defence level, flag the
    # attack has missed
    else:
        missed = True

    # Return the enemy's HP, whether the attack missed, and the attack value
    return enemy_hp, missed, attack_value

# Function to defend from an enemy attack, given a player HP, player's level of
# defence and the enemy's strength
def defend(player_hp, player_def, enemy_str):
    # Randomly pick a defence modifier
    random_def_modifier = random.randint(-5,5)

    # Calulcate the defence value as player's defence modified by the random
    # modifier value
    defence_value = player_def + random_def_modifier

    # Set up a boolean to store if the attack missed, defaulting to False
    missed = False

    # If the defence value is less than the enemy's strength, reduce the
    # player's HP by the amount their strength exceeds the defence value
    if defence_value < enemy_str:
        player_hp -= (enemy_str - defence_value)
        # If the player's HP is now less than 0, set it to 0
        if player_hp < 0:
            player_hp = 0
    # If the enemy's strength did not exceed the player's defence value, flag
    # the attack missed
    else:
        missed = True

    # Return the player's HP, whether the attack missed, and the defence value
    return player_hp, missed, defence_value

# Function to perform a limit break, given a base strength level
def perform_limit_break(base_str):
    # Randomly determine the additional attack value of the limit break
    limit_break_power = random.randint(10, 40)

    # Calculate the total attack value as the limit break power added to the
    # base strength level
    total_lb_attack_value = limit_break_power + base_str

    # Print a message indicating a limit break has engaged, and its power
    print (f"+++LIMIT BREAK ENGAGED!  ATTACK POWER {total_lb_attack_value}")

    # Return the total limit break attack value
    return total_lb_attack_value

# Set up the player's HP, strength and defence values.  Take copies of the
# starting HP and strength levels, as we'll need them later
player_hp = 50
base_player_hp = player_hp
player_str = 50
base_player_str = player_str
player_def = 27

# Set up the enemy's HP, strength and defence values
enemy_hp = 50
enemy_str = 30
enemy_def = 47

# Set up the probability of a limit break when a limit break window has opened
limit_break_prob = 0.1

# Set up the sleep time (in seconds) between battle messages appearing
sleep_time = 2

# Call the enter_name function twice to gather the player and enemy names
player_name = enter_name("player")
enemy_name = enter_name("enemy")

# Keep doing all of the below until the battle ends
while True:
    # Call the display_hp function to display HP of player and enemy
    display_hp(
        player_name=player_name,
        player_hp=player_hp,
        enemy_name=enemy_name,
        enemy_hp=enemy_hp
    )
    # Sleep
    time.sleep(sleep_time)

    # If the player's HP is less than half of its starting value, we're in the
    # limit break window, so randomly decide whether a limit break will be
    # performed by the player.  If it will be, call the perform_limit_break
    # function and update the player's strength value with the newly calculated
    # limit break strength added on
    if player_hp < (0.5 * base_player_hp):
        if random.random() < limit_break_prob:
            player_str = perform_limit_break(player_str)

    # Call the attack_enemy function to perform an attack on the enemy, and
    # store the resultant enemy HP, whether the attack missed, and what the
    # attack value was
    enemy_hp, missed, atk_val = attack_enemy(
        player_str=player_str,
        enemy_hp=enemy_hp,
        enemy_def=enemy_def
    )

    # Call the display_attack_status function to display who attacked who,
    # and what happened
    display_attack_status(player_name, enemy_name, atk_val, enemy_def)
    # Sleep
    time.sleep(sleep_time)

    # If the attack missed, display a message confirming this
    if missed:
        print (f"!!{player_name} MISSED!!")

    # If the enemy now has no HP left, call the display_character_defeat
    # function to indicate the player has won, and break out of the while loop
    if enemy_hp == 0:
        display_character_defeat(player_name, enemy_name)
        break

    # Call the defend function to defend from an enemy attack, and store the
    # resultant player HP, whether the attack missed, and what the defence
    # value was
    player_hp, missed, def_val = defend(
        player_hp = player_hp,
        player_def = player_def,
        enemy_str=enemy_str
    )

    # Call the display_attack_status function to display who attacked who,
    # and what happened
    display_attack_status(enemy_name, player_name, enemy_str, def_val)
    # Sleep
    time.sleep(sleep_time)

    # If the enemy's attack missed, display a message confirming this
    if missed:
        print (f"!!{enemy_name} MISSED!!")

    # If the player now has no HP left, call the display_character_defeat
    # function to indicate the player has been defeated, and break out of the
    # while loop
    if player_hp == 0:
        display_character_defeat(enemy_name, player_name)
        break

    # At the end of the turn, set the player's strength back to its base value
    # (in case it was modified by a limit break)
    player_str = base_player_str

