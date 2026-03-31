from player import Player
from worldmap import WorldMap
from random_encounters import random_encounter

class Game:
    def __init__(self):
        self.player = Player()
        self.map = WorldMap()

    def main_loop(self):
        while True:
            ending = self.map.check_for_ending(self.player)
            if ending:
                print(f"\n📜 Ending reached: {ending}")
                if ending == "True Ending":
                    self.player.unlock_achievement("True Hero")
                    self.map.unlock_new_game_plus(self.player)
                break

            print("\n--- MAIN MENU ---")
            print("1. Travel (Random Encounter)")
            print("2. Rest (Advance Time)")
            print("3. Enter Town")
            print("4. Shop")
            print("5. Black Market (if available)")
            print("6. Liberate Town")
            print("7. Defend Town (if under attack)")
            print("8. View NPC Reaction")
            print("9. View World Map")
            print("10. Advance Main Story")
            print("11. Quit")

            choice = input("> ")

            if choice == "1":
                random_encounter(self.player, self.map)
            elif choice == "2":
                self.map.advance_time(self.player)
            elif choice == "3":
                self.map.enter_town(self.player, "Town")
            elif choice == "4":
                self.map.shop(self.player, "Town")
            elif choice == "5":
                if self.map.black_market_available(self.player, "Town"):
                    self.map.black_market(self.player)
                else:
                    print("No black market here.")
            elif choice == "6":
                self.map.liberate_town(self.player, "Town")
            elif choice == "7":
                self.map.defend_town(self.player)
            elif choice == "8":
                print(self.map.npc_reaction(self.player, "Town"))
            elif choice == "9":
                self.map.display_world_map()
            elif choice == "10":
                self.map.advance_main_story(self.player)
            elif choice == "11":
                print("Goodbye.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    game = Game()
    game.main_loop()
