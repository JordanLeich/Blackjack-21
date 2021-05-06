#!/usr/bin/python3

# Made by Jordan Leich on 6/6/2020, Last updated on 5/6/2021

# Imports
import random
import time
import colors
from playsound import playsound

# Global Variables
user_score = 0
user_balance = 1000
dealer_balance = 5000
user_bet = 0


def another_game():
    """
    Used when 1 single round of blackjack has ended. Allows the user to play another game of blackjack or quit playing
    """
    global user_score, user_balance, dealer_balance
    print(colors.green + "Your win count is", user_score, "and your total balance is $" + str(user_balance), "\n",
          colors.reset)
    time.sleep(1)
    print(colors.red + "The dealers total balance is $" + str(dealer_balance), "\n", colors.reset)
    time.sleep(2)

    if user_balance <= 0:
        print(colors.red + "You don't have any more money to bet! Game Over!\n", colors.reset)
        time.sleep(2)
        quit()
    elif user_balance >= 1:

        if dealer_balance <= 0:
            print(colors.green + "Congratulations! You have beat BlackJack 21 by defeating the dealers balance!\n",
                  colors.reset)
            time.sleep(2)
        elif dealer_balance <= 2500:
            print(colors.green + "The dealers balance is looking small enough for you to win! Your doing well...\n",
                  colors.reset)
            time.sleep(2)
        restart_action = input(
            "Do you want to play again or cash out your earning (yes | no): ")
        print()
        time.sleep(1)
        if restart_action.lower() == "yes" or restart_action.lower() == "y":
            restart()
        elif restart_action.lower() == "no" or restart_action.lower() == "n":
            print(colors.green + "You earned a total of $" + str(user_balance) + str(". Thanks for playing!\n"),
                  colors.reset)
            time.sleep(1)
            quit()
        else:
            print(colors.red + "Invalid input... Restarting choice...\n", colors.reset)
            time.sleep(1)
            another_game()
    else:
        print("User Balance Error...\n")
        time.sleep(1)
        quit()


def restart():
    """
    This restarts the program no matter what if executed
    """
    global user_score
    print("Restarting Blackjack Game...\n")
    time.sleep(1)
    game()


def game():
    """
    This is the main code used for the game entirely
    """
    global user_score, user_balance, user_bet, dealer_balance
    # Dealer cards
    dealer_cards = []
    # Player cards
    player_cards = []

    print(colors.green + "Your balance is $" + str(user_balance), "\n", colors.reset)
    time.sleep(1)
    print(colors.red + "The dealers balance is $" + str(dealer_balance), "\n", colors.reset)
    time.sleep(1)

    user_all = str(input("Would you like to go all in (yes / no): "))

    if user_all.lower() == "y" or user_all.lower() == "yes":
        user_bet = user_balance
    else:
        print()
        user_bet = int(input("How much would you like to bet? "))
        time.sleep(1)
    if user_bet > user_balance:
        print()
        print(colors.red + "Your total balance cannot make this bet! Your bet is too high for your balance!\n",
              colors.reset)
        time.sleep(2)
        game()
    if user_bet <= 0:
        print()
        print(colors.red + "You cannot make a negative bet! Please place a higher bet than 0!\n",
              colors.reset)
        time.sleep(2)
        game()
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print()
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
    if sum(dealer_cards) == 21:
        print(colors.red + "Dealer has 21 and wins!\n", colors.reset)
        time.sleep(1)
        user_score -= 1
        user_balance = user_balance - user_bet
        dealer_balance = dealer_balance + user_bet
        another_game()
    elif sum(dealer_cards) > 21:
        print(colors.green + "Dealer has busted!\n", colors.reset)
        time.sleep(1)
        user_score += 1
        user_balance += user_bet
        dealer_balance -= user_bet
        another_game()
    # Total of Player cards
    while sum(player_cards) < 21:
        action_taken = str(
            input("Do you want to hit, stay, call help, change song, or quit the game (hit | stay | help | song | quit)"
                  ": "))
        print()
        time.sleep(1)

        if len(player_cards) >= 5 and sum(player_cards) < 21:
            time.sleep(0.500)
            print(colors.green + "You have automatically won since you have pulled a total of 5 cards without busting!"
                                 "\n", colors.reset)
            time.sleep(0.500)
            user_score += 1
            user_balance = user_balance + user_bet
            dealer_balance -= user_bet
            another_game()
        if action_taken.lower() == "hit" or action_taken.lower() == "h":
            player_cards.append(random.randint(1, 11))
            print(colors.green + "You now have a total of " + str(sum(player_cards)) + " from these cards",
                  player_cards,
                  colors.reset, "\n")
            time.sleep(1)
        elif action_taken.lower() == "help" or action_taken.lower() == "Help":
            if sum(player_cards) <= 14:
                print(colors.blue + "Since your total is under or equal to a total of 14, we recommend that you hit!\n",
                      colors.reset, )
                time.sleep(1)
            elif sum(player_cards) >= 15:
                print(colors.blue + "Your odds are looking high enough to win, if your card total is closer to 15, "
                                    "we recommend only making 1 hit move and then staying!\n", colors.reset)
                time.sleep(3)
                print(colors.blue + "If your card total is closer to 21, don't risk it! make a stay move!\n",
                      colors.reset)
                time.sleep(3)
            else:
                print(colors.red + "Helping Error Found...\n", colors.reset)
                time.sleep(1)
                quit()
        elif action_taken.lower() == "song" or action_taken.lower() == "change song":
            print("Loading track change...\n")
            time.sleep(1)
            songs()
        elif action_taken.lower() == "q" or action_taken.lower() == "quit" or action_taken.lower() == "end":
            print(colors.green + "Ending game... Thanks for playing!\n", colors.reset)
            time.sleep(1)
            quit()
        elif sum(dealer_cards) <= 15:
            dealer_cards.append(random.randint(1, 11))
            print(colors.red + "The Dealer has pulled a card...\n", colors.reset)
            time.sleep(1)

            if len(dealer_cards) >= 5 and sum(dealer_cards) < 21:
                print(colors.red + "The Dealer has a new total of", str(sum(dealer_cards)), "from these cards",
                      dealer_cards, colors.reset, "\n")
                time.sleep(0.500)
                print(colors.red + "You have automatically lost since the dealer has pulled a total of 5 cards without "
                                   "busting!\n", colors.reset)
                time.sleep(0.500)
                user_score -= 1
                user_balance = user_balance - user_bet
                dealer_balance += user_bet
                another_game()
        else:
            print(colors.red + "The Dealer has a new total of", str(sum(dealer_cards)), "from these cards",
                  dealer_cards, colors.reset, "\n")
            time.sleep(1)
            print(colors.green + "You have a grand total of " + str(sum(player_cards)) + " with", player_cards,
                  colors.reset, "\n")
            time.sleep(1)

            if sum(dealer_cards) > 21:
                print(colors.green + "The Dealer BUSTED! You win! You won $" + str(user_bet) + "!\n", colors.reset)
                time.sleep(1)
                user_score += 1
                user_balance = user_balance + user_bet
                dealer_balance -= user_bet
                another_game()
            elif sum(dealer_cards) > sum(player_cards):
                print(colors.red + "The dealer wins! You lost $" + str(user_bet) + "!\n", colors.reset)
                time.sleep(1)
                user_score -= 1
                user_balance = user_balance - user_bet
                dealer_balance += user_bet
                another_game()
            elif sum(dealer_cards) == 21:
                print(colors.red + "BLACKJACK! The Dealer hit 21! You lost $" + str(user_bet) + "!\n", colors.reset)
                time.sleep(1)
                user_score -= 1
                user_balance = user_balance - user_bet
                dealer_balance += user_bet
                another_game()
            elif sum(dealer_cards) == sum(player_cards):
                print(colors.yellow + "PUSH! This is a tie!", colors.reset, "\n")
                time.sleep(1)
                another_game()
            elif sum(player_cards) > sum(dealer_cards):
                print(colors.green + "You Win! You won $" + str(user_bet) + "!\n", colors.reset)
                time.sleep(1)
                user_score += 1
                user_balance = user_balance + user_bet
                dealer_balance -= user_bet
                another_game()
            else:
                print(colors.red + "Scoring Error Found...", colors.reset, "\n")
                time.sleep(1)
                another_game()
    # Endgame results
    if sum(player_cards) > 21:
        print(colors.red + "BUSTED! The Dealer Wins! You lost $" + str(user_bet) + "!\n", colors.reset)
        time.sleep(1)
        user_score -= 1
        user_balance = user_balance - user_bet
        dealer_balance += user_bet
        another_game()
    elif sum(dealer_cards) > 21:
        print(colors.green + "The Dealer BUSTED! You win! You won $" + str(user_bet) + "!\n", colors.reset)
        time.sleep(1)
        user_score += 1
        user_balance = user_balance + user_bet
        dealer_balance -= user_bet
        another_game()
    elif sum(player_cards) == 21:
        print(colors.green + "BLACKJACK! You hit 21! You won $" + str(user_bet) + "!\n", colors.reset)
        time.sleep(1)
        user_score += 1
        user_balance = user_balance + user_bet
        dealer_balance -= user_bet
        another_game()
    elif sum(dealer_cards) == 21:
        print(colors.red + "BLACKJACK! The Dealer hit 21! You lost $" + str(user_bet) + "!\n", colors.reset)
        time.sleep(1)
        user_score -= 1
        user_balance = user_balance - user_bet
        dealer_balance += user_bet
        another_game()
    elif sum(player_cards) == sum(dealer_cards):
        print(colors.yellow + "PUSH! This is a tie!", colors.reset, "\n")
        time.sleep(1)
        another_game()


def songs():
    """
    Used for the user to able to play songs while playing blackjack
    """
    song_input = str(input("Would you like to play songs from our track list while playing (yes / no): "))
    print()

    if song_input.lower() == "y" or song_input.lower() == "yes":
        song_list = int(
            input("""1. Relax Instrumental
2. Anile - Wish List
3. Exit song selection
Which song would you like to play: """))
        print()

        if song_list == 1:
            playsound("songs\\Relax.mp3", False)
            print("Now proceeding to BlackJack 21!\n")
            time.sleep(1)
            game()
        elif song_list == 2:
            playsound("songs\\Anile - Wish List.mp3", False)
            print("Now proceeding to BlackJack 21!\n")
            time.sleep(1)
            game()
        elif song_list == 3:
            print("Exiting song list and proceeding to BlackJack 21!\n")
            time.sleep(1)
            game()
        else:
            print(colors.red + "Song input from track list error found!\n", colors.reset)
            songs()
    elif song_input.lower() == "n" or song_input.lower() == "no":
        print("No song has been selected! Proceeding to BlackJack 21!\n")
        time.sleep(1)
        game()
    else:
        print(colors.red + "Song input error found!\n", colors.reset)
        time.sleep(1)
        songs()


def intro():
    print(colors.green + 'Hello there! Welcome to Blackjack 21, made by Jordan Leich!\n', colors.reset)
    time.sleep(.500)
    print(colors.yellow + "The goal of this game is to make the dealer go broke! Achieve this by placing your bets and "
                          "dealing your cards wisely, but carefully...\n", colors.reset)
    time.sleep(2)
    songs()


intro()
