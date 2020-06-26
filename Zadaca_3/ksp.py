# 0 - rock
# 1 - paper
# 2 - scissors

import random
from kspError import KspError
class kps:
    def _init_(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name = None

    def broj_u_string(self):
        """
        pretvara brojeve (0, 1, 2) u nazive/tekst (rock, paper, scissors)
        """
        if self.computer_number == 0:
            self.computer_choice_name = "rock"
        elif self.computer_number == 1:
            self.computer_choice_name = "paper"
        elif self.computer_number == 2:
            self.computer_choice_name = "scissors"
        else:
            self.computer_choice_name = None
            raise KspError(103)
        return self.computer_choice_name
        


    def string_u_broj(self):
        """
        pretvara naziv/tekst (rock, paper, scissors) u broj (0, 1, 2)
        """
        if self.player_input == "rock":
            self.player_number = 0
        elif self.player_input == "paper":
            self.player_number = 1
        elif self.player_input == "scissors":
            self.player_number = 2
        else:
            self.player_number = -1
            raise KspError(102)
        return self.player_number

    def play(self):
        # unos korisnikovog teksta
        self.player_input = input("Odaberite rock, paper ili scissors: ").lower()
        # pretvorba korisnikovog teksta u broj
        self.player_number = self.string_u_broj()
        # racunalo odabire pomocu random metode 
        self.computer_number = random.randrange(0,3)
        ostatak = (self.player_number - self.computer_number)%3
        if(self.player_number == -1):
            winner = "Greska"
            raise KspError(101)
        else: 
            if ostatak == 0:
                winner = "Neriješeno"
            elif ostatak == 1:
                winner = "Vi pobjeđujete"
            elif ostatak == 2:
                winner = "Racunalo pobjeđuje"
        self.computer_choice_name = self.broj_u_string()
        print("Vi ste odabrali: {}".format(self.player_input.title()))
        print("Racunalo je odabralo: {}".format(self.computer_choice_name.title()))
        print(winner)

if __name__ == "__main__":
    game = kps()
    game.play()