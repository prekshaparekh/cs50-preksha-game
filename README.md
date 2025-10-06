 # Pixel Runner Game

A simple endless runner game built with Pygame where player jumps over obstacles to achieve the highest score possible.

## Description

Pixel Runner is a 2D side-scrolling game where you control a character that must jump over snails and flies while running. The game keeps track of your score based on how long you survive, and the difficulty increases as obstacles spawn at random intervals.

## Features

- Simple and intuitive controls
- Animated character sprites (walking and jumping)
- Two types of animated obstacles (snails and flies)
- Real-time score tracking
- Game over screen with score display
- Smooth animations at 60 FPS

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Install Python from [python.org](https://www.python.org/)
2. Install Pygame using pip:
```bash
pip install pygame
```

3. Ensure you have the following assets in the correct directories:
   - `Pixeltype.ttf` (font file in root directory)
   - Graphics folder with the following images:
     - `Sky.png`
     - `ground.png`
     - `snail1.png`
     - `snail2.png`
     - `fly1.png`
     - `fly2.png`
     - `player_walk_1.png`
     - `player_walk_2.png`
     - `jump.png`
     - `player_stand.png`

## How to Play

1. Run the game:
```bash
python3 project.py
```

2. **Controls:**
   - **SPACE** - Jump (when on ground) / Start game (on game over screen)
   - **A** - Move left
   - **D** - Move right
   - **Mouse Click** - Jump (when clicking on the player)

3. **Objective:**
   - Jump over obstacles (snails and flies) to survive as long as possible
   - Your score increases with time survived
   - Avoid colliding with obstacles or the game ends

## Game Mechanics

- Player starts at the left side of the screen
- Obstacles spawn randomly on the right side and move left
- Snails move along the ground
- Flies hover at a higher altitude
- Gravity automatically pulls the player down after jumping
- Collision with any obstacle ends the game

## Scoring

- Score is calculated based on the time survived (in seconds)
- The timer starts when the game begins
- Your final score is displayed on the game over screen

## Credits

Game developed using Pygame framework.

---

**Enjoy the game and try to beat your high score!**