#!/usr/bin/python3

# Created by Jordan Leich on 6/6/2020
# Edited by Adam Smith

from random import randint
from time import sleep
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


def load_or_save_game(save_game=None, stats=False):
    # save_game = class instance (i.e. save_game=self)
    """ Changed from trying to load the game when the game first runs
        to where it gets checked during the beginning of the game. """
    user_score, user_balance, dealer_balance, bot_number = 0, 1000, 5000, 0
    bot_balances = []
    
    if not save_game and path.exists("data.json"):
        with open('data.json', 'r') as user_data_file:
            user_data = json.load(user_data_file)
        user_score = user_data['uscore']
        user_balance = user_data['ubalance']
        dealer_balance = user_data['deal_balance']
        bot_balances = user_data['bot_balances']
        if not stats:
            print_green('Save file loaded!\n')
    elif not save_game:
        if not stats:
            print_yellow('Save file not found, A new save file will be created shortly!')
        default_stats = {'ubalance': user_balance, 
                         'uscore': user_score,
                         'deal_balance': dealer_balance, 
                         'bot_balances': bot_balances, 
                        }
        with open('data.json', 'w') as user_data_file:
            json.dump(default_stats, user_data_file)
    else:
        user_score, user_balance, dealer_balance, bot_balances = save_game.get_data()
        print_yellow('Saving game. Please do not exit the program.')
        default_stats = {'ubalance': user_balance, 
                         'uscore': user_score,
                         'deal_balance': dealer_balance, 
                         'bot_balances': bot_balances, 
                        }
        with open('data.json', 'w') as user_data_file:
            json.dump(default_stats, user_data_file)
    return user_balance, user_score, dealer_balance, bot_number, bot_balances



# EXTRA MENUS

def user_error(print_text):
    print_red(print_text)
    sleep(2)


def open_github(print_text, website_append=''):
    """
Used to open website in the users default web browser
    """
    print_green(print_text)
    webbrowser.open_new(f'https://github.com/JordanLeich/Blackjack-21{website_append}')
    sleep(1)


def releases():
    """
    Menu choice to view either the latest or oldest release of this Github project
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
        elif choice == 3:  # exits the loop
            return
        else:
            user_error('User input incorrect please try again...\n')


def donation_opener(print_text, website):
    """
Used to open a donation page in the users default web browser
    """
    print_green(print_text)
    webbrowser.open_new(website)
    sleep(2)


def donate():
    """
Allows the user to be able to donate via PayPal or Cash App methods
    """
    while True:
        print_yellow('Since this project is completely free to use and open source, users have the option to send a donation of their choice but this action is not required.\n')
        sleep(2)
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


def view_stats():  # prints your stats based off the load file
    user_balance, user_score, dealer_balance, bot_number, bot_balances = load_or_save_game(stats=True)
    print_green('Your current in game stats will now be displayed below!\n\n')
    sleep(1)
    print(f'Your balance is ${user_balance}')
    print(f'Your win count is {user_score}')
    print(f'The dealers balance is ${dealer_balance}')
    for c, v in enumerate(bot_balances):
        print(f"Player{c}'s balance is ${v}\n")
    sleep(6)


# GAME HANDLING

def money_transfer_input(input_text, user_balance, money_transfer):
    while True:
        try:
            transfer_amount = int(input(input_text))
            print()
        except ValueError:
            print_red('Please enter a valid dollar amount!')
            continue

        if transfer_amount > user_balance:
            print_red("Sorry, you cannot exceed your balance!")
        elif transfer_amount <= 0:
            print_red(f"Sorry, you cannot make a negative {money_transfer}. Please try again.")
        else:  # exit condition
            return transfer_amount


def print_green(message_text):
    print(f'{colors.green}{message_text}{colors.reset}')


def print_red(message_text):
    print(f'{colors.red}{message_text}{colors.reset}')


def print_yellow(message_text):
    print(f'{colors.yellow}{message_text}{colors.reset}')


def print_blue(message_text):
    print(f'{colors.blue}{message_text}{colors.reset}')


def _lose_bet(player_bet, player_balance, dealer_balance):  # helper func for balances
    return player_balance - player_bet, dealer_balance + player_bet


def _win_bet(player_bet, player_balance, dealer_balance):  # helper func for balances
    return player_balance + player_bet, dealer_balance - player_bet


def donate_to_bot(player_balance, user_balance, player_name):
    if player_balance <= 0:
        print_red(f'{player_name} is bankrupt and can not participating in the game!')
        sleep(1)
        
        if yes_or_no_choice('Would you like to donate some money to get them back in the game (yes / no): '):
            donate_money = money_transfer_input("How much would you like to donate: ", self.user_balance, 'donation')
            player_balance, user_balance = _win_bet(donate_money, player_balance, user_balance)
            print_green('Donation successful!')
    return player_balance, user_balance


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

    def add_bots(self, balance=1000):
        """
        Add bots to the game and set them up with default stats
        """
        self.bot_number += 1
        self.bot_balances.append(balance)
        self.bot_bets.append(0)
        self.bot_cards.append([])
        # self.bot_bankruptcy.append(False)

    def add_bot_balances(self, bot_balances):
        for balance in bot_balances:
            self.add_bots(balance)

    def get_data(self):
        return self.user_score, self.user_balance, self.dealer_balance, self.bot_balances

    def player_balance(self):
        print_green(f'Your balance is ${self.user_balance}\n')
        sleep(1)
        print_red(f'The dealers balance is ${self.dealer_balance}\n')
        sleep(1)

    def donation_from_bot(self): # random bot will donate
        bot_able_to = [c for c, v in enumerate(self.bot_balances) if v > 0] 
        bot_index = randint(0, len(bot_able_to))
        bot_donation_amount = self.bot_balances[bot_index] / 5
        self.user_balance += bot_donation_amount
        self.bot_balances[bot_index] -= bot_donation_amount
        print_green(f'Player{bot_index} has donated ${bot_donation_amount} to you.\n')
        sleep(1)

    def play_game(self):  # sourcery no-metrics
        while self.user_balance > 0:
            self.player_balance()

            # donate to bots only if they don't have any money
            for c, value in enumerate(self.bot_balances):
                if value <= 0:
                    self.bot_balances[c], self.user_balance = donate_to_bot(value, self.user_balance, f'Player{c}')

            for c, v in enumerate(self.bot_cards):
                self.bot_decisions(c)

            if self.bot_number:
                if self.user_balance <= 0 and max(self.bot_balances) <= 0:
                    print_red('All players are bankrupt! You Lost!')
                    sleep(2)
                    return # exits the game
                elif max(self.bot_balances) <= 0:  # only the bots are bankrupt
                    print_yellow('The fate of the game depends on you now!')
                    sleep(2)

            # get money from the bots
            if self.user_balance <= 0 and self.bot_number:
                print_red('You are currently out of money and cannot make a bet!')
                sleep(1)

                # ask for donations from bots
                donation_request = yes_or_no_choice('Would you like to request a donation from another player (yes / no): ')
                if donation_request:
                    if max(self.bot_balances) <= 0:
                        print_red('No other players were able to donate anything to you!')
                        sleep(1)
                    else:
                        self.donation_from_bot()
                # exit game as there is no money w/ player or w/ bots
                if not donation_request or max(self.bot_balances) <= 0:
                    print_green('Thanks for playing!')
                    sleep(1)
                    return

            if yes_or_no_choice("Would you like to go all in (yes / no): "):
                self.user_bet = self.user_balance
                sleep(.5)
            else:
                self.user_bet = money_transfer_input("How many dollars would you like to bet? ",self.user_balance, 'bet')

            # dealer gets cards
            self.dealer_cards = [randint(1, 11) for _ in range(2)]
            print_red(f'The Dealer has ? & {self.dealer_cards[1]}\n')
            sleep(1)

            # player gets cards
            self.user_cards = [randint(1, 11) for _ in range(2)]
            print_green(f'You have a total of {self._user_sum()} from {self.user_cards}\n')

            choice = ''
            while choice not in ['s', 'stay'] and self._user_sum() < 21 and len(self.user_cards) < 5:
                choice = str(
                    input("Do you want to hit, stay, double down, call for help, or quit the game (hit | stay | "
                          "double down | help | quit): "))
                print()
                sleep(1)

                if choice.lower() in ["hit", "h"]:
                    self.user_draws_card()
                elif choice.lower() in ['s', 'stay']:
                    self.dealers_turn()
                elif choice.lower() in ["d", "double", 'double down']:
                    if self._user_sum() <= 11:
                        print(
                            'You will now double down on your bets and pull only 1 more card and then you will stand for '
                            'this round!\n')
                        self.user_bet *= 2
                        sleep(1)
                        self.user_draws_card()
                        self.dealers_turn()
                    else:
                        print_red('You cannot double down here since the sum of your cards is over 11!')
                        sleep(1)
                elif choice.lower() in ["help", "help", 'call help']:
                    if self._user_sum() == [10, 11]:
                        print_blue("Since your total is equal to either 10 or 11, we recommend that this is the best time to double down if you have enough money!")
                        sleep(3)
                    elif self._user_sum() <= 14:
                        print_blue("Since your total is under or equal to 14, we recommend that you hit!")
                        sleep(2)
                    elif self._user_sum() >= 15:
                        print_blue("Your odds are looking high enough to win, if your card total is closer to 15, we recommend only making 1 hit move and then staying!\n")
                        sleep(3)
                        print_blue("If your card total is closer to 21, don't risk it! make a stay move!\n")
                        sleep(3)
                elif choice.lower() in ["q", "quit", "end"]:
                    print_green("Ending game... Thanks for playing!\n")
                    sleep(1)
                    return
                else:  # improper input 
                    user_error("User input incorrect please try again...\n")
                    continue
            # dealer's move
            while self._user_sum() == 21 and self._dealer_sum() < 15:
                self.dealer_draws_card()

            # Endgame results
            self.game_scoring()
            if self.end_round_notification():
                return

    def bot_decisions(self, value):
        if self.bot_balances[value] > 0:
            self.bot_bets[value] = randint(1, self.bot_balances[value])
            print_blue(f'Player{value + 1} decided to bet ${self.bot_bets[value]}\n')
            sleep(1)
        else:
            print_red(f'Player{value + 1} is bankrupt and not playing!')
            return

        self.bot_cards[value] = [randint(1, 11) for _ in range(2)]

        if self._bot_sum(value) > 15:
            print_blue(f'Player{value + 1} chooses to stay!\n')
            sleep(1)

        while self._bot_sum(value) <= 15 and len(self.bot_cards[value]) < 6:
            if len(self.bot_cards[value]) == 5:
                print_blue(f'Player{value + 1} has pulled a total of 5 cards without busting!\n')
            else:
                self.bot_cards[value].append(randint(1, 11))
                print_blue(f"Player{value + 1} has pulled a card...\n")
                sleep(1)
                print_blue(f"Player{value + 1} now has a total of {self._bot_sum(value)} from these cards {self.bot_cards[value]}\n")
                sleep(1)
                if self._bot_sum(value) > 21:
                    print_blue(f'Player{value + 1} has BUSTED!\n')
                elif self._bot_sum(value) > 15:
                    print_blue(f'Player{value + 1} will now stay!\n')
                sleep(1)

    def user_draws_card(self):
        """
        Used for whenever the player is required to draw a card
        """
        self.user_cards.append(randint(1, 11))
        print_green(f'You have a total of {self._user_sum()} from {self.user_cards}\n')
        sleep(1)

    def dealers_turn(self):
        """
        Handles all of the card pulling actions for the dealer
        """
        print_red('The Dealer says No More Bets!\n')
        sleep(.5)

        while self._dealer_sum() <= 15:
            if 11 in self.dealer_cards and not self.insurance_bought:
                if yes_or_no_choice('The dealer has an ace. Would you like to buy insurance (yes / no): '):
                    self.insurance_bought = True
                    insurance_amount = self.user_bet / 2
                    self.user_bet += insurance_amount
                else:
                    self.insurance_bought = False
                    print('Buying insurance has been skipped for you...\n')
                    sleep(1)

            self.dealer_draws_card()

    def _dealer_sum(self):  # helper function for returning the sum of dealer's cards
        return sum(self.dealer_cards)

    def _user_sum(self):  # helper function for returning the sum of user's cards
        return sum(self.user_cards)

    def _bot_sum(self, value):  # helper function for returning the sum of bot's cards
        return sum(self.bot_cards[value])


    def dealer_draws_card(self):
        """
        Allows the dealer to draw a card into their deck
        """
        if (len(self.dealer_cards) == 5 and self._dealer_sum() <= 21) or self._dealer_sum() > 15:
            return

        self.dealer_cards.append(randint(1, 11))
        print_red("The Dealer has pulled a card...\n")
        print_red(f'The Dealer now has {self._dealer_sum()} from these cards {self.dealer_cards}\n')
        sleep(1)

    def game_scoring(self):
        """
        Handles of the end game scoring based upon card results between the dealer and end-user
        """
        print_red(f'The Dealer has a grand total of {self._dealer_sum()} from these cards {self.dealer_cards}\n')
        sleep(1)
        print_green(f"You have a grand total of {self._user_sum()} with {self.user_cards}\n")
        sleep(1)

        if len(self.dealer_cards) == 5 and self._dealer_sum() <= self._user_sum() <= 21:
            print_yellow("PUSH! This is a tie! All bet money is refunded!")
        elif len(self.user_cards) == 5 and self._user_sum() <= self._dealer_sum() <= 21:
            print_yellow("PUSH! This is a tie! All bet money is refunded!")
        elif self._user_sum() == self._dealer_sum():
            print_yellow("PUSH! This is a tie! All bet money is refunded!")
        elif len(self.user_cards) == 5 and self._user_sum() < 21:
            sleep(1)
            print_green("You have automatically won since you have pulled a total of 5 cards without busting!\n")
            self.user_win_stats()
        elif len(self.dealer_cards) == 5 and self._dealer_sum() < 21:
            print_red("You have automatically lost since the dealer has pulled a total of 5 cards without busting!\n")
            sleep(1)
            self.user_loses_stats()
        elif self._user_sum() > 21:
            print_red(f"BUSTED! The Dealer Wins! You lost ${self.user_bet}!\n")
            self.user_loses_stats()
        elif self._dealer_sum() > 21:
            print_green(f"The Dealer BUSTED! You win! You won ${self.user_bet}!\n")
            self.user_win_stats()
        elif self._user_sum() == 21:
            print_green(f"BLACKJACK! You hit 21! You won ${self.user_bet}!\n")
            self.user_win_stats()
        elif self.insurance_bought and self._dealer_sum() == 21:
            print_yellow("BLACKJACK! Since you purchased insurance, you do not lose any money!")
            self.user_loses_stats(0)
            self.insurance_bought = False
        elif 11 in self.dealer_cards and self._dealer_sum() == 21:  # offered insurance - not used
            print_red(
                "BLACKJACK! Since you did not purchased insurance, you will lose 1.5 times your original bet!\n")
            self.user_loses_stats(1.5)
            self.insurance_bought = False
        elif self._dealer_sum() == 21:
            print_green(f"BLACKJACK! The Dealer hit 21! You Lost ${self.user_bet}!\n")
            self.user_loses_stats()
        elif self._user_sum() > self._dealer_sum():
            print_green(f"You Win! Your cards were greater than the dealers deck, You won ${self.user_bet}!\n")
            self.user_win_stats()
        elif self._dealer_sum() >= self._user_sum():
            print_red(f"The dealer wins! Your cards were less than the dealers deck, You lost ${self.user_bet}!\n")
            self.user_loses_stats()

        for c, balance in enumerate(self.bot_balances):
            if balance > 0:
                self.score_bot(c)

    def score_bot(self, i):
        bet, player_value, player_bal = self.bot_bets[i], self._bot_sum(value), self.bot_balances[i]
        dealer_value = self._dealer_sum()

        if len(self.dealer_cards) == 5 and player_value >= dealer_value:
            print_yellow(f"Player{value + 1} pushed this round! Player{i + 1}'s bet has been refunded!\n")
        elif len(self.bot_cards[i]) == 5 and dealer_value >= player_value:
            print_yellow(f"Player{i + 1} pushed this round! Player{i + 1}'s bet has been refunded!\n")
        elif player_value == dealer_value:
            print_yellow(f"Player{i + 1} pushed this round! Player{i + 1}'s bet has been refunded!\n")
        elif len(self.bot_cards[i]) == 5 and player_value < 21:
            self.bot_balances[i], self.dealer_balance = _win_bet(bet, player_bal, self.dealer_balance)
            print_green(f'Player{i + 1} won this round! Player{i + 1} won ${player_bet}\n')
        elif len(self.dealer_cards) == 5 and dealer_value < 21:
            self.bot_balances[i], self.dealer_balance = _lose_bet(bet, player_bal, self.dealer_balance)
            print_red(f'Player{i + 1} lost this round! Player{i + 1} lost ${player_bet}')
        elif player_value > 21:
            self.bot_balances[i], self.dealer_balance = _lose_bet(bet, player_bal, self.dealer_balance)
            print_red(f'Player{i + 1} lost this round! Player{i + 1} lost ${player_bet}\n')
        elif dealer_value > 21:
            self.bot_balances[i], self.dealer_balance = _win_bet(bet, player_bal, self.dealer_balance)
            print_green(f'Player{i + 1} won this round! Player{i + 1} won ${player_bet}\n')
        elif player_value == 21:
            self.bot_balances[i], self.dealer_balance = _win_bet(bet, player_bal, self.dealer_balance)
            print_green(f'Player{i + 1} won this round! Player{i + 1} won ${player_bet}\n')
        elif player_value < dealer_value:
            self.bot_balances[i], self.dealer_balance = _lose_bet(bet, player_bal, self.dealer_balance)
            print_red(f'Player{i + 1} lost this round! Player{i + 1} lost ${player_bet}\n')
        elif player_value > dealer_value:
            self.bot_balances[i], self.dealer_balance = _win_bet(bet, player_bal, self.dealer_balance)
            print_green(f'Player{i + 1} won this round! Player{i + 1} won ${player_bet}\n')

        sleep(1)
        print_blue(f'Player{i + 1} now has a balance of ${self.bot_balances[i]}\n')

    def end_round_notification(self):
        """
    Used when 1 single round of blackjack has ended. Allows the user to play another game of blackjack or quit playing
        """
        print_green(f"You have won {self.user_score} hands\n")
        
        if self.user_balance <= 0 and len(self.bot_balances) == 0:
            print_red("You don't have any more money to bet... Game Over!")
            sleep(2)
        elif self.dealer_balance <= 0:
            print_green("Congratulations! You have beat the BlackJack 21 game by defeating the dealers balance!")
        elif self.dealer_balance <= self.user_balance / 5:
            print_green("The dealers balance is looking small enough for you to win! You're doing well...")
        elif yes_or_no_choice('Would you like to continue (yes / no)'):
            return False
        else:  # exit / cash out / new game
            load_or_save_game(save_game=self)
        return True


    def user_loses_stats(self, multiplier=1.0):
        """
        Update stats when the user loses the round
        """
        sleep(1)
        self.user_score -= 1
        self.user_balance -= (self.user_bet * multiplier)
        self.dealer_balance += (self.user_bet * multiplier)

    def user_win_stats(self, multiplier=1.0):
        """
        Update stats when the user wins the round
        """
        sleep(1)
        self.user_score += 1
        self.user_balance += (self.user_bet * multiplier)
        self.dealer_balance -= (self.user_bet * multiplier)


# MAIN MENU

def yes_or_no_choice(input_text):
    """
To prompt users to fix their mistakes in a yes/no question
    """
    while (text_choice := str(input(input_text)).lower()) not in ['n', 'no', 'nope', 'nah']:
        print()
        if text_choice in ['y', 'yes', 'ya', 'yah', 'sure']:
            return True
        else:  # prompt user to fix mistake made
            user_error("Invalid choice, please say either 'yes' or 'no'\n")
    print()
    return False

def game(user_balance=1000, user_score=0, dealer_balance=5000, players=0, bot_balances=[]):
    """
This is the main code used for the game entirely
    """
    single_player = Blackjack(user_balance, user_score, dealer_balance)
    if bot_balances:
        single_player.add_bot_balances(bot_balances)
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
        sleep(.5)
        if player_num == 1:
            print_green(f'{player_num} bot will be added into the game!\n')
        elif 1 < player_num < 4:
            print_green(f'{player_num} bots will be added into the game!\n')
        else:  # if num is not correct, user retries their selection
            user_error('Number of players incorrect. Choose between 1 to 3 players...\n')
            continue
        return player_num


def custom_user_input(user_message, result=0):  # helper function for custom_game_setup()
    """
Used for taking in an argument while a custom game is being set up
    """
    while result <= 0:
        try:
            result = int(input(user_message))
        except ValueError:
            print_red('Please enter a number.')
            continue
        print()
        sleep(.5)
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
    return user_balance, user_score, dealer_balance


def game_options():
    """
Allows the end-user to be able to play the game with custom money, win counts, and more
    """
    if yes_or_no_choice('Would you like to play music while playing (yes / no): '):
        while True:
            choice = str(input('YouTube Music or Spotify Music? '))
            print()
            if choice.lower() in ['youtube', 'y', 'youtube music']:
                webbrowser.open('https://music.youtube.com/')
            elif choice.lower() in ['spotify', 's', 'spotify music']:
                webbrowser.open('https://open.spotify.com/')
            else:
                print_red('Option not available. Please try again ...\n')
                continue
            break

    while True:
        game_choice = str(input('Would you like to play solo Blackjack, Blackjack with bots, '
                                'or a Custom Game with custom user game settings (blackjack / bots / custom): '))
        print()
        sleep(.5)

        if game_choice.lower() in ['b', 'blackjack', 'blackjack 21', 'black jack', 'n', 'normal', 's', 'solo']:
            game()
        elif game_choice.lower() in ['blackjack with bots', 'blackjack 21 with bots', 'bots', 'bot', 'bo', '1']:
            game(players=bot_player_choice())
        elif game_choice.lower() in ['c', 'custom', 'custom game', 'custom blackjack', 'custom blackjack game']:
            game(*custom_game_setup())
        else:
            user_error("User game selection incorrect please try again....")


def main():
    """
The first piece of the program introduced to the end-user. This section allows the user to 
skip around in the game by using the game mode selection choices
    """
    while True:
        choice = input('Start / Tutorial / Express / Load Game / View Stats / Extras / Quit: ')
        print()
        sleep(.5)

        if choice.lower() in ['start', 'yes', 's']:
            game_options()
        elif choice.lower() in ['no', 'n', 't', 'tutorial']:
            print_green('A youtube video should now be playing... This game will auto resume once the video has been fully played...')
            webbrowser.open("https://www.youtube.com/watch?v=eyoh-Ku9TCI", new=1)
            sleep(140)
            game()
        elif choice.lower() in ['e', 'express']:
            game()
        elif choice.lower() in ['stats', 'view stats', 'v', 'view']:
            view_stats()  # update stats to be more like hands won and total money gained
        elif choice.lower() in ['load', 'load game', 'l']:
            game(*load_or_save_game())
        elif choice.lower() in ['extra', 'extras']:
            extra()
        elif choice.lower() in ['quit', 'q', 'exit']:
            sys.exit()
        else:
            user_error("User input incorrect please try again...\n")


if __name__ == '__main__':
    main()
