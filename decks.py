#!/usr/bin/python3

# Created by Adam Smith on 20211003

# Imports
import random


# classes
class Decks:
    """This class is for shuffling between 1 to 6 decks of cards
        the primary set will be a deck of cards. Up to 5 more
        decks can be added with the add_decks function."""

    def __init__(self):
        self.deck = []
        self.last_round = False
        self.diamond_suit = ['AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD']
        self.spade_suit = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS']
        self.heart_suit = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']
        self.club_suit = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']

    def shoe_build(self, num_deck=1):
        self.deck = (self.diamond_suit + self.spade_suit + self.heart_suit + self.club_suit) * num_deck

    def deck_shuffle(self):
        temp_deck = []
        while len(self.deck) > 0:
            rand_num = random.randint(0, len(self.deck) - 1)
            temp_deck.append(self.deck[rand_num])
            self.deck.pop(rand_num)

        self.deck = temp_deck
        self.deck.insert(int(len(self.deck) / 52) * -15, 'r')

    def show_deck(self):
        print(self.deck)

    def next_card(self):
        if self.deck[0] != 'r':
            next_cd = self.deck[0]
            self.deck.pop(0)
        else:
            next_cd = self.deck[1]
            self.deck.pop(0)
            self.deck.pop(0)
            self.last_round = True

        return next_cd
