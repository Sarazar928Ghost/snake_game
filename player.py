import pygame
from part_body import PartBody


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        #Lorsqu'une direction est choisis et validé on met a True pour bloquer la prochaine demande
        self.waiting = False
        #Gauche de base
        self.direction = 1
        # Contient toute les parties du corps
        self.all_parts_body = pygame.sprite.Group()
        self.image = image

    #Je fais a l'envers comme ça si le serpent est invincible si il se mange lui même on verra sa tête
    def draw(self, surface: pygame.Surface):
        parts = self.all_parts_body.sprites()
        for i in range(len(parts)-1, -1, -1):
            parts[i].draw(surface)

    def move(self, cell_size):
        parts = self.all_parts_body.sprites()
        for i in range(len(parts) - 1, 0, -1):
            parts[i].rect.x = parts[i - 1].rect.x
            parts[i].rect.y = parts[i - 1].rect.y
        if self.direction == 1:
            parts[0].rect.x -= cell_size
        elif self.direction == -1:
            parts[0].rect.x += cell_size
        elif self.direction == 2:
            parts[0].rect.y -= cell_size
        elif self.direction == -2:
            parts[0].rect.y += cell_size
        #Débloque la prochaine demande de direction
        self.waiting = False

    def change_direction(self, direction: int):
        if not self.waiting:
            if self.check_direction(direction):
                self.waiting = True
                self.direction = direction

    def check_direction(self, direction: int):
        if self.direction != direction and self.direction != -direction:
            return True
        return False

    #Fait grandir de 1 en longueur le serpent
    def increase(self):
        self.all_parts_body.add(PartBody(
            self.all_parts_body.sprites()[len(self.all_parts_body.sprites()) - 1].rect.x,
            self.all_parts_body.sprites()[len(self.all_parts_body.sprites()) - 1].rect.y,
            self.image))

    def remove(self, i: int):
        self.all_parts_body.remove(self.all_parts_body.sprites()[i])

    def get_head(self):
        return self.all_parts_body.sprites()[0]
