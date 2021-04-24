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
        self.dirtiness = 0
        # Represents Food, sleeping, Alive
        self.food = 2
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
            print(f'WRONG!!! {self.name} was thinking of {bore}')
            self.boredom -= 1

        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        """Simulate sleeping. The only thing a player can do when the creature is sleeping is try to wake up. However, tiredness and boredom should decrease each round when sleeping"""
        self.isSleeping = True
        self.tiredness -= 3
        self.boredom -= 2

        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0

    def awake(self):
        """Simulate randomly waking a creature up."""
        value = random.randint(0, 2)
        if value == 1:
            print(f"{self.name} just woke up!!")
            self.tiredness = 0
            self.isSleeping = False
        else:
            print(f"{self.name} won't wake up")
            self.sleep()

    def clean(self):
        """Simulate taking a bath to completely clean the creature"""
        self.dirtiness = 0
        print(f"{self.name} has taken a bath. All clean!")

    def forage(self):
        """Simulate forging for food. This will increase the creatures food attributes however , it will also increase their dirtiness"""
        food_found = random.randint(0, 4)
        self.food += food_found

        self.dirtiness += 2

        print(f"{self.name} found {food_found} pieces of food!")

    def show_values(self):
        """Show the current information about the creature """
        print(f"\nCreature name: {self.name}")
        print(f"Hunger (0-10): {self.hunger}")
        print(f"Boredom (0-10): {self.boredom}")
        print(f"Tiredness (0-10): {self.tiredness}")
        print(f"Dirtiness (0-10): {self.dirtiness}")

        print(f"\nFood Inventory: {self.food} pieces.")

        if self.isSleeping:
            print("Current Status: Sleeping")
        else:
            print("Current Status: Awake")

    def increment_values(self, dif):
        """User must set an arbitrary diffuculty. This will control how much 'damage' you take each round. Update the current values of the creatures based on the difficulty."""
        self.hunger += random.randint(0, dif)
        self.dirtiness += random.randint(0, dif)
        if self.isSleeping == False:
            self.boredom += random.randint(0, dif)
            self.tiredness += random.randint(0, dif)

    def kill(self):
        """Check for all conditions to kill or sleep the creature."""
        if self.hunger >= 10:
            print(f"{self.name} has starved to death....")
            self.isAlive = False
        elif self.dirtiness >= 10:
            print(f"{self.name} has suffered an Infection and died...")
            self.isAlive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print(f"{self.name} is bored. Falling asleep...")
            self.isSleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print(f"{self.name} is sleepy. Falling asleep...")
            self.isSleeping = True
