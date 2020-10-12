import pygame
import random
from part_body import PartBody
from player import Player
from apple import Apple

image_body = 'images/body_snake.png'
image_head = 'images/head_body_snake.png'
image_apple = 'images/apple.png'


class Game:
    def __init__(self, screen: pygame.Surface, apple_start: int = 6,
                 body_start: int = 4, cell_size: int = 40):
        self.cell_size = cell_size
        self.body_start = body_start
        self.apple_start = apple_start
        #Quand il y a collision avec la pomme on la met ici
        self.current_apple: Apple = 0
        self.screen = screen
        #Load les images en avance pour éviter de devoir tout le temps les charger
        self.image_body_snake = pygame.transform.scale(pygame.image.load(image_body),
                                                       (self.cell_size, self.cell_size))
        self.image_apple = pygame.transform.scale(pygame.image.load(image_apple),
                                                       (self.cell_size, self.cell_size))
        self.player = Player(self.image_body_snake)
        self.create_start_body_player(body_start)
        self.all_apples = pygame.sprite.Group()
        self.create_start_apple(apple_start)

    # Chaque fois que la boucle tourne
    def update(self):
        self.player.move(self.cell_size)
        if self.check_collision_with_apple(self.player.get_head().rect.x, self.player.get_head().rect.y):
            self.delete_apple()
            self.create_apple()
            #Partie du corp spawn sur sa queue comme ça pas de problème
            self.player.increase()
        elif self.check_collision_head_with_body() or self.check_collision_with_wall():
            self.player.all_parts_body = pygame.sprite.Group()
            self.player.direction = 1
            self.create_start_body_player(self.body_start)
            self.all_apples = pygame.sprite.Group()
            self.create_start_apple(self.apple_start)
        self.player.draw(self.screen)
        self.draw_apple()

    def delete_apple(self):
        self.all_apples.remove(self.current_apple)

    #Centre la tête et met le corps tout a droite
    def create_start_body_player(self, body_start: int):
        width = self.screen.get_width()
        pos_head_width = width - self.body_start * self.cell_size

        height = self.screen.get_height()
        number_cell_height = height / self.cell_size
        pos_head_height = round(number_cell_height / 2) * self.cell_size

        for i in range(body_start):
            self.player.all_parts_body.add(
                PartBody(
                    pos_head_width + i * self.cell_size,
                    pos_head_height,
                    self.image_body_snake)
            )
        #Je met la tête en rouge
        image = pygame.transform.scale(pygame.image.load(image_head),
                                       (self.cell_size, self.cell_size))
        self.player.all_parts_body.sprites()[0].image = image

    def create_start_apple(self, apple_start: int):
        for i in range(apple_start):
            self.create_apple()

    def create_apple(self):
        rand = self.check_pos_random_apple()
        self.all_apples.add(Apple(rand[0], rand[1], self.image_apple))

    def check_pos_random_apple(self):
        rand = self.create_random_pos()
        while self.spawn_apple_check(rand[0], rand[1]):
            rand = self.create_random_pos()
        return rand

    def create_random_pos(self):
        return [
            random.randrange(0, self.screen.get_width() / self.cell_size) * self.cell_size,
            random.randrange(0, self.screen.get_height() / self.cell_size) * self.cell_size
        ]

    # Vérifie si le corps du joueur ou les pommes touche la futur pomme a placer
    def spawn_apple_check(self, rand_x: int, rand_y: int):
        if self.check_collision_with_apple(rand_x, rand_y):
            return True
        for part_body in self.player.all_parts_body:
            if part_body.rect.x == rand_x and part_body.rect.y == rand_y:
                return True
        return False

    def check_collision_with_apple(self, x: int, y: int):
        for apple in self.all_apples:
            if apple.rect.x == x and apple.rect.y == y:
                self.current_apple = apple
                return True
        return False

    # Si la tête du joueur touche une partie de son corps
    def check_collision_head_with_body(self):
        parts = self.player.all_parts_body.sprites()
        for i in range(len(parts) - 1, 0, -1):
            if parts[0].rect.x == parts[i].rect.x and parts[0].rect.y == parts[i].rect.y:
                return True
        return False

    def check_collision_with_wall(self):
        part = self.player.all_parts_body.sprites()[0]
        if part.rect.x > self.screen.get_width() - self.cell_size \
                or part.rect.y > self.screen.get_height() - self.cell_size \
                or part.rect.x < 0 \
                or part.rect.y < 0:
            return True
        return False

    def draw_apple(self):
        for apple in self.all_apples:
            apple.draw(self.screen)
