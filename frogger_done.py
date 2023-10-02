# Retro_frogger_game

#user loads python
import pygame
import random as Random
from pygame.locals import *
from sys import exit

pygame.init()

# Text and font 
font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
info_font = pygame.font.SysFont(font_name, 24)
menu_font = pygame.font.SysFont(font_name, 36)

# --- Loading Images ---
background_filename = 'bg.png'



background = pygame.image.load(background_filename).convert()

