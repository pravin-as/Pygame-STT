import pygame
import random
score = 0 
level = 6
numofswords = 10
speed=0.2 #enemy speed
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
playerImg = pygame.image.load('levib.png').convert_alpha()
playerImg=pygame.transform.scale(playerImg, (100, 150))
playerX = 512
playerY = 600
playerX_change = 0
playerY_change = 0

# Enemy
enemyX =  []
enemyImg =[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numofenemy  = level 
for i in range(numofenemy): 
        enemyImg.append (pygame.image.load('titan.jpg'))
        enemyX.append (random.randint(100, 900))
        enemyY.append (random.randint(50, 500))
        enemyX_change.append (0.3)
        enemyY_change.append (40)

# Sword
swordImg = []
swordX = []
swordY = []
swordX_change = []
swordY_change = []
sword_state = []
for i in range(numofswords): 
    swordImg.append( pygame.image.load('sword.png'))
    swordX.append( 0)
    swordY.append( 600)
    swordX_change.append( 0)
    swordY_change.append( 1)
    sword_state.append( "ready")


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy( x, y  , i):
    screen.blit(enemyImg[i], (x, y))

def checkforcollision(x1, x2 , y1 , y2): 
    Distance = ((x1-x2)**2 + (y1-y2)**2)**0.1
    if(Distance <=  2): 
        return  True
      
    return False    
counterforsword  =  0 
def throw(x, y  , i):
    global sword_state
    sword_state[i] = "fire"
    screen.blit(swordImg[i], (x + 40, y + 40))


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
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
            if event.key == pygame.K_SPACE:
                if sword_state[counterforsword] == "ready":
                    swordX[counterforsword] = playerX
                    throw(swordX[counterforsword], swordY[counterforsword] , counterforsword)
                    counterforsword+=1
                    counterforsword%=numofswords

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 935:
        playerX = 935

   
   
    
    for i in range(numofenemy):
            tan=(enemyY[i]-playerY)/ (enemyX[i]-playerX)
            #tan = l/b
            #sin= l/h
            #h=root(l2 +b2)
            #sin=l/root(l2+b2)
            #sin=tan/root(tan2+1)
            #cos=1/root(tan2+1)

            enemyX_change[i]=speed*(1/(tan**2 +1)**0.5)
            if enemyX[i]>=playerX:
                enemyX_change[i]=-abs(enemyX_change[i])
            else:
                enemyX_change[i]=abs(enemyX_change[i])

            enemyX[i] += enemyX_change[i] 
            enemyY_change[i]=speed*(tan/(tan**2 +1)**0.5)
            if enemyY[i]>=playerY:
                enemyY_change[i]=-abs(enemyY_change[i])
            else:
                enemyY_change[i]=abs(enemyY_change[i])

            enemyY[i] += enemyY_change[i] 
            
        
            # if enemyX[i] <= 0:
            #     enemyX_change[i] = 0.3
            #     enemyY[i] += enemyY_change[i]
            # if enemyX[i] >= 885:
            #     enemyX_change[i] = - 0.3
            #     enemyY[i] += enemyY_change[i]
            for j in range (numofswords):     
                isCollided =  checkforcollision(swordX[j] , enemyX[i] , enemyY[i]  , swordY[j])
                if( isCollided): 
                    enemyX[i] = random.randint(100, 900)
                    enemyY[i] = random.randint(50, 500)
                    swordY[j] = 600
                    score+=1
                    sword_state[j] = "ready"
            enemy(enemyX[i], enemyY[i] , i)
    for i in range (numofswords):
            if swordY[i] <= 0:
                swordY[i] = 600
                sword_state[i] = "ready"

            if sword_state[i] == "fire":
                throw(swordX[i], swordY[i] , i)
                swordY[i] -= swordY_change[i]
     
       
    player(playerX, playerY)
   
    pygame.display.update()
