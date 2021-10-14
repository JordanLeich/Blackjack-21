class Player:
    """This Class is an oop for players. It is to help
    reduce lines throughout the program. When each player
    is created. Their stats start with the same value.
    depending on which game is chosen, depends on what
    value each player gets."""

    def __init__(self, bet_amount=0, mc=0, presence=False,
                 bankrupt=False, cards=None, bank_roll=1000,
                 bot_player=False, dealer=False, p_score=None):
        if cards is None:
            cards = []
        if p_score is None:
            p_score = ['0', '0']
        if dealer:
            bank_roll = 2000000
            table_spot = 0
        else:
            table_spot = None
        self.bet = bet_amount
        self.bank_roll = bank_roll
        self.money_choice = mc
        self.presence = presence
        self.bankrupt = bankrupt
        self.cards = cards
        self.card_value = 0
        self.bot_player = bot_player
        self.dealer = dealer
        self.wlscore = p_score
        self.table_spot = table_spot

    def show_cards(self):
        print(self.cards)

    def add_card(self, cards):
        self.cards.append(cards)

    def sum_of_cards(self, is_dealer=False):
        sum_c = 0
        if is_dealer:
            card_count = 1
        else:
            card_count = len(self.cards)

        for card in range(card_count):
            temp_card = self.cards[card]
            if len(temp_card) > 2:
                sum_c += 10
            elif temp_card[0] in ['J', 'Q', 'K']:
                sum_c += 10
            elif temp_card[0] == 'A':
                if len(self.cards) > 2 and sum_c < 10:
                    sum_c += 11
                else:
                    sum_c += 1
            else:
                sum_c += int(temp_card[0])

        self.card_value = sum_c
        return sum_c

    def betting_amount(self):
        return self.bet

    def bought_insurance(self):
        return self.bet + (self.bet * .5)

    def player_win(self):
        self.wlscore[0] = int(self.wlscore[0]) + 1

    def player_loose(self):
        self.wlscore[1] = int(self.wlscore[1]) - 1
