import random, unicodedata
from time import sleep
from colorama import init, Fore, Back, Style
init(autoreset=True)

heart = unicodedata.lookup('HEAVY BLACK HEART')
rock = Fore.LIGHTBLACK_EX + "Rock" + '\U0000270A'
paper = Fore.BLUE + "Paper" + '\U0000270B'
scissors = Fore.CYAN + "Scissors" + '\U0000270C'
names = ["RM", "Jin", "Suga", "J-Hope", "Jimin", "V", "Jungkook"]
computer_name = Fore.MAGENTA + Style.BRIGHT + random.choice(names) + Style.RESET_ALL
player_score = 0
computer_score = 0

print(Fore.MAGENTA + heart * 7, computer_name, "wants to play with you!", Fore.MAGENTA + heart * 7)
sleep(1)
while True:
    player_move = input('Choose "1" for rock, "2" for paper or "3" for scissors: ')
    if player_move == "1":
        player_move = rock
    elif player_move == "2":
        player_move = paper
    elif player_move == "3":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    print(f"You chose {player_move}.")
    sleep(2)

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"{computer_name} chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Back.MAGENTA + heart * 7 + "You win!" + heart * 7)
        player_score += 1
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
    else:
        print(Fore.RED + "You lose!")
        computer_score += 1
    print(f"Would you like to play against {computer_name} again?")
    play_again = input('Please choose "1" for "yes" or "2" for "no": ')
    if play_again == "2":
        break

print(Fore.LIGHTMAGENTA_EX + Style.DIM + f"You scored {player_score} points. {computer_name}" +
      Fore.LIGHTMAGENTA_EX + Style.DIM + f" scored {computer_score} points.")
print(Fore.MAGENTA + Style.BRIGHT + heart * 7 + " Thank you for playing! " + computer_name,
      Fore.MAGENTA + Style.BRIGHT + " purples you! See you next time! " + heart * 7)
