import random
from rocket import Rocket
from ship import Ship
from tank import Tank
from igraborbeError import IgraborbeError
from random import choice

class Borba(Rocket):
    def __init__(self, x=0, y=0, route = 0):
        super().__init__(x, y)
        self.route = route

    def display_title_bar(self):
        
        print("\t************************************")
        print("\t*** Igra - Borbe tenkova/brodova ***")
        print("\t************************************")

    def get_user_choice(self):
        
        print("\n[1] Pokreni borbu tenkova.")
        print("[2] Pokreni borbu brodova.")
        print("[x] Izlaz.")

        return input("Odaberite što želite napraviti? ")


    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                Tank().fight_tank()
            elif choice == '2':
                Ship().fight_ship()
            elif choice == 'x':
                print("\nHvala na igri i poštenoj borbi. :) Pozdrav!")
            else:
                raise IgraborbeError(101)

if __name__ == "__main__":
    game = Borba()
    game.play()



































