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
GREY = (128, 128, 128)


cell_width = 5
cell_height = 5
moving_group = pygame.sprite.Group()
world_grid = grid.Grid(moving_group, 801, 801, cell_width, cell_height)

running = True
pressed_s = False
pressed_w = False
pressed_r = False

while running:

    mouse_x, mouse_y = pygame.mouse.get_pos() 

    for event in pygame.event.get():

        key_list = pygame.key.get_pressed()
    
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if key_list[K_s]:
                pressed_s = True
            if key_list[K_w]:
                pressed_w= True
            if key_list[K_r]:
                pressed_r = True

        elif event.type == KEYUP:
            pressed_w = False
            pressed_s = False
            pressed_r = False

    if pressed_w:            
        world_grid.add_on_screen(particle.Particle(BLUE, cell_width, cell_height, mouse_x, mouse_y, "water"))
    
    if pressed_s:
        world_grid.add_on_screen(particle.Particle(PASTEL_YELLOW, cell_width, cell_height, mouse_x, mouse_y, "sand"))
    
    if pressed_r:
        world_grid.add_on_screen(particle.Particle(GREY, cell_width, cell_height, mouse_x, mouse_y, "static stone"))


    DISPLAY.fill(BLACK)
    world_grid.update()
    moving_group.update()
    moving_group.draw(DISPLAY)
    pygame.display.flip()
    print(int(clock.get_fps()))
    print(moving_group)
    clock.tick(FPS)