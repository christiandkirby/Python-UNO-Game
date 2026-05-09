import Cards
import Player
import rich
from collections import deque

# -------------------------------------
# Handles Draw Cards
# -------------------------------------
def handle_action_cards(card):
    pass


def handle_draw_cards():
    pass


def handle_skip():
    pass


def handle_reverse():
    pass


def handle_wild():
    pass



# -------------------------------------
# Checks if a player has won the game
# -------------------------------------
def check_for_winner(hand):
    if len(hand) == 0:
        return True
    return False



# -------------------------------------
# Checks if a player has Uno
# -------------------------------------
def check_for_uno(hand):
    if len(hand) == 1:
        return True
    return False




# -------------------------------------
# Initializes the Players for the Game
# -------------------------------------
def initialize_players():
        while True:
            num_of_players = input("How Many Players? (2, 3, or 4) ")
            try:
                num_of_players = int(num_of_players)
                if num_of_players in [2, 3, 4]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input! Please Type 2, 3, or 4!")
                continue
        
        players = [Player.Player("Player " + str(i+1)) for i in range(num_of_players)]
        return num_of_players, players



# -------------------------------------
# Handles a Players Turn
# -------------------------------------
def take_turn(player, hand, drawDeck, discardPile):
    num_of_cards = len(hand)-1
    chosen_card = input(f"Please Pick The Number That Corresponds to the Card You Want.\n"
                        f"(From 0 to {num_of_cards} or -1 to Draw a Card.) ")
    while True:
        try:
            chosen_card = int(chosen_card)
            if chosen_card == -1:
                player.draw_card(hand, drawDeck)
                break
            elif chosen_card in range(0,num_of_cards+1):
                if hand[chosen_card].can_play_on(discardPile[0]):
                    card = hand[chosen_card]
                    player.play_card(card, hand, discardPile, drawDeck)
                    break
                else:
                    print("This Card Cannot Be Played, Please Pick Another Card.\n")
            else:
                raise ValueError

        except ValueError:
            print(f"Invalid Input! Please pick a number from 0 to {num_of_cards} or -1 to Draw a Card.\n")
        
        chosen_card = input(f"Please Pick The Number That Corresponds to the Card You Want.\n"
                            f"(From 0 to {num_of_cards} or -1 to Draw a Card.)")




running = True
while running:
    # Initialize Players
    num_of_players, players = initialize_players() 
    
    # Initialize Card Decks
    unoDeck = Cards.Card.build_deck()
    unoDeck = Cards.Card.shuffle_deck(unoDeck)
    drawDeck = deque(unoDeck)
    discardPile = deque()


    # Dealing Each Players Cards
    for player in players:
        for _ in range(7):
            card = drawDeck.popleft()
            player.hand.append(card)


    # Setting up discard pile
    firstCard = drawDeck.popleft()
    discardPile.append(firstCard)
    print(f"The first card on the play deck is a {discardPile[0]}\n")


    game_still_going = True
    while game_still_going:
        i = 0
        while i < 1:
            selected_player = i % num_of_players
            print(f"Its {players[selected_player].name}'s Turn!\n")
            player = players[selected_player]
            players_hand = players[selected_player].hand
            print(f"{players_hand}\n")
            
            print(f"Top Card on Discard Pile: {discardPile[0]}\n")

            print(f"Number of Cards {player.name} has before turn is {len(players_hand)}\n" )
            take_turn(player, players_hand, drawDeck, discardPile)
            print(f"Number of Cards {player.name} has after turn is {len(players_hand)}\n" )

            # print(f"Top Card on Discard Pile: {discardPile[0]}\n")
        
            i += 1
        game_still_going = False



    running = False