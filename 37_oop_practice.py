class NewClass():
    def __init__(self, class_name):
        self.class_name = class_name
        self.strength = 10
        self.dexterity = 10 
        self.intelligence = 10
        self.health = self.strength * 4 + self.dexterity * 1
        self.mana = self.intelligence * 2
        self.attack_dmg = self.strength * 3 + self.dexterity * 1
        self.spell_dmg = self.intelligence * 3
        self.chance_to_hit = (85 + self.dexterity / 10) / 100
        self.experience = 0
        self.level = 1

    def raise_statistics(self):
        if self.class_name.lower() == "knight":
            self.strength += 4
            self.dexterity += 2
            self.intelligence += 1
        elif self.class_name.lower() == "rogue":
            self.strength += 1
            self.dexterity += 4
            self.intelligence += 2
        elif self.class_name.lower() == "mage":
            self.strength += 1
            self.dexterity += 1
            self.intelligence += 5

    def level_up(self, experience):
        self.experience += experience
        exp_needed = ((self.level - 1) * 100) + (100 * (self.level**2))
        if self.experience < exp_needed:
            print(f"You gained {experience} experience. You still need {exp_needed - self.experience} points of experience to level up.")
        while self.experience >= exp_needed:
            self.experience -= exp_needed
            self.level += 1
            self.raise_statistics()
            print(f"Your {self.class_name} advanced from level {self.level - 1} to level {self.level}.")

    def attack(self):
        pass

knight = NewClass("knight")
knight.level_up(400)
knight.level_up(400)
knight.level_up(400)
knight.level_up(400)
