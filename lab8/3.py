import pygame, sys, random, time, math
from pygame.locals import *

pygame.init()

# window dimensions and grid settings
width, height = 800, 600
cell_size = 20

# colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red   = (255, 0, 0)
blue  = (0, 0, 255)
yellow= (255, 255, 0)

# set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("paint application")
clock = pygame.time.Clock()

# create a canvas surface for drawing
canvas = pygame.Surface((width, height))
canvas.fill(white)

# current drawing settings
current_tool = "pen"
current_color = black
brush_size = 4
eraser_size = 20

# function to display tool instructions on screen
def draw_instructions():
    font = pygame.font.SysFont("verdana", 16)
    instructions = [
        "tools: 1-pen 2-rectangle 3-circle 4-eraser",
        "colors: r-red g-green b-blue y-yellow",
        "press c for black, w for white (eraser uses white)",
    ]
    y = 5
    for line in instructions:
        text = font.render(line, True, black)
        screen.blit(text, (5, y))
        y += 20

# variables for shape drawing
start_pos = None  # stores starting mouse position for rectangle/circle

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # tool
        if event.type == KEYDOWN:
            if event.key == K_1:
                current_tool = "pen"
            elif event.key == K_2:
                current_tool = "rect"
            elif event.key == K_3:
                current_tool = "circle"
            elif event.key == K_4:
                current_tool = "eraser"
            # color
            elif event.key == K_r:
                current_color = red
            elif event.key == K_g:
                current_color = green
            elif event.key == K_b:
                current_color = blue
            elif event.key == K_y:
                current_color = yellow
            elif event.key == K_c:
                current_color = black
            elif event.key == K_w:
                current_color = white

        # mouse button down starts drawing for shapes
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                start_pos = event.pos
                if current_tool in ["pen", "eraser"]:
                    draw_color = white if current_tool == "eraser" else current_color
                    pygame.draw.circle(canvas, draw_color, event.pos, brush_size if current_tool == "pen" else eraser_size)
        # for free drawing with pen or eraser
        if event.type == MOUSEMOTION:
            if event.buttons[0]:
                if current_tool in ["pen", "eraser"]:
                    draw_color = white if current_tool == "eraser" else current_color
                    pygame.draw.circle(canvas, draw_color, event.pos, brush_size if current_tool == "pen" else eraser_size)
        # mouse button up for finalizing shapes
        if event.type == MOUSEBUTTONUP:
            if event.button == 1 and start_pos:
                end_pos = event.pos
                if current_tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(canvas, current_color, rect, 2)
                elif current_tool == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    radius = int(math.hypot(x2 - x1, y2 - y1))
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)
                start_pos = None

    # draw the canvas onto the screen
    screen.fill(white)
    screen.blit(canvas, (0, 0))
    draw_instructions()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()