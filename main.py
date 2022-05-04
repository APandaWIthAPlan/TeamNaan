from Simon.Simon import simon
import os
import pygame
from time import sleep

title = pygame.image.load(os.path.join('MainAssets','bomb.png'))
WHITE = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((800,480))
pygame.display.set_caption("Title")
screen.fill(WHITE)
screen.blit(title,(0,0))
pygame.display.update()
sleep(10)

simon()