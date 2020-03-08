import pygame
import random

#definindo variáveis para o jogo
FPS = 60

#tamanho da janela
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

#tamanho da 'raquete'
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

#Tamanho da bola
BALL_WIDTH = 10
BALL_HEIGHT = 10

#velocidade da raquete e da bola
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

#RGB raquete e bola
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#inicializando a tela
screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)


