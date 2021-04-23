import random


class Creature():
    """Create a simple Tomogachi Clone"""

    def __init__(self, name):
        """Initialise attributes"""
        self.name = name.title()

        # Attributes to track while playing the game.
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtyness = 0
        # Represents Food, sleeping, Alive
        self.food = 0
        self.isSleeping = False
        self.isAlive = True

    def eat(self):
        """Simulate eating. Each time you eat, take one food away from the inventory and randomly take a value away from hunger."""
        if self.food > 0:
            self.food -= 1
            self.hunger -= random.randint(1, 4)
            print(f'Yumm!! {self.name} ate a great meal!')
        else:
            print(f"{self.name} does'nt have any food! Better forage for some.")

        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        """Play a guessing game to lower the creatures boredom
        If you win the game, lower the boredom even more."""
        bore = random.randint(0, 2)
        print(f"\n{self.name} wants to play a game.")
        print(f"{self.name} is thinking a number 0, 1, 2.")
        guess = int(input('What is your guess: '))
        if guess == bore:
            print('That is correct!!!!!!')
            self.boredom -= 3
        else:
            print(f'WRONG!!! {self.name} was thinking of {self.bore}')
            self.boredom -= 1

        if self.boredom < 0:
            self.boredom = 0

    def sleep():
        pass

    def awake():
        pass

    def clean():
        pass

    def forage():
        pass

    def show_values():
        pass

    def increment_values():
        pass

    def kill():
        pass
