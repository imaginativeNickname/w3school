import pygame
import sys
import random

pygame.init()

width, height = 400, 400
cell = 20
cols = width // cell
rows = height // cell

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("snake game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("verdana", 20)

def get_food_position(snake):
    while True:
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        if (x, y) not in snake:
            return (x, y)

snake = [(cols // 2, rows // 2)]
direction = (1, 0)
food = get_food_position(snake)

score = 0
level = 1
food_counter = 0
speed = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    if (
        new_head[0] < 0 or new_head[0] >= cols or
        new_head[1] < 0 or new_head[1] >= rows or
        new_head in snake
    ):
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        score += 10
        food_counter += 1
        food = get_food_position(snake)
        if food_counter % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    screen.fill(black)

    pygame.draw.rect(
        screen,
        red,
        pygame.Rect(food[0] * cell, food[1] * cell, cell, cell)
    )

    for part in snake:
        pygame.draw.rect(
            screen,
            green,
            pygame.Rect(part[0] * cell, part[1] * cell, cell, cell)
        )

    text = font.render(f"score: {score}  level: {level}", True, white)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
sys.exit()