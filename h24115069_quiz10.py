import random
import os
import time

# Define game settings
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 20
SNAKE_HEAD_CHAR = 'O'
SNAKE_BODY_CHAR = '#'
FOOD_CHAR = 'π'
SPECIAL_FOOD_CHAR = 'X'
OBSTACLE_CHAR = 'X'

# Define game variables
snake = [[SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2], [SCREEN_WIDTH // 4 - 1, SCREEN_HEIGHT // 2], [SCREEN_WIDTH // 4 - 2, SCREEN_HEIGHT // 2]]
direction = 'RIGHT'
food = [random.randint(1, SCREEN_WIDTH - 2), random.randint(1, SCREEN_HEIGHT - 2)]
obstacles = []
score = 0
special_food_eaten = 0
game_paused = False

# Create obstacles
obstacles_count = SCREEN_WIDTH * SCREEN_HEIGHT // 20
for _ in range(obstacles_count):
    obstacle_x = random.randint(1, SCREEN_WIDTH - 2)
    obstacle_y = random.randint(1, SCREEN_HEIGHT - 2)
    obstacles.append([obstacle_x, obstacle_y])

# Function to draw the game screen
def draw_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Score:', score, 'Special Food:', special_food_eaten)
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            if [x, y] in snake:
                if [x, y] == snake[0]:
                    print(SNAKE_HEAD_CHAR, end='')
                else:
                    print(SNAKE_BODY_CHAR, end='')
            elif [x, y] == food:
                print(FOOD_CHAR, end='')
            elif [x, y] in obstacles:
                print(OBSTACLE_CHAR, end='')
            else:
                print(' ', end='')
        print()

# Main game loop
while True:
    draw_screen()

    if not game_paused:
        next_key = input('Use arrow keys to move (press Space to pause): ').lower()

        if next_key == 'w':
            direction = 'UP'
        elif next_key == 's':
            direction = 'DOWN'
        elif next_key == 'a':
            direction = 'LEFT'
        elif next_key == 'd':
            direction = 'RIGHT'
        elif next_key == ' ':
            game_paused = True

        # Move the snake
        if direction == 'UP':
            new_head = [snake[0][0], snake[0][1] - 1]
        elif direction == 'DOWN':
            new_head = [snake[0][0], snake[0][1] + 1]
        elif direction == 'LEFT':
            new_head = [snake[0][0] - 1, snake[0][1]]
        elif direction == 'RIGHT':
            new_head = [snake[0][0] + 1, snake[0][1]]

        snake.insert(0, new_head)

        # Check for collision with food
        if snake[0] == food:
            score += 1
            food = [random.randint(1, SCREEN_WIDTH - 2), random.randint(1, SCREEN_HEIGHT - 2)]

        # Check for collision with obstacles
        if snake[0] in obstacles or snake[0][0] == 0 or snake[0][0] == SCREEN_WIDTH - 1 or snake[0][1] == 0 or snake[0][1] == SCREEN_HEIGHT - 1:
            break

        # Remove tail segment if not eating food
        if snake[0] != food:
            snake.pop()

        # Draw special food
        if score % 5 == 0 and special_food_eaten == 0:
            special_food = [random.randint(1, SCREEN_WIDTH - 2), random.randint(1, SCREEN_HEIGHT - 2)]
            special_food_eaten = 1
        elif special_food_eaten > 0 and snake[0] == special_food:
            special_food_eaten -= 1
            special_food = None

        # Slow down the game
        time.sleep(0.1)

# Game over
print('Game over!')
print('Score:', score, 'Normal food eaten:', score - special_food_eaten, 'Special food eaten:', special_food_eaten)
