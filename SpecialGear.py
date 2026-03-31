class SpecialGear:
    def __init__(self, name, attack_bonus=0, hp_bonus=0):
        self.name = name
        self.attack_bonus = attack_bonus
        self.hp_bonus = hp_bonus

    def equip(self, player):
        player.max_damage += self.attack_bonus
        player.max_hp += self.hp_bonus
        player.hp += self.hp_bonus
        print(f"You equipped {self.name}!")
