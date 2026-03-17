
#-------------------------------
# Player Inventory
#-------------------------------
class PlayerInventory:
    def __init__(self):
        self.slots = {
            "Headgear": None,
            "Facegear": None,
            "Undershirtgear": None,
            "Overshirtgear": None,
            "Belt": None,
            "Pants": None,
            "Shoes": None
        }


        self.inventory = [None] * 28

    # -------------------------
    # Gear Slot Functions
    # -------------------------
    def equip(self, slot, item):
        if slot in self.slots:
            self.slots[slot] = item
            print(f"Equipped {item} in {slot}.")
        else:
            print(f"{slot} is not a valid gear slot.")

    def unequip(self, slot):
        if slot in self.slots:
            removed = self.slots[slot]
            self.slots[slot] = None
            print(f"Unequipped {removed} from {slot}.")
        else:
            print(f"{slot} is not a valid gear slot.")

    # -------------------------
    # Inventory Slot Functions
    # -------------------------
    def add_item(self, item):
        for i in range(len(self.inventory)):
            if self.inventory[i] is None:
                self.inventory[i] = item
                print(f"Added {item} to slot {i + 1}.")
                return
        print("Inventory is full! Cannot add item.")

    def remove_item(self, slot_number):
        index = slot_number - 1
        if 0 <= index < len(self.inventory):
            removed = self.inventory[index]
            self.inventory[index] = None
            print(f"Removed {removed} from slot {slot_number}.")
        else:
            print("Invalid slot number.")

    # -------------------------
    # Display Functions
    # -------------------------
    def show_inventory(self):
        print("\n--- GEAR SLOTS ---")
        for slot, item in self.slots.items():
            print(f"{slot}: {item if item else 'Empty'}")

        print("\n--- ITEM SLOTS (28) ---")
        for i, item in enumerate(self.inventory, start=1):
            print(f"Slot {i}: {item if item else 'Empty'}")
