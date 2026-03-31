class Enemy:
    def __init__(self, name, hp, min_damage, max_damage):
        self.name = name
        self.hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage


class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def talk(self):
        print(f"{self.name}: {self.dialogue}")


class Blacksmith(NPC):
    def __init__(self):
        super().__init__(
            "Davey the Blacksmith",
            "Welcome traveler! Need gear? I’ve got the finest steel in the kingdom."
        )


class ShopItem:
    def __init__(self, name, price, effect=None):
        self.name = name
        self.price = price
        self.effect = effect

    def use(self, player):
        if self.effect:
            self.effect(player)
        print(f"You used {self.name}!")
