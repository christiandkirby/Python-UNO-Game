from flask import Flask
from flask import render_template

def card_to_filename(card):
    return repr(card).lower().replace(' ', '_')



app = Flask(__name__)

@app.route("/")
def hello_world():
    # player_hand = [card_to_filename(card) for card in players[0].hand]
    set_of_cards = []
    player_hand = ['red_2', 'blue_skip', 'wild', 'draw_four', 'yellow_reverse', 'green_draw_two']
    return render_template('index.html', top_card ="red_2", player_hand=player_hand)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')