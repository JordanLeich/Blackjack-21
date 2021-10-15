#!/usr/bin/python3

# Created by Jordan Leich on 6/6/2020
# Edited by Adam Smith

# Imports
import random
import time
import webbrowser
import json
import sys
import os
import decks
import player

# from files
from other import colors
from os import path

# Initialize all players, 11 in total, 5 regular players,
# 5 bot players, 1 dealer. They will be using the Player
# class. Depending on the game being played, will determine
# which player/bot will be active along with the dealer.
# The default names will be player1-5 and dealer, bots are 6-10.
# You can change any name you want to, or leave these hard
# coded and add .name to the class so each one can have a
# personalized name. The table can hold a max of 6 players
# 5 players and the dealer.
# Players will start with a bank roll of 1k and the dealer
# will start with 2m. when the game starts and the player0
# wants to load saved data then that will take over.

Player1 = Player()
Player2 = Player()
Player3 = Player()
Player4 = Player()
Player5 = Player()
Dealer = Player(,,True,,,,True,)
Player6 = Player(,,,,,,True,,)
Player7 = Player(,,,,,,True,,)
PLayer8 = Player(,,,,,,True,,)
Player9 = Player(,,,,,,True,,)
Player10 = Player(,,,,,,True,,)





def game_data(load_stats = False, reset_stats = False):
    """ Changed from trying to load the game when the game first runs
        to where it gets checked during the beginning of the game. also
        changed from a try/except to if statement. my opinion of better
        file handling. """

    if path.exists("data.json"):
        file_exist = True
    else:
        file_exist = False

    if load_stats and file_exist:
    # try:  # This try and except block runs first in the code to be able to load a users saved stats, if no stats are
        # found, the default stats are automatically set to the end-users stats
        with open('data.json', 'r') as user_data_file:
            user_data = json.load(user_data_file)
        user_balance = user_data['ubalance']
        user_score = user_data['uscore']
        dealer_balance = user_data['deal_balance']
        player1_balance = user_data['player1_balance']
        player2_balance = user_data['player2_balance']
        player3_balance = user_data['player3_balance']
        print(colors.green + 'Save file loaded!\n' colors.reset)

    #except FileNotFoundError:
    Elif load_stats and not file_exist:
        user_balance = 1000
        player1_balance = 1000
        player2_balance = 1000
        player3_balance = 1000
        user_score = 0
        dealer_balance = 5000
        print(colors.yellow + 'Save file not found, A new save file will be created shortly!', colors.reset)

        print(colors.yellow + 'Save file not found, A new save file will be created shortly!\n' + colors.reset)

print(colors.green + 'All players and the dealers money/stats will be reset to their original defaults...\n' + colors.reset)




# Global Variables
# Changed to oop with the player class. hope it works better and
# easier to maintain

def contributions():
    """
Allows the user to be able to view all of the contributors of this project via GitHub
    """
    #print(colors.green + "Opening all contributors of this project...\n", colors.reset)
    #webbrowser.open_new(
    browser_opener("Opening all contributors of this project...\n",
        "https://github.com/JordanLeich/Blackjack-21/graphs/contributors")
    time.sleep(2)


def releases():
    """
Allows the user to be able to view either the latest or oldest release of this project via GitHub
    """
    while True:
        choice = int(input('''(1) Latest Stable Release
(2) Oldest Release
(3) Return to previous window

Which release would you like to view: '''))
        print()

        if choice == 1:
            browser_opener("Opening the latest stable release...\n",
                           "https://github.com/JordanLeich/Blackjack-21/releases")

        elif choice == 2:
            browser_opener("Opening the oldest release...\n",
                           "https://github.com/JordanLeich/Blackjack-21/releases/tag/v5.0")

        elif choice == 3:
            return
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)


def browser_opener(arg0, arg1):
    """
Used to open a release version in the users default web browser
    """
    print(colors.green + arg0, colors.reset)
    time.sleep(1)
    webbrowser.open_new(arg1)
    time.sleep(1)


def donate():
    """
Allows the user to be able to donate via PayPal or Cash App methods
    """
    while True:
        print(colors.yellow + 'Since this project is completely free to use and open source, users have the option to '
                              'send a donation of their choice but this action is not required.\n', colors.reset)
        time.sleep(2)
        donate_choice = int(input('''(1) PayPal
(2) Cash App
(3) Return to previous window
(4) Exit

Which donation option would you like to use: '''))
        print()

        if donate_choice == 1:
            browser_opener("Opening PayPal Donation page...\n",
                            "https://www.paypal.com/donate/?business=8FGHU8Z4EJPME&no_recurring=0&currency_code=USD")

        elif donate_choice == 2:
            browser_opener("Opening Cash App Donation page...\n", "https://cash.app/$JordanLeich")

        elif donate_choice == 3:
            return
        elif donate_choice == 4:
            break
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)


def extra():
    """
Main hub UI for the user to view additional information or extra parts of this project such as donations and releases
    """
    while True:
        choice = int(input('''(1) Project Releases
(2) Credits
(3) Donate
(4) Return to main window

Which option would you like: '''))
        print()

        if choice == 1:
            releases()
        elif choice == 2:
            contributions()
        elif choice == 3:
            donate()
        elif choice == 4:
            main()
        else:
            print(colors.red + 'User input error found...\n', colors.reset)
            time.sleep(2)


def reset_stats():
    """
Used for the end-user to automatically reset their saved stats back to default while in-game
    """
    # needs some rework
    time.sleep(1)
    user_balance = 1000
    player1_balance = 1000
    player2_balance = 1000
    player3_balance = 1000
    user_score = 0
    dealer_balance = 5000

    #save_game_data()

def another_game():  # sourcery no-metrics skip: hoist-statement-from-if
    """
Used when 1 single round of blackjack has ended. Allows the user to play another game of blackjack or quit playing
    """
    global user_score, user_balance, dealer_balance, user_dealer_money_choice, custom_game_starting_balance, \
        user_data_file, player1_balance, player2_balance, player3_balance
    print(colors.green + "Your win count is", user_score, "and your total balance is $" + str(user_balance), "\n",
          colors.reset)
    time.sleep(1)
    print(colors.red + "The dealers total balance is $" + str(dealer_balance), "\n", colors.reset)
    time.sleep(2)
    with open('data.json', 'w') as user_data_file:
        json.dump({'ubalance': user_balance, 'uscore': user_score,
                   'deal_balance': dealer_balance, 'player1_balance': player1_balance,
                   'player2_balance': player2_balance, 'player3_balance': player3_balance}, user_data_file)

    if user_balance <= 0 and bot_game_selected:
        print(colors.red + 'You are currently out of money and cannot make a bet!', colors.reset)
        time.sleep(1)
        choice = str(input('Since you are playing with others, would you like to request a donation from a player '
                           '(yes / no): '))
        print()
        time.sleep(1)

        if choice.lower() in ['yes', 'y', 'sure']:
            if not player1_bankrupt and player1_presence and (player1_balance / (user_balance + 1)) > user_balance:
                if user_balance == 0:
                    bot_donation_amount = (user_balance + 100) * 1.5
                    user_balance += bot_donation_amount
                    player1_balance -= bot_donation_amount
                    print(colors.green + 'Player1 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
                else:
                    bot_donation_amount = (user_balance + 100) * -1.5
                    user_balance += bot_donation_amount
                    player1_balance -= bot_donation_amount
                    print(colors.green + 'Player1 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
            elif not player2_bankrupt and player2_presence and (player2_balance / (user_balance + 1)) > user_balance:
                if user_balance == 0:
                    bot_donation_amount = (user_balance + 100) * 1.5
                    user_balance += bot_donation_amount
                    player2_balance -= bot_donation_amount
                    print(colors.green + 'Player2 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
                else:
                    bot_donation_amount = (user_balance + 100) * -1.5
                    user_balance += bot_donation_amount
                    player2_balance -= bot_donation_amount
                    print(colors.green + 'Player2 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
            elif not player3_bankrupt and player3_presence and (player3_balance / (user_balance + 1)) > user_balance:
                if user_balance == 0:
                    bot_donation_amount = (user_balance + 100) * 1.5
                    user_balance += bot_donation_amount
                    player3_balance -= bot_donation_amount
                    print(colors.green + 'Player3 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
                else:
                    bot_donation_amount = (user_balance + 100) * -1.5
                    user_balance += bot_donation_amount
                    player3_balance -= bot_donation_amount
                    print(colors.green + 'Player3 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
            else:
                red('No other players were able to donate anything to you!')
                time.sleep(1)
                choice = str(
                    input('Would you like to restart from scratch (yes / no): '))
                print()
                time.sleep(1)
                if choice.lower() in ['yes', 'y', 'sure']:
                    new_game_starting()
                else:
                    green('Thanks for playing!')
                    time.sleep(1)
                    sys.exit()

        elif choice.lower() in ['no', 'n', 'nah']:
            choice = str(input('Since you refuse to take a donation, this is game over for you... Would you like to '
                               'restart from scratch (yes / no): '))
            print()
            time.sleep(1)
            if choice.lower() in ['yes', 'y', 'sure']:
                new_game_starting()
            else:
                print(colors.green + 'Thanks for playing!', colors.reset)
                time.sleep(1)
                sys.exit()
        else:
            print(colors.red + 'Donation request user input error found...', colors.reset)
            time.sleep(1)
            restart_game_error()

    elif user_balance <= 0:
        print(colors.red + "You don't have any more money to bet... Game Over!", colors.reset)
        time.sleep(2)
        user_game_over_choice = getting_input('Would you like to play all over again (yes / no): ', 0.500)

        if user_game_over_choice.lower() in ['y', 'yes']:
            new_game_starting()
        elif user_game_over_choice.lower() in ['n', 'no']:
            exiting_game()
        else:
            print(colors.red + 'User game over choice selection error found...\n', colors.reset)
            time.sleep(2)
            restart_game_error()

    elif user_balance >= 1:
        if dealer_balance <= 0:
            print(
                colors.green + "Congratulations! You have beat the BlackJack 21 game by defeating the dealers balance!"
                , colors.reset)
            time.sleep(2)
        elif dealer_balance <= 2500:
            print(colors.green + "The dealers balance is looking small enough for you to win! You're doing well...",
                  colors.reset)
            time.sleep(2)
        restart_action = getting_input(
            "Do you want to play again or cash out your earning or play a brand new game (play "
            "again / cash out / new game): ", 1)
        if restart_action.lower() in ["play again", "y", 'p', 'yes', 'play']:
            if bot_game_selected:
                bot_game()
            else:
                game()
        elif restart_action.lower() in ["cash out", "n", "no", "c", "cash", "exit", "leave", "q", "quit"]:
            print(colors.green + "You won a total of", user_score, 'games and you walked away with a total of $' +
                  str(user_balance) + str(" dollars. Thanks for playing!\n"), colors.reset)
            time.sleep(1)
            sys.exit()
        elif restart_action.lower() in ["new", "new game", "restart"]:
            new_game_starting()
        else:
            print(colors.red + "Invalid input... Restarting choice...", colors.reset)
            time.sleep(1)
            another_game()
    else:
        print(colors.red + "User Balance Error found...\n", colors.reset)
        time.sleep(1)
        restart_game_error()


def new_game_starting():
    """
Used to start a brand new game from scratch with all default stats being loaded
    """
    global user_balance, dealer_balance, user_score, player1_balance, player2_balance, player3_balance, user_data_file
    print(
        'A brand new game will begin... All saved data will be reset to default cash balances and values!\n')
    time.sleep(2)
    user_balance = 1000
    player1_balance = 1000
    player2_balance = 1000
    player3_balance = 1000
    dealer_balance = 5000
    user_score = 0
    with open('data.json', 'w') as user_data_file:
        json.dump({'ubalance': user_balance, 'uscore': user_score,
                   'deal_balance': dealer_balance, 'player1_balance': player1_balance,
                   'player2_balance': player2_balance, 'player3_balance': player3_balance}, user_data_file)
    main()


def exiting_game():
    """
Exits the game while setting the default stats
    """
    global user_balance, dealer_balance, user_score, user_data_file, player1_balance, player2_balance, player3_balance
    print(colors.green + 'Thanks for playing! Exiting game now...', colors.reset)
    time.sleep(1)
    user_balance = 1000
    player1_balance = 1000
    player2_balance = 1000
    player3_balance = 1000
    user_score = 0
    dealer_balance = 5000
    with open('data.json', 'w') as user_data_file:
        json.dump({'ubalance': user_balance, 'uscore': user_score,
                   'deal_balance': dealer_balance, 'player1_balance': player1_balance,
                   'player2_balance': player2_balance, 'player3_balance': player3_balance}, user_data_file)
    sys.exit()


def new_game_starting_custom_game():
    """
Used to start a new game for a custom game that was previously selected while also loading the default stats
    """
    global user_balance, dealer_balance, user_score, user_data_file, player1_balance, player2_balance, player3_balance
    print(
        'A brand new game will begin... All saved data will be reset to default cash balances and values!\n')
    time.sleep(2)
    user_balance = 1000
    player1_balance = 1000
    player2_balance = 1000
    player3_balance = 1000
    user_score = 0
    dealer_balance = 5000
    with open('data.json', 'w') as user_data_file:
        json.dump({'ubalance': user_balance, 'uscore': user_score,
                   'deal_balance': dealer_balance, 'player1_balance': player1_balance,
                   'player2_balance': player2_balance, 'player3_balance': player3_balance}, user_data_file)
    custom_game_main()


def getting_input(arg0, arg1):
    """
Used for simply receiving input as an argument
    """
    result = input(arg0)
    print()
    time.sleep(arg1)

    return result


def restart_game_error():
    """
Used for error handling to prevent the game from crashing.
    """
    print("Restarting Blackjack Game from scratch...\n")
    main()


def restart_normal_game():
    """
This restarts the program to then begin another game.
    """
    print("Restarting a normal Blackjack Game...\n")
    game()


def restart_bot_game():
    """
This restarts the program to then begin another game.
    """
    print("Restarting a bot Blackjack Game...\n")
    bot_game()


def game():  # sourcery no-metrics skip: assign-if-exp, boolean-if-exp-identity, merge-comparisons
    """
This is the main code used for the game entirely
    """
    global user_score, user_balance, user_bet, dealer_balance, user_cards, dealer_cards, custom_game_starting_balance, \
        normal_game_selected, custom_game_selected, player1_presence, player2_presence, player3_presence, \
        bot_game_selected
    bot_game_selected = False
    player1_presence = False
    player2_presence = False
    player3_presence = False
    if custom_game_selected:
        normal_game_selected = False
    else:
        normal_game_selected = True

    user_cards = []
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
                print(colors.red + 'Please enter a valid dollar amount!', colors.reset)
                continue
            else:
                break

        if user_bet > user_balance:
            user_bet_error_handling("Your total balance cannot make this bet! Your bet is too high for your balance!")

        elif user_bet <= 0:
            user_bet_error_handling("You cannot make a negative bet! Please place a higher bet than 0 dollars!")

    else:
        print(colors.red + 'User input for all in feature found an error!\n', colors.reset)
        time.sleep(1)
        restart_game_error()

    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print(colors.red + "The Dealer has ? &", dealer_cards[1], colors.reset, "\n")
            time.sleep(1)
    # Player Cards
    while len(user_cards) != 2:
        user_cards.append(random.randint(1, 11))
        if len(user_cards) == 2:
            print(colors.green + "You have a total of", str(sum(user_cards)), "from these cards", user_cards,
                  colors.reset, "\n")
            time.sleep(1)
    # Total of Dealer cards
    if sum(dealer_cards) >= 21:
        game_scoring()
    # Total of Player cards
    elif len(user_cards) == 5 and sum(user_cards) < 21 and sum(dealer_cards) < 15:
        dealer_draws_card()
    while sum(user_cards) > 21 and sum(dealer_cards) < 15:
        dealer_draws_card()

    while sum(user_cards) < 21 and len(user_cards) < 5:
        choice = str(
            input("Do you want to hit, stay, double down, call for help, or quit the game (hit | stay | "
                  "double down | help | quit): "))
        print()
        time.sleep(1)

        if len(user_cards) == 5:
            game_scoring()
        elif choice.lower() in ["hit", "h"]:
            user_draws_card()
        elif choice.lower() in ['s', 'stay']:
            dealers_turn()
        elif choice.lower() in ["d", "double", 'double down']:
            if sum(user_cards) <= 11:
                print('You will now double down on your bets and pull only 1 more card and then you will stand for '
                      'this round!\n')
                user_bet *= 2
                time.sleep(1)
                user_draws_card()
                dealers_turn()
            else:
                print(colors.red + 'You cannot double down here since the sum of your cards is over 11!', colors.reset)
                time.sleep(1)
        elif choice.lower() in ["help", "help", 'call help']:
            if sum(user_cards) == [10, 11]:
                print(colors.blue +
                      "Since your total is equal to either 10 or 11, we recommend that this is the best time to double "
                      "down if you have enough money!", colors.reset)
                time.sleep(3)
            elif sum(user_cards) <= 14:
                print(colors.blue + "Since your total is under or equal to 14, we recommend that you hit!", colors.reset)
                time.sleep(2)
            elif sum(user_cards) >= 15:
                print(colors.blue +
                      "Your odds are looking high enough to win, if your card total is closer to 15, we recommend only "
                      "making 1 hit move and then staying!", colors.reset)
                time.sleep(3)
                print(colors.blue + "If your card total is closer to 21, don't risk it! make a stay move!", colors.reset)
                time.sleep(3)
        elif choice.lower() in ["q", "quit", "end"]:
            print(colors.green + "Ending game... Thanks for playing!\n", colors.reset)
            time.sleep(1)
            sys.exit()

        else:
            game_scoring()

    # Endgame results
    game_scoring()


def user_draws_card():
    """
Used for whenever the player is required to draw a card
    """
    global user_cards
    user_cards.append(random.randint(1, 11))
    print(colors.green + "You now have a total of " + str(sum(user_cards)) + " from these cards",
          user_cards, colors.reset, "\n")
    time.sleep(1)
    while sum(user_cards) > 21 and sum(dealer_cards) < 15:
        dealer_draws_card()


def user_bet_error_handling(arg0):
    """
Used for whenever the player makes a bet that causes an error or is logically incorrect
    """
    print(colors.red + arg0, colors.reset)
    time.sleep(2)
    restart_game_error()


def view_stats():
    print(colors.green + 'Your current in game stats will now be displayed below!', colors.reset)
    time.sleep(1)
    print('Your balance is $' + str(user_balance))
    print('Your wincount is ' + str(user_score))
    print('The dealers balance is $' + str(dealer_balance))
    print('Player1 balance is $' + str(player1_balance))
    print('Player2 balance is $' + str(player2_balance))
    print('Player3 balance is $' + str(player3_balance), '\n')
    time.sleep(6)
    main()


def main():
    """
Used as the first piece of the program introduced to the end-user. This section allows the user to skip around in the
game by using the game mode selection choices
    """
    while True:
        user_knowledge = input('''Start 
                                Tutorial 
                                Express
                                View Stats
                                Reset Stats
                                Extras
                                Quit: ''')
        print()
        time.sleep(.5)

        if user_knowledge.lower() in ['start', 'yes', 's']:
            game_options()
        elif user_knowledge.lower() in ['no', 'n', 't', 'tutorial']:
            browser_opener('A youtube video should now be playing... This game will auto resume once the video has been fully '
                  'played...', "https://www.youtube.com/watch?v=eyoh-Ku9TCI")
            time.sleep(140)
            game()
        elif user_knowledge.lower() in ['e', 'express']:
            game()
        elif user_knowledge.lower() in ['stats', 'view stats', 'v', 'view']:
            view_stats()
        elif user_knowledge.lower() in ['reset', 'reset stats']:
            reset_stats()
        elif user_knowledge.lower() in ['extra', 'extras']:
            extra()
        elif user_knowledge.lower() in ['quit', 'q', 'exit']:
            sys.exit()
        else:
            print(colors.red + 'User knowledge input error found... Please try again\n' + colors.reset)
            time.sleep(1)


def game_scoring():  # sourcery skip: remove-colors.redundant-if, remove-redundant-if
    """
Handles of the end game scoring based upon card results between the dealer and end-user
    """
    global user_cards, user_score, user_balance, dealer_balance, dealer_cards, insurance_bought
    print(colors.red + "The Dealer has a grand total of", str(sum(dealer_cards)), "from these cards",
          dealer_cards, colors.reset, "\n")
    time.sleep(1)
    print(colors.green + "You have a grand total of " + str(sum(user_cards)) + " with", user_cards,
          colors.reset, "\n")
    time.sleep(1)

    if len(dealer_cards) == 5 and sum(dealer_cards) <= sum(user_cards) <= 21:
        Push_tie_game_result()
    elif len(user_cards) == 5 and sum(user_cards) <= sum(dealer_cards) <= 21:
        Push_tie_game_result()
    elif sum(user_cards) == sum(dealer_cards):
        Push_tie_game_result()
    elif len(user_cards) == 5 and sum(user_cards) < 21:
        time.sleep(1)
        print(colors.green + "You have automatically won since you have pulled a total of 5 cards without busting!",
              colors.reset)
        user_win_stats()
    elif len(dealer_cards) == 5 and sum(dealer_cards) < 21:
        print(
            colors.red + "You have automatically lost since the dealer has pulled a total of 5 cards without busting!", colors.reset)
        user_loses_stats()
    elif sum(user_cards) > 21:
        print(colors.red + "BUSTED! The Dealer Wins! You lost $" + str(user_bet) + "!\n", colors.reset)
        user_loses_stats()
    elif sum(dealer_cards) > 21:
        print(colors.green + "The Dealer BUSTED! You win! You won $" + str(user_bet) + "!\n", colors.reset)
        user_win_stats()
    elif sum(user_cards) == 21:
        print(colors.green + "BLACKJACK! You hit 21! You won $" + str(user_bet) + "!\n", colors.reset)
        user_win_stats()
    elif insurance_bought and sum(dealer_cards) == 21:
        insurance_game_results("BLACKJACK! Since you purchased insurance, you do not lose any money!")
    elif not insurance_bought and sum(dealer_cards) == 21:
        user_balance -= user_bet + (user_bet / 2)
        insurance_game_results(
            "BLACKJACK! Since you did not purchased insurance, you will lose your original bet plus half the "
            "original amount bet!")
    elif sum(dealer_cards) == 21:
        print(colors.green + "BLACKJACK! The Dealer hit 21! You Lost $" + str(user_bet) + "!\n", colors.reset)
        user_loses_stats()
    elif sum(user_cards) > sum(dealer_cards):
        print(colors.green + "You Win! Your cards were greater than the dealers deck, You won $" + str(user_bet) +
              "!\n", colors.reset)
        user_win_stats()
    elif sum(dealer_cards) > sum(user_cards):
        print(colors.red + "The dealer wins! Your cards were less than the dealers deck, You lost $" + str(user_bet) +
              "!\n", colors.reset)
        user_loses_stats()
    else:  # This else statement is most likely unreachable but still used as a safety net in case anything with
        # scoring goes wrong.
        red('Scoring error found...')
        time.sleep(1)
        restart_game_error()


def insurance_game_results(arg0):
    """
Used for when the player either buys or doesnt buy insurance to get to the endgame results
    """
    print(colors.yellow + arg0, colors.reset)
    time.sleep(1)
    another_game()


def Push_tie_game_result():
    """
Used for when there is a tie game between a player and the dealer
    """
    print(colors.yellow + "PUSH! This is a tie! All bet money is refunded!", colors.reset)
    time.sleep(1)
    another_game()


def user_loses_stats(current_player, bet):
    """
Used when the user loses the round
    """
    current_player.p_score[1] -= 1
    current_player.bank_roll -= bet
    Dealer.bank_roll += bet
    another_game()


def user_win_stats(current_player, bet):
    """
Used when the user wins the round
    """
    current_player.p_score[0] += 1
    current_player.bank_roll += bet
    Dealer.bank_roll -= bet
    another_game()


def bot_game_scoring():  # sourcery no-metrics
    """
Used for the scoring results when a bot game is selected
    """
    global user_score, user_balance, user_bet, dealer_balance, user_cards, dealer_cards, custom_game_starting_balance, \
        player1_cards, player2_cards, player3_cards, player1_balance, player2_balance, player3_balance, player1_bet, \
        player3_bet, player2_bet

    print(colors.red + "The Dealer has a grand total of", str(sum(dealer_cards)), "from these cards",
          dealer_cards, colors.reset, "\n")
    time.sleep(1)

    if player1_presence:
        if len(dealer_cards) == 5 and sum(player1_cards) >= sum(dealer_cards):
            print(colors.yellow + 'Player1 pushed this round! Player1s bet has been refunded!', colors.reset)
            time.sleep(1)
        elif len(player1_cards) == 5 and sum(dealer_cards) >= sum(player1_cards):
            print(colors.yellow + 'Player1 pushed this round! Player1s bet has been refunded!', colors.reset)
            time.sleep(1)
        elif sum(player1_cards) == sum(dealer_cards):
            print(colors.yellow + 'Player1 pushed this round! Player1s bet has been refunded!', colors.reset)
            time.sleep(1)
        elif len(player1_cards) == 5 and sum(player1_cards) < 21:
            player1_balance += player1_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player1 won this round! Player1 won $' + str(player1_bet), colors.reset, '\n')
            time.sleep(1)
        elif len(dealer_cards) == 5 and sum(dealer_cards) < 21:
            player1_balance -= player1_bet
            dealer_balance += player2_bet
            print(colors.red + 'Player1 lost this round! Player1 lost $' + str(player1_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player1_cards) > 21:
            player1_balance -= player1_bet
            dealer_balance += player2_bet
            print(colors.red + 'Player1 lost this round! Player1 lost $' + str(player1_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(dealer_cards) > 21:
            player1_balance += player1_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player1 won this round! Player1 won $' + str(player1_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player1_cards) == 21:
            player1_balance += player1_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player1 won this round! Player1 won $' + str(player1_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player1_cards) < sum(dealer_cards):
            player1_balance -= player1_bet
            dealer_balance += player2_bet
            print(colors.red + 'Player1 lost this round! Player1 lost $' + str(player1_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player1_cards) > sum(dealer_cards):
            player1_balance += player1_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player1 won this round! Player1 won $' + str(player1_bet), colors.reset, '\n')
            time.sleep(1)
        print(colors.blue + 'Player1 now has a balance of $' + str(player1_balance), '\n', colors.reset)
        time.sleep(1)

    if player2_presence:
        if len(dealer_cards) == 5 and sum(player2_cards) >= sum(dealer_cards):
            print(colors.yellow + 'Player2 pushed this round! Player2s bet has been refunded!', colors.reset)
            time.sleep(1)
        elif len(player2_cards) == 5 and sum(dealer_cards) >= sum(player2_cards):
            print(colors.yellow + 'Player2 pushed this round! Player2s bet has been refunded!', colors.reset)
            time.sleep(1)
        elif sum(player2_cards) == sum(dealer_cards):
            print(colors.yellow + 'Player2 pushed this round! Player2s bet has been refunded!', colors.reset)
            time.sleep(1)
        elif len(player2_cards) == 5 and sum(player2_cards) < 21:
            player2_balance += player2_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player2 won this round! Player2 won $' + str(player2_bet), colors.reset, '\n')
            time.sleep(1)
        elif len(dealer_cards) == 5 and sum(dealer_cards) < 21:
            player2_balance -= player2_bet
            dealer_balance += player2_bet
            print(colors.red + 'Player2 lost this round! Player2 lost $' + str(player2_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player2_cards) > 21:
            player2_balance -= player2_bet
            dealer_balance += player2_bet
            print(colors.red + 'Player2 lost this round! Player2 lost $' + str(player2_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(dealer_cards) > 21:
            player2_balance += player2_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player2 won this round! Player2 won $' + str(player2_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player2_cards) == 21:
            player2_balance += player2_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player2 won this round! Player2 won $' + str(player2_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player2_cards) < sum(dealer_cards):
            player2_balance -= player2_bet
            dealer_balance += player2_bet
            print(colors.red + 'Player2 lost this round! Player2 lost $' + str(player2_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player2_cards) > sum(dealer_cards):
            player2_balance += player2_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player2 won this round! Player2 won $' + str(player2_bet), colors.reset, '\n')
            time.sleep(1)
        print(colors.blue + 'Player2 now has a balance of $' + str(player2_balance), '\n', colors.reset)
        time.sleep(1)

    if player3_presence:
        if len(dealer_cards) == 5 and sum(player3_cards) >= sum(dealer_cards):
            print(colors.yellow + 'Player3 pushed this round! Player3s bet has been refunded!', colors.reset)
            time.sleep(1)
        elif len(player3_cards) == 5 and sum(dealer_cards) >= sum(player3_cards):
            print(colors.yellow + 'Player3 pushed this round! Player3s bet has been refunded!', colors.reset)
            time.sleep(1)
        elif sum(player3_cards) == sum(dealer_cards):
            print(colors.yellow + 'Player3 pushed this round! Player3s bet has been refunded!', colors.reset)
            time.sleep(1)
        elif len(player3_cards) == 5 and sum(player3_cards) < 21:
            player3_balance += player3_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player3 won this round! Player3 won $' + str(player2_bet), colors.reset, '\n')
            time.sleep(1)
        elif len(dealer_cards) == 5 and sum(dealer_cards) < 21:
            player3_balance -= player3_bet
            dealer_balance += player2_bet
            print(colors.red + 'Player3 lost this round! Player3 lost $' + str(player3_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player3_cards) > 21:
            player3_balance -= player3_bet
            dealer_balance += player2_bet
            print(colors.red + 'Player3 lost this round! Player3 lost $' + str(player3_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(dealer_cards) > 21:
            player3_balance += player3_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player3 won this round! Player3 won $' + str(player3_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player3_cards) == 21:
            player3_balance += player3_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player3 won this round! Player3 won $' + str(player3_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player2_cards) < sum(dealer_cards):
            player3_balance -= player3_bet
            dealer_balance += player2_bet
            print(colors.red + 'Player3 lost this round! Player3 lost $' + str(player3_bet), colors.reset, '\n')
            time.sleep(1)
        elif sum(player3_cards) > sum(dealer_cards):
            player3_balance += player3_bet
            dealer_balance -= player2_bet
            print(colors.green + 'Player3 won this round! Player3 won $' + str(player3_bet), colors.reset, '\n')
            time.sleep(1)
        print(colors.blue + 'Player3 now has a balance of $' + str(player3_balance), '\n', colors.reset)
        time.sleep(1)

    game_scoring()


def bot_game_dealers_turn():
    """
Used for the dealers turn to make a move while a bot game is selected
    """
    global user_score, user_balance, user_bet, dealer_balance, user_cards, dealer_cards, custom_game_starting_balance, \
        insurance_bought
    print(colors.red + 'The Dealer says No More Bets!\n', colors.reset)
    time.sleep(.500)

    while sum(dealer_cards) <= 15:
        if 11 in dealer_cards:
            insurance_choice = str(input('The dealer has pulled an ace and asks you if you would like to buy '
                                         'insurance (yes / no): '))
            print()
            if insurance_choice.lower() in {'y', 'yes'}:
                insurance_bought = True
                insurance_amount = user_bet / 2
                user_bet += insurance_amount
            elif insurance_choice.lower() in {'n', 'no'}:
                insurance_bought = False
                print('Buying insurance has been skipped for you...\n')
                time.sleep(1)
            else:
                print(colors.red + 'Buying insurance user input error found...\n', colors.reset)
                time.sleep(1)
                restart_game_error()

        bot_game_dealer_draws_card()
    bot_game_scoring()


def bot_game():
    """
This controls the majority of what occurs when a bot game is selected. This is a separate and edited version of the
solo game of blackjack but with the usage of up to 3 bot players added to the game.
    """
    # sourcery no-metrics skip: assign-if-exp, boolean-if-exp-identity, hoist-statement-from-if, lift - duplicated - conditional, merge - nested - ifs, merge - repeated - ifs, merge-nested-ifs, merge-repeated-ifs, remove - colors.redundant - if, remove-colors.redundant-if, remove-redundant-if, swap - nested - ifs, swap-nested-ifs
    # sourcery skip: merge-nested-ifs, merge-repeated-ifs, remove-colors.redundant-if, swap-nested-ifs
    # sourcery skip: lift - duplicated - conditional, merge - nested - ifs, merge - repeated - ifs
    # sourcery skip: remove - colors.redundant - if, swap - nested - ifs
    global user_score, user_balance, user_bet, dealer_balance, user_cards, dealer_cards, \
        player1_cards, player2_cards, player3_cards, number_of_players, player3_bet, player2_bet, player1_bet, \
        bot_game_selected, player1_balance, player2_balance, player3_balance, player1_bankrupt, player2_bankrupt, \
        player3_bankrupt, donate_money, normal_game_selected, custom_game_selected
    bot_game_selected = True
    normal_game_selected = False
    custom_game_selected = False
    user_cards = []
    player1_cards = []
    player2_cards = []
    player3_cards = []
    dealer_cards = []
    print(colors.yellow + 'Each bot will take their turns first and then you will play afterwards!', colors.reset)
    time.sleep(1)

    if player1_balance <= 0:
        player1_bankrupt = True
        print(colors.red + 'Player1 is currently bankrupt and therefore not participating in the game!', colors.reset)
        time.sleep(1)
        donate_money_question = str(input('Would you like to donate some money to this player to get them back in the '
                                          'game (yes / no): '))
        print()
        if donate_money_question.lower() in ['yes', 'y', 'sure']:
            while True:
                try:
                    donate_money = int(input("How much would you like to donate: "))
                    print()
                    time.sleep(.500)
                except ValueError:
                    print()
                    print(colors.red + 'Please enter a valid dollar amount!', colors.reset)
                    continue
                else:
                    break
            if donate_money > user_balance:
                user_bet_error_handling(
                    "Your total balance cannot make this donation! Your donation is too high for your balance!")
            elif donate_money <= 0:
                user_bet_error_handling("You cannot make a negative donation! Please place a higher donation than "
                                        "0 dollars!")
            elif donate_money > player1_balance:
                player1_bankrupt = False
                player1_balance += donate_money
                user_balance -= donate_money
                print(colors.green + 'Donation successful!', colors.reset)
        elif donate_money_question.lower() in ['no', 'n', 'nope', 'nah']:
            print('Donation skipped!\n')
            time.sleep(.5)
        else:
            print(colors.red + 'Donating money input error found...', colors.reset)
            restart_game_error()

    if player2_balance <= 0:
        player2_bankrupt = True
        print(colors.red + 'Player2 is currently bankrupt and therefore not participating in the game!', colors.reset)
        time.sleep(1)
        donate_money_question = str(input('Would you like to donate some money to this player to get them back in the '
                                          'game (yes / no): '))
        print()
        if donate_money_question.lower() in ['yes', 'y', 'sure']:
            while True:
                try:
                    donate_money = int(input("How much would you like to donate: "))
                    print()
                    time.sleep(.500)
                except ValueError:
                    print()
                    print(colors.red + 'Please enter a valid dollar amount!', colors.reset)
                    continue
                else:
                    break
            if donate_money > user_balance:
                user_bet_error_handling(
                    "Your total balance cannot make this donation! Your donation is too high for your balance!")
            elif donate_money <= 0:
                user_bet_error_handling("You cannot make a negative donation! Please place a higher donation than "
                                        "0 dollars!")
            elif donate_money > player2_balance:
                player2_bankrupt = False
                player2_balance += donate_money
                user_balance -= donate_money
                print(colors.green + 'Donation successful!', colors.reset)
        elif donate_money_question.lower() in ['no', 'n', 'nope', 'nah']:
            print('Donation skipped!\n')
            time.sleep(.5)
        else:
            print(colors.red + 'Donating money input error found...', colors.reset)
            restart_game_error()

    if player3_balance <= 0:
        player3_bankrupt = True
        print(colors.red + 'Player3 is currently bankrupt and therefore not participating in the game!', colors.reset)
        time.sleep(1)
        donate_money_question = str(input('Would you like to donate some money to this player to get them back in the '
                                          'game (yes / no): '))
        print()
        if donate_money_question.lower() in ['yes', 'y', 'sure']:
            while True:
                try:
                    donate_money = int(input("How much would you like to donate: "))
                    print()
                    time.sleep(.500)
                except ValueError:
                    print()
                    print(colors.red + 'Please enter a valid dollar amount!', colors.reset)
                    continue
                else:
                    break
            if donate_money > user_balance:
                user_bet_error_handling(
                    "Your total balance cannot make this donation! Your donation is too high for your balance!")
            elif donate_money <= 0:
                user_bet_error_handling("You cannot make a negative donation! Please place a higher donation than "
                                        "0 dollars!")
            elif donate_money > player3_balance:
                player3_bankrupt = False
                player3_balance += donate_money
                user_balance -= donate_money
                print(colors.green + 'Donation successful!', colors.reset)
        elif donate_money_question.lower() in ['no', 'n', 'nope', 'nah']:
            print('Donation skipped!\n')
            time.sleep(.5)
        else:
            print(colors.red + 'Donating money input error found...', colors.reset)
            restart_game_error()

    if player1_balance <= 0:
        player1_bankrupt = True
    else:
        player1_bankrupt = False
    if player2_balance <= 0:
        player2_bankrupt = True
    else:
        player2_bankrupt = False
    if player3_balance <= 0:
        player3_bankrupt = True
    else:
        player3_bankrupt = False

    if number_of_players == 1 and not player1_bankrupt:
        player1_bet = random.randint(1, player1_balance)
        print(colors.blue + 'Player1 decided to bet $' + str(player1_bet), '\n', colors.reset)
        time.sleep(1)
        while len(player1_cards) != 2:
            player1_cards.append(random.randint(1, 11))
            if sum(player1_cards) > 15:
                print(colors.blue + 'Player1 chooses to stay!', colors.reset)
                time.sleep(1)
        while sum(player1_cards) <= 15:
            if len(player1_cards) == 5:
                print(colors.blue + 'Player1 has pulled a total of 5 cards without busting!', colors.reset)
                time.sleep(1)
                break
            elif not player1_bankrupt:
                player1_cards.append(random.randint(1, 11))
                print(colors.blue + "Player1 has pulled a card...\n", colors.reset)
                time.sleep(1)
                print(colors.blue + "Player1 now has a total of " + str(sum(player1_cards)) + " from these cards",
                      player1_cards, colors.reset, "\n")
                time.sleep(1)
                if sum(player1_cards) > 15:
                    print(colors.blue + 'Player1 will now stay!', colors.reset)
                    time.sleep(1)

    elif number_of_players == 2:
        if not player1_bankrupt:
            player1_bet = random.randint(1, player1_balance)
            print(colors.blue + 'Player1 decided to bet $' + str(player1_bet), '\n', colors.reset)
            time.sleep(1)
        if not player2_bankrupt:
            player2_bet = random.randint(1, player2_balance)
            print(colors.blue + 'Player2 decided to bet $' + str(player2_bet), '\n', colors.reset)
            time.sleep(1)
        while len(player1_cards) != 2:
            player1_cards.append(random.randint(1, 11))
        while len(player2_cards) != 2:
            player2_cards.append(random.randint(1, 11))
            if sum(player1_cards) > 15:
                print(colors.blue + 'Player1 chooses to stay!', colors.reset)
                time.sleep(1)
                if sum(player2_cards) > 15:
                    print(colors.blue + 'Player2 chooses to stay!', colors.reset)
                    time.sleep(1)
            elif sum(player2_cards) > 15:
                print(colors.blue + 'Player2 chooses to stay!', colors.reset)
                time.sleep(1)
        while sum(player1_cards) <= 15:
            if len(player1_cards) == 5:
                print(colors.blue + 'Player1 has pulled a total of 5 cards without busting!', colors.reset)
                time.sleep(1)
                break
            elif not player1_bankrupt:
                player1_cards.append(random.randint(1, 11))
                print(colors.blue + "Player1 has pulled a card...\n", colors.reset)
                time.sleep(1)
                print(colors.blue + "Player1 now has a total of " + str(sum(player1_cards)) + " from these cards",
                      player1_cards, colors.reset, "\n")
                time.sleep(1)
                if sum(player1_cards) > 15:
                    print(colors.blue + 'Player1 will now stay!', colors.reset)
                    time.sleep(1)
        while sum(player2_cards) <= 15:
            if len(player2_cards) == 5:
                print(colors.blue + 'Player2 has pulled a total of 5 cards without busting!', colors.reset)
                time.sleep(1)
                break
            elif not player2_bankrupt:
                player2_cards.append(random.randint(1, 11))
                print(colors.blue + "Player2 has pulled a card...\n", colors.reset)
                time.sleep(1)
                print(colors.blue + "Player2 now has a total of " + str(sum(player2_cards)) + " from these cards",
                      player2_cards, colors.reset, "\n")
                time.sleep(1)
                if sum(player2_cards) > 15:
                    print(colors.blue + 'Player2 will now stay!', colors.reset)
                    time.sleep(1)
    elif number_of_players == 3:
        if not player1_bankrupt:
            player1_bet = random.randint(1, player1_balance)
            print(colors.blue + 'Player1 decided to bet $' + str(player1_bet), '\n', colors.reset)
            time.sleep(1)
        if not player2_bankrupt:
            player2_bet = random.randint(1, player2_balance)
            print(colors.blue + 'Player2 decided to bet $' + str(player2_bet), '\n', colors.reset)
            time.sleep(1)
        if not player3_bankrupt:
            player3_bet = random.randint(1, player3_balance)
            print(colors.blue + 'Player3 decided to bet $' + str(player3_bet), '\n', colors.reset)
            time.sleep(1)
        if player1_bankrupt and player2_bankrupt and player3_bankrupt and user_balance <= 0:
            print(
                colors.red + 'All players including you are bankrupt and the game can no longer be continued! You Lost!', colors.reset)
            time.sleep(2)
            new_game_starting()
        elif player1_bankrupt and player2_bankrupt and player3_bankrupt and user_balance > 0:
            print(colors.yellow +
                  'All players are bankrupt but you are still maintaining a positive balance, the fate of the game '
                  'depends on you now!', colors.reset)
            time.sleep(2)
        if player1_bankrupt:
            print(colors.red + 'Player1 is bankrupt and not playing!', colors.reset)
        if player2_bankrupt:
            print(colors.red + 'Player1 is bankrupt and not playing!', colors.reset)
        if player3_bankrupt:
            print(colors.red + 'Player1 is bankrupt and not playing!', colors.reset)
        while len(player1_cards) != 2 and not player1_bankrupt:
            player1_cards.append(random.randint(1, 11))
        while len(player2_cards) != 2 and not player2_bankrupt:
            player2_cards.append(random.randint(1, 11))
        while len(player3_cards) != 2 and not player3_bankrupt:
            player3_cards.append(random.randint(1, 11))
        if sum(player1_cards) > 15:
            print(colors.blue + 'Player1 chooses to stay!', colors.reset)
            time.sleep(1)
            if sum(player2_cards) > 15:
                print(colors.blue + 'Player2 chooses to stay!', colors.reset)
                time.sleep(1)
                if sum(player3_cards) > 15:
                    print(colors.blue + 'Player3 chooses to stay!', colors.reset)
                    time.sleep(1)
            elif sum(player3_cards) > 15:
                print(colors.blue + 'Player3 chooses to stay!', colors.reset)
                time.sleep(1)
        elif sum(player2_cards) > 15:
            print(colors.blue + 'Player2 chooses to stay!', colors.reset)
            time.sleep(1)
            if sum(player3_cards) > 15:
                print(colors.blue + 'Player3 chooses to stay!', colors.reset)
                time.sleep(1)
        elif sum(player3_cards) > 15:
            print(colors.blue + 'Player3 chooses to stay!', colors.reset)
            time.sleep(1)
        while sum(player1_cards) <= 15:
            if len(player1_cards) == 5:
                print(colors.blue + 'Player1 has pulled a total of 5 cards without busting!', colors.reset)
                time.sleep(1)
                break
            elif not player1_bankrupt:
                player1_cards.append(random.randint(1, 11))
                print(colors.blue + "Player1 has pulled a card...\n", colors.reset)
                time.sleep(1)
                print(colors.blue + "Player1 now has a total of " + str(sum(player1_cards)) + " from these cards",
                      player1_cards, colors.reset, "\n")
                time.sleep(1)
                if sum(player1_cards) > 15:
                    print(colors.blue + 'Player1 will now stay!', colors.reset)
                    time.sleep(1)
        while sum(player2_cards) <= 15:
            if len(player2_cards) == 5:
                print(colors.blue + 'Player2 has pulled a total of 5 cards without busting!', colors.reset)
                time.sleep(1)
                break
            elif not player2_bankrupt:
                player2_cards.append(random.randint(1, 11))
                print(colors.blue + "Player2 has pulled a card...\n", colors.reset)
                time.sleep(1)
                print(colors.blue + "Player2 now has a total of " + str(sum(player2_cards)) + " from these cards",
                      player2_cards, colors.reset, "\n")
                time.sleep(1)
                if sum(player2_cards) > 15:
                    print(colors.blue + 'Player2 will now stay!', colors.reset)
                    time.sleep(1)
        while sum(player3_cards) <= 15:
            if len(player3_cards) == 5:
                print(colors.blue + 'Player3 has pulled a total of 5 cards without busting!', colors.reset)
                time.sleep(1)
                break
            elif not player3_bankrupt:
                player3_cards.append(random.randint(1, 11))
                print(colors.blue + "Player3 has pulled a card...\n", colors.reset)
                time.sleep(1)
                print(colors.blue + "Player3 now has a total of " + str(sum(player3_cards)) + " from these cards",
                      player3_cards, colors.reset, "\n")
                time.sleep(1)
                if sum(player3_cards) > 15:
                    print(colors.blue + 'Player3 will now stay!', colors.reset)
                    time.sleep(1)

    if user_balance <= 0 and bot_game_selected:
        print(colors.red + 'You are currently out of money and cannot make a bet!', colors.reset)
        time.sleep(1)
        choice = str(input('Since you are playing with others, would you like to request a donation from a player '
                           '(yes / no): '))
        print()
        time.sleep(1)

        if choice.lower() in ['yes', 'y', 'sure']:
            if not player1_bankrupt and player1_presence and (player1_balance / (user_balance + 1)) > user_balance:
                if user_balance == 0:
                    bot_donation_amount = (user_balance + 100) * 1.5
                    user_balance += bot_donation_amount
                    player1_balance -= bot_donation_amount
                    print(colors.green + 'Player1 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
                else:
                    bot_donation_amount = (user_balance + 100) * -1.5
                    user_balance += bot_donation_amount
                    player1_balance -= bot_donation_amount
                    print(colors.green + 'Player1 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
            elif not player2_bankrupt and player2_presence and (player2_balance / (user_balance + 1)) > user_balance:
                if user_balance == 0:
                    bot_donation_amount = (user_balance + 100) * 1.5
                    user_balance += bot_donation_amount
                    player2_balance -= bot_donation_amount
                    print(colors.green + 'Player2 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
                else:
                    bot_donation_amount = (user_balance + 100) * -1.5
                    user_balance += bot_donation_amount
                    player2_balance -= bot_donation_amount
                    print(colors.green + 'Player2 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
            elif not player3_bankrupt and player3_presence and (player3_balance / (user_balance + 1)) > user_balance:
                if user_balance == 0:
                    bot_donation_amount = (user_balance + 100) * 1.5
                    user_balance += bot_donation_amount
                    player3_balance -= bot_donation_amount
                    print(colors.green + 'Player3 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
                else:
                    bot_donation_amount = (user_balance + 100) * -1.5
                    user_balance += bot_donation_amount
                    player2_balance -= bot_donation_amount
                    print(colors.green + 'Player2 has donated to you $' + str(bot_donation_amount), '\n', colors.reset)
                    time.sleep(1)
            else:
                print(colors.red + 'No other players were able to donate anything to you!', colors.reset)
                time.sleep(1)
                choice = str(
                    input('Would you like to restart from scratch (yes / no): '))
                print()
                time.sleep(1)
                if choice.lower() in ['yes', 'y', 'sure']:
                    new_game_starting()
                else:
                    print(colors.green + 'Thanks for playing!', colors.reset)
                    time.sleep(1)
                    sys.exit()

        elif choice.lower() in ['no', 'n', 'nah']:
            choice = str(input('Since you refuse to take a donation, this is game over for you... Would you like to '
                               'restart from scratch (yes / no): '))
            print()
            time.sleep(1)
            if choice.lower() in ['yes', 'y', 'sure']:
                new_game_starting()
            else:
                print(colors.green + 'Thanks for playing!', colors.reset)
                time.sleep(1)
                sys.exit()
        else:
            print(colors.red + 'Donation request user input error found...', colors.reset)
            time.sleep(1)
            restart_game_error()

    print(colors.green + 'Now it is your turn to play!', colors.reset)
    time.sleep(.5)
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
                print(colors.red + 'Please enter a valid dollar amount!', colors.reset)
                continue
            else:
                break

        if user_bet > user_balance:
            user_bet_error_handling("Your total balance cannot make this bet! Your bet is too high for your balance!")
        elif user_bet <= 0:
            user_bet_error_handling("You cannot make a negative bet! Please place a higher bet than 0 dollars!")
    else:
        print(colors.red + 'User input for all in feature found an error!\n', colors.reset)
        time.sleep(1)
        restart_game_error()
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print(colors.red + "The Dealer has ? &", dealer_cards[1], colors.reset, "\n")
            time.sleep(1)
    # Player Cards
    while len(user_cards) != 2:
        user_cards.append(random.randint(1, 11))
        if len(user_cards) == 2:
            print(colors.green + "You have a total of", str(sum(user_cards)), "from these cards", user_cards,
                  colors.reset, "\n")
            time.sleep(1)
    # Total of Dealer cards
    if sum(dealer_cards) >= 21:
        bot_game_scoring()
    # Total of Player cards
    elif len(user_cards) == 5 and sum(user_cards) < 21 and sum(dealer_cards) < 15:
        dealer_draws_card()
    while sum(user_cards) > 21 and sum(dealer_cards) < 15:
        dealer_draws_card()

    while sum(user_cards) < 21 and len(user_cards) < 5:
        choice = str(
            input("Do you want to hit, stay, double down, call for help, or quit the game (hit | stay | "
                  "double down | help | quit): "))
        print()
        time.sleep(1)

        if len(user_cards) == 5:
            bot_game_scoring()
        elif choice.lower() in ["hit", "h"]:
            user_draws_card()
        elif choice.lower() in ['s', 'stay']:
            bot_game_dealers_turn()
        elif choice.lower() in ["d", "double", 'double down']:
            if sum(user_cards) <= 11:
                print('You will now double down on your bets and pull only 1 more card and then you will stand for '
                      'this round!\n')
                user_bet *= 2
                time.sleep(1)
                user_draws_card()
                bot_game_dealers_turn()
            else:
                print(colors.red + 'You cannot double down here since the sum of your cards is over 11!', colors.reset)
                time.sleep(1)
        elif choice.lower() in ["help", "help", 'call help']:
            if sum(user_cards) == [10, 11]:
                print(colors.blue +
                      "Since your total is equal to either 10 or 11, we recommend that this is the best time to double "
                      "down if you have enough money!", colors.reset)
                time.sleep(3)
            elif sum(user_cards) <= 14:
                print(colors.blue + "Since your total is under or equal to 14, we recommend that you hit!", colors.reset)
                time.sleep(2)
            elif sum(user_cards) >= 15:
                print(colors.blue +
                      "Your odds are looking high enough to win, if your card total is closer to 15, we recommend only "
                      "making 1 hit move and then staying!", colors.reset)
                time.sleep(3)
                print(colors.blue + "If your card total is closer to 21, don't risk it! make a stay move!",
                      colors.reset)
                time.sleep(3)
        elif choice.lower() in ["q", "quit", "end"]:
            print(colors.green + "Ending game... Thanks for playing!\n", colors.reset)
            time.sleep(1)
            sys.exit()
        else:
            bot_game_scoring()

    # Endgame results
    bot_game_scoring()


def bot_player_choice():
    """
Allows the user to choose how many bots will enter a bot game
    """
    global number_of_players, player1_presence, player2_presence, player3_presence
    number_of_players = int(input('How many bots would you like to play with (1, 2, 3): '))
    print()
    time.sleep(.5)
    if number_of_players == 1:
        print(colors.green + '1 bot will be added into the game!', colors.reset)
        player1_presence = True
        player2_presence = False
        player3_presence = False
        time.sleep(1)
    elif number_of_players == 2:
        print(colors.green + '2 bots will be added into the game!', colors.reset)
        player1_presence = True
        player2_presence = True
        player3_presence = False
        time.sleep(1)
    elif number_of_players == 3:
        print(colors.green + '3 bots will be added into the game!', colors.reset)
        player1_presence = True
        player2_presence = True
        player3_presence = True
        time.sleep(1)
    else:
        print(colors.red + 'Number of players input error found...\n', colors.reset)
        time.sleep(1)
        restart_game_error()
    bot_game()


def game_options():
    """
Allows the end-user to be able to play the game but with custom money, win counts, and more
    """
    global user_balance, dealer_balance, user_score, user_dealer_money_choice, custom_game_starting_balance
    music_choice = str(input('Would you like to play music while playing (yes / no): '))
    print()
    time.sleep(.5)

    if music_choice.lower() in ['y', 'yes', 'sure']:
        choice = str(input('YouTube Music or Spotify Music? '))
        print()
        if choice.lower() in ['youtube', 'y', 'youtube music']:
            webbrowser.open('https://music.youtube.com/')
        elif choice.lower() in ['spotify', 's', 'spotify music']:
            webbrowser.open('https://open.spotify.com/')
    elif music_choice.lower() not in ['n', 'no', 'nope']:
        print(colors.red + 'Music choice input error found...\n', colors.reset)
        time.sleep(1)
        game_options()

    while True:
        user_game_picker = str(input('Would you like to play normal solo Blackjack 21, Blackjack 21 with bots, '
                                     'or a Custom Game with custom user game settings (blackjack / bots / custom): '))
        print()
        time.sleep(.5)

        if user_game_picker.lower() in ['b', 'blackjack', 'blackjack 21', 'black jack', 'n', 'normal']:
            game()
        elif user_game_picker.lower() in ['blackjack with bots', 'blackjack 21 with bots', 'bots', 'bot', 'bo', '1']:
            bot_player_choice()
        elif user_game_picker.lower() in ['c', 'custom', 'custom game', 'custom blackjack', 'custom blackjack game']:
            custom_game_main()
        else:
            print(colors.green + 'User game selection choice error found...Please enter correct choice' + colors.reset)


def custom_game_main():
    """
Allows the user to set up and play a custom game
    """
    global custom_game_starting_balance, user_balance, dealer_balance, user_score, user_dealer_money_choice, \
        custom_game_selected
    custom_game_selected = True
    custom_game_starting_balance = custom_game_stat_changer('How much would you like your starting balance to be? ')

    if custom_game_starting_balance <= 0:
        invalid_starting_balance_error('Invalid starting balance... Please choose a balance greater than 0 dollars!')

    user_balance = custom_game_starting_balance
    user_dealer_money_choice = custom_game_stat_changer('How much would you to set the dealers starting balance to? ')

    dealer_balance = user_dealer_money_choice
    user_score_choice = custom_game_stat_changer('How much would you like to set your scoring counter to? ')

    user_score = user_score_choice
    game()


def invalid_starting_balance_error(arg0):
    """
Used for when the user has a negative or invalid starting balance
    """
    print(colors.red + arg0, colors.reset)
    time.sleep(2)
    restart_game_error()


def custom_game_stat_changer(arg0):
    """
Used for taking in an argument while a custom game is being set up
    """
    result = int(input(arg0))
    print()
    time.sleep(.500)
    return result


def dealers_turn():
    """
Handles all of the card pulling actions for the dealer
    """
    global user_score, user_balance, user_bet, dealer_balance, user_cards, dealer_cards, custom_game_starting_balance, \
        insurance_bought
    print(colors.red + 'The Dealer says No More Bets!\n', colors.reset)
    time.sleep(.500)

    while sum(dealer_cards) <= 15:
        if 11 in dealer_cards:
            insurance_choice = str(input('The dealer has pulled an ace and asks you if you would like to buy '
                                         'insurance (yes / no): '))
            print()
            if insurance_choice.lower() in {'y', 'yes'}:
                insurance_bought = True
                insurance_amount = user_bet / 2
                user_bet += insurance_amount
            elif insurance_choice.lower() in {'n', 'no'}:
                insurance_bought = False
                print('Buying insurance has been skipped for you...\n')
                time.sleep(1)
            else:
                print(colors.red + 'Buying insurance user input error found...\n', colors.reset)
                time.sleep(1)
                restart_game_error()

        dealer_draws_card()
    game_scoring()


def bot_game_dealer_draws_card():
    """
Allows the dealer to draw a card while a bot game is selected
    """
    global user_bet, dealer_cards, insurance_bought
    dealer_cards.append(random.randint(1, 11))
    print(colors.red + "The Dealer has pulled a card...\n", colors.reset)
    time.sleep(1)
    print(colors.red + "The Dealer now has a total of " + str(sum(dealer_cards)) + " from these cards",
          dealer_cards, colors.reset, "\n")
    time.sleep(1)

    if len(dealer_cards) == 5 and sum(dealer_cards) <= 21:
        bot_game_scoring()

    elif sum(dealer_cards) > 15:
        print(colors.red + 'The Dealer will now stay!', colors.reset)
        time.sleep(1)
        bot_game_scoring()

    elif sum(dealer_cards) >= 21:
        bot_game_scoring()


def dealer_draws_card():  # sourcery skip: remove-colors.redundant-if, remove-redundant-if
    """
Allows the dealer to draw a card into their deck
    """
    global user_bet, dealer_cards, insurance_bought, bot_game_selected

    if len(dealer_cards) == 5 and sum(dealer_cards) <= 21 and not bot_game_selected:
        game_scoring()
    elif len(dealer_cards) == 5 and sum(dealer_cards) <= 21 and bot_game_selected:
        bot_game_scoring()
    elif sum(dealer_cards) > 15 and not bot_game_selected:
        game_scoring()
    elif sum(dealer_cards) > 15 and bot_game_selected:
        bot_game_scoring()
    elif sum(dealer_cards) >= 21 and not bot_game_selected:
        game_scoring()
    elif sum(dealer_cards) >= 21 and bot_game_selected:
        bot_game_scoring()

    dealer_cards.append(random.randint(1, 11))
    print(colors.red + "The Dealer has pulled a card...\n", colors.reset)
    time.sleep(1)
    print(colors.red + "The Dealer now has a total of " + str(sum(dealer_cards)) + " from these cards",
          dealer_cards, colors.reset, "\n")
    time.sleep(1)

    if len(dealer_cards) == 5 and sum(dealer_cards) <= 21 and not bot_game_selected:
        game_scoring()
    elif len(dealer_cards) == 5 and sum(dealer_cards) <= 21 and bot_game_selected:
        bot_game_scoring()
    elif sum(dealer_cards) > 15 and not bot_game_selected:
        print(colors.red + 'The Dealer will now stay!\n', colors.reset)
        time.sleep(1)
        game_scoring()
    elif sum(dealer_cards) > 15 and bot_game_selected:
        print(colors.red + 'The Dealer will now stay!\n', colors.reset)
        time.sleep(1)
        bot_game_scoring()
    elif sum(dealer_cards) >= 21 and not bot_game_selected:
        game_scoring()
    elif sum(dealer_cards) >= 21 and bot_game_selected:
        bot_game_scoring()


if __name__ == '__main__':
    main()
