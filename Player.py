class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, hand, drawDeck):
        if drawDeck:
            card = drawDeck.popleft()
            hand.append(card)

    def play_card(self, card, hand, discardPile, drawDeck):
        old_card = discardPile.popleft()
        drawDeck.append(old_card)
        discardPile.append(card)
        print(f"Top Card on Discard Pile: {discardPile[0]}\n")
        hand.remove(card)


   
