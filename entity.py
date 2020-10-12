import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)
