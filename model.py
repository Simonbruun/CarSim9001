from random import randint

class Car(object):

    def __init__(self):
        self.theEngine = Engine()

    def updateModel(self, dt):
        self.theEngine.updateModel(dt)
#Klassen for wheel giver hjulenes rotation en værdi, så de kan dreje rundt.
class Wheel(object):
#Dette gøres ved at lave en instansvariable som laver et tilfældigt tal mellem 0 og 360.
    def __init__(self):
        self.orientation = randint(0, 360)
#Laver en funktion som udregner og tildeler en ny værdi for self.orientation, ved hjælp af modulus.
    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360
#Klassen Engine indeholder funktioner for motoren og kalder på instanser fra andre klasser.
class Engine(object):


    def __init__(self):
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()
#Funktion updateModel udregner bilens Rpm hvis theTank.contents er højere end nul.
#Hvis den er mindre end nul, afsluttes funktionen uden at gøre noget.
    def updateModel(self, dt):
        if self.theTank.contents > 0:
            self.currentRpm = self.throttlePosition * self.maxRpm
            self.theGearbox.rotate(self.currentRpm * (dt/60))
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
        else:
            self.currentRpm = 0


#Klassen Gearbox bruger funktioner til at kunne gå op og ned i gear.
class Gearbox(object):

    def __init__(self):
        self.wheels = {'frontLeft':Wheel(), 'frontRight':Wheel(), 'rearLeft':Wheel(), 'rearRight':Wheel()}
        self.currentGear = 0
        self.clutchEngaged = False
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
#Funktionen shiftUp bruges til at gå en op i gear ved at bruge længden af gears og ved at tjekke på clutchEngaged.
    def shiftUp(self):
        if self.currentGear < len(self.gears) - 1 and not self.clutchEngaged:
            self.currentGear += 1
#Funktioen shiftDown er næsten det samme som shiftup, den eneste forskel er at vi ikke bruger længden af gears, men den skal bare være over 0.
    def shiftDown(self):
        if not self.clutchEngaged and self.currentGear > 0:
            self.currentGear -= 1
#Funktionen rotate, kalder på hver instans af wheel i wheels i en løkke.
    def rotate(self, revolutions):
        if self.clutchEngaged:
            for wheel in self.wheels:
                self.wheels[wheel].rotate(revolutions * self.gears[self.currentGear])


#Klassen Tank indeholder funktionen for at kunne fylde bilen op og hvor meget den kan indholde.
class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100

#Funktionen refuel gør at contents lig med capacity, så tanken bliver fuld igen.
    def refuel(self):
        self.contents = self.capacity
#Funktionen remove gør så at bilen forbruger benzin.
    def remove(self, amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            self.contents = 0
