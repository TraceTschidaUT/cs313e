def main() 

    availableArmor = ["plate", "chain", "leather", "none"]
    availableWeapons = ["dagger", "axe", "staff", "sword", "none"]

    for armor in availableArmor:
        tempArmor = Armor(armor)
        print(tempArmor)
    for weapon in availableWeapons:
        tempWeapon = Weapon(weapon)
        print(tempWeapon)

    print("Creating all armor")
    plateMail = Armor("plate")
    print(plateMail)
    chainMail = Armor("chain")
    leatherMail = Armor("leather")
    noneMail = Armor("none")
    traceMail = Armor("trace")
    print()

    print("Creating all weapons")
    dagger = Weapon("dagger")
    print(dagger)
    hands = Weapon("none")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")
    traceWeapon = Weapon("trace")
    print()

    print("Testing Gandalf Weapons and Armor")    
    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    gandalf.unwield()
    gandalf.wield(sword)
    gandalf.unwield()
    gandalf.wield(dagger)
    gandalf.unwield()
    gandalf.wield(axe)
    gandalf.unwield()
    gandalf.wield(hands)
    gandalf.putOnArmor(plateMail)
    gandalf.takeOffArmor()
    gandalf.putOnArmor(traceMail)
    gandalf.takeOffArmor()
    print()
    
    print("Testing Aragorn Weapons and Armor")
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.takeOffArmor()
    aragorn.putOnArmor(chainMail)
    aragorn.wield(axe)
    aragorn.unwield()
    aragorn.wield(sword)
    print()
    
    print(gandalf)
    print(aragorn)

    print("Testing Fireball")
    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    print("Testing Lightning Bolt")
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    print("Testing Heal")
    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)

    print("Testing Fight")
    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)

    print("Testing no spell points")
    gandalf.spellPoints = 100
    gandalf.castSpell("Heal", aragorn)
    gandalf.castSpell("Heal", aragorn)
    gandalf.castSpell("Heal", aragorn)
    gandalf.castSpell("Heal", aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)



main()