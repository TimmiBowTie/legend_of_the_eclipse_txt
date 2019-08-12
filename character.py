class character:

    def __init__(self, name, race, clas):
        self.name = name
        self.race = race
        self.clas = clas

        #secondary stats
        self.magic = 10
        self.wisdom = 10
        self.strength = 10
        self.discipline = 10
        self.dexterity = 10
        self.stealth = 10
        self.charisma = 10
        self.constit = 10

        #primary Stats
        self.health = 0
        self.mana = 0
        self.exp = 0
        self.armour = 0
        self.evasion = 0

        self.mod = [] #modifers for special classes, see modifier tables

        self.secStatSetup()
        self.priStatSetup()

    def secStatSetup(self):
        if self.clas == "Ranger":
            self.wisdom += 2
            self.discipline += 3
            self.dexterity += 3
            self.stealth += 1
        elif self.clas == "Assassin":
            self.wisdom += 4
            self.dexterity += 3
            self.stealth += 2
        elif self.clas == "Rogue":
            self.stealth += 4
            self.dexterity += 3
            self.wisdom += 2
        elif self.clas == "Warrior":
            self.strength += 4
            self.constit += 2
            self.wisdom += 1
            self.discipline += 2
        elif self.clas == "Arcane Knight":
            self.magic += 2
            self.strength += 3
            self.constit += 1
            self.wisdom += 1
            self.discipline += 2
        elif self.clas == "Wizard":
            self.magic += 6
            self.wisdom += 3
        elif self.clas == "Angelic Knight":
            self.magic = 5
            self.wisdom += 3
            self.strength += 5
            self.discipline += 3
            self.dexterity += 2
            self.stealth = 2
            self.charisma += 5
            self.constit += 4



    def priStatSetup(self):
        #base hp + constit*10
        self.health = 100 + self.constit*10

        #mana base + magic*20
        self.mana = 50 + self.magic*20

        #dexterity  is out of 100, base + dexterity
        self.evasion = 15 + self.dexterity
