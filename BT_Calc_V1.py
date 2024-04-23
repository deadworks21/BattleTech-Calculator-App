class Mech:
    def __init__(self):
        self.model = input("What is the mech model? ")
        self.ton = input("what is the tonnage of the mech? ")
        self.num_weapons = int(input('How many weapons does the mech have? '))
        self.walk = int(input("what is the walk speed of the mech "))
        self.run = int(input("what is the running speed of the mech "))
        self.jump = int(input("what is the jump of the mech "))
        self.weapons = []

        for _ in range(self.num_weapons):
            weapon = Weapon()  
            self.weapons.append(weapon)
        
    def __str__(self):
        return "Model: {} | Tonnage: {} | Walk Speed: {} | Run Speed: {} | Jump: {} | Weapons: {}".format(self.model,self.ton,self.walk,self.run,self.jump,self.weapons)
    
class Weapon:
    def __init__(self):
        self.name = input("what is the weapons name? ")
        self.heat = input("How much heat does the weapon build? ")
        self.ammo_types = int(input("How many ammo tpyes does the weapon have? "))
        self.ammo = []
        
        for _ in range(self.ammo_types):
            ammo_count = int(input("How much starting ammo of this type do you have? "))
            self.ammo.append(ammo_count)

    def __str__(self):

        for ammo_count in self.ammo:
            if ammo_count <= 0:
                return "Weapon: {} | Heat: {}".format(self.name,self.heat)

        ammo_info = ""
        for i , ammo_count in enumerate(self.ammo,1):
            ammo_info += "Ammo Type {}: {} | ".format(i,ammo_count)
        return "Weapon: {} | Heat: {} | {}".format(self.name,self.heat,ammo_info)
    

mec = Mech()
print(mec)