import os
import pygame
from time import sleep



def Instruction(num):
    photo = ["titlescreen.png", "wireswap.png", "simonscreen.png", "wirecut.png"]
    title = pygame.image.load(os.path.join('MainAssets',photo[num]))
    WHITE = (255,255,255)
    pygame.init()
    screen = pygame.display.set_mode((800,480))
    if photo == "titlescreen.png":
        pygame.display.set_caption("Title")
    else:
        pygame.display.set_caption("Instruction")
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


def WinScreen():
    title = pygame.image.load(os.path.join('MainAssets',"winscreen.png"))
    WHITE = (255,255,255)
    pygame.init()
    screen = pygame.display.set_mode((800,480))
    pygame.display.set_caption("Congrats!!")
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

def LoseScreen():
    title = pygame.image.load(os.path.join('MainAssets',"losescreen.png"))
    WHITE = (255,255,255)
    pygame.init()
    screen = pygame.display.set_mode((800,480))
    pygame.display.set_caption("ur bad + ratio")
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