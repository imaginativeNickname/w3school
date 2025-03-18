import pygame

pygame.init()
screen = pygame.display.set_mode((900,780))
done = False

circle_x, circle_y = 450, 390
radius = 25
speed = 20

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and circle_y - speed >= radius: 
        circle_y -= speed
    if keys[pygame.K_DOWN] and circle_y + speed <= 780 - radius: 
        circle_y += speed
    if keys[pygame.K_LEFT] and circle_x - speed >= radius: 
        circle_x -= speed
    if keys[pygame.K_RIGHT] and circle_x + speed <= 900 - radius: 
        circle_x += speed

    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), radius)
    pygame.display.flip()