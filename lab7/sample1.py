import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((900,780))
pygame.display.set_caption("Watches")

background = pygame.image.load("clock.png")
background = pygame.transform.scale(background, (980,780))
bg_rect = background.get_rect()

center_x = bg_rect.width // 2
center_y = bg_rect.height // 2

seconds = pygame.image.load("leftarm.png")
minuts = pygame.image.load("rightarm.png")

def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image,new_rect)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(background, (0,0))

    time = datetime.now()
    minuts_angle = -(time.minute * 6)
    seconds_angle = -(time.second * 6)

    blitRotateCenter(screen,seconds,(center_x,center_y),seconds_angle)
    blitRotateCenter(screen,minuts,(center_x,center_y),minuts_angle)

    pygame.display.flip()
