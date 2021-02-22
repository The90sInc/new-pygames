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
        print(event) #prints out all the actions that take place on the  screen
pygame.quit()
quit()