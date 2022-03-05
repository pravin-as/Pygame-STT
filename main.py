import pygame
import random
import math 
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
playerImg=pygame.transform.scale(playerImg, (250, 200))
playerX = 512
playerY = 550
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
sword_angle = []
for i in range(numofswords): 
    swordImgtemp= pygame.image.load('sword2.png').convert_alpha()
    swordImgtemp=pygame.transform.scale(swordImgtemp, (50,50))
    swordImg.append(swordImgtemp)
    swordX.append( 0)
    swordY.append( 600)
    swordX_change.append( 0)
    swordY_change.append( 1)
    sword_state.append( "ready")
    sword_angle.append(0)


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
            if event.key == pygame.K_UP:
                playerY_change = -0.8
            if event.key == pygame.K_DOWN:
                playerY_change = 0.8
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_DOWN  or event.key == pygame.K_UP:
                    playerY_change = 0
        #handle for the bullets top get fired in anydirection
        if event.type == pygame.MOUSEBUTTONDOWN : 
                x, y  = pygame.mouse.get_pos()
                print(x, y) 
                
                if sword_state[counterforsword] == "ready":
                    swordX[counterforsword] = playerX
                    swordY[counterforsword] = playerY
                    sword_angle[counterforsword] = math.atan2(y-playerY , x- playerX)
                    # print(sword_angle[counterforsword])
                    throw(swordX[counterforsword], swordY[counterforsword] , counterforsword)
                    counterforsword+=1
                    counterforsword%=numofswords
       
              
    playerX += playerX_change
    playerY +=  playerY_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 935:
        playerX = 935

    if playerY <= 0:
        playerY = 0
    if playerY >= 600:
        playerY = 600

   
   
    
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
            print(sword_angle[i])
            print(swordX[i] , swordY[i] , sword_state[i])
            dx  = 2.0*math.cos(sword_angle[i])
            dy  = 3.0*math.sin(sword_angle[i])
            swordX[i]+=dx
            swordY[i]+=dy
            if swordX[i] <= 0 or swordX[i] >= 900 : 
                swordY[i] = playerY 
                sword_angle[i] =  0
                sword_state[i] = "ready"
            if swordY[i] <= 0 or swordY[i] >=600 :
                swordY[i] = playerY
                sword_angle[i] =  0
                sword_state[i] = "ready"
            
            if sword_state[i] == "fire":
                throw(swordX[i], swordY[i] , i)
               
              
     
       
    player(playerX, playerY)
   
    pygame.display.update()
