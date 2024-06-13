from decouple import config
from random import randint
money = int(config('MY_MONEY'))
attempts = []
for i in range(1, int(config('AMOUNT_OF_ATTEMPTS'))+1):
    attempts.append(i)
min_number = int(config('MIN_NUM'))
max_number = int(config('MAX_NUM'))


def start_game():
    while True:
        start = input("What would you like to start").lower()
        if start == "no":
            break
        global money, guessed_num, attempts
        bet = int(input(f'welcome to the game, enter your bet, your money ={money}:__'))
        if bet > money:
            print("you can't bet more than you have")
            break
        num = randint(min_number, max_number + 1)
        for attempt in attempts:
            print(f'{attempt}')
            guessed_num = int(input('enter your guessed number between 1 - 30:__'))
            if guessed_num == num:
                print(f'you win')
                money += bet * 2
                break
            else:
                continue
        if guessed_num != num:
            money -= bet
            print(f'you lost yor money {money}')
