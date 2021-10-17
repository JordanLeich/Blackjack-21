#!/usr/bin/python3

# Created by Jordan Leich on 6/6/2020
# Edited by Adam Smith

from time import sleep
import webbrowser
import json
import sys
import os
from os import path

# from files
from other.colors import print_green, print_red, print_yellow, print_blue
from blackjack import Blackjack


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


def open_github(print_text, website_append=''):
    """
    Open github in the users default web browser
    """
    print_green(print_text)
    webbrowser.open_new(f'https://github.com/JordanLeich/Blackjack-21{website_append}')
    sleep(1)


def donation_opener(website):
    """
    Open a donation page in the users default web browser
    """
    print_green("Opening PayPal Donation page...\n")
    webbrowser.open_new(website)
    sleep(2)


def extra():
    """
Main hub UI for the user to view additional information or extra parts of this project such as donations and releases
    """
    while True:
        print("(1) View Stats")
        print("(2) Project Releases")
        print("(3) Credits")
        print("(4) Donate")
        print("(5) Main Menu\n")
        choice = input("Which choice would you like to pick:  ")
        print()
        sleep(.5)

        if choice == '1':
            view_stats()  # update stats to be more like hands won and total money gained
        elif choice == '2':
            open_github("Opening the latest stable release...\n", "/releases")
        elif choice == '3':
            open_github("Opening all contributors of this project...\n", "/graphs/contributors")
        elif choice == '4':
            donation_opener("https://www.paypal.com/donate/?business=8FGHU8Z4EJPME&no_recurring=0&currency_code=USD")
        elif choice == '5':
            os.system('clear')
            return
        else:
            print_red("Please select a number from 1 - 5.\n")


def view_stats():  # prints your stats based off the load file
    user_balance, user_score, dealer_balance, _, bot_balances = load_or_save_game(stats=True)
    print_green('Your current in game stats will now be displayed below!\n\n')
    sleep(1)
    print(f'Your balance is ${user_balance}')
    print(f'Your win count is {user_score}')
    print(f'The dealers balance is ${dealer_balance}\n')
    for c, v in enumerate(bot_balances):
        print(f"Player{c}'s balance is ${v}")
    sleep(6)


def game(user_balance=1000, user_score=0, dealer_balance=5000, players=0, bot_balances=[]):
    """
    Main code used for the game entirely
    """
    single_player = Blackjack(user_balance, user_score, dealer_balance)
    if bot_balances:
        single_player.add_bot_balances(bot_balances)
    for _ in range(players):
        single_player.add_bots()
    single_player.play_game()


def bot_player_choice():
    """
    User chooses how many bots to play with
    """
    while True:
        player_num = int(input('How many bots would you like to play with: '))
        print()
        sleep(.5)
        get_plural = 'bot' if player_num == 1 else 'bots'
        print_green(f'{player_num} {get_plural} will be added into the game!\n')
        sleep(1)
        return player_num


def custom_user_input(user_message, result=0):
    """
    helper function for custom_game_setup() - validates that user input is a number greater than 0
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


def custom_game_setup():
    """
    Set up a custom game
    """
    user_balance = custom_user_input('How much money would you like to start with: ')
    dealer_balance = custom_user_input('How much money would you like the dealer to start with: ')
    user_score = custom_user_input('How much would you like to set your scoring count to: ')
    return user_balance, user_score, dealer_balance


def game_options():
    """
Allows the end-user to be able to play the game with custom money, win counts, and more
    """
    while True:
        print("(1) Play alone")
        print("(2) Play with bots")
        print("(3) Play with custom settings")
        print("(4) Tutorial")
        print("(5) Main menu")
        print("(6) Exit\n")
        game_choice = input("Which choice would you like to pick:  ")
        print()
        sleep(.5)

        if game_choice == '1':
            game()
        elif game_choice == '2':
            game(players=bot_player_choice())
        elif game_choice == '3':
            game(*custom_game_setup())
        elif game_choice == '4':
            print_green('A youtube video should now be playing... ')
            webbrowser.open("https://www.youtube.com/watch?v=eyoh-Ku9TCI", new=1)
        elif game_choice == '5':
            return
        elif game_choice == '6':
            sys.exit()
        else:
            print_red("Please select a number from 1 - 6.\n")


def main():
    while True:
        print_green("Welcome to BlackJack 21\n")
        print("(1) New Game")  # tutorial
        print("(2) Load Existing Game")
        print("(3) Options")  # view stats, extras, releases, donate
        print("(4) Quit\n")

        choice = input('Which choice would you like to pick:  ')
        print()
        sleep(.5)

        if choice == '1':
            print_blue("Welcome Player!\n")
            game_options()
        elif choice == '2':
            game(*load_or_save_game())
        elif choice == '3':
            extra()
        elif choice == '4':
            print_green("Exiting the Game")
            sys.exit()
        else:
            print_red("Please select a number from 1 - 4.\n")


if __name__ == '__main__':
    main()
