#!/usr/bin/python3

# Created by Jordan Leich on 6/6/2020
# Edited by Adam Smith
import json
from os import path
from random import randint
from time import sleep

# from files
from other.colors import print_green, print_red, print_yellow, print_blue

'''
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

Player1 = Player(5, 0, False, False, None, 1000, False, False, None)
Player2 = Player(5, 0, False, False, None, 1000, False, False, None)
Player3 = Player(5, 0, False, False, None, 1000, False, False, None)
Player4 = Player(5, 0, False, False, None, 1000, False, False, None)
Player5 = Player(5, 0, False, False, None, 1000, False, False, None)
Dealer = Player(0, 0, True, False, None, 2000000, False, True, None)
Player6 = Player(5, 0, False, False, None, 1000, True, False, None)
Player7 = Player(5, 0, False, False, None, 1000, True, False, None)
PLayer8 = Player(5, 0, False, False, None, 1000, True, False, None)
Player9 = Player(5, 0, False, False, None, 1000, True, False, None)
Player10 = Player(5, 0, False, False, None, 1000, True, False, None)
decks = Decks()
decks.shoe_build(4)
decks.deck_shuffle()


def display_table(dealer_turn=1):
    """This function is to create a text based table """
    print("Player1 Cards: " + str(Player1.cards) + "Cards sum: ", Player1.sum_of_cards())
    print("Dealer Cards: " + str(Dealer.cards[0]) + " + [?]", "Cards sum: ", Dealer.sum_of_cards(True))

    print('-' * 12 + 'Dealer' + '-' * 12)
    print('------------------------------')
    card_line = []
    for i in Dealer.cards:
        if len(i) > 2:
            card_line.append('[' + str(i) + ']')
        else:
            card_line.append('[ ' + str(i) + ']')
    if dealer_turn == 1:
        print('-' * 10 + str(card_line[0]) + '[ ? ]' + '-' * 10)
    else:
        print('-' * 10 + str(card_line[0]) + str(card_line[1]) + '-' * 10)


def game():
    """This is the main game function. It will deal with single player
    and multiple players. """
    Player1.presence = True
    Player1.table_spot = 1
    print_green("Game Starting")
    # Using while loop to cycle through all the players and dealer
    # finished_game = False # TODO: finish this line and line below.
    # while not finished_game:

    for _ in range(2):
        if Player1.presence:
            Player1.cards.append(decks.next_card())
        if Dealer.presence:
            Dealer.cards.append(decks.next_card())
    print()
    display_table()
    display_table(2)

    user_knowledge = input("Which choice would you like to pick:  ")
    print()
    Player1.cards = []
    Dealer.cards = []
'''


def load_or_save_game(save_game=None, stats=False):
    # save_game = class instance (i.e. save_game=self)
    """
    loads the game only when Load Game feature used
    """
    user_score, user_balance, dealer_balance, bot_number = 0, 1000, 5000, 0
    bot_balances = []

    if not save_game and path.exists("data.json"):
        with open('data.json', 'r') as user_data_file:
            user_data = json.load(user_data_file)
        user_score = user_data['score']
        user_balance = user_data['balance']
        dealer_balance = user_data['deal_balance']
        bot_balances = user_data['bot_balances']
        if not stats:
            print_green('Save file loaded!\n')
    elif not save_game:
        if not stats:
            print_yellow('Save file not found, A new save file will be created shortly!\n')
            sleep(1)
        default_stats = {'balance': user_balance,
                         'score': user_score,
                         'deal_balance': dealer_balance,
                         'bot_balances': bot_balances,
                         }
        with open('data.json', 'w') as user_data_file:
            json.dump(default_stats, user_data_file)
    else:
        user_score, user_balance, dealer_balance, bot_balances = save_game.get_data()
        print_yellow('Saving game... Please do not exit the program!\n')
        default_stats = {'balance': user_balance,
                         'score': user_score,
                         'deal_balance': dealer_balance,
                         'bot_balances': bot_balances,
                         }
        with open('data.json', 'w') as user_data_file:
            json.dump(default_stats, user_data_file)
    return user_balance, user_score, dealer_balance, bot_number, bot_balances


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

    def print_user_dealer_balance(self):
        print_green(f'Your balance is ${self.user_balance}\n')
        sleep(1)
        print_red(f'The dealers balance is ${self.dealer_balance}\n')
        sleep(1)

    def donation_from_bot(self):  # random bot will donate
        bot_able_to = [c for c, v in enumerate(self.bot_balances) if v > 0]
        bot_index = randint(0, len(bot_able_to))
        bot_donation_amount = self.bot_balances[bot_index] / 5
        self.user_balance += bot_donation_amount
        self.bot_balances[bot_index] -= bot_donation_amount
        print_green(f'Player{bot_index} has donated ${bot_donation_amount} to you.\n')
        sleep(1)

    def play_game(self):  # sourcery no-metrics
        while self.user_balance > 0:
            self.print_user_dealer_balance()

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
                    return  # exits the game
                elif max(self.bot_balances) <= 0:  # only the bots are bankrupt
                    print_yellow('The fate of the game depends on you now!')
                    sleep(2)

            # get money from the bots
            if self.user_balance <= 0 and self.bot_number:
                print_red('You are currently out of money and cannot make a bet!')
                sleep(1)

                # ask for donations from bots
                donation_request = yes_or_no_choice(
                    'Would you like to request a donation from another player (yes / no): ')
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
                self.user_bet = money_transfer_input("How many dollars would you like to bet? ", self.user_balance,
                                                     'bet')

            # dealer gets cards
            self.dealer_cards = [randint(1, 11) for _ in range(2)]
            print_red(f'The Dealer has ? & {self.dealer_cards[1]}\n')
            sleep(1)

            # player gets cards
            self.user_cards = [randint(1, 11) for _ in range(2)]
            print_green(f'You have a total of {self._user_sum()} from {self.user_cards}\n')
            sleep(1)

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
                        print_blue(
                            "Since your total is equal to either 10 or 11, we recommend that this is the best time to double down if you have enough money!")
                        sleep(3)
                    elif self._user_sum() <= 14:
                        print_blue("Since your total is under or equal to 14, we recommend that you hit!")
                        sleep(2)
                    elif self._user_sum() >= 15:
                        print_blue(
                            "Your odds are looking high enough to win, if your card total is closer to 15, we recommend only making 1 hit move and then staying!\n")
                        sleep(3)
                        print_blue("If your card total is closer to 21, don't risk it! make a stay move!\n")
                        sleep(3)
                elif choice.lower() in ["q", "quit", "end"]:
                    print_green("Ending game... Thanks for playing!\n")
                    sleep(1)
                    return
                else:  # improper input 
                    print_red("User input incorrect please try again...\n")
                    sleep(1)
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
                print_blue(
                    f"Player{value + 1} now has a total of {self._bot_sum(value)} from these cards {self.bot_cards[value]}\n")
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

        while self._dealer_sum() <= 15 and len(self.dealer_cards) <= 5:
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

    def _bot_sum(self, value):  # helper function for returning the sum of bots cards
        return sum(self.bot_cards[value])

    def dealer_draws_card(self):
        """
        Allows the dealer to draw a card into their deck
        """
        if (len(self.dealer_cards) == 5 and self._dealer_sum() <= 21) or self._dealer_sum() > 15:
            return

        self.dealer_cards.append(randint(1, 11))
        print_red("The Dealer has pulled a card...\n")
        sleep(1)
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
        bet, player_value, player_balance = self.bot_bets[i], self._bot_sum(i), self.bot_balances[i]
        dealer_value = self._dealer_sum()

        if len(self.dealer_cards) == 5 and player_value >= dealer_value:
            print_yellow(f"Player{value + 1} pushed this round! Player{i + 1}'s bet has been refunded!\n")
        elif len(self.bot_cards[i]) == 5 and dealer_value >= player_value:
            print_yellow(f"Player{i + 1} pushed this round! Player{i + 1}'s bet has been refunded!\n")
        elif player_value == dealer_value:
            print_yellow(f"Player{i + 1} pushed this round! Player{i + 1}'s bet has been refunded!\n")
        elif len(self.bot_cards[i]) == 5 and player_value < 21:
            self.bot_balances[i], self.dealer_balance = _win_bet(bet, player_balance, self.dealer_balance)
            print_green(f'Player{i + 1} won this round! Player{i + 1} won ${bet}\n')
        elif len(self.dealer_cards) == 5 and dealer_value < 21:
            self.bot_balances[i], self.dealer_balance = _lose_bet(bet, player_balance, self.dealer_balance)
            print_red(f'Player{i + 1} lost this round! Player{i + 1} lost ${bet}')
        elif player_value > 21:
            self.bot_balances[i], self.dealer_balance = _lose_bet(bet, player_balance, self.dealer_balance)
            print_red(f'Player{i + 1} lost this round! Player{i + 1} lost ${bet}\n')
        elif dealer_value > 21:
            self.bot_balances[i], self.dealer_balance = _win_bet(bet, player_balance, self.dealer_balance)
            print_green(f'Player{i + 1} won this round! Player{i + 1} won ${bet}\n')
        elif player_value == 21:
            self.bot_balances[i], self.dealer_balance = _win_bet(bet, player_balance, self.dealer_balance)
            print_green(f'Player{i + 1} won this round! Player{i + 1} won ${bet}\n')
        elif player_value < dealer_value:
            self.bot_balances[i], self.dealer_balance = _lose_bet(bet, player_balance, self.dealer_balance)
            print_red(f'Player{i + 1} lost this round! Player{i + 1} lost ${bet}\n')
        elif player_value > dealer_value:
            self.bot_balances[i], self.dealer_balance = _win_bet(bet, player_balance, self.dealer_balance)
            print_green(f'Player{i + 1} won this round! Player{i + 1} won ${bet}\n')

        sleep(1)
        print_blue(f'Player{i + 1} now has a balance of ${self.bot_balances[i]}\n')

    def end_round_notification(self):
        """
    Used when 1 single round of blackjack has ended. Allows the user to play another game of blackjack or quit playing
        """
        print_green(f"You have won {self.user_score} hands\n")
        sleep(1)

        if self.user_balance <= 0 and len(self.bot_balances) == 0:
            print_red("You don't have any more money to bet... Game Over!")
            sleep(2)
        elif self.dealer_balance <= 0:
            print_green("Congratulations! You have beat the BlackJack 21 game by defeating the dealers balance!")
        elif self.dealer_balance <= self.user_balance / 5:
            print_green("The dealers balance is looking small enough for you to win! You're doing well...")
        elif yes_or_no_choice('Would you like to continue (yes / no): '):
            sleep(1)
            return False
        else:  # exit / cash out / new game
            load_or_save_game(save_game=self)
        return True

    def user_loses_stats(self, multiplier=1.0):
        """
        Update stats when the user loses the round
        """
        self.user_score -= 1
        self.user_balance -= (self.user_bet * multiplier)
        self.dealer_balance += (self.user_bet * multiplier)

    def user_win_stats(self, multiplier=1.0):
        """
        Update stats when the user wins the round
        """
        self.user_score += 1
        self.user_balance += (self.user_bet * multiplier)
        self.dealer_balance -= (self.user_bet * multiplier)


def yes_or_no_choice(input_text):
    """
To prompt users to fix their mistakes in a yes/no question
    """
    while (text_choice := str(input(input_text)).lower()) not in ['n', 'no', 'nope', 'nah']:
        print()
        if text_choice in ['y', 'yes', 'ya', 'yah', 'sure']:
            return True
        print_red("Invalid choice, please say either 'yes' or 'no'\n")
        sleep(1)
    return False
