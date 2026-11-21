import math
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Add more Sprites")
clock = pygame.time.Clock()

background = pygame.Surface((800, 500))
background.fill((30, 30, 60))

playerImg = pygame.Surface((64, 64), pygame.SRCALPHA)
pygame.draw.rect(playerImg, (50, 180, 255), (8, 8, 48, 48), border_radius=8)
pygame.draw.polygon(playerImg, (255, 255, 255), [(32, 0), (18, 18), (46, 18)])

enemyImg = pygame.Surface((64, 64), pygame.SRCALPHA)
pygame.draw.rect(enemyImg, (255, 80, 80), (8, 8, 48, 48), border_radius=12)
pygame.draw.circle(enemyImg, (255, 255, 255), (24, 30), 5)
pygame.draw.circle(enemyImg, (255, 255, 255), (40, 30), 5)

font = pygame.font.Font(None, 32)

# Player
playerX = 370
playerY = 380
playerX_change = 0
playerY_change = 0
score = 0

num_of_enemies = 7
enemyX = []
enemyY = []
for _ in range(num_of_enemies):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 400))


def isCollision(x1, y1, x2, y2):
    distance = math.sqrt(((x1 + 32) - (x2 + 32)) ** 2 + ((y1 + 32) - (y2 + 32)) ** 2)
    return distance < 40


running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playerX_change = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    playerX = max(0, min(playerX, 736))
    playerY = max(0, min(playerY, 436))

    for i in range(num_of_enemies):
        if isCollision(playerX, playerY, enemyX[i], enemyY[i]):
            score += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 400)
        screen.blit(enemyImg, (enemyX[i], enemyY[i]))

    screen.blit(playerImg, (playerX, playerY))
    screen.blit(font.render("Score : " + str(score), True, (255, 255, 255)), (10, 10))
    pygame.display.update()
    clock.tick(60)