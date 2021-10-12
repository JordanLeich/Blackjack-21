class Player:
    """This Class is an oop for players. It is to help
    reduce lines throughout the program. When each player
    is created. Their stats start with the same value.
    depending on which game is chosen, depends on what
    value each player gets."""

    def __init__(self, bet_amount=0, mc=0, presence=False,
                 bankrupt=False, cards=None, bank_roll=1000,
                 bot_player=False, dealer=False, p_score=None):
        if cards == None:
            cards = []
        if p_score == None:
            p_score == [0,0]
        if dealer:
            bank_roll = 2000000
        self.bet = bet_amount
        self.bank_roll = bank_roll
        self.money_choice = mc
        self.presence = presence
        self.bankrupt = bankrupt
        self.cards = cards
        self.bot_player = bot_player
        self.dealer = dealer
        self.wlscore = p_score


    def show_cards(self):
        print(self.cards)

    def add_card(self, cards):
        self.cards.append(cards)

    def sum_of_cards(self):
        sum_c = 0
        for card in range(len(self.cards)):
            temp_card = self.cards[card]
            if len(temp_card) > 2:
                sum_c += 10
            elif temp_card[0] in ['J','Q','K']:
                sum_c += 10
            elif temp_card[0] == 'A':
                if len(self.cards) > 2 and (sum_c + 11) < 21:
                    sum_c += 11
                else:
                    sum_c += 1 
            else:
                sum_c += int(temp_card[0])

            #sum_card += int(temp_card)
        print(self.cards, 'card sum' , sum_c)
        #return sum_card

    def betting_amount(self):
        return self.bet

    def bought_insurance(self):
        return self.bet + (self.bet * .5)

    def player_win(self):
        self.p_score[0] += 1

    def player_loose(self):
        self.p_score[1] -= 1


