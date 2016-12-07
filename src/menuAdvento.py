#! /usr/bin/env python
import pygame
import time
from FGAme import *
from pygame.locals import *
from sys import exit
from battlefield import Battlefield

#Inicializa o menu principal
def mainMenu():

    #inicializa os objetos do menu principal
    pygame.font.init()
    screen = pygame.display.set_mode((1300, 700), 0, 32)
    pygame.display.set_caption('ADVENTO > Menu Principal')

    init = pygame.image.load('images/opt_init.png').convert_alpha()
    exit = pygame.image.load('images/opt_exit.png').convert_alpha()


    #textos que aparecem no menu principal
    list_text = list()

    aux = 0
    #Clock e laço de update do menu principal
    clock = pygame.time.Clock()
    while True:
        if aux == 0:
            screen.blit(init,(60,300),[300,0,300,300])
        else:
            screen.blit(init,(60,300),[0,0,300,300])

        if aux == 1:
            screen.blit(exit,(1030, 300),[300,0,300,300])
        else:
            screen.blit(exit,(1030, 300),[0,0,300,300])

        #Habilita que a janela seja fechada pelo "x"
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


        #Habilita os controles do jogo pelo teclado
        pressed_keys = pygame.key.get_pressed()

        #Comandos da seta de controle do menu principal
        #Para cima
        if pressed_keys[K_LEFT]:
            aux -= 1
            time.sleep(1/7)
            if aux < 0:
                aux = 3


        #Para baixo
        if pressed_keys[K_RIGHT]:
            aux += 1
            time.sleep(1/7)
            if aux > 3:
                aux = 0

        #Confrima opção
        if pressed_keys[K_RETURN]:
            if aux == 0:
                Battlefield()
            elif aux == 1:
                pygame.quit()
                exit()

        #Atualização dos objetos na tela
        pygame.display.update()

        #Clock máximo do uptade
        time_passed = clock.tick(30)
