import math
import pygame
import random

from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))

background = pygame.image.load('background.jpg')

mixer.music.load('music.mp3')
mixer.music.play()


pygame.display.set_caption("Chicken Invaders")
icon = pygame.image.load('download.jpg')
pygame.display.set_icon(icon)

jucator = pygame.image.load('racheta1.png')
jucatorX = 370
jucatorY = 480

score = 0

position1 = 0
position2 = 0

chicken = []
chickenX = []
chickenY = []
chicken_position1 = []
chicken_position2 = []
nr= 6

for i in range(nr):
    chicken.append(pygame.image.load('invader.png'))
    chickenX.append(random.randint(0,800))
    chickenY.append(random.randint(30,100))
    chicken_position1.append(1)
    chicken_position2.append(30)

bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bullet_position1 = 0
bullet_position2 = 6
status = "ready"

score_stat = 0
font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10

def scoreF(x,y) :
    score = font.render("Score :" + str(score_stat),True,(255,255,255))
    screen.blit(score,(x,y))

def jucatorF(x,y) :
    screen.blit(jucator, (x, y))

def chickenF(x,y,i) :
    screen.blit(chicken[i], (x, y))

def shotF(x,y) :
    global status
    status = "fire"
    screen.blit(bullet, (x+16,y+10))

def boom(ax,ay,bx,by) :
     d = math.sqrt((ax-bx)**2 + (ay-by)**2)
     if d < 27 :
         return True
     else :
         return False

running = True
while running :

    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                position1 = -2
            if event.key == pygame.K_RIGHT :
                position1 = 2
            if event.key == pygame.K_DOWN :
                position2 = 2
            if event.key == pygame.K_UP :
                position2 = -2
            if event.key == pygame.K_SPACE :
                if status == "ready" :
                    bullet_s = mixer.Sound('laser.wav')
                    bullet_s.play()
                    bulletX = jucatorX
                    shotF(bulletX, bulletY)
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT :
                position1 = position2 = 0

    jucatorX = jucatorX + position1
    jucatorY = jucatorY + position2

    if jucatorX <= 0:
        jucatorX = 0
    elif jucatorX >= 736 :
        jucatorX = 736

    if jucatorY <= 0:
        jucatorY = 0
    elif jucatorY >= 536:
        jucatorY = 536

    for i in range(nr) :
        chickenX[i] = chickenX[i] + chicken_position1[i]
        if chickenX[i] <= 0:
            chicken_position1[i] = 1
            chickenY[i] = chickenY[i] + chicken_position2[i]
        elif chickenX[i] >= 736 :
            chicken_position1[i] = -1
            chickenY[i] = chickenY[i] + chicken_position2[i]

        accident = boom(chickenX[i], chickenY[i], bulletX, bulletY)
        if accident:

            bulletY = jucatorY
            status = "ready"
            score_stat = score_stat + 1
            chickenX[i] = random.randint(0,800)
            chickenY[i] = random.randint(30,100)

        chickenF(chickenX[i], chickenY[i],i)

    if bulletY <= 0:
        bulletY = jucatorY
        status = "ready"

    if status == "fire" :
        shotF(bulletX, bulletY)
        bulletY = bulletY - bullet_position2



    jucatorF(jucatorX, jucatorY)
    scoreF(textX,textY)
    pygame.display.update()