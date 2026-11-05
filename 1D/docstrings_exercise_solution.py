import random
import time

def enter_name(character_type: str) -> str:
    """Capture a character name from the user for the given character type
    and return it.

    Args:
        character_type: The type of character to be named.

    Returns:
        The name input by the user.
    """
    name = input(f"What is the name of the {character_type}? ")
    return name

def display_hp(
    player_name: str, player_hp: int, enemy_name: str, enemy_hp: str
):
    """Display messages confirming the current player and enemy names and their
    levels of HP

    Args:
        player_name: Name of the player.
        player_hp: Health Points of the player.
        enemy_name: Name of the enemy.
        enemy_hp: Health Points of the enemy.
    """
    print (f"{player_name} has {player_hp}HP")
    print (f"{enemy_name} has {enemy_hp}HP")

def display_attack_status(
    attacker: str, victim: str, atk_val: int, def_val: int
):
    """Display who attacked who and with what strength, as well as who
    defended, and how many points of the attack were defended.

    Args:
        attacker: Name of the attacker.
        victim: Name of the victim.
        atk_val: Value of the attack in attack points.
        def_val: Value of the defence in defence points.
    """
    print (f"{attacker} attacked {victim} with a power of {atk_val}.")
    print (f"{victim} defended {def_val} points of the attack")

def display_character_defeat(victor: str, victim: str):
    """Display the victory / defeat message for a given victor and victim.

    Args:
        victor: Name of the victor.
        victim: Name of the victim.
    """
    print (f"{victim} has been defeated by {victor}")

def attack_enemy(
    player_str: int, enemy_hp: int, enemy_def: int
) -> int, bool, int:
    """Attack the enemy by randomly modifying the strength of the player and
    using that as the attack value.  If the attack value exceeds the enemy's
    defence, reduce their HP by the amount that the attack exceeds the defence.
    Otherwise flag that the attack missed.  Set any negative HP values to 0.
    
    Args:
        player_str: Strength statistic of the player.
        enemy_hp: Current Health Points of the enemy.
        enemy_def: Defence statistic of the enemy.

    Returns:
        The resultant enemy HP, whether the attack missed and the attack value 
        that was calculated.
    """
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

def defend(
    player_hp: int, player_def: int, enemy_str: int
) -> int, bool, int:
    """Defend from an enemy attack by randomly modifying the player's defence
    statistic and using that as the defence value.  If the enemy's strength
    exceeds the player's defence value, the player's HP is reduced by the
    amount the defence value is exceeded.  Otherwise flag that the attack
    missed.  Set any negative HP values to 0.

    Args:
        player_hp: Current Health Points of the player.
        player_def: Defence statistic of the player.
        enemy_str: Strength statistic of the enemy.

    Returns:
        The resultant player HP, whether the attack missed and the calculated
        defence value.
    """
    random_def_modifier = random.randint(-5,5)

    defence_value = player_def + random_def_modifier

    missed = False

    if defence_value < enemy_str:
        player_hp -= (enemy_str - defence_value)
        if player_hp < 0:
            player_hp = 0
    else:
        missed = True

    return player_hp, missed, defence_value

def perform_limit_break(base_str: str) -> int:
    """Perform a limit break and therefore augment the strength of the
    character.  Randomly select an augmentation value for the limit break, and
    add it to the character's base strength statistic.  Display a message
    saying that a limit break has engaged, with the total resultant strength
    value.

    Args:
        base_str: The base strength statistic of the character.

    Returns:
        The augmented strength statistic after the limit break has applied.
    """
    limit_break_power = random.randint(10, 40)

    total_lb_attack_value = limit_break_power + base_str

    print (f"+++LIMIT BREAK ENGAGED!  ATTACK POWER {total_lb_attack_value}")

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

