from PlayerInventory import PlayerInventory


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.min_damage = 5
        self.max_damage = 12
        self.defense = 0
        self.crit_rate = 0.1
        self.gold = 50

        self.inventory = PlayerInventory()

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"You healed for {amount} HP!")

    def use_item(self):
        print("Using consumable items not implemented yet.")
