import random

from ability import Ability
from armor import Armor


class Hero:
    # we want our hero to have a default "starting_hp",
    # so we can set that in the function header.
    def _init_(self, name, starting_hp=100):
        ''' Instance properties:
        abilities: list
        armors: list
        name: String
        starting_hp: Integer
        current_hp: Integer
        '''
        # abilities and armors don't have starting values, 
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armor = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_hp = starting_hp
        # when a hero is created, their current health is 
        # always the same as their starting health (no damage taken yet!)
        self.current_hp = starting_hp
    
    def fight(self, opponent): 
        '''current Hero will take turns fighting the opponent hero passed in.
        '''
        outcome = ['wins', 'loses', 'draw']
        result = random.choice(outcome)
        print(f"{self.name} {result} against {opponent.name}")
        pass


    def add_ability(self, ability):
        ''' Add avility to abilities list '''

        # we use the append method to add ability objects to our list.
        self.abilities.append(ability)
    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        self.armor.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total_damage:Int
        '''

        # start the total out at 0
        total_damage = 0 
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage
    
    def defend(self):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
        # start the total out at 0
        total_block = 0 
        # loop through all of our hero's armor
        for ability in self.armor:
            # add the damage of each attack to our running total
            total_block += ability.block()
        # return the total blocked damage
        return total_block
    
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_hp to the current
        # minus the amount returned from calling self.defend(damage).

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check the current_hp of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Spiderman")
    opponent = Hero("Storm")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    Hero.add_ability(ability1)
    Hero.add_ability(ability2)
    Hero.add_ability(ability3)
    Hero.add_ability(ability4)
    Hero.fight(opponent)

