from Creatures_class import Creature,Dragon_Ball,Wizard
import random

def main():
    welcome_screen()
    game_core()

def welcome_screen():
    print('-------------------------------------')
    print('Welcome to my Wizard Game')
    print('-------------------------------------')

def game_core():
    creatures = [Creature('Sampa the Tigress',58448),
                 Creature('Slayer the Hammerhead',20920),
                 Creature('Tweedly the Slithrer',90932),
                 Dragon_Ball('Toothless',34342,mutation=3),
                 Dragon_Ball('Sacred_Ashes',2090,mutation=5),
                 Wizard('The Evil Marshmallow',988)
                 ]
    hero = Wizard('Kicki the witch',9999) # need to create a hero

    while True:
        #randomly choose a creature
        #current_creature = creatures[random.randint(0, len(creatures)-1)]
        current_creature = random.choice(creatures)

        print(f'A creature {current_creature.name} has appeared from the forest of dread')

        cmd = input(f'Our glorious Hero---> {hero.name}, Do you want to [a] Attack,[c] chicken out and run , [l] look around helplessly')

        if cmd == 'a':
            #Attack
            if hero.attack(current_creature):
                print('Heeee haahahah the Wizard wins!')
                creatures.remove(current_creature)
            else:
                print('It is with sadness that I have to say that the Wizard is vanquished')
            pass
        elif cmd == 'l':
            pass
        else:
            pass

        if not creatures:
            print('There is nothing left to vanquish')
            break

if __name__ == "__main__":

    main()