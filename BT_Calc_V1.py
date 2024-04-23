class Mech:
    def __init__(self):
        self.model = input("What is the mech model? ")
        self.ton = input("what is the tonnage of the mech? ")
        self.num_weapons = int(input('How many weapons does the mech have? '))
        self.walk = int(input("what is the walk speed of the mech "))
        self.run = int(input("what is the running speed of the mech "))
        self.jump = int(input("what is the jump of the mech "))
        self.weapons = []
        
        weapon_dict = {}
        for _ in range(self.num_weapons):
            weapon = Weapon()
            if weapon.name in weapon_dict:
                print('You already have {} of {}. Do you want to group them? [Yes/No]'.format(weapon_dict[weapon.name], weapon.name))
                if input().strip().lower() == 'yes':
                    if isinstance(weapon_dict[weapon.name],Weapon):
                        group = WeaponGroup()
                        group.Add_Weapon(weapon_dict[weapon.name])
                        group.Add_Weapon(weapon)
                        weapon_dict[weapon.name] = group 
                else:
                    self.weapons.append(weapon)
            else:
                weapon_dict[weapon.name] = weapon
                
        for weapon in weapon_dict.values():
            self.weapons.append(weapon)
        
    def __str__(self):
        return "Model: {} | Tonnage: {} | Walk Speed: {} | Run Speed: {} | Jump: {} | Weapons: {}".format(self.model,self.ton,self.walk,self.run,self.jump,self.weapons)
    
class Weapon:
    def __init__(self):
        self.name = input("what is the weapon/weapon groups name? ")
        self.heat = input("How much heat does the weapon/weapon group build? ")
        self.ammo_types = int(input("How many ammo tpyes does the weapon/weapon group have? "))
        self.ammo = []
        self.damage = int(input("How much damage does this weapon/weapon group do? "))
        
        
        
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
    
class WeaponGroup:
    def __init__(self):
        self.weapons = []
    
    def Add_Weapon(self,weapon):
        self.weapons.append(weapon)
        
    def Group_Heat(self):
        return sum(Weapon.heat for weapon in self.weapons)
    
    def Group_Damage(self):
        return sum(Weapon.damage for weapon in self.weapons)   
    
    def __str__(self):
        weapon = Weapon()
        return "Weapon Group: {} | Heat per weapon {} | Damage per weapon {} ".format(weapon.name, weapon.heat, weapon.damage)
        

mec = Mech()
print(mec)