class Companion:
    def __init__(self, name, bonus_attack=0, bonus_hp=0):
        self.name = name
        self.bonus_attack = bonus_attack
        self.bonus_hp = bonus_hp

    def apply_bonus(self, player):
        player.max_hp += self.bonus_hp
        player.hp += self.bonus_hp
        player.max_damage += self.bonus_attack
        print(f"{self.name} boosts your stats!")
