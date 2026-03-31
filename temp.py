import time
import random


def typing_challenge(context_word):
    words_to_type = [context_word, "quick", "escape", "action", "now", "fire", "bombard", "blitz"]
    TIMEOUT = 6

    print("\n--- ACTION CHALLENGE ---")
    print(f"Type the specified word as fast as you can. You have {TIMEOUT} seconds.")

    word_to_type = random.choice(words_to_type)
    print(f"\nType this word: '{word_to_type}'")

    start_time = time.time()
    try:
        user_input = input("Your turn: ")
        end_time = time.time()
        time_taken = end_time - start_time

        if user_input == word_to_type and time_taken < TIMEOUT:
            print(f"SUCCESS! You typed it in {time_taken:.2f} seconds.")
            return True
        else:
            print("\n--- FAILED CHALLENGE! ---")
            if user_input != word_to_type:
                print(f"You typed '{user_input}', but the word was '{word_to_type}'.")
            else:
                print(f"You took too long! You took {time_taken:.2f} seconds.")
            return False
    except (KeyboardInterrupt, EOFError):
        print("\nChallenge abandoned.")
        return False
