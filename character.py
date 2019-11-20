class character:
    from spells import spells

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
        self.level = 1
        self.armour = 0
        self.evasion = 0
        self.acc = 0

        self.mod = [] #modifers for special classes, see modifier tables

        self._secStatSetup_()
        self._priStatSetup_()

    def _secStatSetup_(self):
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
        elif self.clas == "Arch Angel":
            self.magic = 5
            self.wisdom += 3
            self.strength += 4
            self.discipline = 10
            self.dexterity += 3
            self.stealth = 5
            self.charisma = 5
            self.constit += 4
        elif self.clas == "Dwarven War Master":
            self.magic = 0
            self.wisdom += 5
            self.strength += 10
            self.discipline += 4
            self.dexterity = 4
            self.stealth = 10
            self.charisma = 10
            self.constit += 6
        elif self.clas == "Templar":
            self.magic = 3
            self.wisdom += 6
            self.strength += 8
            self.discipline += 2
            self.dexterity = 8
            self.stealth = 3
            self.charisma += 4
            self.constit += 5
        elif self.clas == "Ork Battle Master":
            self.magic = 0
            self.wisdom += 3
            self.strength += 7
            self.discipline += 4
            self.dexterity = 7
            self.stealth += 3
            self.charisma = 5
            self.constit += 10

    def _priStatSetup_(self):
        #base hp + constit*10
        self.health = 100 + self.constit*10

        #mana base + magic*20
        if self.magic < 10:
            self.mana = 50
        else:
            self.mana = 50 + self.magic*20

        #evasion is base 0
        self.evasion = 0

        #accuarcy 85%
        self.acc = 85


    #combat related
    def dmgInChk(self, preDMG, type):
        """
        calculates dmg taken given info

        :param preDMG: dmg coming before reduction
        :param type: type of dmg, p for pierce r for regular
        :return: na
        """
        if type == "r" and self.armour != 0:
            check = preDMG - self.armour
        if check > 0:
            self.health -= check
        elif type == "r" and self.armour == 0:
            self.health -= preDMG
        elif type == "p":
            self.health -= preDMG

    def dmgOut(self):
        pass

    def getSpeed(self):
        """
        calcs speed

        :return: net speed
        """

        return self.dexterity - self.armour

    #checks

    def strCheck(self):
        pass

    def charCheck(self):
        pass

    def magCheck(self):
        pass

    def dexCheck(self):
        pass

    def stlCheck(self):
        pass

    def wisCheck(self):
        pass

    #leveling
    #note leveling up is done post combat

    def addExp(self, exp):
        self.exp += exp
        self._isLvlUp_()

    def _isLvlUp_(self):
        if self.level == 0:
            #exp to lvl up 50
            if self.exp >= 50:
                self.exp -= 50
                self._lvlUp_(0)
        elif self.level >= 1 and self.level <= 10:
            #exp to lvl up 100
            if self.exp >= 100:
                self.exp -= 100
                self._lvlUp_(1)
        elif self.level >= 11 and self.level <= 20:
            #exp to lvl up 200
            if self.exp >= 200:
                self.exp -= 200
                self._lvlUp_(2)
        elif self.level >= 21 and self.level <= 30:
            #exp to lvl up 300
            if self.exp >= 300:
                self.exp -= 300
                self._lvlUp_(3)
        elif self.level >= 31 and self.level <= 40:
            #exp to lvl up 400
            if self.exp >= 400:
                self.exp -= 400
                self._lvlUp_(4)
        elif self.level >= 41 and self.level <= 50:
            #exp to lvl up 500
            if self.exp >= 500:
                self.exp -= 500
                self._lvlUp_(5)



    def _lvlUp_(self, tier):
        print("**********************")
        print("You leveled up!")

        avPoints = 0

        if tier == 0:
            avPoints = 5
        elif tier == 1:
            avPoints = 3
        elif tier == 2:
            avPoints = 4
        elif tier == 3:
            avPoints = 5
        elif tier == 4:
            avPoints = 5
        elif tier == 5:
            avPoints = 5

        for i in range(avPoints):
            print("You have {} points avilible!".format(avPoints))

            print()
            print("Current stats:")
            print("1. Magic        : ", self.magic)
            print("2. Wisdom       : ", self.wisdom)
            print("3. Strength     : ", self.strength)
            print("4. Discipline   : ", self.discipline)
            print("5. Dexterity    : ", self.dexterity)
            print("6. Stealth      : ", self.stealth)
            print("7. Charisma     : ", self.charisma)
            print("8. Constitution : ", self.constit)
            print()

            print("To add points to a stat type stat# then a space then the amount of points you want to add (up to {} points)".format(avPoints))
            userIn = str(input("Enter: "))
            stat, val = userIn.split(" ")
            stat = int(stat)
            val = int(val)

            if val <= avPoints and val >= 0 and stat > 0 and stat <= 8:
                if stat == 1:
                    self.magic += val
                    avPoints -= val
                elif stat == 2:
                    self.wisdom += val
                    avPoints -= val
                elif stat == 3:
                    self.strength += val
                    avPoints -= val
                elif stat == 4:
                    self.discipline += val
                    avPoints -= val
                elif stat == 5:
                    self.dexterity += val
                    avPoints -= val
                elif stat == 6:
                    self.stealth += val
                    avPoints -= val
                elif stat == 7:
                    self.charisma += val
                    avPoints -= val
                elif stat == 8:
                    self.constit += val
                    avPoints -= val

            if avPoints == 0:
                break

        print("**********************")


