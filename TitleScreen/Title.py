import os
import pygame
from time import sleep



def Startup():
    
    buttons = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]
    title = pygame.image.load(os.path.join('MainAssets','clock.jpg'))
    WHITE = (255,255,255)
    pygame.init()
    screen = pygame.display.set_mode((800,480))
    pygame.display.set_caption("Title")
    screen.fill(WHITE)
    screen.blit(title,(0,0))
    pygame.display.update()
    Taco = True
    clock = pygame.time.Clock()

    while(Taco==True):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z: # 'z' key for window close
                    pygame.quit()
                    return
