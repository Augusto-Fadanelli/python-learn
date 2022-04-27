# pip install pygame

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 640
height = 480
screen = pygame.display.set_mode((width, height)) # Cria janela com o tamanho especificado
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()

# Movement of rect
# Inicializa no centro da tela
rect_x = width/2 - 40/2
rect_y = height/2 - 50/2

# Movement of player
player_x = width/2
player_y = height/2

# Loop do jogo
while True:
    clock.tick(60) # Seta o fps do jogo
    # Preenche a tela com a cor definida (R,G,B)
    screen.fill((0,0,0))
    # Checar eventos a cada iteração
    for event in pygame.event.get():
        # Fecha janela
        if event.type == QUIT:
            pygame.quit()
            exit()
        # Se tecla foi pressionada
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                player_x -= 5 # Move para a esquerda
            if event.key == K_d:
                player_x += 5 # Move para a direita
            if event.key == K_w:
                player_y -= 5 # Move para cima
            if event.key == K_s:
                player_y += 5 # Move para baixo
        '''
        # Se a tecla está sendo pressionada
        if pygame.key.get_pressed()[K_a]:
            player_x -= 5 # Move para a esquerda
        if pygame.key.get_pressed()[K_d]:
            player_x += 5 # Move para a direita
        if pygame.key.get_pressed()[K_w]:
            player_y -= 5 # Move para cima
        if pygame.key.get_pressed()[K_s]:
            player_y += 5 # Move para baixo

    # Shapes
    # Forma(screen, (R,G,B), (x,y), raio) | Coordenada no centro do circle
    pygame.draw.circle(screen, (0,0,255), (100, 100), 40)
    # Forma(screen, (R,G,B), (x,y), (x,y), espessura) | Coordenadas do primeiro e segundo pontos
    pygame.draw.line(screen, (255,255,0), (300, 0), (400, 480), 5)
    # Forma(screen, (R,G,B), (x,y,width,height)) | Coordenada no canto superior esquerdo do rect
    pygame.draw.rect(screen, (255,0,0), (rect_x, rect_y, 40, 50))

    # Player
    pygame.draw.circle(screen, (222,144,138), (player_x,player_y), 15)

    # Movement of rect
    if rect_x == width:
        rect_x = 0
    if rect_y == height:
        rect_y = 0
    rect_x += 10
    rect_y += 1

    # Atualiza
    pygame.display.update()

