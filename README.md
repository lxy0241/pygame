# Ping Pong Game

## Group Name
Mayo

## Group Member

Lim Xing Ying

Goh Ee Theng

Hoh Zhi Qi

## Overview
This is a Python Ping Pong Game. The game combines the classic elements of Ping Pong with a twist: before the game begins, players need to complete a Rock-Paper-Scissors(RPS) match to determine who serves first. The ball always starts from the winner's side, and the game's difficulty increases as the speed progressively ramps up, providing a fun and challenging experience.
 

## Installation

**1. Clone the Repository**

git clone https://github.com/yourusername/ping-pong-rps-game.git

cd ping-pong-rps-game

**2. Install Pygame**

Ensure you have Pygame installed. If not, you can install it using pip.

pip install pygame

**3. Add Background Music**

Place your background music file in  Music directory at the root of the project. The music file should be named Background.mp3

## Controls

**Paper-Rock-Scissors Match**

Player 1:

1 for Paper

2 for Rock

3 for Scissors

Player 2: 

J for paper

K for Rock

L for scissors

**Ping Pong Gameplay**

Player 1:

W to move the paddle up

S to move the paddle down

Player 2:

Up Arrow to move the paddle up

Down Arrow to move the paddle down

## Game Mechanics

**1)Rock-Paper-Scissors:**

-Players choose Rock, Paper, or Scissors to determine who serves first.

-If there is a tie, players must choose again until there is a winner.

**2)Ping Pong Match:**

-Players control paddles to keep the ball in play.

-The game ends when one player reaches the winning score (11 points).

-The player who wins the Rock-Paper-Scissors round serves first.

**3)Score Tracking:**

-The score is displayed at the top of the screen.

-The game resets the ball position when a point is scored.

-The game ends when either player reaches the winning score.

**4)Game Over:**

-The game displays a "Game Over" screen with the winner.

-Options to quit the game or play again are provided.

## Code Structure:

**1)Initialization:**

-Sets up the game window, initializes pygame, and loads resources.

**2)Game Loop:**

-Handles game events, updates game state, and draws the game screen.

**3)Functions:**

reset_ball(): Resets the ball position and direction.

draw_gradient_background(): Draws a gradient background.

draw_game(): Draws game elements including paddles, ball, and score.

draw_buttons(): Draws buttons on the game over screen.

rock_paper_scissors(): Handles the Rock-Paper-Scissors game.

game_over_screen(): Displays the game over screen.

## Game Action

Esc to quit the game

Mouse Click on the "Quit" button to exit or "Play Again" to restart after the game ends

## How to Play
1. The game begins with a Rock-Paper-Scissors match between the two players.
   
2.  The winner of the PRS match serves the ball from their side.
   
3. Players control their paddles to hit the ball back and forth.

4. The game ends when one player reaches 11 points and the winner is declared

5. After the game, players can choose to play again or quit.

## Photo

![Paper-Rock-Scissors](https://github.com/lxy0241/pygame/blob/main/Screenshot/Screenshot%202024-09-04%20135511.png)

![Gameplay](https://github.com/lxy0241/pygame/blob/main/Screenshot/Screenshot%202024-09-04%20135533.png)

