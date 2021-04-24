from prac import *


def show_menu(creature):
    """Show the menu options for the player.

    Args:
        creature ([Instance]): [If Sleeping, the player can Only try to wake the creature up by default]
    """
    if creature.isSleeping:
        choice = input("\nEnter (6) to try and wake up")
        choice = 6
    else:
        print("\n Enter (1) to eat.")
        print("\nEnter (2) to play.")
        print("\nEnter (3) to sleep.")
        print("\nEnter (4) to take a bath.")
        print("\nEnter (5) to forage for food.")
        choice = input("What is your choice: ")

    return choice


def call_action(creature, choice):
    """Call the appropriate class methods based on the choice.

    Args:
        creature ([Instance]]): [description]
        choice ([str]): [description]
    """
    if choice == '1':
        creature.eat()
    elif choice == '2':
        creature.play()
    elif choice == '3':
        creature.sleep()
    elif choice == '4':
        creature.clean()
    elif choice == '5':
        creature.awake()

    else:
        print('Sorry, that is not a valid move.')


print('Welcome to the Pythonagachi Simulator App')

diff = int(input('Please choose a difficulty level (1-5): '))
if diff > 5:
    diff = 5
elif diff < 1:
    diff = 1

running = True
while running:
    name = input('What name would you like to give your pet Pythonagachi: ')
    player = Creature(name)
