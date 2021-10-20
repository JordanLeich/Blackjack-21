from pygame import *
import pygame
from random import randint


def bad_luck():
    mixer.init()
    soundObj = pygame.mixer.Sound('sounds/badluck.wav')
    soundObj.play()


def good_luck():
    mixer.init()
    number = randint(1, 2)
    if number == 1:
        soundObj = pygame.mixer.Sound('sounds/goodluck.wav')
        soundObj.play()
    elif number == 2:
        soundObj = pygame.mixer.Sound('sounds/cashreg.wav')
        soundObj.play()
