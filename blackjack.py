#!/usr/bin/python3

# Created by Jordan Leich on 6/6/2020
# Edited by Adam Smith

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

# Player1 = Player()
# Player2 = Player()
# Player3 = Player()
# Player4 = Player()
# Player5 = Player()
# Dealer = Player(,,True,,,,True,)
# Player6 = Player(,,,,,,True,,)
# Player7 = Player(,,,,,,True,,)
# PLayer8 = Player(,,,,,,True,,)
# Player9 = Player(,,,,,,True,,)
# Player10 = Player(,,,,,,True,,)


def game_data(load_stats=False, reset_stats=False):
    """ Changed from trying to load the game when the game first runs
        to where it gets checked during the beginning of the game. also
        changed from a try/except to if statement. my opinion of better
        file handling. """

    if path.exists("data.json"):
        file_exist = True
    else:
        file_exist = False

    if load_stats and file_exist:
        with open('data.json', 'r') as user_data_file:
            user_data = json.load(user_data_file)
        user_balance = user_data['ubalance']
        user_score = user_data['uscore']
        dealer_balance = user_data['deal_balance']
        player1_balance = user_data['player1_balance']
        player2_balance = user_data['player2_balance']
        player3_balance = user_data['player3_balance']
        print(colors.green + 'Save file loaded!\n', colors.reset)

    elif load_stats and not file_exist:
        user_balance = 1000
        player1_balance = 1000
        player2_balance = 1000
        player3_balance = 1000
        user_score = 0
        dealer_balance = 5000
        print(colors.yellow + 'Save file not found, A new save file will be created shortly!', colors.reset)

        print(colors.yellow + 'Save file not found, A new save file will be created shortly!\n' + colors.reset)


print(
    colors.green + 'All players and the dealers money/stats will be reset to their original defaults...\n' + colors.reset)


# EXTRA MENUS

def user_error(print_text):
    print(colors.red + print_text + colors.reset)
    time.sleep(2)


def open_github(print_text, website_append=''):
    """
Used to open website in the users default web browser
    """
    print(colors.green + print_text + colors.reset)
    time.sleep(1)
    webbrowser.open_new("https://github.com/JordanLeich/Blackjack-21" + website_append)
    time.sleep(1)


def releases():
    """
Allows the user to be able to view either the latest or oldest release of this project via GitHub
    """
    while True:
        choice = int(input('''(1) Latest Stable Release
(2) Oldest Release
(3) Return to Menu

Which would you like to view: '''))
        print()

        if choice == 1:
            open_github("Opening the latest stable release...\n", "/releases")
        elif choice == 2:
            open_github("Opening the oldest release...\n", "/releases/tag/v5.0")
        elif choice == 3:  # breaks the loop
            return
        else:
            user_error('User input incorrect please try again...\n')


def donation_opener(arg0, arg1):
    """
Used to open a donation page in the users default web browser
    """
    print(colors.green + arg0, colors.reset)
    webbrowser.open_new(arg1)
    time.sleep(2)


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

Which donation option would you like to use: '''))
        print()

        if donate_choice == 1:
            donation_opener("Opening PayPal Donation page...\n",
                            "https://www.paypal.com/donate/?business=8FGHU8Z4EJPME&no_recurring=0&currency_code=USD")
        elif donate_choice == 2:
            donation_opener("Opening Cash App Donation page...\n", "https://cash.app/$JordanLeich")
        elif donate_choice == 3:
            return
        else:
            user_error('User input incorrect please try again...\n')


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
            open_github("Opening all contributors of this project...\n", "/graphs/contributors")
        elif choice == 3:
            donate()
        elif choice == 4:
            return
        else:
            user_error('User input incorrect please try again...\n')


# Work In Progress Parts

def view_stats(user_balance, user_score, dealer_balance, player1_balance, player2_balance, player3_balance):
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


def getting_input(arg0, arg1):  # revamp for yes/no questions
    """
Used for simply receiving input as an argument
    """
    result = input(arg0)
    print()
    time.sleep(arg1)

    return result


def user_bet_error_handling(arg0):  # improve bet handling situations # need to get rid of
    """
Used for whenever the player makes a bet that causes an error or is logically incorrect
    """
    print(colors.red + arg0, colors.reset)
    time.sleep(2)
    restart_game_error()


def restart_game_error():  # NEED TO GET RID OF
    """
Used for error handling to prevent the game from crashing.
    """
    print("Restarting Blackjack Game from scratch...\n")
    main()


# MAIN MENU + GAME HANDLING

def player_win_text(message_text):  # helper functions for score_bot
    print(colors.green + message_text, colors.reset, '\n')
    time.sleep(1)


def player_lose_text(message_text):  # helper functions for score_bot
    print(colors.red + message_text, colors.reset, '\n')
    time.sleep(1)


def player_tie_text(message_text):  # helper functions for score_bot
    print(colors.yellow + message_text, colors.reset, '\n')
    time.sleep(1)


def donate_to_bot(player_balance, user_balance, player_name):
    if player_balance <= 0:
        print(colors.red + f'{player_name} is bankrupt and can not participating in the game!', colors.reset)
        time.sleep(1)
        donate_money_question = str(input('Would you like to donate some money to get them back in the '
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
            else:
                player_balance += donate_money
                user_balance -= donate_money
                print(colors.green + 'Donation successful!', colors.reset)
                return player_balance, user_balance
        elif donate_money_question.lower() in ['no', 'n', 'nope', 'nah']:
            print('Donation skipped!\n')
            time.sleep(.5)
        else:
            print(colors.red + 'Donating money input error found...', colors.reset)
            restart_game_error()


class Blackjack:
    def __init__(self, user_balance, user_score, dealer_balance):
        # user attributes
        self.user_cards = []
        self.user_bet = 0
        self.user_score = user_score
        self.user_balance = user_balance
        self.insurance_bought = False
        self.donate_money = 0
        # dealer attributes
        self.dealer_balance = dealer_balance
        self.dealer_cards = []
        # bot attributes -- not bots but multiple other users
        self.bot_number = 0
        self.bot_balances = []  # start w/ 1000 or custom
        self.bot_bets = []  # start w/ 0
        self.bot_cards = []  # list of list start empty
        # self.bot_bankruptcy = []
        # game attributes
        self.bot_game_selected = False
        self.custom_game_selected = False

    def add_bots(self):
        """
        Add bots to the game and set them up with default stats
        """
        self.bot_number += 1
        self.bot_balances.append(1000)
        self.bot_bets.append(0)
        self.bot_cards.append([])
        # self.bot_bankruptcy.append(False)

    def player_balance(self):
        print(colors.green + f'Your balance is ${self.user_balance}\n', colors.reset)
        time.sleep(1)
        print(colors.red + f'The dealers balance is ${self.dealer_balance}\n', colors.reset)
        time.sleep(1)

    def donation_from_bot(self):
        for c, balance in enumerate(self.bot_balances):
            if balance > 0:
                bot_donation_amount = balance / 5
                self.user_balance += bot_donation_amount
                self.bot_balances[c] -= bot_donation_amount
                print(colors.green + f'Player{c} has donated ${bot_donation_amount} to you.\n', colors.reset)
                time.sleep(1)
                break

    def play_game(self):  # sourcery no-metrics
        while self.user_balance > 0:
            self.player_balance()

            # donate to bots only if they don't have any money
            for c, value in enumerate(self.bot_balances):
                if value <= 0:
                    self.bot_balances[c], self.user_balance = donate_to_bot(value, self.user_balance, f'Player{c}')

            for c, v in enumerate(self.bot_cards):
                self.bot_decisions(c)

            if self.user_balance <= 0 and max(self.bot_balances) <= 0:
                print(colors.red + 'All players are bankrupt! You Lost!', colors.reset)
                time.sleep(2)
                sys.exit()
            elif max(self.bot_balances) <= 0:  # only the bots are bankrupt
                print(colors.yellow + 'The fate of the game depends on you now!', colors.reset)
                time.sleep(2)

            # get money from the bots
            if self.user_balance <= 0 and len(self.bot_balances):
                print(colors.red + 'You are currently out of money and cannot make a bet!', colors.reset)
                time.sleep(1)
                choice = str(input('Would you like to request a donation from another player (yes / no): '))
                print()
                time.sleep(1)

                # ask for donations from bots
                if choice.lower() in ['yes', 'y', 'sure']:
                    if max(self.bot_balances) <= 0:
                        print(colors.red + 'No other players were able to donate anything to you!', colors.reset)
                        time.sleep(1)
                        choice = str(
                            input('Would you like to restart from scratch (yes / no): '))
                        print()
                        time.sleep(1)
                        if choice.lower() in ['yes', 'y', 'sure']:
                            reset_stats()
                        else:
                            print(colors.green + 'Thanks for playing!', colors.reset)
                            time.sleep(1)
                            sys.exit()
                    else:
                        self.donation_from_bot()
                elif choice.lower() in ['no', 'n', 'nah']:
                    choice = str(
                        input('Since you refuse to take a donation, this is game over for you... Would you like to '
                              'restart from scratch (yes / no): '))
                    print()
                    time.sleep(1)
                    if choice.lower() in ['yes', 'y', 'sure']:
                        reset_stats()
                    else:
                        print(colors.green + 'Thanks for playing!', colors.reset)
                        time.sleep(1)
                        sys.exit()
                else:
                    print(colors.red + 'Donation request user input error found...', colors.reset)
                    time.sleep(1)
                    restart_game_error()

            user_all_in = str(input("Would you like to go all in (yes / no): "))
            print()
            time.sleep(.500)

            if user_all_in.lower() in ["y", "yes"]:
                self.user_bet = self.user_balance
                time.sleep(.500)
            elif user_all_in.lower() in ["n", "no"]:
                while True:
                    try:
                        self.user_bet = int(input("How many dollars would you like to bet? "))
                        print()
                        time.sleep(.500)
                    except ValueError:
                        print()
                        print(colors.red + 'Please enter a valid dollar amount!', colors.reset)
                        continue
                    else:
                        break

                if self.user_bet > self.user_balance:
                    user_bet_error_handling(
                        "Your total balance cannot make this bet! Your bet is too high for your balance!")
                elif self.user_bet <= 0:
                    user_bet_error_handling("You cannot make a negative bet! Please place a higher bet than 0 dollars!")

            else:
                print(colors.red + 'User input for all in feature found an error!\n', colors.reset)
                time.sleep(1)
                continue

            # dealer gets cards
            self.dealer_cards = [random.randint(1, 11) for _ in range(2)]
            print(colors.red + f'The Dealer has ? & {self.dealer_cards[1]}\n', colors.reset)

            time.sleep(1)
            # player gets cards
            self.user_cards = [random.randint(1, 11) for _ in range(2)]
            print(colors.green + f'You have a total of {sum(self.user_cards)} from {self.user_cards}\n', colors.reset)

            time.sleep(1)

            # Total of Dealer cards
            if sum(self.dealer_cards) >= 21:
                self.game_scoring()
            # Total of Player cards
            elif len(self.user_cards) == 5 and sum(self.user_cards) < 21 and sum(self.dealer_cards) < 15:
                self.dealer_draws_card()

            while sum(self.user_cards) == 21 and sum(self.dealer_cards) < 15:
                self.dealer_draws_card()

            choice = ''
            while choice not in ['s', 'stay'] and sum(self.user_cards) < 21 and len(self.user_cards) < 5:
                choice = str(
                    input("Do you want to hit, stay, double down, call for help, or quit the game (hit | stay | "
                          "double down | help | quit): "))
                print()
                time.sleep(1)

                if choice.lower() in ["hit", "h"]:
                    self.user_draws_card()
                elif choice.lower() in ['s', 'stay']:
                    self.dealers_turn()
                elif choice.lower() in ["d", "double", 'double down']:
                    if sum(self.user_cards) <= 11:
                        print(
                            'You will now double down on your bets and pull only 1 more card and then you will stand for '
                            'this round!\n')
                        self.user_bet *= 2
                        time.sleep(1)
                        self.user_draws_card()
                        self.dealers_turn()
                    else:
                        print(colors.red + 'You cannot double down here since the sum of your cards is over 11!',
                              colors.reset)
                        time.sleep(1)
                elif choice.lower() in ["help", "help", 'call help']:
                    if sum(self.user_cards) == [10, 11]:
                        print(colors.blue +
                              "Since your total is equal to either 10 or 11, we recommend that this is the best time to double "
                              "down if you have enough money!", colors.reset)
                        time.sleep(3)
                    elif sum(self.user_cards) <= 14:
                        print(colors.blue + "Since your total is under or equal to 14, we recommend that you hit!",
                              colors.reset)
                        time.sleep(2)
                    elif sum(self.user_cards) >= 15:
                        print(colors.blue +
                              "Your odds are looking high enough to win, if your card total is closer to 15, we "
                              "recommend only making 1 hit move and then staying!\n", colors.reset)
                        time.sleep(3)
                        print(colors.blue + "If your card total is closer to 21, don't risk it! make a stay move!\n",
                              colors.reset)
                        time.sleep(3)
                elif choice.lower() in ["q", "quit", "end"]:
                    print(colors.green + "Ending game... Thanks for playing!\n", colors.reset)
                    time.sleep(1)
                    sys.exit()
                else:
                    self.game_scoring()
                    break
            # Endgame results
            self.game_scoring()
            self.end_round_notification()

    def bot_decisions(self, value):
        if self.bot_balances[value] > 0:
            self.bot_bets[value] = random.randint(1, self.bot_balances[value])
            print(colors.blue + f'Player{value + 1} decided to bet $' + str(self.bot_bets[value]), '\n', colors.reset)
            time.sleep(1)
        else:
            print(colors.red + f'Player{value + 1} is bankrupt and not playing!', colors.reset)
            return

        self.bot_cards[value] = [random.randint(1, 11) for _ in range(2)]

        if sum(self.bot_cards[value]) > 15:
            print(colors.blue + f'Player{value + 1} chooses to stay!\n', colors.reset)
            time.sleep(1)

        while sum(self.bot_cards[value]) <= 15:
            if len(self.bot_cards[value]) == 5:
                print(colors.blue + f'Player{value + 1} has pulled a total of 5 cards without busting!\n', colors.reset)
                time.sleep(1)
                break
            elif self.bot_balances[value] > 0:
                self.bot_cards[value].append(random.randint(1, 11))
                print(colors.blue + f"Player{value + 1} has pulled a card...\n", colors.reset)
                time.sleep(1)
                print(colors.blue + f"Player{value + 1} now has a total of " + str(
                    sum(self.bot_cards[value])) + " from these cards",
                      self.bot_cards[value], colors.reset, "\n")
                time.sleep(1)
                if sum(self.bot_cards[value]) > 21:
                    print(colors.blue + f'Player{value + 1} has BUSTED!\n', colors.reset)
                    time.sleep(1)
                elif sum(self.bot_cards[value]) > 15:
                    print(colors.blue + f'Player{value + 1} will now stay!\n', colors.reset)
                    time.sleep(1)

    def user_draws_card(self):
        """
        Used for whenever the player is required to draw a card
        """
        self.user_cards.append(random.randint(1, 11))
        print(colors.green + f'You have a total of {sum(self.user_cards)} from {self.user_cards}\n', colors.reset)
        time.sleep(1)
        while sum(self.user_cards) == 21 and sum(self.dealer_cards) < 15:
            self.dealer_draws_card()

    def dealers_turn(self):
        """
        Handles all of the card pulling actions for the dealer
        """
        print(colors.red + 'The Dealer says No More Bets!\n', colors.reset)
        time.sleep(.500)

        while sum(self.dealer_cards) <= 15:
            if 11 in self.dealer_cards and not self.insurance_bought:
                insurance_choice = str(input('The dealer has an ace. Would you like to buy insurance (yes / no): '))
                print()
                if insurance_choice.lower() in ['y', 'yes']:
                    self.insurance_bought = True
                    insurance_amount = self.user_bet / 2
                    self.user_bet += insurance_amount
                elif insurance_choice.lower() in ['n', 'no']:
                    self.insurance_bought = False
                    print('Buying insurance has been skipped for you...\n')
                    time.sleep(1)
                else:
                    print(colors.red + 'Buying insurance user input error found...\n', colors.reset)
                    continue

            self.dealer_draws_card()

    def dealer_draws_card(self):
        """
        Allows the dealer to draw a card into their deck
        """
        if len(self.dealer_cards) == 5 and sum(self.dealer_cards) <= 21:
            self.game_scoring()
        elif sum(self.dealer_cards) > 15:
            self.game_scoring()
        elif sum(self.dealer_cards) >= 21:
            self.game_scoring()

        self.dealer_cards.append(random.randint(1, 11))
        print(colors.red + "The Dealer has pulled a card...\n", colors.reset)
        time.sleep(1)
        print(colors.red + f'The Dealer now has {sum(self.dealer_cards)} from these cards {self.dealer_cards}\n',
              colors.reset)
        time.sleep(1)

    def game_scoring(self):
        """
        Handles of the end game scoring based upon card results between the dealer and end-user
        """
        print(colors.red + "The Dealer has a grand total of", str(sum(self.dealer_cards)), "from these cards",
              self.dealer_cards, colors.reset, "\n")
        time.sleep(1)
        print(colors.green + "You have a grand total of " + str(sum(self.user_cards)) + " with", self.user_cards,
              colors.reset, "\n")
        time.sleep(1)

        if len(self.dealer_cards) == 5 and sum(self.dealer_cards) <= sum(self.user_cards) <= 21:
            player_tie_text("PUSH! This is a tie! All bet money is refunded!")
        elif len(self.user_cards) == 5 and sum(self.user_cards) <= sum(self.dealer_cards) <= 21:
            player_tie_text("PUSH! This is a tie! All bet money is refunded!")
        elif sum(self.user_cards) == sum(self.dealer_cards):
            player_tie_text("PUSH! This is a tie! All bet money is refunded!")
        elif len(self.user_cards) == 5 and sum(self.user_cards) < 21:
            time.sleep(1)
            print(colors.green + "You have automatically won since you have pulled a total of 5 cards without "
                                 "busting!\n", colors.reset)
            self.user_win_stats()
        elif len(self.dealer_cards) == 5 and sum(self.dealer_cards) < 21:
            print(colors.red + "You have automatically lost since the dealer has pulled a total of 5 cards without "
                               "busting!\n", colors.reset)
            time.sleep(1)
            self.user_loses_stats()
        elif sum(self.user_cards) > 21:
            print(colors.red + "BUSTED! The Dealer Wins! You lost $" + str(self.user_bet) + "!\n", colors.reset)
            self.user_loses_stats()
        elif sum(self.dealer_cards) > 21:
            print(colors.green + "The Dealer BUSTED! You win! You won $" + str(self.user_bet) + "!\n", colors.reset)
            self.user_win_stats()
        elif sum(self.user_cards) == 21:
            print(colors.green + "BLACKJACK! You hit 21! You won $" + str(self.user_bet) + "!\n", colors.reset)
            self.user_win_stats()
        elif self.insurance_bought and sum(self.dealer_cards) == 21:
            player_tie_text("BLACKJACK! Since you purchased insurance, you do not lose any money!")
            self.user_loses_stats(0)
            self.insurance_bought = False
        elif 11 in self.dealer_cards and sum(self.dealer_cards) == 21:  # offered insurance - not used
            self.user_balance -= self.user_bet + (self.user_bet / 2)
            player_lose_text(
                "BLACKJACK! Since you did not purchased insurance, you will lose 1.5 times your original bet!")
            self.user_loses_stats(1.5)
            self.insurance_bought = False
        elif sum(self.dealer_cards) == 21:
            print(colors.green + "BLACKJACK! The Dealer hit 21! You Lost $" + str(self.user_bet) + "!\n", colors.reset)
            self.user_loses_stats()
        elif sum(self.user_cards) > sum(self.dealer_cards):
            print(colors.green + "You Win! Your cards were greater than the dealers deck, You won $" +
                  str(self.user_bet) + "!\n", colors.reset)
            self.user_win_stats()
        elif sum(self.dealer_cards) > sum(self.user_cards):
            print(colors.red + "The dealer wins! Your cards were less than the dealers deck, You lost $" + str(
                self.user_bet) +
                  "!\n", colors.reset)
            self.user_loses_stats()
        else:  # This else statement is most likely unreachable but still used as a safety net in case anything with
            # scoring goes wrong.
            print(colors.red + 'Scoring error found...', colors.reset)
            time.sleep(1)
            restart_game_error()

        for c, balance in enumerate(self.bot_balances):
            if balance > 0:
                self.score_bot(c)

    def score_bot(self, value):
        player_bet = self.bot_bets[value]

        if len(self.dealer_cards) == 5 and sum(self.bot_cards[value]) >= sum(self.dealer_cards):
            player_tie_text(f"Player{value + 1} pushed this round! Player{value + 1}'s bet has been refunded!")
        elif len(self.bot_cards[value]) == 5 and sum(self.dealer_cards) >= sum(self.bot_cards[value]):
            player_tie_text(f"Player{value + 1} pushed this round! Player{value + 1}'s bet has been refunded!")
        elif sum(self.bot_cards[value]) == sum(self.dealer_cards):
            player_tie_text(f"Player{value + 1} pushed this round! Player{value + 1}'s bet has been refunded!")
        elif len(self.bot_cards[value]) == 5 and sum(self.bot_cards[value]) < 21:
            self.bot_balances[value] += player_bet
            self.dealer_balance -= player_bet
            player_win_text(f'Player{value + 1} won this round! Player{value + 1} won $' + str(player_bet))
        elif len(self.dealer_cards) == 5 and sum(self.dealer_cards) < 21:
            self.bot_balances[value] -= player_bet
            self.dealer_balance += player_bet
            player_lose_text(f'Player{value + 1} lost this round! Player{value + 1} lost $' + str(player_bet))
        elif sum(self.bot_cards[value]) > 21:
            self.bot_balances[value] -= player_bet
            self.dealer_balance += player_bet
            player_lose_text(f'Player{value + 1} lost this round! Player{value + 1} lost $' + str(player_bet))
        elif sum(self.dealer_cards) > 21:
            self.bot_balances[value] += player_bet
            self.dealer_balance -= player_bet
            player_win_text(f'Player{value + 1} won this round! Player{value + 1} won ${player_bet}')

        elif sum(self.bot_cards[value]) == 21:
            self.bot_balances[value] += player_bet
            self.dealer_balance -= player_bet
            player_win_text(f'Player{value + 1} won this round! Player{value + 1} won ${player_bet}')

        elif sum(self.bot_cards[value]) < sum(self.dealer_cards):
            self.bot_balances[value] -= player_bet
            self.dealer_balance += player_bet
            player_lose_text(f'Player{value + 1} lost this round! Player{value + 1} lost $' + str(player_bet))
        elif sum(self.bot_cards[value]) > sum(self.dealer_cards):
            self.bot_balances[value] += player_bet
            self.dealer_balance -= player_bet
            player_win_text(f'Player{value + 1} won this round! Player{value + 1} won ${player_bet}')

        time.sleep(1)
        print(colors.blue + f'Player{value + 1} now has a balance of $' + str(self.bot_balances[value]), '\n',
              colors.reset)

    def end_round_notification(self):
        """
    Used when 1 single round of blackjack has ended. Allows the user to play another game of blackjack or quit playing
        """
        print(colors.green + "Your win count is", self.user_score,
              "and your total balance is $" + str(self.user_balance), "\n",
              colors.reset)
        time.sleep(1)
        print(colors.red + "The dealers total balance is $" + str(self.dealer_balance), "\n", colors.reset)

        if self.user_balance <= 0 and len(self.bot_balances) == 0:
            print(colors.red + "You don't have any more money to bet... Game Over!", colors.reset)
            time.sleep(2)
        else:
            if self.dealer_balance <= 0:
                print(colors.green + "Congratulations! You have beat the BlackJack 21 game by defeating the dealers "
                                     "balance!", colors.reset)
                time.sleep(2)
            elif self.dealer_balance <= 2500:
                print(colors.green + "The dealers balance is looking small enough for you to win! You're doing well...",
                      colors.reset)
                time.sleep(2)
            ''' 
            # figure out the most appropriate place for this -- to get out of the multiple for loops properly

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
            '''

    def user_loses_stats(self, multiplier=1.0):
        """
        Update stats when the user loses the round
        """
        time.sleep(1)
        self.user_score -= 1
        self.user_balance -= (self.user_bet * multiplier)
        self.dealer_balance += (self.user_bet * multiplier)

    def user_win_stats(self, multiplier=1.0):
        """
        Update stats when the user wins the round
        """
        time.sleep(1)
        self.user_score += 1
        self.user_balance += (self.user_bet * multiplier)
        self.dealer_balance -= (self.user_bet * multiplier)


def game(user_balance=1000, user_score=0, dealer_balance=5000, players=0):
    """
This is the main code used for the game entirely
    """
    single_player = Blackjack(user_balance, user_score, dealer_balance)
    for _ in range(players):
        single_player.add_bots()
    single_player.play_game()


# GAME SETUP #

def bot_player_choice():
    """
    User chooses how many bots to play with
    """
    while True:
        player_num = int(input('How many bots would you like to play with (1, 2, 3): '))
        print()
        time.sleep(.5)
        if player_num == 1:
            print(colors.green + str(player_num) + ' bot will be added into the game!\n', colors.reset)
            time.sleep(1)
            return player_num
        elif 1 < player_num < 4:
            print(colors.green + str(player_num) + ' bots will be added into the game!\n', colors.reset)
            time.sleep(1)
            return player_num
        else:  # if num is not the correct bot count have the user retry their selection
            user_error('Number of players incorrect. Choose between 1 to 3 players...\n')
            continue


def custom_user_input(user_message):  # helper function for custom_game_setup()
    """
Used for taking in an argument while a custom game is being set up
    """
    result = 0
    while result <= 0:
        result = int(input(user_message))
        print()
        time.sleep(.500)
        if result <= 0:
            print('Please choose a number greater than 0.')
    return result


def custom_game_setup():  # fix user input validate
    """
Allows the user to set up and play a custom game
    """
    user_balance = custom_user_input('How much money would you like to start with? ')
    dealer_balance = custom_user_input('How much money would you like the dealer to start with? ')
    user_score = custom_user_input('How much would you like to set your scoring count to? ')
    return user_balance, dealer_balance, user_score


def game_options():
    """
Allows the end-user to be able to play the game with custom money, win counts, and more
    """
    while True:
        music_choice = str(input('Would you like to play music while playing (yes / no): '))
        print()
        time.sleep(.5)

        if music_choice.lower() in ['y', 'yes', 'sure']:
            while True:
                choice = str(input('YouTube Music or Spotify Music? '))
                print()
                if choice.lower() in ['youtube', 'y', 'youtube music']:
                    webbrowser.open('https://music.youtube.com/')
                elif choice.lower() in ['spotify', 's', 'spotify music']:
                    webbrowser.open('https://open.spotify.com/')
                else:
                    print(colors.red + 'Option not available. Please try again ...\n', colors.reset)
                    continue
                break
            break
        elif music_choice.lower() not in ['n', 'no', 'nope']:
            print(colors.red + 'Music choice not found. Please try again ...\n', colors.reset)
            time.sleep(1)
        else:  # exit the loop - 'no' selected
            break
    while True:
        game_choice = str(input('Would you like to play solo Blackjack, Blackjack with bots, '
                                'or a Custom Game with custom user game settings (blackjack / bots / custom): '))
        print()
        time.sleep(.5)

        if game_choice.lower() in ['b', 'blackjack', 'blackjack 21', 'black jack', 'n', 'normal', 's', 'solo']:
            game()
        elif game_choice.lower() in ['blackjack with bots', 'blackjack 21 with bots', 'bots', 'bot', 'bo', '1']:
            game(players=bot_player_choice())
        elif game_choice.lower() in ['c', 'custom', 'custom game', 'custom blackjack', 'custom blackjack game']:
            game(custom_game_setup())
        else:
            user_error("User game selection incorrect please try again....")


def reset_stats():
    print(colors.green + 'All players and the dealers money/stats will be reset to their original defaults...\n',
          colors.reset)
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
    main()


def main():
    """
The first piece of the program introduced to the end-user. This section allows the user to 
skip around in the game by using the game mode selection choices
    """
    while True:
        choice = input('Start / Tutorial / Express / View Stats / Reset Stats / Extras / Quit: ')
        print()
        time.sleep(.5)

        if choice.lower() in ['start', 'yes', 's']:
            game_options()
        elif choice.lower() in ['no', 'n', 't', 'tutorial']:
            print(colors.green +
                  'A youtube video should now be playing... This game will auto resume once the video has been fully '
                  'played...', colors.reset)
            webbrowser.open("https://www.youtube.com/watch?v=eyoh-Ku9TCI", new=1)
            time.sleep(140)
            game()
        elif choice.lower() in ['e', 'express']:
            game()
        elif choice.lower() in ['stats', 'view stats', 'v', 'view']:
            view_stats()  # update stats to be more like hands won and total money gained
        elif choice.lower() in ['reset', 'reset stats']:
            reset_stats()
        elif choice.lower() in ['extra', 'extras']:
            extra()
        elif choice.lower() in ['quit', 'q', 'exit']:
            sys.exit()
        else:
            user_error("User input incorrect please try again...\n")


if __name__ == '__main__':
    main()
