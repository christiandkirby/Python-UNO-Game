from flask import Flask, session
from flask import render_template, redirect, url_for, request, jsonify
import Game, Cards, Player
from collections import deque

def card_to_filename(card):
    if card.category == 'action' and card.action in ['wild', 'draw four']:
        return card.action.replace(' ', '_')
    return repr(card).lower().replace(' ', '_')


players = []
drawDeck = None
discardPile = None
selected_player = 0
direction = 1
num_of_players = 0
game_active = False


app = Flask(__name__)
app.secret_key = "pythonUNO"

@app.route("/")
def start_screen():
    return render_template('startScreen.html')


@app.route("/start", methods=['POST'])
def start_game():
    global players, num_of_players, unoDeck, drawDeck, discardPile, direction, selected_player, game_active

    # Initialize Players
    num_of_players = int(request.form.get('num_of_players'))
    players = Game.initialize_players(num_of_players)

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

    return redirect(url_for("gameplay"))


@app.route("/gameplay")
def gameplay():
    current = players[selected_player]
    player_hand = [card_to_filename(card) for card in current.hand]
    top_card = card_to_filename(discardPile[0])

    opponents = [p for p in players if p != current]

    zones = {
        "top": None,
        "left": None,
        "right": None
    }

    if num_of_players == 2:
        zones["top"] = len(opponents[0].hand)

    elif num_of_players == 3:
        zones["left"] = len(opponents[0].hand)
        zones["right"] = len(opponents[1].hand)

    elif num_of_players == 4:
        zones["top"] = len(opponents[0].hand)
        zones["left"] = len(opponents[1].hand)
        zones["right"] = len(opponents[2].hand)

    return render_template(
        "gameplay.html",
        player_hand=player_hand,
        top_card=top_card,
        current_player=current.name,
        num_of_players=num_of_players,
        zones=zones
    )


@app.route('/play_card', methods=['POST'])
def play_card():
    global selected_player, direction, num_of_players, players
    current = players[selected_player]
    data = request.get_json()
    card_index = data['card_index']
    color = data.get('color', None)
    card = current.hand[card_index] 

    if card.can_play_on(discardPile[0]):
        current.play_card(card, current.hand, discardPile, drawDeck)

        if color:
            Game.handle_wild(discardPile[0], color)
        
        if card.action in ['reverse', 'skip', 'draw two', 'draw four']:
            selected_player, direction = Game.handle_action_cards(discardPile[0], selected_player, 
                                                                direction, num_of_players, 
                                                                players, drawDeck)
        else:
            selected_player = (selected_player + direction) % num_of_players
        
        return jsonify({
            'success': True,
            'player_hand': [card_to_filename(c) for c in current.hand],
            'top_card': card_to_filename(discardPile[0]),
            'current': players[selected_player].name
        })
    else:
        return jsonify({
            'success': False,
            'message': 'That card cannot be played!'
        })


@app.route('/draw_card', methods=['POST'])
def draw_card():
    global selected_player, direction, num_of_players, players
    current = players[selected_player]
    current.draw_card(current.hand, drawDeck)

    selected_player = (selected_player + direction) % num_of_players

    return jsonify({
        'player_hand': [card_to_filename(c) for c in current.hand],
        'current': players[selected_player].name
    })


@app.route('/select_color', methods=['POST'])
def select_color():
    pass


@app.route('/game_state', methods=['GET'])
def get_game_state():
    current = players[selected_player]
    return {
        'current_player': current.name,
        'player_hand': [card_to_filename(card) for card in current.hand],
        'top_card': card_to_filename(discardPile[0]),
        'zones': None, # Placeholder for zones if needed : get_zone_assignments()
        'num_of_players': num_of_players,
        'direction': direction
    }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')