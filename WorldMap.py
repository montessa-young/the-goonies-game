from Dungeons import Dungeon
from NPC import Enemy


class WorldMap:
    def __init__(self):
        self.locations = {
            "Town": "A peaceful place to rest.",
            "Forest": "Dangerous creatures lurk here.",
            "Dungeon": Dungeon("Ancient Dungeon", [
                Enemy("Skeleton", 40, 4, 9),
                Enemy("Zombie", 45, 3, 8)
            ])
        }

    def travel(self, player):
        print("\nWhere would you like to go?")
        locations = list(self.locations.keys())
        for i, loc in enumerate(locations, 1):
            print(f"{i}. {loc}")

        choice = input("> ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(locations)):
            print("Invalid choice.")
            return

        location = locations[int(choice) - 1]
        print(f"You travel to the {location}.")

        dest = self.locations[location]
        if isinstance(dest, Dungeon):
            dest.enter(player)
        else:
            print(dest)
