#!/usr/bin/python3

# Created by Jordan Leich on 6/6/2020

# Imports
import random
import time
from other import colors
import webbrowser
import json


def highlight(color, string):
    print(color + string + colors.reset + '\n')


def red(string):
    highlight(colors.red, string)


def green(string):
    highlight(colors.green, string)


def yellow(string):
    highlight(colors.yellow, string)


def blue(string):
    highlight(colors.blue, string)


try:  # This try and except block runs first in the code to be able to load a users saved stats, if no stats are
    # found, the default stats are automatically set to the end-users stats
    with open('data.json', 'r') as user_data_file:
        user_data = json.load(user_data_file)
    user_balance = user_data['ubalance']
    user_score = user_data['uscore']
    dealer_balance = user_data['deal_balance']
    green('Save file found and loaded!')
except FileNotFoundError:
    user_balance = 1000
    user_score = 0
    dealer_balance = 5000
    yellow('Save file not found, A new save file has been created!')

# Global Variables
user_bet = 0
user_dealer_money_choice = 0
user_money_choice = 0
player_cards = []
dealer_cards = []


def another_game():
    """
Used when 1 single round of blackjack has ended. Allows the user to play another game of blackjack or quit playing
    """
    global user_score, user_balance, dealer_balance, user_dealer_money_choice, user_money_choice, user_data_file
    print(colors.green + "Your win count is", user_score, "and your total balance is $" + str(user_balance), "\n",
          colors.reset)
    time.sleep(1)
    print(colors.red + "The dealers total balance is $" + str(dealer_balance), "\n", colors.reset)
    time.sleep(2)
    with open('data.json', 'w') as user_data_file:
        user_data_file.write(json.dumps({'ubalance': user_balance, 'uscore': user_score,
                                         'deal_balance': dealer_balance}))
    if user_balance <= 0:
        red("You don't have any more money to bet... Game Over!")
        time.sleep(2)
        user_game_over_choice = getting_input('Would you like to play all over again (yes / no): ', 0.500)

        if user_game_over_choice.lower() in ['y', 'yes']:
            new_game_starting()
        elif user_game_over_choice.lower() in ['n', 'no']:
            exiting_game()
        else:
            red('User game over choice selection error found... Restarting game...\n')
            time.sleep(2)
            main()

    elif user_balance >= 1:

        if dealer_balance <= 0:
            green("Congratulations! You have beat the BlackJack 21 game by defeating the dealers balance!")
            time.sleep(2)
        elif dealer_balance <= 2500:
            green("The dealers balance is looking small enough for you to win! You're doing well...")
            time.sleep(2)
        restart_action = getting_input(
            "Do you want to play again or cash out your earning or play a brand new game (play "
            "again / cash out / new game): ", 1)

        if restart_action.lower() in ["play again", "y", 'p', 'yes', 'play']:
            restart()
        elif restart_action.lower() in ["cash out", "n", "no", "c", "cash"]:
            print(colors.green + "You won a total of", user_score, 'games and you walked away with a total of $' +
                  str(user_balance) + str(" dollars. Thanks for playing!\n"), colors.reset)
            time.sleep(1)
            quit()
        elif restart_action.lower() in ["new", "new game"]:
            new_game_starting()
        else:
            red("Invalid input... Restarting choice...")
            time.sleep(1)
            another_game()
    else:
        red("User Balance Error found...\n")
        time.sleep(1)
        restart()


def new_game_starting():
    global user_balance, dealer_balance, user_score
    print('A brand new game will begin...\n')
    time.sleep(1)
    user_balance = 1000
    dealer_balance = 5000
    user_score = 0
    main()


def exiting_game():
    global user_balance, dealer_balance, user_score, user_data_file
    green('Thanks for playing! Exiting game now...')
    time.sleep(1)
    user_balance = 1000
    user_score = 0
    dealer_balance = 5000
    with open('data.json', 'w') as user_data_file:
        user_data_file.write(json.dumps({'ubalance': user_balance, 'uscore': user_score,
                                         'deal_balance': dealer_balance}))
    quit()


def new_game_starting_custom_game():
    global user_balance, dealer_balance, user_score, user_data_file
    print('A brand new game will begin...\n')
    time.sleep(1)
    user_balance = 1000
    user_score = 0
    dealer_balance = 5000
    with open('data.json', 'w') as user_data_file:
        user_data_file.write(json.dumps({'ubalance': user_balance, 'uscore': user_score,
                                         'deal_balance': dealer_balance}))
    custom_game_main()


def getting_input(arg0, arg1):
    result = input(arg0)
    print()
    time.sleep(arg1)

    return result


def restart():
    """
This restarts the program no matter what if executed
    """
    global user_score
    print("Restarting Blackjack Game...\n")
    time.sleep(1)
    game()


def game():  # sourcery no-metrics
    """
This is the main code used for the game entirely
    """
    global user_score, user_balance, user_bet, dealer_balance, player_cards, dealer_cards, user_money_choice
    player_cards = []
    dealer_cards = []

    print(colors.green + "Your balance is $" + str(user_balance), "\n", colors.reset)
    time.sleep(1)
    print(colors.red + "The dealers balance is $" + str(dealer_balance), "\n", colors.reset)
    time.sleep(1)

    user_all_in = str(input("Would you like to go all in (yes / no): "))
    print()
    time.sleep(.500)

    if user_all_in.lower() in ["y", "yes"]:
        user_bet = user_balance
        time.sleep(.500)
    elif user_all_in.lower() in ["n", "no"]:
        while True:
            try:
                user_bet = int(input("How much would you like to bet in dollar amount? "))
                print()
                time.sleep(.500)
            except ValueError:
                print()
                red('Please enter a valid dollar amount!')
                continue
            else:
                break

        if user_bet > user_balance:
            user_bet_error_handling("Your total balance cannot make this bet! Your bet is too high for your balance!")

        elif user_bet <= 0:
            user_bet_error_handling("You cannot make a negative bet! Please place a higher bet than 0 dollars!")

    else:
        red('User input for all in feature found an error!\n')
        time.sleep(1)
        restart()

    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print(colors.red + "The Dealer has ? &", dealer_cards[1], colors.reset, "\n")
            time.sleep(1)
    # Player Cards
    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(player_cards) == 2:
            print(colors.green + "You have a total of", str(sum(player_cards)), "from these cards", player_cards,
                  colors.reset, "\n")
            time.sleep(1)
    # Total of Dealer cards
    if sum(dealer_cards) >= 21:
        game_scoring()
    # Total of Player cards
    elif len(player_cards) == 5 and sum(player_cards) < 21:
        game_scoring()

    while sum(player_cards) < 21 and len(player_cards) < 5:
        choice = str(
            input("Do you want to hit, stay, double down, call for help, or quit the game (hit | stay | "
                  "double | help | quit): "))
        print()
        time.sleep(1)

        if len(player_cards) == 5:
            game_scoring()
        elif choice.lower() in ["hit", "h"]:
            user_draws_card()
        elif choice.lower() in ['s', 'stay']:
            dealers_turn()
        elif choice.lower() in ["d", "double", 'double down']:
            if sum(player_cards) <= 11:
                print('You will now double down on your bets and pull only 1 more card and then you will stand for '
                      'this round!\n')
                user_bet *= 2
                time.sleep(1)
                user_draws_card()
                dealers_turn()
            else:
                red('You cannot double down here since the sum of your cards is over 11!')
                time.sleep(1)
        elif choice.lower() in ["help", "help", 'call help']:
            if sum(player_cards) <= 14:
                blue("Since your total is under or equal to a total of 14, we recommend that you hit!")
                time.sleep(2)
            elif sum(player_cards) >= 15:
                blue("Your odds are looking high enough to win, if your card total is closer to 15, we recommend only "
                     "making 1 hit move and then staying!")
                time.sleep(3)
                blue("If your card total is closer to 21, don't risk it! make a stay move!")
                time.sleep(3)
        elif choice.lower() in ["q", "quit", "end"]:
            green("Ending game... Thanks for playing!\n")
            time.sleep(1)
            quit()

        else:
            game_scoring()

    # Endgame results
    game_scoring()


def user_draws_card():
    """
Used for whenever the player is required to draw a card
    """
    global player_cards
    player_cards.append(random.randint(1, 11))
    print(colors.green + "You now have a total of " + str(sum(player_cards)) + " from these cards",
          player_cards, colors.reset, "\n")
    time.sleep(1)


def user_bet_error_handling(arg0):
    """
Used for whenever the player makes a bet that causes an error or is logically incorrect
    """
    red(arg0)
    time.sleep(2)
    game()


def main():
    """
Used as the first piece of the program introduced to the end-user. This section allows the user to skip around in the
game by using the game mode selection choices
    """
    green('Hello there! Welcome to Blackjack 21, made by Jordan Leich!')
    time.sleep(1)
    yellow('''The goal of this game is to make the dealer go broke and score the most amount of money! 
Achieve this by placing your bets and dealing your cards wisely, but carefully...''')
    time.sleep(2)

    user_knowledge = input('Do you know how to play Blackjack 21 or would you like to watch a tutorial via youtube or '
                           'skip all setup options to play Blackjack 21 quickly (start / tutorial / express): ')
    print()
    time.sleep(1)

    if user_knowledge.lower() in ['start', 'yes', 's']:
        custom_game_main()
    elif user_knowledge.lower() in ['no', 'n', 't', 'tutorial']:
        green('A youtube video should now be playing... This game will auto resume once the video has been fully '
              'played...')
        url = "https://www.youtube.com/watch?v=eyoh-Ku9TCI"
        webbrowser.open(url, new=1)
        time.sleep(140)
        game()
    elif user_knowledge.lower() in ['e', 'express']:
        print('Express option has been selected, proceeding to Blackjack 21...\n')
        time.sleep(.500)
        game()
    else:
        red('User knowledge input error found...')
        time.sleep(1)
        main()


def game_scoring():
    """
Handles of the end game scoring based upon card results between the dealer and end-user
    """
    global player_cards, user_score, user_balance, dealer_balance, dealer_cards
    print(colors.red + "The Dealer has a grand total of", str(sum(dealer_cards)), "from these cards",
          dealer_cards, colors.reset, "\n")
    time.sleep(1)
    print(colors.green + "You have a grand total of " + str(sum(player_cards)) + " with", player_cards,
          colors.reset, "\n")
    time.sleep(1)

    if len(player_cards) == 5 and sum(player_cards) < 21:
        time.sleep(1)
        green("You have automatically won since you have pulled a total of 5 cards without busting!")
        user_win_stats()
    elif len(dealer_cards) == 5 and sum(dealer_cards) < 21:
        red("You have automatically lost since the dealer has pulled a total of 5 cards without busting!")
        user_loses_stats()
    elif sum(player_cards) > 21:
        print(colors.red + "BUSTED! The Dealer Wins! You lost $" + str(user_bet) + "!\n", colors.reset)
        user_loses_stats()
    elif sum(dealer_cards) > 21:
        print(colors.green + "The Dealer BUSTED! You win! You won $" + str(user_bet) + "!\n", colors.reset)
        user_win_stats()
    elif sum(player_cards) == 21:
        print(colors.green + "BLACKJACK! You hit 21! You won $" + str(user_bet) + "!\n", colors.reset)
        user_win_stats()
    elif sum(dealer_cards) == 21:
        print(colors.red + "BLACKJACK! The Dealer hit 21! You lost $" + str(user_bet) + "!\n", colors.reset)
        user_loses_stats()
    elif sum(player_cards) > sum(dealer_cards):
        print(colors.green + "You Win! Your cards were greater than the dealers deck, You won $" + str(user_bet) +
              "!\n", colors.reset)
        user_win_stats()
    elif sum(dealer_cards) > sum(player_cards):
        print(colors.red + "The dealer wins! Your cards were less than the dealers deck, You lost $" + str(user_bet) +
              "!\n", colors.reset)
        user_loses_stats()
    elif sum(player_cards) == sum(dealer_cards):
        yellow("PUSH! This is a tie! All bet money is refunded!")
        time.sleep(1)
        another_game()
    else:  # This else statement is most likely unreachable but still used as a safety net in case anything with
        # scoring goes wrong.
        red('Scoring error found...')
        time.sleep(1)
        restart()


def user_loses_stats():
    global user_score, user_balance, dealer_balance
    time.sleep(1)
    user_score -= 1
    user_balance -= user_bet
    dealer_balance += user_bet
    another_game()


def user_win_stats():
    global user_score, user_balance, dealer_balance
    time.sleep(1)
    user_score += 1
    user_balance += user_bet
    dealer_balance -= user_bet
    another_game()


def custom_game():
    """
Allows the end-user to be able to play the game but with custom money, win counts, and more
    """
    global user_balance, dealer_balance, user_score, user_dealer_money_choice, user_money_choice
    user_game_picker = input('Would you like to play normal Blackjack 21 or a Custom Game with custom user game '
                             'settings (blackjack / custom): ')
    print()
    time.sleep(1)

    if user_game_picker.lower() in ['b', 'blackjack', 'blackjack 21']:
        game_selection_choice('Normal Blackjack 21 has been selected...\n', 0.500)

    elif user_game_picker.lower() in ['c', 'custom', 'custom game']:
        custom_game_main()
    else:
        invalid_starting_balance_error('User game selection choice error found... Restarting choice selection...')


def custom_game_main():
    global user_money_choice, user_balance, dealer_balance, user_score, user_dealer_money_choice
    print('Custom Blackjack 21 has been selected...\n')
    time.sleep(.500)
    user_money_choice = custom_game_stat_changer('How much would you like your starting balance to be? ')

    if user_money_choice <= 0:
        invalid_starting_balance_error('Invalid starting balance... Please choose a balance greater than 0 dollars!')

    user_balance = user_money_choice
    user_dealer_money_choice = custom_game_stat_changer('How much would you to set the dealers starting balance to? ')

    dealer_balance = user_dealer_money_choice
    user_score_choice = custom_game_stat_changer('How much would you like to set your scoring counter to? ')

    user_score = user_score_choice
    game_selection_choice('Now proceeding to Blackjack 21 game with your custom settings...\n', 1)


def invalid_starting_balance_error(arg0):
    red(arg0)
    time.sleep(2)
    custom_game_main()


def game_selection_choice(arg0, arg1):
    print(arg0)
    time.sleep(arg1)
    game()


def custom_game_stat_changer(arg0):
    result = int(input(arg0))
    print()
    time.sleep(.500)
    return result


def dealers_turn():
    """
Handles all of the card pulling actions for the dealer
    """
    global user_score, user_balance, user_bet, dealer_balance, player_cards, dealer_cards, user_money_choice
    red('The Dealer says No More Bets...')
    time.sleep(1)

    if len(dealer_cards) == 5 and sum(dealer_cards) <= 21:
        game_scoring()

    elif sum(dealer_cards) > 15:
        game_scoring()

    elif sum(dealer_cards) >= 21:
        game_scoring()

    while sum(dealer_cards) <= 15:
        _extracted_from_dealers_turn_18()


def _extracted_from_dealers_turn_18():
    dealer_cards.append(random.randint(1, 11))
    red("The Dealer has pulled a card...")
    time.sleep(1)
    print(colors.red + "The Dealer now has a total of " + str(sum(dealer_cards)) + " from these cards",
          dealer_cards, colors.reset, "\n")
    time.sleep(1)

    if len(dealer_cards) == 5 and sum(dealer_cards) <= 21:
        game_scoring()

    elif sum(dealer_cards) > 15:
        game_scoring()

    elif sum(dealer_cards) >= 21:
        game_scoring()


if __name__ == '__main__':
    main()
