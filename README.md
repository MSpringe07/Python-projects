# Space Invaders Game

## Description
A Space Invaders game built with Pygame. Control a spaceship, shoot enemies and a boss, with score tracking, difficulty increase, and pause/resume functionality.

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/space-invaders.git
    ```
2. Install Pygame:
    ```sh
    pip install pygame
    ```

## Running the Game
1. Navigate to the game directory:
    ```sh
    cd space-invaders
    ```
2. Run the game:
    ```sh
    python main.py
    ```

## Controls
- **Left Arrow / A**: Move left
- **Right Arrow / D**: Move right
- **Space**: Shoot bullet
- **Escape**: Pause/Resume game

## Features
- Player spaceship and bullets
- Multiple enemies with increasing difficulty
- Boss enemy with special behaviors
- Obstacles that block bullets
- Pause, resume, and exit buttons
- Score tracking and display
- Game over and boss defeated messages

## Code Overview
- **player()**: Draws the player spaceship.
- **draw_enemy()**: Draws an enemy.
- **fire_bullet()**: Fires a bullet.
- **isCollision()**: Checks collisions.
- **show_score()**: Displays score.
- **boss_defeated_text()**: Displays a message.
- **game_over_text()**: Displays a message.
- **generate_obstacles()**: Generates obstacles.
- **check_bullet_obstacle_collision()**: Checks collisions.
- **draw_boss()**: Draws the boss.
- **move_boss()**: Moves the boss.
- **boss_shoot()**: Handles boss shooting.
- **show_boss_lives()**: Displays boss lives.
- **check_boss_collision()**: Checks collisions.
- **check_boss_bullet_collision()**: Checks collisions.
- **fire_boss_bullet()**: Fires a bullet.
- **move_boss_bullet()**: Moves the bullet.
- **draw_boss_bullet()**: Draws the bullet.
- **calculate_bullet_direction()**: Calculates direction.
- **isCollisionPlayerBossBullet()**: Checks collisions.

## License
MIT License
