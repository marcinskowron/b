import random

game_options = ['p', 'n', 'k']

trials = 0

won = 0

while True:

    print("\n[p] Papier\n[n] Nożyce\n[k] Kamień")

    players_choice = input("Twój wybór: ").lower()

    if players_choice in game_options:

        computers_choice = random.choice(game_options)

        if players_choice == computers_choice:

            print("oooooooooooooooooooo\n\tREMIS\noooooooooooooooooooo")

            trials += 1

        elif (players_choice == 'p' and computers_choice == 'k') or (
                players_choice == 'n' and computers_choice == 'p') or (
                players_choice == 'k' and computers_choice == 'n'):

            print("oooooooooooooooooooo\n\tWYGRANA\noooooooooooooooooooo")

            trials += 1

            won += 1

        else:

            print("oooooooooooooooooooo\n\tPRZEGRANA\noooooooooooooooooooo")

            trials += 1

    else:

        print("Nie rozpoznano wyboru. Prawidłowe wybory to 'p', 'n' lub 'k'")

    print('Liczba gier:', trials, '\nWygrane:', won)

    continue_choice = input("Kontynuować grę? [y/n]")

    if continue_choice.lower() == 'n':
        break