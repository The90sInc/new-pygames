#create screen
import pygame
pygame.init()
dis = pygame.display.set_mode((400,300))
pygame.display.update()

#creating a game loop to keep screen from disappearing
pygame.display.set_caption("Snake Game using Pygame")
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True #to quit game screen

pygame.quit()
quit()