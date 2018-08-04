from Game_Logic import PSR_player,Roll
import random

def main():
    welcome_screen()
    game_core()

def welcome_screen():
    print('-------------------------------------')
    print('Welcome to my Paper Scissors Rock game')
    print('-------------------------------------')

def game_core():

    # refactor, create a create_rolls method
    roll_list = []
    roll_paper = Roll()
    roll_paper.set_roll('paper',['rock'],['scissors'])
    roll_list.append(roll_paper)
    roll_scissors = Roll()
    roll_scissors.set_roll('scissors',['paper'],['rock'])
    roll_list.append(roll_scissors)
    roll_rock = Roll()
    roll_rock.set_roll('rock',['scissors'],['paper'])
    roll_list.append(roll_rock)

    #chose a random roll out of the list of objects
    chosen_roll = Roll()
    chosen_roll = random.choice(roll_list)
    print(chosen_roll.roll_name)

    human_choice = Roll()

    while True:
        cmd = input('Hi, Do you want to choose [a] Paper,[b] Scissors , [c] Rock, OR press Ctrl+C to quit')

        if cmd == 'a':
            human_choice.set_roll('paper',['rock'],['scissors'])
            #refactor , put the outcome calculation in a method
            if human_choice.roll_name in chosen_roll.can_defeat:
                print(f"You chose {human_choice.roll_name} and you defeated the computer's choice which was {chosen_roll.roll_name}")
            else:
                print(f"you have lost,You chose {human_choice.roll_name} and the computer's choice  was {chosen_roll.roll_name}")
            break

        if cmd == 'b':
            human_choice.set_roll('scissors',['paper'],['rock'])
            if human_choice.roll_name in chosen_roll.can_defeat:
                print(f"You chose {human_choice.roll_name} and you defeated the computer's choice which was {chosen_roll.roll_name}")
            else:
                print(f"you have lost,You chose {human_choice.roll_name} and the computer's choice  was {chosen_roll.roll_name}")
            break

        if cmd == 'c':
            human_choice.set_roll('rock',['scissors'],['paper'])
            if human_choice.roll_name in chosen_roll.can_defeat:
                print(f"You chose {human_choice.roll_name} and you defeated the computer's choice which was {chosen_roll.roll_name}")
            else:
                print(f"you have lost,You chose {human_choice.roll_name} and the computer's choice  was {chosen_roll.roll_name}")
            break

if __name__ == "__main__":

    main()
