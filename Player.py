import random

class Player:
    def __init__(self, name="Hero"):
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
        self.max_stamina = 100
        self.stamina = self.max_stamina
        self.gold = 100
        self.inventory = []

        # Reputation & alignment
        self.reputation = 0          # 0–100
        self.alignment = 0           # -100 evil, 0 neutral, +100 good

        # NPC memory
        self.npc_memory = {}

        # Achievements
        self.achievements = {
            "First Blood": False,
            "Town Savior": False,
            "Master of Commerce": False,
            "Guild Master": False,
            "Legend Hunter": False,
            "World Explorer": False,
            "Event Conqueror": False,
            "Questline Champion": False,
            "True Hero": False
        }

        # New Game+
        self.new_game_plus = False

    def increase_reputation(self, amount):
        self.reputation = min(100, self.reputation + amount)
        print(f"Your reputation increased to {self.reputation}.")

    def decrease_reputation(self, amount):
        self.reputation = max(0, self.reputation - amount)
        print(f"Your reputation decreased to {self.reputation}.")

    def change_alignment(self, amount):
        self.alignment = max(-100, min(100, self.alignment + amount))
        print(f"Your alignment is now {self.alignment}.")

    def unlock_achievement(self, name):
        if name in self.achievements and not self.achievements[name]:
            self.achievements[name] = True
            print(f"\n🏆 ACHIEVEMENT UNLOCKED: {name}!")

    def all_achievements_complete(self):
        return all(self.achievements.values())

