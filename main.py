
import pygame
import random
import math 
from pygame import mixer
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
strin = random.randint(1,2)
strin = str( str(strin)+".wav")
mixer.music.load(strin)
mixer.music.play(-1)
# Player
playerImg = pygame.image.load('levib.png').convert_alpha()
playerImg=pygame.transform.scale(playerImg, (250, 200))
playerX = 512
playerY = 200
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
        localX=[random.randint(0, 100),random.randint(900, 1000)]
        localY=[random.randint(0, 50),random.randint(700,740 )]
        enemyX.append (localX[random.randint(0, 1)])
        enemyY.append (localY[random.randint(0, 1)])
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


myfont=pygame.font.Font("freesansbold.ttf",30)
def showscore(x,y):
	scorernd = myfont.render("Score:" + str(score),True, (255,255,255))
	screen.blit(scorernd,(x,y))
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


def spawn_enemy(i):
        localX=[random.randint(0, 100),random.randint(900, 1000)]
        localY=[random.randint(0, 50),random.randint(700,740 )]
        enemyX[i]= (localX[random.randint(0, 1)])
        enemyY[i]= (localY[random.randint(0, 1)])

over_font = pygame.font.Font('freesansbold.ttf', 50)
over_font2 = pygame.font.Font('freesansbold.ttf', 40)
#Game over text
def game_over_screen():
    over_text = over_font.render("GAME OVER!!!", True, (255, 255, 255))
    screen.blit(over_text, (300, 300))
    game_over_key()


def game_over_key():
    over_text = over_font2.render("Press up To Restart or down to End game", True, (255, 255, 255))
    screen.blit(over_text, (100, 400))

game_over_decider = False
 
# Whenever running is true game continues
# Running is false when quit button is placed.
running = True
while running:

    if game_over_decider == True:
        game_over_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        if event.type == pygame.KEYDOWN:
    
            if event.key == pygame.K_UP or event.key== pygame.K_w:
                running = True
                game_over_decider = False
                playerX = 0
                playery = 700
                score = 0
                for j in range(numofenemy): 
                    enemyY[j] = 700 - playerY


            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                running = False
        continue
            

    # filling colour in game
    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        if event.type == pygame.KEYDOWN:
    
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.8
            if event.key == pygame.K_UP or event.key== pygame.K_w:
                playerY_change = -0.8
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0.8
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_w:
                    playerY_change = 0

        
             
        #handle for the bullets top get fired in anydirection
        if event.type == pygame.MOUSEBUTTONDOWN : 
                x, y  = pygame.mouse.get_pos()
                # print(x, y) 
                
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
                    spawn_enemy(i)
                    swordY[j] = 600
                    score+=1
                    sword_state[j] = "ready"
            enemy(enemyX[i], enemyY[i] , i)
    for i in range (numofswords):
            # print(sword_angle[i])
            # print(swordX[i] , swordY[i] , sword_state[i])
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
               
              
     
    for j in range (numofenemy ):     
                isCollided =  checkforcollision(enemyX[j] ,playerX , playerY  , enemyY[j])
                if( isCollided): 
                    game_over_screen()
                    game_over_decider = True
                #    enemyX = 1000
                #    enemyY = 700
                #    running = False
       
    player(playerX, playerY)
    showscore(10,10)
   
    pygame.display.update()
