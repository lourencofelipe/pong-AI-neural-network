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

#atualiza movimento da raquete1
def updatePaddle1(action, paddle1YPos):
    #se mover para cima
    if(action[1] == 1):
        paddle1YPos = paddle1YPos - PADDLE_SPEED
    #se mover para baixo
    if(action[2] == 1):
        paddle1YPos = paddle1YPos - PADDLE_SPEED
    
    #não deixa sair da tela
    if(paddle1YPos < 0):
        paddle1YPos = 0
    if(paddle1YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle1YPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle1YPos

def updatePaddle2(paddle2YPos, ballYPos):
    
    if (paddle2YPos + PADDLE_HEIGHT/2 < ballYPos + BALL_HEIGHT/2):
        paddle2YPos = paddle2YPos + PADDLE_SPEED
    #move para cima
    if (paddle2YPos + PADDLE_HEIGHT/2 > ballYPos + BALL_HEIGHT/2):
        paddle2YPos = paddle2YPos - PADDLE_SPEED
    #não deixa a bola tocar o topo
    if (paddle2YPos < 0):
        paddle2YPos = 0
    #não deixa a bola tocar a parte inferior
    if (paddle2YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle2YPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle2YPos

class PongGame:
    def __init__ (self):
       #definindo número aleatório para direção inicial da bola
        num = random.randInt(0, 9)
        #recupera o ponto
        self.tally = 0
        #Inicializando a posição inicial da raquete
        self.paddle1YPos = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
        self.paddle2YPos  = WINDOW_HEIGHT  / 2 - PADDLE_HEIGHT / 2
        #definindo a direção da bola
        self.ballXDirection = 1
        self.ballYDirection = 1
        #ponto inicial
        self.ballXpos = WINDOW_HEIGHT /2 - BALL_WIDTH / 2

    def getPresentFrame(self):
        #Para cada frame é chamado o evento da fila
        pygame.event.pump()
        #deixando o background preto
        screen.fill(BLACK)
        #desenhando as raquetes
        drawPaddle1(self.paddle1YPos)
        drawPaddle2(self.paddle2YPos)
        #desenhando a bola
        drawBall(self.ballXDirection, self.ballYDirection)
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        #atualizando a janela
        pygame.display.flip()
        #retorna os dados da imagem
        return image_data
