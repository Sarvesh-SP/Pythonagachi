from prac import *


def show_menu(creature):
    """Show the menu options for the player.

    Args:
        creature ([Instance]): [If Sleeping, the player can Only try to wake the creature up by default]
    """
    if creature.isSleeping:
        choice = input("\nEnter (6) to try and wake up: ")
        choice = '6'
    else:
        print("\nEnter (1) to eat.")
        print("Enter (2) to play.")
        print("Enter (3) to sleep.")
        print("Enter (4) to take a bath.")
        print("Enter (5) to forage for food.")
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
        creature.forage()
    elif choice == '6':
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

    rounds = 1
    while player.isAlive:
        print("\n....................................................................................")
        print(f"Round #{rounds}")
        player.show_values()
        rChoice = show_menu(player)
        call_action(player, rChoice)
        print(f"\nRound # {rounds} Summary.")

        player.show_values()
        input("\nPress (enter) to continue...")

        player.increment_values(diff)
        player.kill()

        rounds += 1

    print("\nR.I.P")
    print(f"{player.name} survived a total of {rounds - 1} rounds.")

    choice = input("would you lke to play again (y/n): ").lower()

    if choice != 'y':
        running = False
        print("Thank you for playing Pythonagachi.")
