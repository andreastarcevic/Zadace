import random
from rocket import Rocket

class Tank(Rocket):
    def __init__(self, x=0, y=0, route = 0):
        super().__init__(x, y)
        self.route = route
    
    
    def fight_tank(self):
        tankNum = int(input("Unesite broj tenkova na ratnom polju: ")) 
        tanks = []
        rockets = []
        for x in range(0,tankNum): 
            x = random.randint(0,100)
            y = random.randint(1,100)
            self.route = random.randint(0,10)
            tanks.append(Tank(x,y,self.route))
        
        for x in range(0, tankNum): 
            x = random.randint(0,100)
            y = random.randint(1,100)
            rockets.append(Rocket(x, y))
        
        for index, tank in enumerate(tanks):
            print("Tenk {} je napravio {} rutu/e".format(index+1, tank.route))
        
        print("\n")
        yourTank = int(input("Od {} tenkova, vaš tenk je pod brojem: ".format(tankNum)))
        
        chosenTank = tanks[yourTank-1]
        for index, tank in enumerate(tanks):
            distance = chosenTank.get_distance(tank)
            print("Vaš Tenk je udaljen {} kilometara od tenka broj {}.".format(distance, index+1))
        
        print("\n")
        for index, rocket in enumerate(rockets):
            distance = chosenTank.get_distance(rocket)
            print("Vaš tenk je udaljen {} kilometara od rakete broj {}.".format(distance, index+1))