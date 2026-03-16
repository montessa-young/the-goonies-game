import random
import time
import sys
def intro():
    def print_slow(text, delay=0.07):
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write("\n")
    def print_slow2(text, delay=0.01):
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write("\n")
    # start game variable "start"
    # end game variable "end"
    # credits variable "credits"
    # gold variable "gold"
    # player variable name "p_name"
    # health variable "hp"
    # weapon variable "weapon"

    gold = random.randint(3,10)
    health = random.randint(30,45)

    # text title screen

    print_slow("Welcome to the GOONIES game!")
    print("               -------------")
    print(" ")
    time.sleep(1)

    # user menu w/ input and time variables

    print_slow("Please enter any option with their corresponding number")
    print("                         ------------------------------")
    time.sleep(1)
    print(" ")
    print_slow2("1. Start Game")
    time.sleep(.5)
    print_slow2("2. End Game")
    time.sleep(.5)
    print_slow2("3. Credits")
    time.sleep(.7)

    print(" ")
    start_input = int(input("Please enter any option: "))
intro()