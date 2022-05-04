from Simon.Simon import Simon
from Snip.snip import SnipSnip
from Wire.Wire import WireGame
from TitleScreen.Title import Instruction, LoseScreen, WinScreen
import os
import pygame
from time import sleep



Instruction(0)
Instruction(1)
result = WireGame()
if result == "win":
    Instruction(2)
    result = Simon()
    if result == "win":
        Instruction(3)
        result = SnipSnip()
        if result == "win":
            WinScreen()
        else:
            LoseScreen()   
    else:
        LoseScreen()
else:
    LoseScreen()