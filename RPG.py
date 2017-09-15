#  File: RPG.py
#  Description: An RPG game via the command line 
#  Student's Name: Trace Tschida
#  Student's UT EID: TRT729
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 9/15/2017
#  Date Last Modified: 9/15/2017

class Weapon():

    # initalizer
    def __init__ (self, _weapon_type):

        self.weapon_type = _weapon_type
        
        # determine the weapon type
        if _weapon_type == "dagger":
            self.damage = 4
        elif _weapon_type == "axe":
            self.damage = 6
        elif _weapon_type == "staff":
            self.damage = 6
        elif _weapon_type == "sword":
            self.damage = 10
        elif _weapon_type == "none":
            self.damage = 1
        else: # if the weapon is not of type defined
            self.weapon_type = None
            self.damage = None

            # inform the user that the weapon does not exist
            print("This weapon is not valid")

    # str method to print information
    def __str__(self):
        return ("")

class Armor():

    # initalizer
    def __init__(self, _armor_type):
        self.armor_type = _armor_type

        # determine the amount of protection
        if _armor_type == "plate":
            self.protection = 2
        elif _armor_type == "chain":
            self.protection = 5
        elif _armor_type == "leather":
            self.armor_type = 8
        elif _armor_type == "none":
            self.protection = 10
        else: # if the armor is not a valid type
            self.armor_type = None
            self.protection = None

            # inform the user that the armor type does not exist 
            print("This armor type does not exist")

class RPGCharacter():
    
    def __init__(self, _name):
        self.name = _name
        self.weapon = Weapon("none")
        self.armor = Armor("none")
    
    def unwield (self):
        self.weapon = Weapon("none")

        # print the message 
        print(self.name + " is no longer wielding anything.")

    def takeOffArmor (self):
        self.armor = Armor("none")

        # print the message 
        print(self.name + " is no longer wearing anything")
    
    def fight(self, _character):

        # print the message 
        print(self.name + " attacks " + _character.name + " with a(n)" + self.weapon.weapon_type)
        
        # deduct the health 
        _character.health -= self.weapon.damage
        print(self.name + " does " + str(self.weapon.damage) + " damage to " + _character.name)

        # print the opponets health
        print(_character.name + " is now down to " +str(_character.health) + " health")

        # check for defeat 
        self.checkForDefeat()

    def __str__(self):
        return("{0:s} \n Current Health: {1:f} \n Current Spell Points: {2:f} \n Wielding: {3:s} \n Wearing: {4:s} \n Armor Class: {5:f}".format(self.name, self.health, self.spellPoints, self.weapon.weapon_type, self.armor.armor_type, self.armor.protection))

    def checkForDefeat(self, _character):
        if _character.health < 0:
            print(_character.name + " has been defeated")

class Fighter(RPGCharacter):
    
    # class variables and methods
    maxHealth = 40
    maxSpellPoints = 0
    availableArmor = ["plate", "chain", "leather", "none"]
    availableWeapons = ["dagger", "axe", "staff", "sword", "none"]

    # instance variables and methods
    
    def __init__(self, _name): 
        # call the superclass' constructor
       super().__init__(_name)
       self.health = 40
       self.spellPoints = 0

    def wield (self, _weapon_type):

        # determine if the weapon is allowed
        if _weapon_type in self.availableWeapons:

            self.weapon = _weapon_type

            # print the message
            print(self.name + " is now wielding a(n) " + self.weapon.weapon_type)
        
        else: # if the weapon can be used
            print("Weapon not allowed for the character class") 

    def putOnArmor (self, _armor_type):

        # check to see if armor type if allowed 
        if _armor_type in self.availableArmor:

            # set the armor 
            self.armor = _armor_type

            # print the message 
            print(self.name + " is now wearing " + self.armor.armor_type)
        
        else: # if the armor type cannot be worn
            print("Armor not allowed for this character class")

class Wizard(RPGCharacter):

    # class variables and methods
    maxHealth = 16
    maxSpellPoints = 20
    availableArmor = ["none"]
    availableWeapons = ["dagger", "staff"]

    # call the superclass' constructor
    def __init__(self, _name):
        super().__init__(_name)
        self.health = 16
        self.spellPoints = 20

    def wield (self, _weapon_type):

        # determine if the weapon is allowed
        if _weapon_type in self.availableWeapons:

            self.weapon = _weapon_type

            # print the message
            print(self.name + " is now wielding a(n) " + self.weapon.weapon_type)
        
        else: # if the weapon can be used
            print("Weapon not allowed for the character class")

    def putOnArmor (self, _armor_type):

        # check to see if armor type if allowed 
        if _armor_type in self.availableArmor:

            # set the armor 
            self.armor = _armor_type

            # print the message 
            print(self.name + " is now wearing " + self.armor.armor_type)
        
        else: # if the armor type cannot be worn
            print("Armor not allowed for this character class")
    
    def castSpell(self, _spell_name, _character):

        # create the spell instance
        if _spell_name in ["Fireball", "Lightning Bolt" , "Heal"]:
            
            # create a new spell 
            spell = Spell(_spell_name)

            # check to see if character has enough points
            if self.spellPoints - spell.spellPoints < 0:

                print("Insufficient spell points")
                return 

            else: # if there is enough spell points

                # deduct the spell points
                self.spellPoints -= spell.spellPoints

                # determine the output for the spell based on type
                if spell.name == "Heal":

                    # check to see if the heal is more than max health 
                    if _character.health + spell.effect > _character.maxHealth:
                        _character.health = _character.maxHealth
                    else:
                        _character.health -= spell.effect

                    print(self.name + " heals " + _character.name + " for 6 health points")
                
                else:

                    # change the heal of the target
                    _character.health -= spell.effect
                    
                    print(self.name + " cast " + _spell_name + " at " + _character.name)
                    print(_character.name + " is now down to " + _character.health + " health")

                    # check for defeat
                    self.checkForDefeat()    

        else:
            print ("Unknown spell name. Spell failed.")
            return


class Spell():

    # set the properties for the spell
    def __init__(self, _spell_name):

        self.name = _spell_name

        if _spell_name == "Fireball":
            self.spellPoints = 3
            self.effect = 5
        elif _spell_name == "Lightning Bolt":
            self.spellPoints = 10
            self.effect = 10
        elif _spell_name == "Heal":
            self.spellPoints = 6
            self.effect = -6
        else:
            self.spellPoints = 0
            self.effect = 0
            self.name = None

            print("That spell does not exist")

def main():


main()