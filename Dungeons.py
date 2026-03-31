from BattleSystem import BattleSystem
from NPC import Enemy


class Dungeon:
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

    def enter(self, player):
        print(f"You enter the {self.name}...")

        for enemy in self.enemies:
            print(f"A {enemy.name} blocks your path!")
            battle = BattleSystem(player, enemy, qte_word="dungeon")
            if not battle.start_battle():
                print("You failed to clear the dungeon...")
                return False

        print(f"You cleared the {self.name}!")
        return True
