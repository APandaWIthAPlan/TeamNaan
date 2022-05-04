

# imports
import pygame
from random import randint
from time import time, sleep
from math import atan, degrees
import os

def WireGame():
    # global variables
    global countdown


    #countdown
    COUNTDOWN = 10
    start_time = time() # Used for countdown calculations later

    # window setup
    HEIGHT = 480
    WIDTH = 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Wire Scramble Game") # Window Title
    SCALE_FACTOR = HEIGHT/678 # window height over the height of the background image

    # Color presets
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BG_GREY = (58, 61, 65)
    LIGHT_GREY = (200, 200, 200)
    RED = (255, 3, 23)
    BLUE = (38, 38, 255)
    YELLOW = (255, 236, 24)
    GREEN = (3, 255, 3)

    # Framerate
    FPS = 30

    # fonts
    pygame.font.init()
    STANDARD_FONT = pygame.font.SysFont('calibri', 20, bold=True)
    COUNTDOWN_FONT = pygame.font.SysFont('monospace', 28, bold=True)

    # images
    BG = pygame.transform.scale(pygame.image.load((os.path.join('WireAssets','among_us_bg.png'))), (HEIGHT, HEIGHT))
    LIGHT = pygame.transform.scale(pygame.image.load((os.path.join('WireAssets','light.png'))), (round(39*SCALE_FACTOR), round(19*SCALE_FACTOR)))

    RED_END = pygame.transform.scale(pygame.transform.flip(pygame.image.load((os.path.join('WireAssets','red_end.png'))), True, False), (round(88*SCALE_FACTOR), round(36*SCALE_FACTOR)))
    BLUE_END = pygame.transform.scale(pygame.transform.flip(pygame.image.load((os.path.join('WireAssets','blue_end.png'))), True, False), (round(88*SCALE_FACTOR), round(36*SCALE_FACTOR)))
    YELLOW_END = pygame.transform.scale(pygame.transform.flip(pygame.image.load((os.path.join('WireAssets','yellow_end.png'))), True, False), (round(88*SCALE_FACTOR), round(36*SCALE_FACTOR)))
    GREEN_END = pygame.transform.scale(pygame.transform.flip(pygame.image.load((os.path.join('WireAssets','green_end.png'))), True, False), (round(88*SCALE_FACTOR), round(36*SCALE_FACTOR)))

    RED_WIRE = pygame.transform.scale(pygame.image.load((os.path.join('WireAssets','red_wire.png'))), (round(88*SCALE_FACTOR), round(26*SCALE_FACTOR)))
    BLUE_WIRE = pygame.transform.scale(pygame.image.load((os.path.join('WireAssets','blue_wire.png'))), (round(88*SCALE_FACTOR), round(26*SCALE_FACTOR)))
    YELLOW_WIRE = pygame.transform.scale(pygame.image.load((os.path.join('WireAssets','yellow_wire.png'))), (round(88*SCALE_FACTOR), round(26*SCALE_FACTOR)))
    GREEN_WIRE = pygame.transform.scale(pygame.image.load((os.path.join('WireAssets','green_wire.png'))), (round(88*SCALE_FACTOR), round(26*SCALE_FACTOR)))


    SELECTOR = pygame.transform.scale(pygame.image.load((os.path.join('WireAssets','selector.png'))), (round(54*SCALE_FACTOR), round(54*SCALE_FACTOR)))


    # rects list
    rects = [] # rects.append((pygame.Rect(), ))
    rects.append((pygame.Rect(HEIGHT, 0, WIDTH-HEIGHT, HEIGHT), LIGHT_GREY))
    rects.append((pygame.Rect(HEIGHT, 0, 3, HEIGHT), BLACK))

    rects.append((pygame.Rect(WIDTH-90, 0, 90, 40), BG_GREY))
    rects.append((pygame.Rect(WIDTH-92, 0, 2, 42), BLACK))
    rects.append((pygame.Rect(WIDTH-90, 40, 90, 2), BLACK))


    END_POS_1 = (round(HEIGHT-(88*SCALE_FACTOR)), round((135*SCALE_FACTOR)-(36*SCALE_FACTOR)/2)) # coords for the four wire end locations on the background
    END_POS_2 = (round(HEIGHT-(88*SCALE_FACTOR)), round((278*SCALE_FACTOR)-(36*SCALE_FACTOR)/2))
    END_POS_3 = (round(HEIGHT-(88*SCALE_FACTOR)), round((420*SCALE_FACTOR)-(36*SCALE_FACTOR)/2))
    END_POS_4 = (round(HEIGHT-(88*SCALE_FACTOR)), round((562*SCALE_FACTOR)-(36*SCALE_FACTOR)/2))

    LIGHT_POS_1 = (round(642*SCALE_FACTOR), round(100*SCALE_FACTOR)) # coords for the indicator lights next to the wire ends
    LIGHT_POS_2 = (round(642*SCALE_FACTOR), round(244*SCALE_FACTOR))
    LIGHT_POS_3 = (round(642*SCALE_FACTOR), round(386*SCALE_FACTOR))
    LIGHT_POS_4 = (round(642*SCALE_FACTOR), round(527*SCALE_FACTOR))

    SEL_POS_1 = (round(45*SCALE_FACTOR), round((133-27)*SCALE_FACTOR))
    SEL_POS_2 = (round(45*SCALE_FACTOR), round((276-27)*SCALE_FACTOR))
    SEL_POS_3 = (round(45*SCALE_FACTOR), round((420-27)*SCALE_FACTOR))
    SEL_POS_4 = (round(45*SCALE_FACTOR), round((562-27)*SCALE_FACTOR))

    WIRE_START_1 = (round(64*SCALE_FACTOR), round(133*SCALE_FACTOR))
    WIRE_START_2 = (round(64*SCALE_FACTOR), round(276*SCALE_FACTOR))
    WIRE_START_3 = (round(64*SCALE_FACTOR), round(420*SCALE_FACTOR))
    WIRE_START_4 = (round(64*SCALE_FACTOR), round(562*SCALE_FACTOR))

    WIRE_STOP_1 = (round((HEIGHT-64)*SCALE_FACTOR), round(133*SCALE_FACTOR))
    WIRE_STOP_2 = (round((HEIGHT-64)*SCALE_FACTOR), round(276*SCALE_FACTOR))
    WIRE_STOP_3 = (round((HEIGHT-64)*SCALE_FACTOR), round(420*SCALE_FACTOR))
    WIRE_STOP_4 = (round((HEIGHT-64)*SCALE_FACTOR), round(562*SCALE_FACTOR))

    wire_list = [RED_WIRE, BLUE_WIRE, YELLOW_WIRE, GREEN_WIRE]

    end_pos_list = [END_POS_1, END_POS_2, END_POS_3, END_POS_4]
    light_pos_list = [LIGHT_POS_1, LIGHT_POS_2, LIGHT_POS_3, LIGHT_POS_4]
    sel_pos_list = [SEL_POS_1, SEL_POS_2, SEL_POS_3, SEL_POS_4]

    wire_starts_list = [WIRE_START_1, WIRE_START_2, WIRE_START_3, WIRE_START_4]
    wire_stops_list = [WIRE_STOP_1, WIRE_STOP_2, WIRE_STOP_3, WIRE_STOP_4]

    WIRE_REF = (88*SCALE_FACTOR, 26*SCALE_FACTOR)


    color_names = ["RED", "BLUE", "YELLOW", "GREEN"]
    ends = [RED_END, BLUE_END, YELLOW_END, GREEN_END]
    ends_index_list = [0,1,2,3]

    done = 0
    solutions_index_list = [4]*4
    while done < 4:
        index = randint(0,3)
        if index not in solutions_index_list:
            solutions_index_list[done] = index
            done += 1

    done = 0
    colors_index_list = [4]*4
    while done < 4:
        index = randint(0,3)
        if index not in colors_index_list:
            colors_index_list[done] = index
            done += 1


    # texts list
    texts = []
    texts.append(['0', COUNTDOWN_FONT, (round(WIDTH-80), round(6)), RED])
    texts.append([f"{color_names[solutions_index_list[0]]} -> RED", STANDARD_FONT, (round(HEIGHT+((WIDTH-HEIGHT)/2)-70), round(HEIGHT/3)), eval(color_names[solutions_index_list[colors_index_list[0]]])])
    texts.append([f"{color_names[solutions_index_list[1]]} -> BLUE", STANDARD_FONT, (round(HEIGHT+((WIDTH-HEIGHT)/2)-70), round(HEIGHT/3+30)), eval(color_names[solutions_index_list[colors_index_list[1]]])])
    texts.append([f"{color_names[solutions_index_list[2]]} -> YELLOW", STANDARD_FONT, (round(HEIGHT+((WIDTH-HEIGHT)/2)-70), round(HEIGHT/3+60)), eval(color_names[solutions_index_list[colors_index_list[2]]])])
    texts.append([f"{color_names[solutions_index_list[3]]} -> GREEN", STANDARD_FONT, (round(HEIGHT+((WIDTH-HEIGHT)/2)-70), round(HEIGHT/3+90)), eval(color_names[solutions_index_list[colors_index_list[3]]])])



    def draw_window(rects, texts, images, active_lights, selected, sel_pos):

        WIN.blit(BG, (0,0))
        for I in range(4):
            WIN.blit(ends[I], end_pos_list[I])
            if active_lights[I]:
                WIN.blit(LIGHT, light_pos_list[I])

        if selected:
            WIN.blit(SELECTOR, sel_pos)
        
        for rect in rects:
            pygame.draw.rect(WIN, rect[1], rect[0])
        
        for text in texts:
            T = text[1].render(text[0], 1, text[3])
            WIN.blit(T, text[2])

        for image in images:
            WIN.blit(image[0], image[1])

        pygame.display.update()



    def main(rects, texts, start_time):
        active_lights = [False, False, False, False]
        selected = 0
        sel_pos = (0,0)
        cd_penalty = 0
        images = [] # []

        run = True
        clock = pygame.time.Clock()

        while run: ############################################################ MAIN LOOP

            countdown = COUNTDOWN - (time()-start_time) # Countdown Logic
            countdown -= cd_penalty
            if 0 < countdown < 60:
                countdown = str(round(countdown, 1))
                if float(countdown) < 10: countdown = "0" + countdown
                texts[0][0] = countdown
            elif countdown >= 60:
                countdown = round(countdown)
                countdown_m = str(countdown // 60)
                countdown_s = str(round(countdown%60))
                if int(countdown_s) < 10: countdown_s = "0" + countdown_s
                texts[0][0] = countdown_m + ":" + countdown_s

            else: # Lose condition
                texts[0][0] = "00.0"
                if len(texts) <= 5:
                    texts.append(["You Lose!", COUNTDOWN_FONT, (round(HEIGHT+(WIDTH-HEIGHT)/2-70), round(HEIGHT/2+40)), BLACK])
                winlose = "bad"
                sleep(3)
                run = False

            if active_lights == [True, True, True, True]: # Win condition
                if len(texts) <= 5:
                    texts.append(["You Win!", COUNTDOWN_FONT, (round(HEIGHT+(WIDTH-HEIGHT)/2-70), round(HEIGHT/2+40)), BLACK])
                winlose = "win"
                sleep(3)
                run = False



            clock.tick(FPS) 
            for event in pygame.event.get(): # Event Loop
                if event.type == pygame.QUIT:
                    run = False
            
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_c: # 'c' key for progress reset
                        selected = 0
                        active_lights = [False, False, False, False]
                        cd_penalty = 0
                        start_time = time()
                        for _ in range(len(texts)):
                            if len(texts) > 5: texts.pop(-1)
                        images = []
                    
                    if event.key == pygame.K_x: # 'x' key for instant win
                        selected = 0
                        active_lights = [True, True, True, True]
                    
                    if event.key == pygame.K_z: # 'z' key for window close
                        winlose = "win"
                        run = False


                    if event.key == pygame.K_a: # 'a' key for red button
                        if selected:
                            if selected-1 == solutions_index_list[0]:
                                if not active_lights[0]:
                                    x_dist = (2*wire_starts_list[0][0]) + wire_stops_list[solutions_index_list[0]][0]
                                    y_dist = wire_stops_list[0][1] - wire_starts_list[solutions_index_list[0]][1]
                                    angle = -1*degrees(atan(y_dist/x_dist))
                                    h_dist = ((x_dist**2) + (y_dist**2)) ** (1/2)
                                    image = pygame.transform.rotate(pygame.transform.scale(wire_list[solutions_index_list[0]], (round(h_dist), round(WIRE_REF[1]))), angle)
                                    y_offset = 0
                                    if y_dist > 0:
                                        y_offset = round(y_dist)
                                    images.append([image, (wire_starts_list[0][0], round(wire_starts_list[0][1]-(WIRE_REF[1]/2))-y_offset)])
                                active_lights[0] = True
                            else:
                                cd_penalty += 15
                            selected = 0
                        else:
                            sel_pos = sel_pos_list[0]
                            selected = 1
                            
                    if event.key == pygame.K_s: # 's' key for blue button
                        if selected:
                            if selected-1 == solutions_index_list[1]:
                                if not active_lights[1]:
                                    x_dist = (2*wire_starts_list[1][0]) + wire_stops_list[solutions_index_list[1]][0]
                                    y_dist = wire_stops_list[1][1] - wire_starts_list[solutions_index_list[1]][1]
                                    angle = -1*degrees(atan(y_dist/x_dist))
                                    h_dist = ((x_dist**2) + (y_dist**2)) ** (1/2)
                                    image = pygame.transform.rotate(pygame.transform.scale(wire_list[solutions_index_list[1]], (round(h_dist), round(WIRE_REF[1]))), angle)
                                    y_offset = 0
                                    if y_dist > 0:
                                        y_offset = round(y_dist)
                                    images.append([image, (wire_starts_list[1][0], round(wire_starts_list[1][1]-(WIRE_REF[1]/2))-y_offset)])
                                active_lights[1] = True
                            else:
                                cd_penalty += 15
                            selected = 0
                        else:
                            sel_pos = sel_pos_list[1]
                            selected = 2
                            
                    if event.key == pygame.K_d: # 'd' key for yellow button
                        if selected:
                            if selected-1 == solutions_index_list[2]:
                                if not active_lights[2]:
                                    x_dist = (2*wire_starts_list[2][0]) + wire_stops_list[solutions_index_list[2]][0]
                                    y_dist = wire_stops_list[2][1] - wire_starts_list[solutions_index_list[2]][1]
                                    angle = -1*degrees(atan(y_dist/x_dist))
                                    h_dist = ((x_dist**2) + (y_dist**2)) ** (1/2)
                                    image = pygame.transform.rotate(pygame.transform.scale(wire_list[solutions_index_list[2]], (round(h_dist), round(WIRE_REF[1]))), angle)
                                    y_offset = 0
                                    if y_dist > 0:
                                        y_offset = round(y_dist)
                                    images.append([image, (wire_starts_list[2][0], round(wire_starts_list[2][1]-(WIRE_REF[1]/2))-y_offset)])
                                active_lights[2] = True
                            else:
                                cd_penalty += 15
                            selected = 0
                        else:
                            sel_pos = sel_pos_list[2]
                            selected = 3
                            
                    if event.key == pygame.K_f: # 'f' key for green button
                        if selected:
                            if selected-1 == solutions_index_list[3]:
                                if not active_lights[3]:
                                    x_dist = (2*wire_starts_list[3][0]) + wire_stops_list[solutions_index_list[3]][0]
                                    y_dist = wire_stops_list[3][1] - wire_starts_list[solutions_index_list[3]][1]
                                    angle = -1*degrees(atan(y_dist/x_dist))
                                    h_dist = ((x_dist**2) + (y_dist**2)) ** (1/2)
                                    image = pygame.transform.rotate(pygame.transform.scale(wire_list[solutions_index_list[3]], (round(h_dist), round(WIRE_REF[1]))), angle)
                                    y_offset = 0
                                    if y_dist > 0:
                                        y_offset = round(y_dist)
                                    images.append([image, (wire_starts_list[3][0], round(wire_starts_list[3][1]-(WIRE_REF[1]/2))-y_offset)])
                                active_lights[3] = True
                            else:
                                cd_penalty += 15
                            selected = 0
                        else:
                            sel_pos = sel_pos_list[3]
                            selected = 4


            draw_window(rects, texts, images, active_lights, selected, sel_pos)

        pygame.quit()
        return winlose
        

    return main(rects, texts, start_time)
