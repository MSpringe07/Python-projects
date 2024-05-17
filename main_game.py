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
        "y": random.randint(-screen_height // 2, screen_height // 2),  # Start within the screen vertically,
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
bulletY_change = 3
bullet_state = "ready"

# Boss Bullet
boss_bulletImg = pygame.image.load('bullet.png')
boss_bullet_width = 10
boss_bullet_height = 10
boss_bulletImg = pygame.transform.scale(boss_bulletImg, (boss_bullet_width, boss_bullet_height))
boss_bulletY = 480
boss_bulletY_change = 3
boss_bullet_state = "ready"

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
resume_text_rect.center = resume_button_rect.center
# Exit button
exit_button_text = font.render("Exit", True, (255, 255, 255))
exit_button_rect = pygame.Rect(screen_width - exit_button_text.get_width() - 20, 170, exit_button_text.get_width() + 20, exit_button_text.get_height() + 20)
exit_text_rect = exit_button_text.get_rect(center=exit_button_rect.center)

# Centering text vertically within the button
exit_text_rect.center = exit_button_rect.center

# Flags
show_options = False
resume_clicked = False
exit_clicked = False
stop_button_clicked = False
game_paused = False

# Variables for "Thank you for playing" message
thank_you_time = None
thank_you_duration = 5000  # 5 seconds in milliseconds

# Define obstacle width and height
obstacles = []
obstacle_width = 100
obstacle_height = 50

# Define Boss attributes
bossImg = pygame.image.load('BOSS.png')
boss_width = bossImg.get_width()
boss_height = bossImg.get_height()
bossX = (screen_width - boss_width) / 2
bossY = 50
bossX_change = 0.3
boss_health = 15
boss_bullet_speed = 2
boss_shoot_frequency = 2000  # Boss shoots every 50 frames
boss_last_shot = 0  # Tracks the last frame boss shot
boss_lives = 15
boss_score = 0

boss_bulletX = 0
boss_bulletY = 0
boss_bullet_state = "ready"

boss_hits_player_count = 0

# Functions
def player(x, y):
    screen.blit(playerImg, (x, y))  

def draw_enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y, direction):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    
def isCollision(enemyX, enemyY, bulletX, bulletY, enemy_width, enemy_height, bullet_width, bullet_height):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    return distance < max(enemy_width, enemy_height) / 2 + max(bullet_width, bullet_height) / 2

def show_score(x, y):
    score_value = font.render("Score : " + str(score), True, (0, 255, 230))
    screen.blit(score_value, (x, y))

def boss_defeated_text():
    boss_defeated = over_font.render("BOSS DEFEATED!", True, (12, 143, 193))
    screen.blit(boss_defeated, (200, 250))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (225, 255, 225))
    screen.blit(over_text, (200, 250))

def generate_obstacles():
    num_obstacles = random.randint(1, 3)  # Random number of obstacles between 1 and 3
    for _ in range(num_obstacles):
        obstacle_type = random.choice(["obstacle1.png", "obstacle2.png"])  # Randomly select obstacle image
        obstacle_img = pygame.image.load(obstacle_type)
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacle_y = random.randint(max(screen_height * 1 // 4, obstacle_height), screen_height - obstacle_height)
        obstacle = {
            "img": obstacle_img,
            "x": obstacle_x,
            "y": obstacle_y
        }
        obstacles.append(obstacle)

# Call the function to generate obstacles
generate_obstacles()

def check_bullet_obstacle_collision(bullet_rect):
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle["x"], obstacle["y"], obstacle_width, obstacle_height)
        if bullet_rect.colliderect(obstacle_rect):
            return True
    return False

def draw_boss():
    screen.blit(bossImg, (bossX, bossY))

def move_boss():
    global bossX, bossX_change
    bossX += bossX_change
    if bossX <= 0:
        bossX_change = 0.3
    elif bossX >= screen_width - boss_width:
        bossX_change = -0.3

def boss_shoot():
    global boss_last_shot, boss_bullet_state
    current_time = pygame.time.get_ticks()
    if current_time - boss_last_shot >= boss_shoot_frequency:
        boss_last_shot = current_time
        if boss_bullet_state == "ready":
            fire_boss_bullet(bossX, bossY, playerX, playerY)  # Include playerX and playerY
        return True
    return False

def show_boss_lives(x, y):
    boss_lives_text = font.render("Boss Lives: " + str(boss_lives), True, (255, 255, 255))
    screen.blit(boss_lives_text, (x, y))

def check_boss_collision(score, boss_score, bossX, bossY):
    global bullet_state, bulletY, boss_lives
    if bullet_state == "fire":
        if isCollision(bossX, bossY, bulletX, bulletY, boss_width, boss_height, bullet_width, bullet_height):
            bullet_state = "ready"
            bulletY = 480
            boss_lives -= 1
            if boss_lives <= 0:
                screen.fill((0, 0, 0))  # Black color
                boss_defeated_text()  # Display game over text
                pygame.display.update()
                pygame.time.wait(5000)  # Wait for 5 seconds before closing the game
                pygame.quit()
                sys.exit()
                return score, boss_score + 1  # Increment boss_score
            else:
                return score + 1, boss_score  # Increment score
            
    return score, boss_score

def check_boss_bullet_collision():
    global boss_hits_player_count, boss_bullet_state, playerX, playerY, running, boss_bulletX, boss_bulletY
    if boss_bullet_state == "fire":
        if isCollisionPlayerBossBullet(playerX, playerY, boss_bulletX, boss_bulletY, player_width, player_height, boss_bullet_width, boss_bullet_height):
            boss_bullet_state = "ready"
            boss_hits_player_count += 1
            print("Boss Hits Player Count:", boss_hits_player_count)
            if boss_hits_player_count >= 3:
                game_over_text()
                pygame.display.update()
                pygame.time.wait(5000)
                pygame.quit()
                sys.exit()

def fire_boss_bullet(bossX, bossY, playerX, playerY):
    global boss_bullet_state, boss_bulletX, boss_bulletY
    boss_bullet_state = "fire"
    boss_bulletX = bossX + (boss_width - boss_bullet_width) / 2
    boss_bulletY = bossY + boss_height

def move_boss_bullet():
    global boss_bulletY, boss_bullet_state
    if boss_bullet_state == "fire":
        boss_bulletY += boss_bullet_speed  # Move the bullet straight down

        # If the bullet moves off screen, reset it
        if boss_bulletY > screen_height:
            boss_bullet_state = "ready"


# Function to draw boss bullet
def draw_boss_bullet():
    if boss_bullet_state == "fire":
        screen.blit(boss_bulletImg, (boss_bulletX, boss_bulletY))

def calculate_bullet_direction(bossX, bossY, playerX, playerY):
    directionX = playerX - bossX
    directionY = playerY - bossY
    distance = math.sqrt(directionX**2 + directionY**2)
    return directionX / distance, directionY / distance

def isCollisionPlayerBossBullet(playerX, playerY, bulletX, bulletY, player_width, player_height, bullet_width, bullet_height):
    if (playerX < bulletX + bullet_width and
        playerX + player_width > bulletX and
        playerY < bulletY + bullet_height and
        playerY + player_height > bulletY):
        return True
    return False

# Variables to track enemy speed increase
speed_increase_threshold = 5  # Increase speed every 5 points
speed_increase_amount = 0.05  # Amount to increase speed
score_before_increase = 0

# Set the frequency of enemy spawns
spawn_frequency = 10  # Adjust this value to change the spawn frequency

running = True
enemy_shot_count = 0
boss_active = False  # Flag to track if boss is active
enemy_spawn_timer = 0
max_enemies = 10  # Maximum number of enemies on the screen
boss_spawned = False
   
while running:
    screen.fill((2, 34, 68))
    screen.blit(background, (0, 0))

    # Spawn regular enemies
    enemy_spawn_timer += 1
    # Spawn a new enemy when one of the starting 8 has been shot
    if len(enemies) < max_enemies and enemy_spawn_timer >= 100:
        print("Enemy Shot Count:", enemy_shot_count)
        # print("Boss Spawned:", boss_spawned)

        # Spawn regular enemies
        enemy = {
            "img": enemyImg,
            "x": random.randint(0, screen_width - enemy_width),
            "y": random.randint(-screen_height // 4, -enemy_height),  # Adjusted spawning range
            "x_change": random.choice([-0.1, 0.1]),  # Random initial direction
            "y_change": 40
        }
        enemies.append(enemy)
        enemy_spawn_timer = 0  # Reset spawn timer
        
         # Spawn boss after 50 enemies shot
    if enemy_shot_count >= 5 and not boss_spawned:
        bossX = (screen_width - boss_width) / 2
        boss_health = 15
        boss_active = True
        boss_spawned = True  # Set the flag to avoid repeated spawning
        enemy_shot_count = 0  # Reset enemy shot count when boss spawns

        boss_bulletX = bossX + (boss_width - boss_bullet_width) / 2

    # Update Boss behavior
    if boss_active and not game_paused:
        move_boss()
        draw_boss()
        if boss_shoot():
            fire_boss_bullet(bossX, bossY, playerX, playerY)  # Pass playerX and playerY here
        move_boss_bullet()
        draw_boss_bullet()
        score, boss_score = check_boss_collision(score, boss_score, bossX, bossY)
        show_boss_lives(textX, textY + 40)
 
    # Check for collision between bullet and obstacle
    bullet_rect = pygame.Rect(bulletX, bulletY, bullet_width, bullet_height)
    if check_bullet_obstacle_collision(bullet_rect):
        # If collision detected, stop bullet
        bulletY = 480
        bullet_state = "ready"

    # Check for collision between boss bullet and player
    if boss_bullet_state == "fire":
        if isCollisionPlayerBossBullet(playerX, playerY, boss_bulletX, boss_bulletY, player_width, player_height, boss_bullet_width, boss_bullet_height):
            boss_bullet_state = "ready"  # Reset boss bullet state after collision
            boss_hits_player_count += 1
            playerX = (screen_width - player_width) / 2
            playerY = screen_height - player_height - 10
            if boss_hits_player_count >= 3:
                screen.fill((0, 0, 0))
                game_over_text()
                pygame.display.update()
                pygame.time.wait(5000)
                pygame.quit()
                sys.exit()
            
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
                    bulletY = playerY  # Start bullet from player's position
                    fire_bullet(bulletX, bulletY, "down")
            elif event.key == pygame.K_ESCAPE:  # Stop button
                show_options = not show_options  # Toggle the flag
                stop_button_clicked = True 
                game_paused = True 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if stop_button_rect.collidepoint(mouse_pos):
                show_options = not show_options  # Toggle the flag
                stop_button_clicked = True 
                game_paused = True
                if game_paused:
                    bossX_change = 0
                    boss_bullet_speed = 0
            elif resume_button_rect.collidepoint(mouse_pos):
                show_options = False
                resume_clicked = True
                game_paused = False
                if not game_paused:
                    # Resume boss movement and bullet when game is unpaused
                    bossX_change = 0.3
                    boss_bullet_speed = 2
            elif exit_button_rect.collidepoint(mouse_pos):
                thank_you_time = pygame.time.get_ticks()  # Record the time when the message is triggered
                exit_clicked = True
                # Pause the game loop
                running = False
                
    # Resume game if resume button clicked
    if resume_clicked:
        resume_clicked = False
        game_paused = False
        # Restart enemy movement
        for enemy in enemies:
            enemy["x_change"] = 0.2  # Adjust as needed based on your game

    # Stop enemy movement if stop button clicked
    if stop_button_clicked:
        for enemy in enemies:
            enemy["x_change"] = 0
        stop_button_clicked = False  # Reset the flag

    # Update game state only if not paused
    if not game_paused:
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= screen_width - player_width:
            playerX = screen_width - player_width

        if boss_active:
            move_boss()
            draw_boss()
            
            if boss_shoot():  # Check if the boss should shoot
                fire_boss_bullet(bossX, bossY, playerX, playerY)
                
            if boss_bullet_state == "fire":
                move_boss_bullet()
                draw_boss_bullet()
            
            score, boss_score = check_boss_collision(score, boss_score, bossX, bossY)
            show_boss_lives(textX, textY + 40)

            if boss_bulletY >= screen_height:  # Reset boss bullet if it goes off-screen
                boss_bullet_state = "ready"

            check_boss_bullet_collision()

        if boss_active:
            collision = isCollision(bossX, bossY, playerX, playerY, boss_width, boss_height, player_width, player_height)
            if collision:
                boss_hits_player_count += 1
                print("Boss Hits Player Count:", boss_hits_player_count)
                playerX = (screen_width - player_width) / 2
                playerY = screen_height - player_height - 10  # Adjusted position to fit above the bottom edge
                if boss_hits_player_count >= 3:
                    game_over_text()
                    pygame.display.update()
                    pygame.time.wait(5000)  # Wait for 5 seconds before closing the game
                    pygame.quit()
                    sys.exit()
                else:
                    # Boss hit but not defeated
                    boss_lives_text = font.render("Boss Lives: " + str(boss_lives), True, (255, 255, 255))
                    screen.blit(boss_lives_text, (textX, textY + 40))  # Update boss lives display

        for enemy in enemies:
            enemy["x"] += enemy["x_change"]
            if enemy["x"] <= 0:
                enemy["x_change"] = abs(enemy["x_change"])  # Make sure the speed is positive
                enemy["y"] += enemy["y_change"]
            elif enemy["x"] >= screen_width - enemy_width:
                enemy["x_change"] = -abs(enemy["x_change"])  # Make sure the speed is negative
                enemy["y"] += enemy["y_change"]

            # Check if enemy reaches the player's horizontal line
            if enemy["y"] + enemy_height >= playerY:
                game_over_text()
                pygame.display.update()
                # Wait for user input on the game over screen
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    if not running:
                        break
                # End game loop
                break
    
            collision = isCollision(enemy["x"], enemy["y"], bulletX, bulletY, enemy_width, enemy_height, bullet_width, bullet_height)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score += 1
                # Increment enemy shot count only if the boss is not active
                if not boss_active:
                    enemy_shot_count += 1
                # Regenerate enemy
                enemies.remove(enemy)  # Remove the shot enemy
                new_enemy_spawned = False  # Reset the flag

            # Draw each enemy
            draw_enemy(enemy["x"], enemy["y"])  # Add this line

    # Increase enemy speed if score has increased by 5 points
    if score >= score_before_increase + speed_increase_threshold and not boss_active:
        score_before_increase = score
        # Increase enemy speed
        for enemy in enemies:
            if enemy["x_change"] > 0:
                enemy["x_change"] += speed_increase_amount
            else:
                enemy["x_change"] -= speed_increase_amount

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY, "down")
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

    # Draw obstacles
    for obstacle in obstacles:
        screen.blit(obstacle["img"], (obstacle["x"], obstacle["y"]))  

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