''' 
Functionality
- represent a hand of cards (repr)
- calculate the value of the hand 
'''

class Hands:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.total()

    def total(self):
        self.value = 0
        aces = 0
        for card in self.cards:
            if card.rank in ['Jack', 'Queen', 'King']:
                self.value += 10
            elif card.rank == 'Ace':
                aces += 1
                self.value += 11
            else:
                self.value += int(card.rank)
        while self.value > 21 and aces:
            self.value -= 10
            aces -= 1   
    

