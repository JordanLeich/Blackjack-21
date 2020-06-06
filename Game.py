# Made by Jordan Leich on 6/6/2020

# Imports
import random
import time

# Dealer cards
dealer_cards = []
# Player cards
player_cards = []


while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has ??? &", dealer_cards[1])
        print()

# Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have", player_cards)
        print()

# Total of Dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
    print()
    time.sleep(3)
    quit()
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")
    print()
    time.sleep(3)
    quit()

# Total of Player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit: "))
    print()
    time.sleep(2)
    if action_taken == "hit" or action_taken == "h":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
        print()
        time.sleep(3)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print()
        time.sleep(3)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        print()
        time.sleep(3)
        if sum(dealer_cards) > sum(player_cards):
            print("The dealer wins!")
            print()
            time.sleep(3)
            quit()
        else:
            print("You win!")
            print()
            time.sleep(3)
            quit()
            break

# Endgame results
if sum(player_cards) > 21:
    print("BUSTED! The dealer wins.")
    print()
elif sum(player_cards) == 21:
    print("BLACKJACK! You hit 21!")
    print()
