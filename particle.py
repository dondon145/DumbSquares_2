import pygame


class Particle(pygame.sprite.Sprite):

    def update_rect(self):
        self.rect.center = (self.pos_x, self.pos_y)

    def get_pos(self):
        return self.pos_x, self.pos_y
    
    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
    
    def change_pos_by(self, x, y):
        self.pos_x += x
        self.pos_y += y
    
    def get_color(self):
        return self.color
    
    def get_material(self):
        return self.material
    
    def set_color(self, color):
        self.color = color

    def update(self):
        self.get_pos()
        self.get_color()
        self.update_rect()

    def __init__(self, color, width, height, pos_x, pos_y, material):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.material = material

        # mutable attributes
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color