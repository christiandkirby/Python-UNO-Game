from flask import Flask, session
from flask import render_template, redirect, url_for, request
import Game, Cards
from collections import deque

def card_to_filename(card):
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
    num_of_players = request.form.get('num_of_players')
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
    return render_template('gameplay.html', 
        player_hand=player_hand,
        top_card=top_card,
        current_player=current.name,
        num_of_players=num_of_players
    )

@app.route('/play_card', methods=['POST'])
def play_card():
    pass

@app.route('/draw_card', methods=['POST'])
def draw_card():
    pass

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
        'zones': get_zone_assignments(),
        'num_of_players': num_of_players,
        'direction': direction
    }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')