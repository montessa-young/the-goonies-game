import random
from temp import typing_challenge


class BattleSystem:
    def __init__(self, player, enemy, qte_word=None):
        self.player = player
        self.enemy = enemy
        self.qte_word = qte_word  # word used for QTE (dodge/bonus)

    def player_attack(self):
        damage = random.randint(self.player.min_damage, self.player.max_damage)
        crit_chance = random.random()

        if crit_chance <= self.player.crit_rate:
            damage = int(damage * 1.5)
            print("CRITICAL HIT!")

        damage = max(0, damage)
        self.enemy.hp -= damage
        print(f"You dealt {damage} damage to {self.enemy.name}!")

    def enemy_attack(self):
        base_damage = random.randint(self.enemy.min_damage, self.enemy.max_damage)

        success = False
        if self.qte_word:
            print(f"\n{self.enemy.name} is about to strike!")
            success = typing_challenge(self.qte_word)

        if success:
            print("You dodged the attack!")
            damage = 0
        else:
            defense = getattr(self.player, "defense", 0)
            damage = max(0, base_damage - defense)

        self.player.hp -= damage
        print(f"{self.enemy.name} dealt {damage} damage to you!")

    def start_battle(self):
        print(f"\nA wild {self.enemy.name} appears!")

        while self.player.hp > 0 and self.enemy.hp > 0:
            print("\n--- Your Turn ---")
            print("1. Attack")
            print("2. Use Item")
            print("3. Run")

            choice = input("> ").strip()

            if choice == "1":
                self.player_attack()
            elif choice == "2":
                self.player.use_item()
            elif choice == "3":
                print("You ran away!")
                return False
            else:
                print("Invalid choice.")
                continue

            if self.enemy.hp <= 0:
                print(f"You defeated {self.enemy.name}!")
                return True

            print("\n--- Enemy Turn ---")
            self.enemy_attack()

            if self.player.hp <= 0:
                print("You were defeated...")
                return False
