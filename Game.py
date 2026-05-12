import Cards
import Player
import rich
from collections import deque

# -------------------------------------
# Handles Action Cards
# Parameter(s): card --> Card Object
# Return Value(s): None
# -------------------------------------
def handle_action_cards(card, selected_player, direction, num_of_players, players, drawDeck):
    if card.action == 'skip':
        selected_player = handle_skip(selected_player, direction, num_of_players)
        return selected_player, direction
    elif card.action == 'reverse':
        direction = handle_reverse(direction)
        return selected_player, direction
    elif card.action == 'wild':
        handle_wild(card)
        return selected_player, direction

    else:
        selected_player = handle_draw_cards(card, selected_player, direction, players, num_of_players, drawDeck)
        return selected_player, direction


# ---------------------------------------------------
# Handles Draw Cards (NO STACKING FOR VERSION 1.0)
# Parameter(s): card --> Card Object
# Return Value(s): selected_player --> int
# ---------------------------------------------------
def handle_draw_cards(card, selected_player, direction, players, num_of_players, drawDeck):
    if card.action == 'draw two':
        selected_player = handle_skip(selected_player, direction, num_of_players)
        next_player = players[selected_player]
        for _ in range(2):
            next_player.draw_card(next_player.hand, drawDeck)
        return selected_player
    else:
        handle_wild(card)
        selected_player = handle_skip(selected_player, direction, num_of_players)
        next_player = players[selected_player]
        for _ in range(4):
            next_player.draw_card(next_player.hand, drawDeck)
            
        return selected_player



# -------------------------------------
# Handles Skip Cards
# Parameter(s): None
# Return Value(s): None
# -------------------------------------
def handle_skip(selected_player, direction, num_of_players):
    return (selected_player + direction) % num_of_players


# -------------------------------------
# Handles Reverse Cards
# Parameter(s): None
# Return Value(s): None
# -------------------------------------
def handle_reverse(direction):
    return direction * -1


# -------------------------------------
# Handles Wild Cards
# Parameter(s): card --> Card Object
# Return Value(s): None
# -------------------------------------
def handle_wild(card):
    color = input(f"What Color Do You Want to Select? (1:Red, 2:Yellow, 3:Green, 4:Blue): ")
    while True:
        try:
            color = int(color)
            match color:
                case 1:
                    card.color = 'red'
                    break
                case 2:
                    card.color = 'yellow'
                    break
                case 3:
                    card.color = 'green'
                    break
                case 4:
                    card.color = 'blue'
                    break
                case _:
                    raise ValueError
        except ValueError:
            print(f"Invalid Input! Please Type 1, 2, 3, 4!")
        color = input(f"What Color Do You Want to Select? (1:Red, 2:Yellow, 3:Green, 4:Blue): ")





# -------------------------------------
# Checks if a player has won the game
# Parameter(s): hand --> Array of Card Objects
# Return Value(s): running (Boolean: True/False)
# -------------------------------------
def check_for_winner(hand, game_still_going):
    if len(hand) == 0:
        game_still_going = False
        return game_still_going
    else:
        return game_still_going



# -------------------------------------
# Checks if a player has Uno
# Parameter(s): hand --> Array of Card Objects
# Return Value(s): Boolean (True/False)
# -------------------------------------
def check_for_uno(player, hand, drawDeck):
    if len(hand) == 1:
        said_uno = input(f"You have UNO please type UNO correctly!(CASE INSENSITIVE)\n" 
                         f"Otherwise You get a 2 card penalty! ")
        if said_uno.upper() != 'UNO': 
            player.draw_card(hand, drawDeck) 
            player.draw_card(hand, drawDeck)




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
# Handles a Player's Turn
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

                    # If a player draws a playable card
                    if hand[-1].can_play_on(discardPile[0]):
                        player.play_card(hand[-1], hand, discardPile, drawDeck)
                        return True
                    else:
                        return False

            elif chosen_card in range(0,num_of_cards+1):
                if hand[chosen_card].can_play_on(discardPile[0]):
                    card = hand[chosen_card]
                    player.play_card(card, hand, discardPile, drawDeck)
                    return True
                else:
                    print("This Card Cannot Be Played, Please Pick Another Card.\n")
            else:
                raise ValueError

        except ValueError:
            print(f"Invalid Input! Please pick a number from 0 to {num_of_cards} or -1 to Draw a Card.\n")
        
        chosen_card = input(f"Please Pick The Number That Corresponds to the Card You Want.\n"
                            f"(From 0 to {num_of_cards} or -1 to Draw a Card.) ")




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

    # Initialize Turn Variables
    direction = 1
    selected_player = 0
    
    # Setting up discard pile
    firstCard = drawDeck.popleft()
    discardPile.append(firstCard)

    # Handles Draw Four Starter Card Edge Case
    while discardPile[0].action == 'draw four':
        card = discardPile.popleft()
        drawDeck.append(card)
        firstCard = drawDeck.popleft()
        discardPile.append(firstCard)

    print(f"The first card on the play deck is a {discardPile[0]}\n")

    # Handles If Starting Card is an Action Card
    if discardPile[0].action != None:
            selected_player, direction = handle_action_cards(discardPile[0], selected_player, 
                                                             direction, num_of_players, 
                                                             players, drawDeck)


    game_still_going = True
    while game_still_going:
        player = players[selected_player]
        print(f"Its {player.name}'s Turn!\n")
        players_hand = player.hand
        print(f"{players_hand}\n")
        
        print(f"Top Card on Discard Pile: {discardPile[0]}\n")

        print(f"Number of Cards {player.name} has before turn is {len(players_hand)}\n" )
        was_card_played = take_turn(player, players_hand, drawDeck, discardPile)
        print(f"Number of Cards {player.name} has after turn is {len(players_hand)}\n" )

        # Handling Card Gameplay
        if was_card_played:
            if discardPile[0].action != None:
                selected_player, direction = handle_action_cards(discardPile[0], selected_player, 
                                                                    direction, num_of_players, 
                                                                    players, drawDeck)
            check_for_uno(player, players_hand, drawDeck)
            game_still_going = check_for_winner(players_hand, game_still_going)
        
        
        selected_player = (selected_player + direction) % num_of_players
    print(f"{player.name} wins! 🎉")
    running = False