import pygame
import random
import math

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("jamil's gaming world! ")

#player section
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 550
X_change = 0
def player(x,y):
    screen.blit(playerImg,(x,y))
#enemy section

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemy = 6

for i in range(number_of_enemy): 
    enemyImg.append(pygame.image.load("play.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.2)
    enemyY_change.append(20)
def enemy(x,y, i):
    screen.blit(enemyImg[i],(x,y))
# bullet section
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 550
bulletX_change = 0
bulletY_change = 0.3
bullet_state = "ready"
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+10,y+10))

# collition detection
def isCollition(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# score section 
"""score_value= 0
font  = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
def show_score(x,y):
    score = font.render("score: "+ str(score_value) , True , (255,255,255))
    screen.blit(score , (x,y))"""


running = True
while running:
    screen.fill((70,70,70))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_change = -0.3
            elif event.key == pygame.K_RIGHT:
                X_change = 0.3
            
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        
        elif event.type == pygame.KEYUP:
            X_change = 0
        
     
        

    if playerX >= 770:
        playerX = 770
    elif playerX <= 0:
        playerX =  0
    
    playerX += X_change
    player(playerX,playerY)

    for i in range(number_of_enemy):
        enemyX[i] += enemyX_change[i]
        
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 770:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        
        collition = isCollition(enemyX[i],enemyY[i],bulletX,bulletY)
        if collition:
            bulletY = 550
            bullet_state = "ready"
            #score_value += 1
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)
    
        enemy(enemyX[i],enemyY[i], i )

    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

#    show_score(textX,textY)


    pygame.display.update()
        