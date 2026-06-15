# 🎮 Python UNO Game

A browser-based implementation of the classic UNO card game built with Python. Players can create a game, draw and play cards according to UNO rules, and compete to empty their hand before everyone else.

**Live Demo:** https://python-uno-game.onrender.com/

---

## Features

- 🃏 Full UNO gameplay experience
- 🔄 Turn-based game logic
- 🎨 Color and number matching mechanics
- ⚡ Action cards (Skip, Reverse, Draw Two, Wild, Wild Draw Four)
- 🎲 Randomized deck generation and shuffling
- 🌐 Browser-accessible deployment via Render
- 📱 Simple and intuitive user interface

---

## Tech Stack

### Backend

- Python, Flask

### Frontend

- HTML
- CSS
- JavaScript

### Deployment

- Render

---

## How It Works

The application simulates a complete UNO game by:

1. Creating and shuffling a standard UNO deck
2. Dealing cards to players
3. Managing turn order and player actions
4. Validating legal card plays
5. Processing special card effects
6. Detecting win conditions and ending the game

Game state is maintained on the server to ensure that all player actions follow UNO rules.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/python-uno-game.git
cd python-uno-game
```

### Create a Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Navigate to:

```text
http://localhost:5000
```

---

## Project Structure

```text
python-uno-game/
│
├── static/              # CSS, JavaScript, assets
├── templates/           # HTML templates
├── app.py               # Application entry point
├── requirements.txt
└── README.md
```

---

## Challenges Solved

- Implementing UNO rule validation
- Managing turn order and special card effects
- Maintaining game state throughout gameplay
- Handling edge cases for Wild and Draw Four cards
- Deploying a Python web application for public access

---

## Future Improvements

- Multiplayer support
- AI opponents with varying difficulty levels
- User authentication
- Game statistics and leaderboards
- Additional UNO variants and house rules

---

## What I Learned

Through this project, I strengthened my skills in:

- Object-Oriented Programming (OOP)
- Python application development
- State management
- Backend and frontend integration
- Web deployment workflows
- Designing game logic and rule systems

---

## Screenshots

Add screenshots here to showcase gameplay.

```md
![Game Screenshot](images/game_screenshot.png)
```

---

## License

This project is licensed under the MIT License.
