from Player import Player
from WorldMap import WorldMap
from RandomEncounters import random_encounter
from Shop import shop
from StoryManager import StoryState, run_story
from SaveManager import save_game, load_game, auto_save


class Game:
    def __init__(self, player=None, story=None):
        self.player = player if player else Player("Hero")
        self.map = WorldMap()
        self.story = story if story else StoryState()

    def show_achievements(self):
        print("\n--- Achievements ---")
        if not self.story.achievements:
            print("No achievements yet.")
            return
        for a in sorted(self.story.achievements):
            print(f"- {a}")

    def gear_menu(self):
        while True:
            print("\n--- Gear Menu ---")
            print("1. View Equipped Gear")
            print("2. View Inventory")
            print("3. Equip Item")
            print("4. Unequip Item")
            print("0. Back")

            choice = input("> ").strip()

            if choice == "1":
                self.player.inventory.show_gear()
            elif choice == "2":
                self.player.inventory.show_inventory()
            elif choice == "3":
                item = input("Enter item name to equip: ")
                self.player.inventory.equip_item(self.player, item, self.story)
            elif choice == "4":
                slot = input("Enter slot to unequip: ")
                self.player.inventory.unequip(self.player, slot, self.story)
            elif choice == "0":
                return
            else:
                print("Invalid choice.")

    def save_menu(self):
        print("\n--- Save Menu ---")
        print("1. Save to Slot1")
        print("2. Save to Slot2")
        print("3. Save to Slot3")
        print("0. Back")
        choice = input("> ").strip()

        if choice == "1":
            save_game("Slot1", self.player, self.story)
        elif choice == "2":
            save_game("Slot2", self.player, self.story)
        elif choice == "3":
            save_game("Slot3", self.player, self.story)
        elif choice == "0":
            return
        else:
            print("Invalid choice.")

    def load_menu(self):
        print("\n--- Load Menu ---")
        print("1. Load Slot1")
        print("2. Load Slot2")
        print("3. Load Slot3")
        print("4. Load AutoSave")
        print("0. Back")
        choice = input("> ").strip()

        slot_map = {"1": "Slot1", "2": "Slot2", "3": "Slot3", "4": "AutoSave"}

        if choice in slot_map:
            p, s = load_game(slot_map[choice])
            if p:
                self.player = p
                self.story = s
        elif choice == "0":
            return
        else:
            print("Invalid choice.")

    def main_loop(self):
        print("\nWelcome to the RPG!")

        while True:
            print("\n--- Main Menu ---")
            print("1. Travel")
            print("2. Random Encounter")
            print("3. Story Progression")
            print("4. Gear Menu")
            print("5. Shop")
            print("6. Achievements")
            print("7. Save Game")
            print("8. Load Game")
            print("9. Quit")

            choice = input("> ").strip()

            if choice == "1":
                self.map.travel(self.player)
                auto_save(self.player, self.story)

            elif choice == "2":
                random_encounter(self.player)
                auto_save(self.player, self.story)

            elif choice == "3":
                alive = run_story(self.player, self.story)
                auto_save(self.player, self.story)
                if not alive:
                    print("\nYou died in the story segment.")
                    print("Load a save from the Load Game menu.")

            elif choice == "4":
                self.gear_menu()

            elif choice == "5":
                shop(self.player, self.story)

            elif choice == "6":
                self.show_achievements()

            elif choice == "7":
                self.save_menu()

            elif choice == "8":
                self.load_menu()

            elif choice == "9":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")
