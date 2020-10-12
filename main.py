import pygame
import time
from game import Game

pygame.init()
width = 1080
height = 720
cell_size = 40
speed = 0.09
screen = pygame.display.set_mode([width + cell_size, height + cell_size])

bg = pygame.transform.scale(pygame.image.load('images/bg.jpg'), (width + cell_size, height + cell_size))

running = True
game = Game(screen, cell_size=cell_size)

while running:

    #Permet d'éffacer a chaque fois les dessins
    screen.blit(bg, (0, 0))

    #Dessin et mouvement du joueur + collision
    game.update()

    #Vitesse du serpent
    time.sleep(speed)


    #Actualise l'écran
    pygame.display.flip()

    for event in pygame.event.get():
        #Quand le joueur clic sur la croix rouge
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            #1 = gauche;;;;-1 = droite;;;;2 = haut;;;;-2 = bas
            if event.key == pygame.K_DOWN:
                game.player.change_direction(-2)
            elif event.key == pygame.K_UP:
                game.player.change_direction(2)
            elif event.key == pygame.K_LEFT:
                game.player.change_direction(1)
            elif event.key == pygame.K_RIGHT:
                game.player.change_direction(-1)

