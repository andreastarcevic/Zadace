# prvo pretvorimo stringove (tekst) u brojeve i rjesavamo s modulom, a to znači (igrac1-racunaloigrac2)%5...
# ostatak 1 ili 2 - Win igrac1...3, 4 Win racunaloigrac2...0 Nerijeseno
# "rock","Spock","paper","lizard","scissors" pretvoriti u sljedeće brojeve:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random
from rpslsError import RpslsError 
class Rpsls:
    def _init_(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name = None

    def broj_u_string(self):
        """
        pretvara brojeve (0, 1, 2, 3, 4) u nazive/tekst (rock, spock, paper, lizard, scissors)
        """
        if self.computer_number == 0:
            self.computer_choice_name = "rock"
        elif self.computer_number == 1:
            self.computer_choice_name = "spock"
        elif self.computer_number == 2:
            self.computer_choice_name = "paper"
        elif self.computer_number == 3:
            self.computer_choice_name = "lizard"
        elif self.computer_number == 4:
            self.computer_choice_name = "scissors"
        else:
            self.computer_choice_name = None
            raise RpslsError(103)
        return self.computer_choice_name
        


    def string_u_broj(self):
        """
        pretvara naziv/tekst (rock, spock, paper, lizard, scissors) u broj (0, 1, 2, 3, 4)
        """
        if self.player_input == "rock":
            self.player_number = 0
        elif self.player_input == "spock":
            self.player_number = 1
        elif self.player_input == "paper":
            self.player_number = 2
        elif self.player_input == "lizard":
            self.player_number = 3
        elif self.player_input == "scissors":
            self.player_number = 4
        else:
            self.player_number = -1
            raise RpslsError(102)
        return self.player_number

    def play(self):
        """
        Glavna logika.
        Prvo, radi se korisnikov input, zatim pretvara korisnikov input u broj (metoda string_u_broj), utvrduje 
        pobjednika i na kraju pretvara odabrani broj racunaloigrac2 u tekst (metoda broj_u_string), 
        odabir pobjednika s ostatkom i na kraju ispisuje pobjednika (Winner)
        """
        # unos korisnikovog teksta
        self.player_input = input("Odaberite rock, Spock, paper, lizard ili scissors: ").lower()
        # pretvorba korisnikovog teksta u broj
        self.player_number = self.string_u_broj()
        # racunalo odabire pomocu random metode 
        self.computer_number = random.randrange(0,5)
        ostatak = (self.player_number - self.computer_number)%5
        if(self.player_number == -1):
            winner = "Greska"
            raise RpslsError(101)
        else: 
            if ostatak == 0:
                winner = "Neriješeno"
            elif ostatak == 1 or ostatak == 2:
                winner = "Vi (čovjek) pobjeđujete"
            elif ostatak == 3 or ostatak == 4:
                winner = "Racunalo pobjeduje"
        self.computer_choice_name = self.broj_u_string()
        print("Vi (covjek) ste odabrali: {}".format(self.player_input.title()))
        print("Racunalo je odabralo: {}".format(self.computer_choice_name.title()))
        print(winner)

if __name__ == "__main__":
    game = Rpsls()
    game.play()
