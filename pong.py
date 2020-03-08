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

#iniciando a função da bola
def drawBall(ballXpos, ballYpos):
    ball = pygame.rect(ballXpos, ballYpos, BALL_WIDTH, BALL_HEIGHT)
    pygame.draw.rect(screen, WHITE, ball)

#inicializando a função da raquete1
def drawPaddle1(paddle1YPos):
    paddle1 = pygame.rect(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle1)
 
 #inicializando a raquete2
def drawPaddle2(paddle2YPos):
    paddle2 = pygame.rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle2)

def updateBall(paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection):
    #atualiza posição X e Y
    ballXPos = ballYPos + ballXDirection * BALL_X_SPEED
    ballYPos = ballYPos + ballYDirection * BALL_Y_SPEED
    score = 0

    #verifica a colisão, se a bola tocar o lado esquerdo, alterna a direção
    if(ballXPos <= PADDLE_BUFFER + PADDLE_WIDTH and ballYPos + BALL_HEIGHT >= paddle1YPos and ballYPos - BALL_HEIGHT <= paddle1YPos + PADDLE_HEIGHT):
        ballXDirection = 1
    elif(ballXPos <= 0):
        ballXDirection = 1
        score = 1
        return [score, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection]

    if(ballXPos >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER and ballYPos + BALL_HEIGHT >= paddle2YPos and ballYPos - BALL_HEIGHT <= paddle2YPos + PADDLE_HEIGHT):
        ballXDirection = -1
    elif(ballXPos >= WINDOW_WIDTH - BALL_WIDTH):
        ballXDirection = -1
        score = 1
        return [score, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection]

    if(ballYPos <= 0):
        ballYPos = 0
        ballYDirection = 1
    elif(ballYDirection >= WINDOW_HEIGHT - BALL_HEIGHT):
        ballYPos = WINDOW_HEIGHT - BALL_HEIGHT
        ballYDirection = -1
        return [score, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection]
)
    