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

# from files
from other import colors
from os import path
from decks import Decks
from player import Player

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
    print("Game Starting")
    # Using while loop to cycle through all the players and dealer
    finished_game = False
    while !finished_game:
        
    for i in range(2):
        if Player1.presence:
            Player1.cards.append(decks.next_card())
        if Dealer.presence:
            Dealer.cards.append(decks.next_card())
    print()
    display_table()
    display_table(2)

    user_knowledge = input("? ")
    Player1.cards = []
    Dealer.cards = []


def new_game_menu():
    """This menu is to see if the player wants to play by their self
    or add players. there can be 5 extra players added. whether its bots
    or players the main person had to decide for. Each of the menus 
    will revert back to the previous menu it come from so there cant be
    any accidental exits before saves or loading games. """
    while True:
        os.system('cls')
        print(colors.green + "Welcome Player! Thank you for Joining Us\n" 
                             "Here at the BlackJack Game\n" + colors.reset)
        print("(1) Would you be Playing alone?")
        print("(2) Would you like to play with others?")
        print("(3) Or go back to the main menu?")
        user_knowledge = input("? ")
        if user_knowledge not in ['1', '2', '3']:
            print(colors.red + user_knowledge + " Is Not a valid input" + colors.reset + "\n")
            time.sleep(1)
        elif user_knowledge == '1':
            game()
        elif user_knowledge == '2':
            pass
        elif user_knowledge == '3':
            os.system('cls')
            return


def main():
    """
Used as the first piece of the program introduced to the end-user. This section allows the user to skip around in the
game by using the game mode selection choices
    """
    while True:
        # Main Start menu
        # did the print command to make the alignment easier to work with
        os.system('cls')
        print("Welcome to BlackJack")
        print("(1) New Game")
        print("(2) Load Existing Game")
        print("(3) Options")
        print("(4) Quit")
        user_knowledge = input("? ")

        print()
        time.sleep(.5)

        if user_knowledge not in ['1', '2', '3', '4']:
            print(colors.red + "Input error. Please select a number from 1 - 4" + colors.reset)

        elif user_knowledge == '1':
            # print(colors.blue + "Welcome Player! we are headed to the New Game Menu" + colors.reset)
            new_game_menu()

        elif user_knowledge == '2':
            print(colors.blue + "Loading into the previous game." + colors.reset)

        elif user_knowledge == '3':
            print(colors.blue + "Heading to the Options Menu." + colors.reset)

        elif user_knowledge == '4':
            print(colors.green + "Exiting the Game" + colors.reset)
            sys.exit()


if __name__ == '__main__':
    main()
