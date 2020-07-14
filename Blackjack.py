# Made by Jordan Leich on 6/6/2020, Last updated on 7/13/2020

# Imports
import random
import time
from colored import fg, attr

# Global Variables
user_score = 0
user_balance = 1000
user_bet = 0
green = fg('green')
red = fg('red')
blue = fg('blue')
yellow = fg('yellow')
reset = attr('reset')


def another_game():
    global user_score, user_balance
    print("Your total score is", user_score, 'and your total balance is $', user_balance)
    print()
    time.sleep(3)

    if user_balance <= 0:
        print("You don't have any more money to bet! Game Over!\n")
        time.sleep(3)
        quit()

    elif user_balance >= 1:
        restart_action = input("Do you want to play again (yes | no): ")
        print()
        time.sleep(3)

        if restart_action == 'yes' or restart_action == 'y':
            restart()

        elif restart_action == 'no' or restart_action == 'n':
            print(green + 'Thanks for playing!')
            print()
            time.sleep(2)
            quit()

        else:
            print("Invalid input... Restarting choice...")
            print()
            time.sleep(3)
            another_game()

    else:
        print("User Balance Error...\n")
        time.sleep(2)
        quit()


def restart():
    global user_score, user_restart
    print("Restarting Blackjack Game...")
    print()
    time.sleep(3)
    game()


def game():
    global user_score, user_balance, user_bet
    # Dealer cards
    dealer_cards = []
    # Player cards
    player_cards = []

    print(green + 'Your balance is', user_balance, '\n', reset)
    time.sleep(2)
    user_bet = int(input('How much would you like to bet? '))
    time.sleep(2)

    if user_bet > user_balance:
        print()
        print(red + 'Your total balance cannot make this bet! Your bet is too high for your balance!\n', reset)
        time.sleep(3)
        game()

    if user_bet < 0:
        print()
        print(red + 'You cannot make a negative bet! Please place a higher bet than 0!\n', reset)
        time.sleep(3)
        game()

    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(4, 11))
        if len(dealer_cards) == 2:
            print()
            print(red + "Dealer has ??? &", dealer_cards[1], reset)
            print()

    # Player Cards
    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(player_cards) == 2:
            print("You have a total of", str(sum(player_cards)), 'from these cards', player_cards)
            print()

    # Total of Dealer cards
    if sum(dealer_cards) == 21:
        print(red + "Dealer has 21 and wins!")
        print()
        time.sleep(3)
        user_score -= 1
        user_balance = user_balance - user_bet
        another_game()

    elif sum(dealer_cards) > 21:
        print(green + "Dealer has busted!", reset)
        print()
        time.sleep(3)
        user_score += 1
        user_balance += user_bet
        another_game()

    # Total of Player cards
    while sum(player_cards) < 21:
        action_taken = str(input("Do you want to hit, stay, or call for help (hit | stay | help): "))
        print()
        time.sleep(2)

        if action_taken == "hit" or action_taken == "h":
            player_cards.append(random.randint(1, 11))
            print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
            print()
            time.sleep(3)

        elif action_taken == "help" or action_taken == "Help":
            if sum(player_cards) <= 14:
                print(blue + "Since your total is under or equal to a total of 14, we recommend that you hit!", reset)
                print()
                time.sleep(3)

            elif sum(player_cards) >= 15:
                print(blue + "Your odds are looking high enough to win, if your card total is closer to 15, "
                             "we recommend only "
                             "making 1 hit move and then staying!", reset)
                print()
                time.sleep(3)
                print(blue + "If your card total is closer to 21, don't risk it! make a stay move!", reset)
                print()
                time.sleep(3)

            else:
                print(red + "Helping Error...\n")
                time.sleep(3)
                quit()

        elif sum(dealer_cards) <= 15:
            dealer_cards.append(random.randint(1, 11))
            print(red + "The Dealer has pulled a card...", reset)
            print()
            time.sleep(2)

        else:
            print(red + "The Dealer has a new total of", str(sum(dealer_cards)), 'from these cards', dealer_cards,
                  reset)
            print()
            time.sleep(3)
            print("You have a grand total of " + str(sum(player_cards)) + " with", player_cards)
            print()
            time.sleep(3)

            if sum(dealer_cards) > 21:
                print(green + "The Dealer BUSTED! You win! You won $", user_bet, '!\n', reset)
                time.sleep(2)
                user_score += 1
                user_balance = user_balance + user_bet
                another_game()

            elif sum(dealer_cards) > sum(player_cards):
                print(red + "The dealer wins! You lost $", user_bet, '!\n', reset)
                time.sleep(3)
                user_score -= 1
                user_balance = user_balance - user_bet
                another_game()

            elif sum(dealer_cards) == 21:
                print(red + "BLACKJACK! The Dealer hit 21! You lost $", user_bet, '!\n', reset)
                time.sleep(2)
                user_score -= 1
                user_balance = user_balance - user_bet
                another_game()

            elif sum(dealer_cards) == sum(player_cards):
                print(yellow + 'PUSH! This is a tie!', reset)
                print()
                time.sleep(2)
                another_game()

            elif sum(player_cards) > sum(dealer_cards):
                print(green + "You Win! You won $", user_bet, '!\n', reset)
                time.sleep(2)
                user_score += 1
                user_balance = user_balance + user_bet
                another_game()

            else:
                print(red + "Error...", reset)
                print()
                time.sleep(3)
                another_game()

    # Endgame results
    if sum(player_cards) > 21:
        print(red + "BUSTED! The Dealer Wins! You lost $", user_bet, '!\n', reset)
        time.sleep(2)
        user_score -= 1
        user_balance = user_balance - user_bet
        another_game()

    elif sum(dealer_cards) > 21:
        print(green + "The Dealer BUSTED! You win! You won $", user_bet, '!\n', reset)
        time.sleep(2)
        user_score += 1
        user_balance = user_balance + user_bet
        another_game()

    elif sum(player_cards) == 21:
        print(green + "BLACKJACK! You hit 21! You won $", user_bet, '!\n', reset)
        time.sleep(2)
        user_score += 1
        user_balance = user_balance + user_bet
        another_game()

    elif sum(dealer_cards) == 21:
        print(red + "BLACKJACK! The Dealer hit 21! You lost $", user_bet, '!\n', reset)
        time.sleep(2)
        user_score -= 1
        user_balance = user_balance - user_bet
        another_game()

    elif sum(player_cards) == sum(dealer_cards):
        print(yellow + 'PUSH! This is a tie!', reset)
        print()
        time.sleep(2)
        another_game()


game()
