from Game import Game
from SaveManager import initialize_save_file, load_game


def main_menu():
    initialize_save_file()

    while True:
        print("=== RPG GAME ===")
        print("1. New Game")
        print("2. Load Game")
        print("3. Quit")

        choice = input("> ").strip()

        if choice == "1":
            name = input("Enter your name: ").strip() or "Hero"
            game = Game()
            game.player.name = name
            game.main_loop()

        elif choice == "2":
            print("\nWhich slot?")
            print("1. Slot1")
            print("2. Slot2")
            print("3. Slot3")
            print("4. AutoSave")
            print("0. Back")

            c = input("> ").strip()
            slot_map = {"1": "Slot1", "2": "Slot2", "3": "Slot3", "4": "AutoSave"}

            if c in slot_map:
                p, s = load_game(slot_map[c])
                if p:
                    game = Game(p, s)
                    game.main_loop()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
