import pygame
import random

# Initialise the game
pygame.init();

# create screen
screen = pygame.display.set_mode((1024, 768))

# Background
background = pygame.image.load("wallpaper.png")

# Title and Icon
pygame.display.set_caption("Attack on Titans")
icon = pygame.image.load("logo.png")
pygame.display.set_icon((icon))

# Player
playerImg = pygame.image.load('levi.png')
playerX = 512
playerY = 600
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('titan.jpg')
enemyX = random.randint(100, 900)
enemyY = random.randint(50, 500)
enemyX_change = 0.3
enemyY_change = 40

# Sword
swordImg = pygame.image.load('sword.png')
swordX = 0
swordY = 600
swordX_change = 0
swordY_change = 1
sword_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def throw(x, y):
    global sword_state
    sword_state = "fire"
    screen.blit(swordImg, (x + 40, y + 40))


# Whenever running is true game continues
# Running is false when quit button is placed.
running = True
while running:

    # filling colour in game
    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if sword_state == "ready":
                    swordX = playerX
                    throw(swordX, swordY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 935:
        playerX = 935

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    if enemyX >= 885:
        enemyX_change = - 0.3
        enemyY += enemyY_change

    if swordY <= 0:
        swordY = 600
        sword_state = "ready"

    if sword_state == "fire":
        throw(swordX, swordY)
        swordY -= swordY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
