#import RPi.GPIO as GPIO
from time import sleep
import random
import os
import pygame

def SnipSnip():
    pins = [4,6,13,18]
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    photo = ["wires1.png","wires2.png", "wires3.png"]
    title = pygame.image.load(os.path.join('SnipAssets',random.choice(photo)))
    WHITE = (255,255,255)
    pygame.init()
    screen = pygame.display.set_mode((800,480))
    pygame.display.set_caption("SnipSnip")
    screen.fill(WHITE)
    screen.blit(title,(0,0))
    pygame.display.update()
    Taco = True
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z: # 'z' key for window close
                    pygame.quit()
                    return "win"  
#        for i in pins:
#            if GPIO.input(i) == 0:
#                sleep(0.5)
#                if GPIO.input(i) == 0:
#                    if i == 18:
#                        return "win"
#                    else:
#                        return "bad"
        sleep(1)
        title = pygame.image.load(os.path.join('SnipAssets',random.choice(photo)))
        screen.blit(title,(0,0))
        pygame.display.update()   
