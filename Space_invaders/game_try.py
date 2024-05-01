import pygame
import random
import math
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))

# Set the title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship_trile.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
player_width = playerImg.get_width()
player_height = playerImg.get_height()
playerX = (screen_width - player_width) / 2
playerY = screen_height - player_height - 10  # Adjusted position to fit above the bottom edge
playerX_change = 0

# Enemies
enemyImg = pygame.image.load('alein_spaceship.png')
enemy_width = enemyImg.get_width()
enemy_height = enemyImg.get_height()
num_of_enemies = 6
enemies = []
for _ in range(num_of_enemies):
    enemy = {
        "img": enemyImg,
        "x": random.randint(0, screen_width - enemy_width),
        "y": random.randint(50, 150),
        "x_change": 0.3,
        "y_change": 40
    }
    enemies.append(enemy)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bullet_width = 10
bullet_height = 10
bulletImg = pygame.transform.scale(bulletImg, (bullet_width, bullet_height))
bulletX = 0
bulletY = 480
bulletY_change = 1
bullet_state = "ready"

# Score
score = 0
font = pygame.font.Font('Warzone.ttf', 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('Warzone.ttf', 64)

# Stop button
stop_button_rect = pygame.Rect(screen_width - 120, 20, 100, 50)
stop_button_color = (64, 64, 64)  # Dark gray color
stop_button_text = font.render("Stop", True, (255, 255, 255))
text_rect = stop_button_text.get_rect(center=stop_button_rect.center)

# Resume button
resume_button_text = font.render("Resume", True, (255, 255, 255))
resume_button_rect = pygame.Rect(screen_width - resume_button_text.get_width() - 20, 100, resume_button_text.get_width() + 20, resume_button_text.get_height() + 20)
resume_text_rect = resume_button_text.get_rect(center=resume_button_rect.center)

# Centering text vertically within the button
resume_text_rect.centery = resume_button_rect.centery

# Exit button
exit_button_text = font.render("Exit", True, (255, 255, 255))
exit_button_rect = pygame.Rect(screen_width - exit_button_text.get_width() - 20, 170, exit_button_text.get_width() + 20, exit_button_text.get_height() + 20)
exit_text_rect = exit_button_text.get_rect(center=exit_button_rect.center)

# Centering text vertically within the button
exit_text_rect.centery = exit_button_rect.centery

# Flags
show_options = False
resume_clicked = False
exit_clicked = False

# Variables for "Thank you for playing" message
thank_you_time = None
thank_you_duration = 1000  # 5 seconds in milliseconds

# Functions
def player(x, y):
    screen.blit(playerImg, (x, y))

def draw_enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    return distance < 27

def show_score(x, y):
    score_value = font.render("Score : " + str(score), True, (0, 255, 230))
    screen.blit(score_value, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Game loop
running = True
while running:
    screen.fill((2, 34, 68))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.5
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.5
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX + (player_width - bullet_width) / 2  # Center bullet horizontally
                    fire_bullet(bulletX, bulletY)
            elif event.key == pygame.K_ESCAPE:  # Stop button
                show_options = not show_options  # Toggle the flag

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if stop_button_rect.collidepoint(mouse_pos):
                show_options = not show_options  # Toggle the flag
            elif resume_button_rect.collidepoint(mouse_pos):
                show_options = False
            elif exit_button_rect.collidepoint(mouse_pos):
                thank_you_time = pygame.time.get_ticks()  # Record the time when the message is triggered
                # Pause the game loop
                running = False

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= screen_width - player_width:
        playerX = screen_width - player_width

    for enemy in enemies:
        enemy["x"] += enemy["x_change"]
        if enemy["x"] <= 0:
            enemy["x_change"] = 0.2
            enemy["y"] += enemy["y_change"]
        elif enemy["x"] >= screen_width - enemy_width:
            enemy["x_change"] = -0.2
            enemy["y"] += enemy["y_change"]
        
        collision = isCollision(enemy["x"], enemy["y"], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemy["x"] = random.randint(0, screen_width - enemy_width)
            enemy["y"] = random.randint(50, 150)

        draw_enemy(enemy["x"], enemy["y"])

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    # Draw stop button
    pygame.draw.rect(screen, stop_button_color, stop_button_rect)
    screen.blit(stop_button_text, text_rect)  # Center the text within the button

    # Draw options
    if show_options:
        pygame.draw.rect(screen, (128, 128, 128), resume_button_rect)
        pygame.draw.rect(screen, (128, 128, 128), exit_button_rect)
        screen.blit(resume_button_text, (screen_width - 210, 115))
        screen.blit(exit_button_text, (screen_width - 180, 185))

    pygame.display.update()

# Display "Thank you for playing" message for 5 seconds before closing the window
if thank_you_time is not None:
    screen.fill((2, 34, 68))
    thank_you_text = font.render("Thank you for playing!", True, (255, 255, 255))
    screen.blit(thank_you_text, (200, 250))
    pygame.display.update()

    # Wait for 5 seconds
    pygame.time.wait(thank_you_duration)

# Quit pygame
pygame.quit()
sys.exit()
