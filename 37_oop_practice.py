class NewClass:
    def __init__(self, class_name):
        self.class_name = class_name
        self.dead = False
        self.experience = 0
        self.level = 1
        self.attack = 10
        self.spell_dmg = 10
        self.health = self.level * 4 + self.attack * 1
        self.attacks = {
            "Knight": {"Slash": self.attack},
            "Rogue": {"Poisoned_knife": int(self.attack * 0.75 + self.spell_dmg * 0.5)},
            "Mage": {"Fireball": int(self.spell_dmg * 1.5)},
        }

    def raise_statistics(self):
        if self.class_name.lower() == "knight":
            self.attack += 5
            self.spell_dmg += 1
            self.health += 18
        elif self.class_name.lower() == "rogue":
            self.attack += 4
            self.spell_dmg += 2
            self.health += 16
        elif self.class_name.lower() == "mage":
            self.attack += 1
            self.spell_dmg += 5
            self.health += 10

    def level_up(self, experience):
        self.experience += experience
        exp_needed = ((self.level - 1) * 100) + (100 * (self.level**2))
        if self.experience < exp_needed:
            print(
                f"You gained {experience} experience. You still need {exp_needed - self.experience} points of experience to level up."
            )
        while self.experience >= exp_needed:
            self.experience -= exp_needed
            self.level += 1
            self.raise_statistics()
            exp_needed = ((self.level - 1) * 100) + (100 * (self.level**2))
            print(
                f"Your {self.class_name} advanced from level {self.level - 1} to level {self.level}."
            )

    def combat(self):
        attack, damage = list(self.attacks[self.class_name].items())[0]
        print(f"{self.class_name} used {attack} to deal {damage} damage.")
        return damage

    def take_dmg(self, hp):
        self.health -= hp
        if self.health <= 0:
            self.dead = True
            print(f"Your {self.class_name} took fatal damage. You are dead.")
        else:
            print(f"You took {hp} damage. You have {self.health} health left.")

    def show_statistics(self):
        print(
            f"Your {self.class_name} has {self.level} level, has {self.attack} attack, {self.spell_dmg} spell damage and currently has {self.health} health."
        )


knight = NewClass("Knight")
mage = NewClass("Mage")
knight.level_up(15000)
mage.level_up(15000)
knight.show_statistics()
mage.show_statistics()
while not knight.dead or not mage.dead:
    mage.take_dmg(knight.combat())
    if not mage.dead:
        knight.take_dmg(mage.combat())
    else:
        break
