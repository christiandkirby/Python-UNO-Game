import random

class Card:
    def __init__(self, color, number, category, action):
        self.color = color
        self.number = number
        self.category = category
        self.action = action


    def __repr__(self):
        if self.number != None:
            return f"{self.color} {self.number}".title()
        elif self.color != None:
            return f"{self.color} {self.action}".title()  
        else:
            return f"{self.action}".title()


    
    # -------------------------------------------------------
    # Generates the UNO Card Deck of 108 Cards
    # Parameters: None
    # Return Value(s): card_deck -> list of Card() objects
    # -------------------------------------------------------
    def build_deck(): 
        card_deck = [] 

        # Making Number Cards 
        for color in ['red', 'yellow', 'green', 'blue']:
            for num in [0,1,2,3,4,5,6,7,8,9]:
                if num == 0:
                    card_deck.append(Card(color=color, number=num, category='number',action=None))
                else:
                    card_deck.append(Card(color=color, number=num, category='number',action=None))
                    card_deck.append(Card(color=color, number=num, category='number',action=None))
        

        # Making Color Actions Cards
        for color in ['red', 'yellow', 'green', 'blue']:
            for action in ['skip', 'draw two', 'reverse']:
                card_deck.append(Card(color=color, number=None, category='action', action=action))
                card_deck.append(Card(color=color, number=None, category='action', action=action))
        

        # Making Wild Cards
        for wild_action in ['wild', 'draw four']:
            card_deck.append(Card(color=None, number=None, category='action', action=wild_action))
            card_deck.append(Card(color=None, number=None, category='action', action=wild_action))
            card_deck.append(Card(color=None, number=None, category='action', action=wild_action))
            card_deck.append(Card(color=None, number=None, category='action', action=wild_action))
        
        return card_deck
    
    # -----------------------------------------------------------
    # Shuffles the Card Deck
    # Parameters: card_deck
    # Return Value(s): ordered card deck -> shuffled card deck 
    # -----------------------------------------------------------
    def shuffle_deck(card_deck):
        random.shuffle(card_deck)
        return card_deck


    # ---------------------------------------------------------------------
    # Checks if a card is playable 
    # Parameters: top_card; current card at the top of the discard pile.
    # Return Value(s): True or False
    # ---------------------------------------------------------------------
    def can_play_on(self, top_card):
        # Check if card has the same color or if the card is a wild
        if self.color == top_card.color or self.color == None:
            return True

        # Check if card as the same number/symbol
        if self.number != None:
            if self.number == top_card.number:
                return True
        else:
            if self.action == top_card.action:
                return True
        return False
