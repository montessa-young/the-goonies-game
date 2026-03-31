import json
import time
from NPC import Davey
#------------------------
# Starting Menu
#------------------------
def start_menu():
    print("Welcome to GAME.")
    time.sleep(1)
    print("Please input one of the following options.")
    print("1. Start Game")
    print("2. Quit")

    choice = input(": ")

    if choice == "1":
        print("Starting game...")
        Davey()
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid option. Try again.")
        start_menu()
#-----------------------
# In Game Menu
#-----------------------
def in_game_menu():
    print("\n--- IN‑GAME MENU ---")
    time.sleep(0.5)
    print("1. Resume")
    print("3. Quit")

    choice = input("> ")

    if choice == "1":
        print("Resuming game...")
        return "resume"

    elif choice == "2":
        print("Returning to main menu...")
        return "quit"

    else:
        print("Invalid option. Try again.")
        return in_game_menu()