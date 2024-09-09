# Hand Pop Game

This project demonstrates a simple hand-tracking game where balls fall from the top of the screen, and the player's task is to "pop" them using their hands, tracked by a webcam. The game utilizes OpenCV for video capture and MediaPipe for hand tracking.

### Installation

To run the game, you'll need to have Python installed along with the required libraries:

1. Clone the repository:
```
git clone https://github.com/1adore1/hand_pop.git
```
2. Install the required Python libraries:
```
pip install -r requirements.txt
```

### How to Run

To start the game, execute the following command:
```
python hand_tracking_ball_game.py
```
Make sure your webcam is connected, as the game requires video input to track your hand.

### Gameplay Instructions

* Balls will randomly fall from the top of the screen.
* Your score increases each time a ball touches any point on your hand.
* The game ends when you press the 'q' key to quit.
---
