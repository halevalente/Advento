import pygame

display_width = 800
display_height = 600
 
#color
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
blue = (0, 0, 200)
bright_red = (255,0,0)
bright_blue = (0,0,255)

screen = pygame.display.set_mode((800, 600), 0, 32) 
# background = pygame.image.load('images/espaco.png').convert()       

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Advento')
clock = pygame.time.Clock()