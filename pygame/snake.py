import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

# Score
 # (Font, size, Bold, Italic)
font = pygame.font.SysFont('Arial',40,True,True)
score = 0

# Snake
snake_x = screen_width/2 - 10
snake_y = screen_height/2 - 10
snake_speed = 5
control_x = snake_speed
control_y = 0

# Food
food_x = randint(32, 608)
food_y = randint(32, 448)
 # song
eat_song = pygame.mixer.Sound('eat_song.wav')

snake_list = []
def growth_snake(snake_list):
    for pos in snake_list:
        pygame.draw.rect(screen, (0,255,0), (pos[0], pos[1], 20, 20))

while True:
    clock.tick(60)
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Snake controls and movement
        if event.type == KEYDOWN:
            if event.key == K_a:
                if not control_x == snake_speed: # Prevents snake from reversing direction
                    control_x = -snake_speed
                    control_y = 0
            if event.key == K_d:
                if not control_x == -snake_speed:  # Prevents snake from reversing direction
                    control_x = snake_speed
                    control_y = 0
            if event.key == K_w:
                if not control_y == snake_speed:  # Prevents snake from reversing direction
                    control_x = 0
                    control_y = -snake_speed
            if event.key == K_s:
                if not control_y == -snake_speed:  # Prevents snake from reversing direction
                    control_x = 0
                    control_y = snake_speed

    snake_x += control_x
    snake_y += control_y

    # Snake shapes
    snake_head = pygame.draw.rect(screen, (0,255,0), (snake_x,snake_y,20,20))

    # Food shape
    food = pygame.draw.circle(screen, (255,0,0), (food_x,food_y), 10)

    # Snake Collision
    if snake_head.colliderect(food):
        food_x = randint(32, 608)
        food_y = randint(32, 448)
        score += 1
        eat_song.play()

    head_list = []
    head_list.append(snake_x)
    head_list.append(snake_y)
    snake_list.append(head_list)
    snake_size = score + 3
    if len(snake_list) > snake_size:
        del snake_list[0]
    growth_snake(snake_list)

    # Score
    message = f'Score: {score}'
    # (text, anti-aliasing, (R,G,B))
    formatted_text = font.render(message, False, (0,0,0))
    screen.blit(formatted_text, (450, 40))

    pygame.display.update()