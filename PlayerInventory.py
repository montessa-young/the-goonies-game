from SaveManager import auto_save

class PlayerInventory:
    def __init__(self):
        self.items = []
        self.gear = {
            "Headgear": None,
            "Facegear": None,
            "Undershirt": None,
            "Overshirt": None,
            "Belt": None,
            "Pants": None,
            "Shoes": None,
            "Swords": None,
            "Shields": None,
            "Guns": None
        }

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item['name']} to your inventory.")

    def equip_item(self, player, item_name, story=None):
        for item in self.items:
            if item["name"] == item_name:
                slot = self.find_slot_for_item(item_name)

                if slot is None:
                    print("This item cannot be equipped.")
                    return

                if self.gear[slot]:
                    old = self.gear[slot]
                    self.remove_stats(player, old)
                    self.items.append(old)
                    print(f"Unequipped {old['name']}.")

                self.gear[slot] = item
                self.apply_stats(player, item)
                self.items.remove(item)

                print(f"Equipped {item['name']} in {slot}.")
                if story:
                    auto_save(player, story)
                return

        print("You don't have that item.")

    def unequip(self, player, slot, story=None):
        if slot not in self.gear:
            print("Invalid slot.")
            return

        if self.gear[slot] is None:
            print("Nothing is equipped there.")
            return

        item = self.gear[slot]
        self.remove_stats(player, item)
        self.items.append(item)
        self.gear[slot] = None

        print(f"Unequipped {item['name']} from {slot}.")
        if story:
            auto_save(player, story)

    def apply_stats(self, player, item):
        player.max_damage += item["atk"]
        player.defense += item["def"]
        player.max_hp += item["hp"]
        player.hp += item["hp"]

    def remove_stats(self, player, item):
        player.max_damage -= item["atk"]
        player.defense -= item["def"]
        player.max_hp -= item["hp"]
        if player.hp > player.max_hp:
            player.hp = player.max_hp

    def find_slot_for_item(self, item_name):
        for slot in self.gear:
            if item_name in slot or slot in item_name:
                return slot
        return None
