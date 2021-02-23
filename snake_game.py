#create screen
import pygame
pygame.init()
dis = pygame.display.set_mode((400,300))

#creating a game loop to keep screen from disappearing
pygame.display.set_caption("Snake Game using Pygame")

#initialize color variables and create snake
blue=(0,0,255)
red=(255,0,0)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True#to quit game screen
    pygame.draw.rect(dis,blue,[200,150,10,10])
    pygame.display.update()

pygame.quit()
quit()