import pygame
from pygame.locals import *
import grid
import particle

pygame.init()

FPS = 60
clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 800
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

# COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PASTEL_YELLOW = (253, 253, 150)


cell_width = 10
cell_height = 10
moving_group = pygame.sprite.Group()
world_grid = grid.Grid(moving_group, 801, 801, cell_width, cell_height)
sand_particle = particle.Particle(PASTEL_YELLOW, 10, 10, 400, 0)

running = True
pressed = False

while running:

    mouse_x, mouse_y = pygame.mouse.get_pos() 

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            pressed = True
        elif event.type == KEYUP:
            pressed = False

    if pressed:            
        world_grid.add_on_screen(particle.Particle(PASTEL_YELLOW, cell_width, cell_height, mouse_x, mouse_y))
    
    DISPLAY.fill(BLACK)
    world_grid.update()
    moving_group.update()
    moving_group.draw(DISPLAY)
    pygame.display.flip()
    #print(clock.get_fps())
    #print(moving_group)
    clock.tick(FPS)