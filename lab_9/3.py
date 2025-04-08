import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
ERASER = WHITE

clock = pygame.time.Clock()
drawing = False
last_pos = None
start_pos = None
color = BLACK
shape = "circle"
radius = 5

screen.fill(WHITE)

def draw_circle(pos):
    pygame.draw.circle(screen, color, pos, radius)

def draw_rectangle(start, end):
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(screen, color, rect, 2)

def draw_square(start, end):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    x, y = start
    pygame.draw.rect(screen, color, pygame.Rect(x, y, side, side), 2)

def draw_right_triangle(start, end):
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x2, y2), (x1, y2)]
    pygame.draw.polygon(screen, color, points, 2)

def draw_equilateral_triangle(start, end):
    x1, y1 = start
    side = abs(end[0] - x1)
    height = int(side * (math.sqrt(3)/2))
    points = [
        (x1, y1),
        (x1 + side, y1),
        (x1 + side // 2, y1 - height)
    ]
    pygame.draw.polygon(screen, color, points, 2)

def draw_rhombus(start, end):
    x1, y1 = start
    x2, y2 = end
    mid_x = (x1 + x2) // 2
    mid_y = (y1 + y2) // 2
    points = [
        (mid_x, y1),
        (x2, mid_y),
        (mid_x, y2),
        (x1, mid_y)
    ]
    pygame.draw.polygon(screen, color, points, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                if shape == "rectangle":
                    draw_rectangle(start_pos, end_pos)
                elif shape == "square":
                    draw_square(start_pos, end_pos)
                elif shape == "right_triangle":
                    draw_right_triangle(start_pos, end_pos)
                elif shape == "equilateral_triangle":
                    draw_equilateral_triangle(start_pos, end_pos)
                elif shape == "rhombus":
                    draw_rhombus(start_pos, end_pos)
                drawing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_b:
                color = BLUE
            if event.key == pygame.K_e:
                color = ERASER
            if event.key == pygame.K_1:
                shape = "rectangle"
            if event.key == pygame.K_2:
                shape = "square"
            if event.key == pygame.K_3:
                shape = "right_triangle"
            if event.key == pygame.K_4:
                shape = "equilateral_triangle"
            if event.key == pygame.K_5:
                shape = "rhombus"

    if drawing and shape == "circle":
        draw_circle(pygame.mouse.get_pos())

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
