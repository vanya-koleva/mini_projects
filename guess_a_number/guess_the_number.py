import random
import time
import unicodedata
from colorama import init, Fore, Back, Style
init(autoreset=True)

purple = Fore.MAGENTA + Style.BRIGHT
light_purple = Fore.LIGHTMAGENTA_EX
back = Back.BLACK
hearts = unicodedata.lookup('HEAVY BLACK HEART') * 7
names = ["RM", "Jin", "Suga", "J-Hope", "Jimin", "V", "Jungkook"]
computer_name = purple + random.choice(names) + Style.RESET_ALL
print(f"{back}{purple}{hearts}Can you guess the number {computer_name}{back}{purple} has in mind?{hearts}")
print(f"{computer_name} challenges you to guess the numbers he has in mind."
      f"\nBut you only have one minute! \nHow many numbers can you guess?")
time.sleep(4)


def guess_the_number():
    level = 1
    score = 0
    time_limit = 60
    starting_time = time.time()

    while True:
        print(f"{light_purple}{hearts}Level {level} {hearts}")
        max_number = level * 100
        computer_move = random.randint(1, max_number)
        attempts = 0

        while True:
            player_move = input(f"The number is between 1 and {max_number}. Make a guess: ")
            if not player_move.isdigit():
                print("Invalid input. Try again...")
                continue
            player_move = int(player_move)
            attempts += 1

            if player_move == computer_move:
                print(f"{light_purple}Congratulations! You guessed it in {attempts} attempts.")
                score += max_number - attempts
                print(f"{light_purple}Your score is now {score}.")
                break
            elif player_move > computer_move:
                print(Fore.LIGHTBLUE_EX + "Too high!")
            else:
                print(Fore.LIGHTRED_EX + "Too low!")

        elapsed_time = time.time() - starting_time
        if elapsed_time >= time_limit:
            print(f"{purple}Time is up! You reached level {level} with a score of {score}.\n{hearts}보라해!{hearts}")
            break

        level += 1


guess_the_number()
