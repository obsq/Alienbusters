#  Alienbusters

# made with python 3.7.3
# PyCharm 2018.3.1
# coded on 11.07.2020
# coded by o3b3s0q1

# copyright(c) o3b3s0q1
# All rights reserved



import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("E:\packground.png")

mixer.music.load("E:\packground.wav")
mixer.music.play(-1)

pygame.display.set_caption("spacex")

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

stextx = 10
stexty = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


playerimg = pygame.image.load("E:\player.png")
playerx = 370
playery = 480


enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
no_of_enemies = 6

for i in range(no_of_enemies):
    enemyimg.append(pygame.image.load("E:\enemy.png"))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(4)
    enemyy_change.append(40)


bulletimg = pygame.image.load("E:\pullet.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = "ready"

playerx_change = 0

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))

def iscollision(enemyx, enemyy, bulletx, bullety):
    distx = enemyx - bulletx
    disty = enemyy - bullety
    distance = math.sqrt(math.pow(distx,2) + (math.pow(disty,2)))
    if distance < 27:
        return True
    else:
        return False




running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("E:\laser.wav")
                    bullet_sound.play()
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            playerx_change = 0

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    playerx += playerx_change

    if playerx <= 0:
        playerx = 0
    if playerx >= 740:
        playerx = 740


    for i in range(no_of_enemies):

        if enemyy[i] > 440:
            for j in range(no_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= -23:
            enemyx_change[i] = 4
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 740:
            enemyx_change[i] = -4
            enemyy[i] += enemyy_change[i]

        collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            explosion_sound = mixer.Sound("E:\explosion.wav")
            explosion_sound.play()
            bullety = 480
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i], enemyy[i], i)

    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change
        

    player(playerx, playery)
    show_score(stextx, stexty)
    show_high_score(hstextx, hstexty)
    pygame.display.update()
