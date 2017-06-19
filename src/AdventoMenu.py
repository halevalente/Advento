import advento
import pygame
import time
import random
from settings import *
from battlefield import *
from text import text_objects


def game_intro():     
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Advento", largeText, white)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        button("Começar",310,300,200,100,bright_blue,blue, game_loop)
        button("Sair",310,450,200,100,bright_red,red,quitgame)
   
        pygame.display.update()
        clock.tick(15)
		
def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
	
def game_loop():
    advento.run()

def quitgame():
	pygame.quit()

def main():
    pygame.init()

if __name__ == '__main__':
    main()

game_intro()
game_loop()

quit()