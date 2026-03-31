import random
from BattleSystem import BattleSystem
from NPC import Enemy


def random_encounter(player):
    encounters = [
        Enemy("Goblin", 30, 3, 7),
        Enemy("Wolf", 25, 4, 8),
        Enemy("Bandit", 35, 5, 10)
    ]

    enemy = random.choice(encounters)
    battle = BattleSystem(player, enemy, qte_word="fight")
    return battle.start_battle()
