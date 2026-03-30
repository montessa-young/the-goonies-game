import BlacksmithBuyables.py
from BlacksmithBuyables.py import Headgear_Buyables
import time
import random
#----------------------
# Davey (Black Smith)
#----------------------

class NPC:
    def Davey():
        Intro_Davey_Dialogue = ("Davey: Would you like to buy; Headgear, Facegear, Undershirtgear, Overshirtgear, Belt, Pants, Shoes?")
        print(Intro_Davey_Dialogue)
        Choice_001 = input()
        if Choice_001 == "Headgear" or "headgear":
            print(Headgear_Buyables)


#----------------------
# Micheal Jackson (Intro)
#----------------------

class NPC:
    def MikeJack():
        while True:
            autosaveran = random.randint(1,6)
            Intro_MikeJack_Dial = ("Michael Jackson: Would you like to go on a quick adventure with me? y/n")
            yn_choice = ()
            if yn_choice == "y":
                print("Awesome sauce! Come with me to your first battle!")
                break
            elif yn_choice == "n":
                print("Too bad! You can't play the game without starting it!")
                break
            else:
                print("Please retry, invalid option")
        time.sleep(1)
        print("Hey, just to let you know that 8 is the pause menu, and 9 is the inventory button,")
        print("the menu or inventory will NOT be available during quick times, boss battles, shops,")
        print("etc., etc., so be prepared for that")
        time.sleep(10)
        print("Auto Saving...")
        time.sleep(autosaveran)
        Davey()

#----------------------
# Mario (50 Mafia Boss)
#----------------------


#----------------------
# George Droyd (5 thug)
#----------------------


#----------------------
# Rick Astley (20 thug)
#----------------------


#----------------------
# Master Chief (45 thug)
#----------------------


#----------------------
# Sonic (60 Emperor)
#----------------------


#----------------------
# jacksepticeye (38 Mercenary)
#----------------------


#----------------------
# Thugs
#----------------------


#----------------------
# Guards
#----------------------


#----------------------
# Royal Guards
#----------------------


#----------------------
# Police
#----------------------


#----------------------
# Donald Trump (55 President)
#----------------------


#----------------------
# Julius Caesar (50 Emperor
#----------------------