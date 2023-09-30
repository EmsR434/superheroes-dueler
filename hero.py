import random



class Hero:
    def _init_(self, name, starting_hp=100):
        self.name = name
        self.starting_hp = starting_hp
        self.current_hp = starting_hp
    
    def fight(self, opponent): 
        '''current Hero will take turns fighting the opponent hero passed in.
        '''



if __name__ == "_main_":
    my_hero = Hero("Spiderman", 300)
    opponent = Hero("Storm", 200)

    Hero.fight(opponent)
