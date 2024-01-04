import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Breaking Bricks")
screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

#bat
bat = pygame.image.load('./images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100

#ball
ball = pygame.image.load('./images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (200,200)
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

#brick
brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_row = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2

for y in range(brick_row):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX,brickY))

print (screen.get_height())


game_over = False
while not game_over:
    rt = clock.tick(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()
    
    if pressed[K_RIGHT]:
        bat_rect[0]+= 0.5 * rt
    elif pressed[K_LEFT]:
        bat_rect[0]-= 0.5 * rt
    elif pressed[K_SPACE]:
        ball_served = True

    if bat_rect[0] + bat_rect.width >= ball_rect[0] >= bat_rect[0] and ball_rect[1] + ball_rect.height >= bat_rect[1] and sy > 0:
        sy*= -1
        sx*= 1.01
        sy*= 1.01
        continue

    #top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy*= -1

    #left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx*= -1

    #botton
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        ball_served = False
        ball_rect.topleft = ball_start

    #rigth
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx*= -1

    if ball_served:
        ball_rect[0]+= sx
        ball_rect[1]+= sy

    screen.fill("black")
    
    for b in bricks:
        screen.blit(brick, b)

    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)



    pygame.display.update()

pygame.quit()