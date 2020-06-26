class HutError(Exception):
    def _init_(self, code):
        self.error_message = ''
        self.error_dict ={
            000: "Kod 000: Nespecificirana greška u programskom kodu za klasu Hut",
            101: "Kod 101: Uneseni broj je izvan zadanog raspona: Broj > 5",
            102: "Kod 102: Uneseni broj je izvan zadanog raspona: Broj nije pozitivan",
            103: "Kod 103: Uneseni broj je izvan zadanog raspona: Broj je 0",
            104: "Kod 104: Unesena vrijednost nije broj"
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        print("\n Opis greške: {}".format(self.error_message))

class HutError000(Exception):
    def _init_(self, msg = ''):
        self.error_message = self.znakovi + 'Kod 000: Nespecificirana greška u programskom kodu za klasu Hut' + '\n'
        print("Opis greške: {}".format(self.error_message))

class HutError101(Exception):
    def _init_(self, msg = ''):
        self.error_message = self.znakovi + 'Kod 101: Uneseni broj je izvan zadanog raspona: Broj > 5' + '\n'
        print("Opis greške: {}".format(self.error_message))

class HutError102(Exception):
    def _init_(self, msg = ''):
        self.error_message = self.znakovi + 'Kod 102: Uneseni broj je izvan zadanog raspona: Broj nije pozitivan' + '\n'
        print("Opis greške: {}".format(self.error_message))

class HutError103(Exception):
    def _init_(self, msg = ''):
        self.error_message = self.znakovi + 'Kod 103: Uneseni broj je izvan zadanog raspona: Broj je 0' + '\n'
        print("Opis greške: {}".format(self.error_message))

class HutError104(Exception):
    def _init_(self, msg = ''):
        self.error_message = self.znakovi + 'Kod 104: Unesena vrijednost nije broj' + '\n'
        print("Opis greške: {}".format(self.error_message))