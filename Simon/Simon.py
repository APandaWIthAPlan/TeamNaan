from time import sleep
import os
from random import randint
import pygame
from pygame.mixer import Sound

#pygame setup
pygame.init()


#visual assets, all single images that just load over the whole screen
WHITE = (255,255,255)
bomb = pygame.image.load(os.path.join('Assets','bomb.png'))
bombyellow = pygame.image.load(os.path.join('Assets',"bombyellow.png"))
bombred = pygame.image.load(os.path.join('Assets','bombred.png'))
bombblue = pygame.image.load(os.path.join('Assets', 'bombblue.png'))
bombgreen = pygame.image.load(os.path.join('Assets','bombgreen.png'))
bombwin = pygame.image.load(os.path.join('Assets', 'bombwin.png'))
bomball = pygame.image.load(os.path.join('Assets','bomball.png'))

#display setup
screen = pygame.display.set_mode((800,480))
pygame.display.set_caption("Simon")
screen.fill(WHITE)
screen.blit(bomb,(0,0))
pygame.display.update()
clock = pygame.time.Clock()

class Simon:

    done = False

    def __init__(self):
        self.sounds = [
            Sound(os.path.join('Assets',"one.wav")),
            Sound(os.path.join('Assets',"two.wav")),
            Sound(os.path.join('Assets',"three.wav")),
            Sound(os.path.join('Assets',"four.wav")),
            Sound(os.path.join('Assets',"uhoh.wav"))
        ]
        self.lights = [bombred,bombblue,bombyellow,bombgreen]
        self.gamekeys = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]
        self.restart()

    def all_on(self):
        screen.blit(bomball,(0,0))
        pygame.display.update()

    def all_off(self):
        screen.blit(bomb,(0,0))
        pygame.display.update()

    def lose(self):
        print("xd you lost") # xd
        self.sounds[4].play() #feel free to remove this but i find it hilarious
        sleep(0.5)
        for _ in range(0,6):
            self.sounds[1].play()
            self.all_on()
            sleep(0.1)
            self.all_off()
            sleep(0.1)

        self.done = True
        pygame.quit()

    def generate_next_value(self): # if you couldn't guess, this generates the next value
        print("Next value being generated")
        self.seq.append(randint(0,3))

    def play_sequence(self):
        print("Sequence playing")
        for s in self.seq: # for index in sequence, correct light lights up, and sound plays
            screen.blit(self.lights[s],(0,0))
            pygame.display.update()
            self.sounds[s].play()
            sleep(1)
            screen.blit(bomb,(0,0)) # sets back to original image before playing the next light 
            pygame.display.update()
            sleep(0.25)
            
        print("Sequence finished") #print statements are strewn about for debug purposes

    def user_turn(self,):
        print("It is the users turn")
        user_active = True
        num_switches_pressed = 0
        while user_active:
            clock.tick(60) # game is set at 60fps
            detected_a_press = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    return
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_c]:
                self.restart()
                return
            for i in range(len(self.gamekeys)):     #loops over each color button
                if keys_pressed[self.gamekeys[i]]:
                    detected_a_press = True
                    print("Detected a press")
                    button_index = i
                    break

            if detected_a_press:
                detected_a_press = False        # set back to false for next loop
                screen.blit(self.lights[button_index],(0,0))
                pygame.display.update()
                self.sounds[button_index].play()
                sleep(1)
                screen.blit(bomb,(0,0))
                pygame.display.update()
                sleep(0.25)

                if button_index != self.seq[num_switches_pressed]: # checks if correct button was pressed
                    user_active = False
                    self.lose()

                num_switches_pressed +=1

                if num_switches_pressed == len(self.seq): # when the amount of buttons is pressed user turn is over
                    user_active = False

    def restart(self): # resets the sequence when 'c' is pressed, also sets the sequence in the init
        self.seq = [randint(0,3), randint(0,3)]

    def win(self):
            for _ in range(0,4):
                self.sounds[3].play()
                self.all_on()
                sleep(0.1)
                self.all_off()
                sleep(0.1)
            screen.blit(bombwin,(0,0))
            pygame.display.update()
            sleep(1)

                    
    # main program
    def run(self):
        print("Welcome to Simon!")
        print("Repeat the sequence")
        while not self.done:
            if len(self.seq) == 6: # finishes game after 3 turns, add more for more, etc
                print("Woohoo you win")
                self.win()
                break  
            self.generate_next_value()
            
            self.play_sequence()
            self.user_turn()
        pygame.quit() #prevents program from hanging when done       


s = Simon()
s.run()




            
    





