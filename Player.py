class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, drawDeck):
        if drawDeck:
            self.hand.append(drawDeck.popleft())

    def play_card(self, card, discardPile):
        self.hand.remove(card)
        discardPile.append(card)

   
