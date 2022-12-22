#Singleplayer, turn-based RPG.
#Edigon
#Ayman Mohammad, Jonah Bron
#January 5th, 2019


'''IMPORTING MODULES'''

import pygame 
import time
import pygame_textinput


'''INITIALIZATION'''

pygame.init()
pygame.font.init()
pygame.mixer.init()

gameDisplay = pygame.display.set_mode((1280,720)) #Makes the resolution 1280x720p
pygame.display.set_caption("Edigon") #Renames the window title appropriately
pygame.display.set_icon(pygame.image.load("sword.png")) #Changes the icon of the window


'''VARIABLE LIST - Jonah'''

fadeTick = 60
Username = "" 

FirstCreditY = -200 # Where the first credit is positioned
SecondCreditY = -300 # Where the second credit is positioned
ThirdCreditY = -400 # Where the third credit is positioned
FourthCreditY = -500 # Where the fourth credit is positioned
FifthCreditY = -600 # Where the fifth credit is positioned
SixthCreditY = -700 # Where the sixth credit is positioned

'''VARIABLE LIST - Ayman'''

clock = pygame.time.Clock() #Frames per second

vel = 5 #Character's speed

bVel = 6 #Enemy attack's speed

xChar = 640 #Character's x value
yChar = 420 #Character's y value

bullet1X = -50 #First bullet x value
bullet1Y = 459 #First bullet y value

bullet2X = -50 #Second bullet x value
bullet2Y = 518 #Second bullet y value

bullet3X = -50 #Third bullet x value
bullet3Y = 333 #Third bullet y value

healthPoint = 200 #Primary variable for player's health
newHealth = 200 #Secondary variable for player's health

boss_healthPoint = 200 #Primary variable for boss's health bar
boss_newHealth = 200 #Secondary variable for boss's health bar

sPos = 426 #Selection indicator's location

pWidth = 200 #Width of player's health bar
bWidth = 200 #Width of boss's health bar

attackX = 429 #X value of selection indicator for fight menu
attackY = 347 #Y value of selection indicator for fight menu
attackXY = (attackX,attackY) #Previous two variables combined for more versatility

fireballX = 1280 #Fireball's x value
fireballY = 100 #Fireball's y value

star1X = 1280 #First star's x value
star2X = 1303 #Second star's x value
star3X = 1303 #Third star's x value

star1Y = 140 #First star's y value
star2Y = 100 #Second star's y value
star3Y = 180 #Third star's y value

dazzleX = 1280 #Sword's x value
dazzleY = 145 #Sword's y value

rainX = 1280 #Whirlpool's x value
rainY = 100 #Whirlpool's y value


'''BOOLEAN VARIABLE LIST (LOGIC) - Jonah'''

gameExit = False # Variable that makes a loop constantly run.

UserNameCompleted = False
howDarkCompleted = False # Variable used for the fading of the text in the beginning.
running = True # Variable that makes a loop constantly run.
MainMenuRunning = True
Hovered = False # Variable is set to true if hovered over a text. But used in mostly when there is a click.
TestingStages = True # Just used for some print functions to check for errors.

'''BOOLEAN VARIABLE LIST (LOGIC) - Ayman'''

gameExit = False #Determines if game is running or not

playerDead = False #Determines if player is dead or not (lost battle)
bossDead = False #Determines if the boss is dead or not (won battle)

playerAttack = False #Determines if player is attacking or defending
playerDefense = True #Determines if player is defending or attacking

selectionAttack = False #Determines if the fight menu is activated or not
attackSelect = False #Determines if the player is selecting an attack or not

starSplitter = False #Determines if they confirmed this move or not
dazzleSlash = False #Determines if they confirmed this move or not
rainCutter = False #Determines if they confirmed this move or not
fireBall = False #Determines if they confirmed this move or not

skeleHit = False #Determines if the enemy has been hit or not


'''COUNTER VARIABLE LIST & RGB COLOURS - Jonah'''

CurrentCharacters = 0 # Current characters to check to see if you used to many characters.
ThanksForPlayingY = 0
x = 0
yellow = (255,255,0) # Color

'''COUNTER VARIABLE LIST & RGB COLOURS - Ayman'''

stillCount = 0 # A counter, used to count.
skeleCount = 0 # A counter, used to count.
skeleframeCount = 0 # A counter, used to count.

black = (0,0,0) # The shade black.
white = (255,255,255) # The tint white
red = (255, 0, 0) # The color red
hpYellow = (250,255,0) #Health bar colour
btnOrange = (255,138,0) #Button colours
hpBorder = (222,199,0) #Health bar border colour


'''SOUND LIBRARY - Jonah'''

pygame.mixer.music.load('MenuClickButton.wav') # Loads minecraft sound

'''SPRITE LIST & SOUND LIBRARY - Ayman'''

'''---------[Sprites]---------'''

#Player
combatAvatar = pygame.image.load("Avatar.png").convert_alpha()

#Skeleton Still Animation
skeleSprite = [pygame.image.load("Skele/SP1.png"),pygame.image.load("Skele/SP2.png"),pygame.image.load("Skele/SP3.png"),pygame.image.load("Skele/SP4.png"),pygame.image.load("Skele/SP5.png"),pygame.image.load("Skele/SP6.png"),pygame.image.load("Skele/SP7.png"),pygame.image.load("Skele/SP8.png"),pygame.image.load("Skele/SP9.png"),pygame.image.load("Skele/SP10.png"),pygame.image.load("Skele/SP11.png")]

#Skeleton Damaged Animation
skeleSprite2 = [pygame.image.load("Skele/SH1.png"),pygame.image.load("Skele/SH2.png"),pygame.image.load("Skele/SH3.png"),pygame.image.load("Skele/SH4.png"),pygame.image.load("Skele/SH5.png"),pygame.image.load("Skele/SH6.png"),pygame.image.load("Skele/SH7.png"),pygame.image.load("Skele/SH8.png")]

#Bone Arrow
boneAttack = pygame.image.load("boneAttack.png").convert_alpha()

#Fireball
fireballSprite = pygame.image.load("Fireball.png") # Loads the image

#Select Indicator
selectArrow = pygame.image.load("selectArrow.png") # Loads the image

#Stars
starSprite = pygame.image.load("Star.png") # Loads the image

#Dazzledash Sword
swordSprite = pygame.image.load("Dazzleslash.png") # Loads the image

#Whirlpool
waterSprite = pygame.image.load("Rain Cutter.png") # Loads the image

#Turning bone-arrows and player's avatar into masks for collision detection
''' First attack '''
bullet1 = pygame.mask.from_surface(boneAttack)
bullet2 = pygame.mask.from_surface(boneAttack)
bullet3 = pygame.mask.from_surface(boneAttack)
''' Second attack '''
bullet4 = pygame.mask.from_surface(boneAttack)
bullet5 = pygame.mask.from_surface(boneAttack)
bullet6 = pygame.mask.from_surface(boneAttack)

combatMask = pygame.mask.from_surface(combatAvatar)

'''---------[Sounds]---------'''

fireballFX = pygame.mixer.Sound("Fireball.wav") # Fireball sound 
fireballFX.set_volume(0.1) # Sets the volume 

starFX = pygame.mixer.Sound("Star.wav") # Star sound
starFX.set_volume(0.1) # Sets the volume 

slashFX = pygame.mixer.Sound("Slash.wav") # Slash sound
slashFX.set_volume(0.1) # Sets the volume 

waterFX = pygame.mixer.Sound("Water.wav") # Water sound
waterFX.set_volume(0.1) # Sets the volume 


'''AYMAN'S FUNCTIONS'''

#Player Avatar

def combatChar(xChar,yChar): # Combat function
    global combatMask
    global playerDefense, playerAttack

    if playerDefense is False and playerAttack:
        return
    else:
        combatRect = combatAvatar.get_rect()
        cX = xChar - combatRect.center[0]
        cY = yChar - combatRect.center[1]
        gameDisplay.blit(combatAvatar,(cX,cY))

        characterMove()

#Combat Box (Border)

def combatBox(): # Makes the combat Box
    gameDisplay.fill(white, rect=[390,299,10,250])
    gameDisplay.fill(white, rect=[881,299,10,250])
    gameDisplay.fill(white, rect=[400,299,481,10])
    gameDisplay.fill(white, rect=[400,539,481,10])

#Player Stats

def playerStats(): # Displays the players stats
    global newHealth
    global hpYellow
    global hpBorder
    global pWidth

    size1 = pygame.font.SysFont("Palatino Linotype",18) # Font
    size1.set_bold(True) # Sets the font to bold
    
    PlayerName = size1.render(Username, False, (white)) # Displays the username.
    PlayerLevel = size1.render("LV. 100", False, (white)) # Displays the level.
    HP = size1.render("HP", False, (white)) # Displays the Hp
    hpNum = size1.render(str(newHealth)+"/200", False, (white)) # Displays the HP is a number

    '''[Name, Level & HP]'''

    gameDisplay.blit(PlayerName,(319,585)) # Draws the players name.
    gameDisplay.blit(PlayerLevel,(464,585)) # Draws the players Level.
    gameDisplay.blit(HP,(580,585)) # Draws the players HP.
    gameDisplay.fill(hpYellow, rect=[620,580,pWidth,30])
    gameDisplay.blit(hpNum,(834,589))

    '''[HP Border]'''
    
    gameDisplay.fill(hpBorder, rect=[616,580,4,30])
    gameDisplay.fill(hpBorder, rect=[820,580,4,30])
    gameDisplay.fill(hpBorder, rect=[616,576,208,4])
    gameDisplay.fill(hpBorder, rect=[616,610,208,4])

#Boss Stats

def bossStats():
    global boss_healthPoint
    global hpYellow
    global hpBorder
    global bWidth

    size1 = pygame.font.SysFont("Palatino Linotype",18)
    size1.set_bold(True)
    
    bossLevel = size1.render("Boss Level: 100", False, (white))
    bossHP = size1.render("HP", False, (white))
    hpNum = size1.render(str(boss_healthPoint)+"/200", False, (white))

    '''[Level & HP]'''

    gameDisplay.blit(bossLevel,(355,30))
    gameDisplay.blit(bossHP, (792,30))
    gameDisplay.fill(hpYellow, rect=[833,21,bWidth,30])
    gameDisplay.blit(hpNum, (1047,30))

    '''[HP Border]'''

    gameDisplay.fill(hpBorder, rect=[833,51,200,4])
    gameDisplay.fill(hpBorder, rect=[833,17,200,4])
    gameDisplay.fill(hpBorder, rect=[829,17,4,38])
    gameDisplay.fill(hpBorder, rect=[1033,17,4,38])

#Fight Button

def combatButtons():
    btnTxt = pygame.font.SysFont("Arial Black",24)
    btnTxt.set_bold(True)
    
    btnFight = gameDisplay.fill(btnOrange, rect=[461,629,345,61])
    fightTxt = btnTxt.render("FIGHT", False, (white))
    gameDisplay.blit(fightTxt, (582, 643))

#Skeleton Sprite Still

def fightSkele():
    global stillCount
    global skeleHit
    # Function for animating sprite
    if skeleHit == True:
        return

    if stillCount + 1 >= 60:
        stillCount = 0

    gameDisplay.blit(skeleSprite[stillCount//6], (585,67))
    stillCount += 1

#Skeleton Sprite Damaged
    
def dmgSkele():
    global skeleCount
    global skeleframeCount
    global skeleHit
    # Function for animating sprite
    if skeleHit == False:
        return
    
    if skeleframeCount == 1:
        return

    if skeleCount + 1 >= 60:
        skeleCount = 0

    gameDisplay.blit(skeleSprite2[skeleCount//10], (585,67))
    skeleCount += 1

    if skeleCount == 59:
        skeleframeCount += 1   

#Boss Name

def bossName():
    # Displays the boss name and outlines the rectangle as white
    skeleName = pygame.font.Font("FrankRuhlLibre-Black.ttf", 18)
    Balhazar = skeleName.render("BALHAZAR THE UNDEAD", False, (white))
    gameDisplay.blit(Balhazar, (528,28))

    gameDisplay.fill(white, rect=[516,25,4,30])
    gameDisplay.fill(white, rect=[760,25,4,30])
    gameDisplay.fill(white, rect=[516,25,248,4])
    gameDisplay.fill(white, rect=[516,51,248,4])

#Boss Attack

def bossAttack():
    global bullet1, bullet2, bullet3
    global bullet1X, bullet2X, bullet3X
    global xChar, yChar
    global combatMask
    global healthPoint
    global newHealth
    global pWidth
    global playerDead
    global playerDefense, playerAttack
    global attackSelect
    global starSplitter, dazzleSlash, rainCutter, fireBall
    ## Draws the projectiles, moves them in the direction of your character.
    if playerDefense is False and playerAttack:
        bullet1X = -50
        bullet2X = -50
        bullet3X = -50
        return
    
    if bullet1X == 1330:
        playerDefense = False
        playerAttack = True
        attackSelect = False
        starSplitter = False
        dazzleSlash = False
        rainCutter = False
        fireBall = False
        return

    if bullet1X != 1330:
        bullet1X += bVel
    gameDisplay.blit(boneAttack, (bullet1X, bullet1Y))
    
    if bullet2X != 1330:
        bullet2X += bVel
    gameDisplay.blit(boneAttack, (bullet2X, bullet2Y))

    if bullet3X != 1330:
        bullet3X += bVel
    gameDisplay.blit(boneAttack, (bullet3X, bullet3Y))
    # Hit detection
    offset = round(xChar) - bullet1X, round(yChar) - bullet1Y 
    result = bullet1.overlap(combatMask, offset)
    if result:
        healthPoint -= 2
        pWidth -= 2
        newHealth = str(healthPoint)
        # Sounds that are trigger when health is 50 or below.
        if healthPoint <= 50:
            pygame.mixer.music.load("LowHP.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1,0.0)
        if healthPoint == 0:
            newHealth = "0"
            playerDead = True

    offset2 = round(xChar) - bullet2X, round(yChar) - bullet2Y
    result2 = bullet2.overlap(combatMask, offset2)
    if result2:
        healthPoint -= 2
        pWidth -= 2
        newHealth = str(healthPoint)
        # Sounds that are trigger when health is 50 or below.
        if healthPoint <= 50:
            pygame.mixer.music.load("LowHP.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1,0.0)
        if healthPoint == 0:
            newHealth = "0"
            playerDead = True

    offset3 = round(xChar) - bullet3X, round(yChar) - bullet3Y
    result3 = bullet2.overlap(combatMask, offset3)
    if result3:
        healthPoint -= 2
        pWidth -= 2
        newHealth = str(healthPoint)
        # Sounds that are trigger when health is 50 or below.
        if healthPoint <= 50:
            pygame.mixer.music.load("LowHP.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1,0.0)
        if healthPoint == 0:
            newHealth = "0"
            playerDead = True

#Fight Moves Menu

def attackMoves():
    global attackSelect
    global starSplitter 
    global dazzleSlash
    global rainCutter 
    global fireBall
    # Draws fight menu and displays it to the screen.
    if attackSelect == False:
        return
    elif starSplitter == True:
        return
    elif dazzleSlash == True:
        return
    elif rainCutter == True:
        return
    elif fireBall == True:
        return
    else:
        if playerDefense is False and playerAttack:
            attack = pygame.font.SysFont("Palatino Linotype", 24)
            attack.set_bold(True)
            attack1 = attack.render("Star Splitter", False, (white))
            attack2 = attack.render("Dazzleslash", False, (white))
            attack3 = attack.render("Rain Cutter", False, (white))
            attack4 = attack.render("Fireball", False, (white))
            gameDisplay.blit(attack1, (461,347))
            gameDisplay.blit(attack2, (690,347))
            gameDisplay.blit(attack3, (461,468))
            gameDisplay.blit(attack4, (690,468))
            gameDisplay.blit(selectArrow,(attackXY))
            

'''EVENT HANDLER FUNCTIONS'''
        
#Character Movement

def characterMove():
    global xChar, yChar, vel
    # Event handler for the character movement. Keeps player from moving once it hits the edge of the rectangle.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        xChar -= vel
    if keys[pygame.K_d]:
        xChar += vel
    if keys[pygame.K_w]:
        yChar -= vel
    if keys[pygame.K_s]:
        yChar += vel

    if xChar <= 416.5:
        xChar = 416.5
    if xChar >= 863.5:
        xChar = 863.5
    if yChar <= 323:
        yChar = 323
    if yChar >= 524:
        yChar = 524

        '''This function goes into combatChar(xChar,yChar)'''

#Button Selection

def btnSelect():
    global sPos
    global selectionAttack, attackSelect
    global playerDefense, playerAttack

    keys = pygame.key.get_pressed()
    # Event handler, which controls the button selection.
    if playerAttack and playerDefense is False:
        
        if not attackMoves() and keys[pygame.K_z]:
            selectionAttack = True
            
        if keys[pygame.K_z] and sPos == 426:
            attackSelect = True
            
        if attackSelect == True and keys[pygame.K_x]:
            attackSelect = False

#Menu Movement

def moveSelect():
    global attackXY
    
    keys = pygame.key.get_pressed()
    # Event handler, which selects which attack you will use.
    if attackSelect == True:
        if keys[pygame.K_d] and attackXY == (429,347): #Star Splitter --> Dazzleslash
            attackXY = (658,347)
        if keys[pygame.K_a] and attackXY == (658,347): #Dazzleslash --> Star Splitter
            attackXY = (429,347)
        if keys[pygame.K_s] and attackXY == (429,347): #Star Splitter --> Rain Cutter
            attackXY = (429,468)
        if keys[pygame.K_w] and attackXY == (429,468): #Rain Cutter --> Star Splitter
            attackXY = (429,347)
        if keys[pygame.K_s] and attackXY == (658,347): #Dazzleslash --> Fireball
            attackXY = (658,468)
        if keys[pygame.K_w] and attackXY == (658,468): #Fireball --> Dazzleslash
            attackXY = (658,347)
        if keys[pygame.K_d] and attackXY == (429,468): #Rain Cutter --> Fireball
            attackXY = (658,468)
        if keys[pygame.K_a] and attackXY == (658,468): #Fireball --> Rain Cutter
            attackXY = (429,468)

        confirmSelect()

#Move Selection

def confirmSelect():
    global attackSelect
    global starSplitter 
    global dazzleSlash
    global rainCutter 
    global fireBall
    global selectionAttack
    global skeleHit
    global playerDefense, playerAttack
    global boss_healthPoint
    global boss_newHealth
    global bWidth

    keys = pygame.key.get_pressed()
    # Event handler, which confirms the move you will be using.
    if selectionAttack == True:
        if attackXY == (429,347) and keys[pygame.K_RETURN]:
            starSplitter = True
        elif attackXY == (658,347) and keys[pygame.K_RETURN]:
            dazzleSlash = True
        elif attackXY == (429,468) and keys[pygame.K_RETURN]:
            rainCutter = True
        elif attackXY == (658,468) and keys[pygame.K_RETURN]:
            fireBall = True
            
    if starSplitter == True:
        attack1()
        starAttack()
        selectionAttack = False
    elif dazzleSlash == True:
        attack2()
        slashAttack()
        selectionAttack = False
    elif rainCutter == True:
        attack3()
        waterAttack()
        selectionAttack = False
    elif fireBall == True:
        attack4()
        fireballAttack()
        selectionAttack = False
            
        '''This function has been called in moveSelect()'''


'''PLAYER ATTACKS (FUNCTIONS)'''

'''[Sprites]'''
# These functions draw and animate the sprites.
def starAttack():
    global star1X
    global star2X
    global star3X
    global star1Y
    global star2Y
    global star3Y
    global skeleHit
    global bullet1X
    global bullet2X
    global bullet3X
    global playerDefense
    global starSplitter

    if playerDefense and playerAttack is False:
        star1X = 1280
        star2X = 1303
        star3X = 1303
        return

    else:
        if star1X != -68:
            star1X -= 4
        gameDisplay.blit(starSprite, (star1X, star1Y))

        if star2X != -45:
            star2X -= 5
        gameDisplay.blit(starSprite, (star2X, star2Y))

        if star3X != -45:
            star3X -= 5
        gameDisplay.blit(starSprite, (star3X, star3Y))

        if star1X <= 640:
            skeleHit = True
            dmgSkele()
            starFX.play(0,0)
            #light up effect
        if star1X <= 340:
            skeleHit = False
            starFX.stop()

                
def slashAttack():
    global dazzleX
    global dazzleY
    global skeleHit

    if playerDefense and playerAttack is False:
        dazzleX = 1280
        return

    else:
        gameDisplay.blit(swordSprite, (dazzleX,dazzleY))

        if dazzleX != -196:
            dazzleX -= 6

        if dazzleX <= 636:
            skeleHit = True
            dmgSkele()
            slashFX.play(0,0)
        if dazzleX <= 270:
            skeleHit = False
            slashFX.stop()


def waterAttack():
    global rainX
    global rainY
    global skeleHit

    if playerDefense and playerAttack is False:
        rainX = 1280
        return

    else:
        gameDisplay.blit(waterSprite, (rainX,rainY))

        if rainX != -196:
            rainX -= 6

        if rainX <= 637:
            skeleHit = True
            dmgSkele()
            waterFX.play(0,0)
        if rainX <= 270:
            skeleHit = False
            waterFX.stop()

def fireballAttack():
    global fireballX
    global fireballY
    global skeleHit

    if playerDefense and playerAttack is False:
        fireballX = 1280
        return

    else:
        gameDisplay.blit(fireballSprite, (fireballX,fireballY))

        if fireballX != -550:
            fireballX -= 5
        if fireballX <= 637:
            skeleHit = True
            dmgSkele()
            fireballFX.play(0,0)
        if fireballX <= 270:
            skeleHit = False
            fireballFX.stop()

'''[Dialogue]'''
# These functions generate dialogue when you attack.
def attack1():
    global star1X
    global playerDefense, playerAttack

    if playerDefense and playerAttack is False:
        return

    if star1X == -68:
        playerDefense = True
        playerAttack = False
    else:
        attack = pygame.font.SysFont("Palatino Linotype", 24)
        attack.set_bold(True)
        starAttack = attack.render("You used...Star Splitter!", False, (white))
        gameDisplay.blit(starAttack, (432, 347))

def attack2():
    global dazzleX
    global playerDefense, playerAttack
    
    if playerDefense and playerAttack is False:
        return
    
    if dazzleX == -196:
        playerDefense = True
        playerAttack = False
    else:
        attack = pygame.font.SysFont("Palatino Linotype", 24)
        attack.set_bold(True)
        dazzleAttack = attack.render("You used...Dazzleslash!", False, (white))
        gameDisplay.blit(dazzleAttack, (432, 347))

def attack3():
    global rainX
    global playerDefense, playerAttack

    if playerDefense and playerAttack is False:
        return

    if rainX == -196:
        playerDefense = True
        playerAttack = False
    else:
        attack = pygame.font.SysFont("Palatino Linotype", 24)
        attack.set_bold(True)
        rainAttack = attack.render("You used...Rain Cutter!", False, (white))
        gameDisplay.blit(rainAttack, (432, 347))

def attack4():
    global fireballX
    global playerDefense, playerAttack
    
    if playerDefense and playerAttack is False:
        return
    
    if fireballX == -550:
        playerDefense = True
        playerAttack = False
    else:
        attack = pygame.font.SysFont("Palatino Linotype", 24)
        attack.set_bold(True)
        fireAttack = attack.render("You used...Fireball!", False, (white))
        gameDisplay.blit(fireAttack, (432, 347))
    
         
'''TEXT & TRANSITION FUNCTIONS'''

'''[Text]'''
# These functions aid in having smoother transitions through phases
def fightTxt(string):
    dialogueText = pygame.font.SysFont("Arial Black",48)
    text = ''
    for i in range(len(string)):
        text += string[i]
        text_surface = dialogueText.render(text, True, white)
        gameDisplay.blit(text_surface, (235,326))
        pygame.display.update()
        pygame.time.wait(25) #100
        
def deathTxt(string):
    dialogueText = pygame.font.SysFont("Arial Black",48)
    text = ''
    for i in range(len(string)):
        text += string[i]
        text_surface = dialogueText.render(text, True, white)
        gameDisplay.blit(text_surface, (500,326))
        pygame.display.update()
        pygame.time.wait(25) #100

def winTxt1(string):
    dialogueText = pygame.font.SysFont("Arial Black",48)
    text = ''
    for i in range(len(string)):
        text += string[i]
        text_surface = dialogueText.render(text, True, white)
        gameDisplay.blit(text_surface, (204,326))
        pygame.display.update()
        pygame.time.wait(25) #100

def winTxt2(string):
    dialogueText = pygame.font.SysFont("Arial Black",48)
    text = ''
    for i in range(len(string)):
        text += string[i]
        text_surface = dialogueText.render(text, True, white)
        gameDisplay.blit(text_surface, (219,326))
        pygame.display.update()
        pygame.time.wait(25) #100

'''[Transition]'''

def transitionWhite():
    fade = pygame.Surface((1280, 720))
    fade.fill(white)
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        gameDisplay.fill(black)
        gameDisplay.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1) #2
        
def transitionBlack():
    fade = pygame.Surface((1280, 720))
    fade.fill(white)
    for alpha in range(255, 0, -1):
        fade.set_alpha(alpha)
        gameDisplay.fill(black)
        gameDisplay.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1) #2

def deathScreen():
    global gameExit
    global playerDead
    
    if playerDead == False:
        return
    if gameExit == True:
        pygame.quit()
        quit()
    else:
        pygame.mixer.music.load("Game Over.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(0,0.0)
        gameDisplay.fill(black)
        deathTxt("You died...")
        pygame.time.wait(10999)
        pygame.mixer.fadeout(100)

def winScreen():
    global gameExit
    global bossDead

    if bossDead == False:
        return
    if gameExit == True:
        pygame.quit()
        quit()
    else:
        pygame.mixer.music.load("Victory Theme.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(0,0.0)
        gameDisplay.fill(black)
        winTxt1("You...did it! You slayed Balhazar!")
        pygame.time.wait(1000)
        gameDisplay.fill(black)
        winTxt2("Thanks to you, everyone is free!")
        pygame.time.wait(7000)
        

def attackPhase():
    global playerDefense, playerAttack
    global attackSelect
    
    if attackSelect:
        return
    else:
        if playerDefense is False and playerAttack:
            turn1 = pygame.font.SysFont("Palatino Linotype", 24)
            turn1.set_bold(True)
            yourTurn = turn1.render("Your turn... choose wisely.", False, (white))
            gameDisplay.blit(yourTurn, (432,347))
            gameDisplay.blit(selectArrow, (sPos,649))
# Main loop which controls all the other functions and runs them.
def main_loop():
    global gameExit
    global xChar, yChar
    global playerDefense
    global bullet1X, bullet2X, bullet3X
    global bullet4X, bullet5X, bullet6X
    global bPos, sPos
    global attackXY
    global boss_healthPoint
    global boss_newHealth
    global bWidth
    global boss_healthPoint
    global boss_newHealth
    global star1X, fireballX, rainX, dazzleX
    global playerDead
    global bossDead
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

        #Event Handlers

        '''Event handler put into the following:

           -characterMove()

           '''
        
        btnSelect()

        #Functions

        gameDisplay.fill(black)
        combatChar(xChar,yChar)
        combatBox()
        playerStats()
        combatButtons()
        fightSkele()
        bossName()
        bossStats()
        bossAttack()
        attackPhase()
        moveSelect() #<--- event handler*

        if attackSelect == True:
            attackMoves()

        if playerDead == True:
            return
        if bossDead == True:
            return

        if boss_healthPoint == 0:
            bossDead = True
            return
        
        if star1X == 640:
            if boss_healthPoint != (boss_newHealth - 2):
                boss_healthPoint -= 10
                bWidth -= 10
        if fireballX == 550:
            if boss_healthPoint != (boss_newHealth - 2):
                boss_healthPoint -= 40
                bWidth -= 40
        if rainX == 512:
            if boss_healthPoint != (boss_newHealth - 2):
                boss_healthPoint -= 20
                bWidth -= 20
        if dazzleX == 518:
            if boss_healthPoint != (boss_newHealth - 2):
                boss_healthPoint -= 30
                bWidth -= 30

        if boss_healthPoint <= 0:
            boss_healthPoint = 0
        
        pygame.display.update()
        clock.tick(60)


'''CONFIGURABLES - Jonah'''

howDark = 210
MaxCharactersForYourName = 8
AllowMinecraftSounds = "Yes"
AllowCredits = True


'''JONAH'S FONTS'''

size1 = pygame.font.SysFont("Palatino Linotype",200)
size1.set_underline(True)
size2 = pygame.font.SysFont("Palatino Linotype",30)
size3 = pygame.font.SysFont("Palatino Linotype",64)
size4 = pygame.font.SysFont("Palatino Linotype",150)
size5 = pygame.font.SysFont("Palatino Linotype",50)
NameSize = pygame.font.SysFont("Palatino Linotype",24)
InstructionsSizeText = pygame.font.SysFont("Palatino Linotype",36)
InstructionsSizeTitle = pygame.font.SysFont("Palatino Linotype",48)

'''[Text/Titles] - Jonah'''

GameTitleFinnish = size1.render("Edigon", False, (white))
GameTitle = size1.render("Edigon", False, (white))

#Main Menu

StartGame = size3.render("Start", False, (white))
StartGame_rect = StartGame.get_rect()
StartGame_rect.x, StartGame_rect.y = 600,388
Controls = size3.render("Controls", False, (white))
Controls_rect = Controls.get_rect()
Controls_rect.x, Controls_rect.y = 920,388
EndCredits = size3.render("End Credits", False, (white))
EndCredits_rect = EndCredits.get_rect()
EndCredits_rect.x, EndCredits_rect.y = 110,388
MenuText = ""

#End Credits

ThanksForPlaying = size3.render("Thanks for playing!", False, (white))
FirstCredit = size3.render("Developed by Jonah & Ayman", False, (white))
SecondCredit = size3.render("Story by Jonah & Ayman", False, (white))
ThirdCredit = size3.render("Pseudocode by Jonah & Ayman", False, (white))
FourthCredit = size3.render("Animations programmed by Ayman", False, (white))
FifthCredit = size3.render("Menu & GUI's made by Jonah", False, (white))
SixthCredit = size3.render("Music by Toby Fox", False, (white))

#For Controls

Confirm = InstructionsSizeText.render("[Z or Enter] - Confirm", False, (white))
Cancel = InstructionsSizeText.render("[X or Shift] - Cancel", False, (white))
Menu = InstructionsSizeText.render("[C or Ctrl] - Menu (In-Game)", False, (white))
Quit = InstructionsSizeText.render("[Hold ESC] - Quit", False, (white))
ControlsStartGame = InstructionsSizeTitle.render("Begin Game", False, (white))
ControlsTitles = InstructionsSizeTitle.render("Controls", False, (white))
ControlsStartGame_rect = ControlsStartGame.get_rect()
ControlsStartGame_rect.x, ControlsStartGame_rect.y = 890,600

#To Begin

BeginGameText = size2.render("[ press z to continue ]", False, (white))

#Character Name

CharacterNamePart1 = InstructionsSizeTitle.render("Please enter your avatar's name to begin", False, (white))
CharacterNamePart2 = InstructionsSizeTitle.render("Your name needs to be 8 characters or less", False, (white))

CharacterNamePart3 = size3.render("Continue", False, (white))
CharacterNamePart3_rect = CharacterNamePart3.get_rect()
CharacterNamePart3_rect.x, CharacterNamePart3_rect.y = 500,600

GoBackMainMenu = size3.render("Go back", False, (white))
GoBackMainMenu_rect = GoBackMainMenu.get_rect()
GoBackMainMenu_rect.x, GoBackMainMenu_rect.y = 540,600

QuitGameMenu = size3.render("Quit Game", False, (white))
QuitGameMenu_rect = QuitGameMenu.get_rect()
QuitGameMenu_rect.x, QuitGameMenu_rect.y = 110,600

GoBackControls = size3.render("Go back", False, (white))
GoBackControls_rect = GoBackControls.get_rect()
GoBackControls_rect.x, GoBackControls_rect.y = 250,600

Settings = size3.render("Settings", False, (white))
Settings_rect = Settings.get_rect()
Settings_rect.x, Settings_rect.y = 920,600

ToggleEndCredits = size2.render("End Credits: Activated", False, (white))
ToggleEndCredits_rect = ToggleEndCredits.get_rect()
ToggleEndCredits_rect.x, ToggleEndCredits_rect.y = 200,250

GameSettings = size5.render("Settings", False, (white))
GameSettings_rect = GameSettings.get_rect()

GameSettingsBack = size5.render("Go Back", False, (white))
GameSettingsBack_rect = GameSettingsBack.get_rect()
GameSettingsBack_rect.x, GameSettingsBack_rect.y = 125,600
print("Minecraft sounds are: ", AllowMinecraftSounds)
if AllowMinecraftSounds == "Yes":
	ToggleMinecraftSounds = size2.render("Minecraft sounds: Activated", False, (white))
else:
	ToggleMinecraftSounds = size2.render("Minecraft sounds: De-Activated", False, (white))
ToggleMinecraftSounds_rect = ToggleMinecraftSounds.get_rect()
ToggleMinecraftSounds_rect.x, ToggleMinecraftSounds_rect.y = 200,200

'''FUNCTIONS - Jonah'''

def RenderMenuText():
	global MenuText
	MainMenuEdigonStart = size3.render(MenuText, False, (white))
	gameDisplay.blit(MainMenuEdigonStart, (50,100))
	pygame.display.update()
	return
def GameSettings():
    global AllowMinecraftSounds
    global running
    global GameSettingsBack
    global ToggleMinecraftSounds
    global ToggleEndCredits
    global AllowCredits
    MinecraftText = ""
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        Settings = size3.render("Settings", False, (white))
        StartVariable = "Minecraft sounds: Activate"
        gameDisplay.fill(black)
        gameDisplay.blit(Settings, (500,50))
        gameDisplay.blit(GameSettingsBack, (125,600))
        gameDisplay.blit(ToggleMinecraftSounds, (200,200))
        gameDisplay.blit(ToggleEndCredits, (200,250))
        pygame.display.update()
        # When hovering over the buttons they will turn yellow and white depending on your actions. Once clicked it will change the variable.
        if ToggleMinecraftSounds_rect.collidepoint(pygame.mouse.get_pos()):
                if AllowMinecraftSounds == "Yes":
                    ToggleMinecraftSounds = size2.render("Minecraft sounds: Activated", True, (yellow))
                else:
                    ToggleMinecraftSounds = size2.render("Minecraft sounds: De-Activated", True, (yellow))
        else:
                if AllowMinecraftSounds == "Yes":
                    ToggleMinecraftSounds = size2.render("Minecraft sounds: Activated", True, (white))
                else:
                    ToggleMinecraftSounds = size2.render("Minecraft sounds: De-Activated", True, (white))
        if ToggleEndCredits_rect.collidepoint(pygame.mouse.get_pos()):
                if AllowCredits == True:
                    ToggleEndCredits = size2.render("ToggleEndCredits: Activated", True, (yellow))
                else:
                    ToggleEndCredits = size2.render("ToggleEndCredits: De-Activated", True, (yellow))
        else:
                if AllowCredits == True:
                    ToggleEndCredits = size2.render("ToggleEndCredits: Activated", True, (white))
                else:
                    ToggleEndCredits = size2.render("ToggleEndCredits: De-Activated", True, (white))
        if GameSettingsBack_rect.collidepoint(pygame.mouse.get_pos()):
            GameSettingsBack = size3.render("Go back", True, (yellow))
        else:
            GameSettingsBack = size3.render("Go back", True, (white))
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if ToggleMinecraftSounds_rect.collidepoint(pygame.mouse.get_pos()):
                    print(AllowMinecraftSounds)
                    if AllowMinecraftSounds == "Yes":
                        AllowMinecraftSounds = "No"
                        MinecraftText = ("Minecraft sounds: De-activated")
                    elif AllowMinecraftSounds == "No":
                        MinecraftText = ("Minecraft sounds: Activate")
                        AllowMinecraftSounds = "Yes"
                if ToggleEndCredits_rect.collidepoint(pygame.mouse.get_pos()):
                    if AllowCredits == True:
                        AllowCredits = False
                        MinecraftText = ("Minecraft sounds: De-activated")
                    elif AllowCredits == False:
                        MinecraftText = ("Minecraft sounds: Activate")
                        AllowCredits = True
                        ToggleMinecraftSounds = size3.render(MinecraftText, True, (yellow))
                        ToggleMinecraftSounds = size3.render(MinecraftText, True, (yellow))
                if GameSettingsBack_rect.collidepoint(pygame.mouse.get_pos()):
                    if AllowMinecraftSounds == "Yes":
                        pygame.mixer.music.play(0)
                    MainMenu()
                    return
def MainMenu():
    global gameExit
    global Settings
    global MainMenuRunning
    global Hovered
    global Controls
    global StartGame
    global EndCredits
    global GoBackMainMenu
    global QuitGameMenu
    global FirstCreditY
    global SecondCreditY
    global ThirdCreditY
    global FourthCreditY
    global FifthCreditY
    global SixthCreditY
    while MainMenuRunning:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    MainMenuRunning = False
        gameDisplay.fill(black)
        gameDisplay.blit(StartGame, (600,388))
        gameDisplay.blit(EndCredits, (110,388))
        gameDisplay.blit(Controls, (920,388))
        gameDisplay.blit(GoBackMainMenu, (540,600))
        gameDisplay.blit(Settings, (920,600))
        gameDisplay.blit(QuitGameMenu, (110,600))
        UsernameString = Username
        global MenuText
        MenuText = ("Hello, " + Username +"."+" Welcome To Edigon")
        RenderMenuText()
        pygame.display.update()
        if Controls_rect.collidepoint(pygame.mouse.get_pos()):
                Controls = size3.render("Controls", True, (yellow))
        else:
                Controls = size3.render("Controls", True, (white))
        if StartGame_rect.collidepoint(pygame.mouse.get_pos()):
                StartGame = size3.render("Start", True, (yellow))
        else:
                StartGame = size3.render("Start", True, (white))
        if EndCredits_rect.collidepoint(pygame.mouse.get_pos()):
                EndCredits = size3.render("End Credits", True, (yellow))
        else:
                EndCredits = size3.render("End Credits", True, (white))
        if GoBackMainMenu_rect.collidepoint(pygame.mouse.get_pos()):
                GoBackMainMenu = size3.render("Go back", True, (yellow))
        else:
                GoBackMainMenu = size3.render("Go back", True, (white))
        if Settings_rect.collidepoint(pygame.mouse.get_pos()):
                Settings = size3.render("Settings", True, (yellow))
        else:
                Settings = size3.render("Settings", True, (white))
        if QuitGameMenu_rect.collidepoint(pygame.mouse.get_pos()):
                QuitGameMenu = size3.render("Quit Game", True, (yellow))
        else:
                QuitGameMenu = size3.render("Quit Game", True, (white))
        ev = pygame.event.get()
        for event in ev:
                pos = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if Controls_rect.collidepoint(pygame.mouse.get_pos()):
                                print("clicked controls")
                                if AllowMinecraftSounds == "Yes":
                                    pygame.mixer.music.play(0)
                                    Controls = size3.render("--Controls--", True, (white))
                                Control()
                                return
                        elif StartGame_rect.collidepoint(pygame.mouse.get_pos()):
                                if AllowMinecraftSounds == "Yes":
                                    pygame.mixer.music.play(0)
                                Start()
                                return
                        elif EndCredits_rect.collidepoint(pygame.mouse.get_pos()):
                                FirstCreditY = -200
                                SecondCreditY = -300
                                ThirdCreditY = -400
                                FourthCreditY = -500
                                FifthCreditY = -600
                                SixthCreditY = -700
                                if AllowMinecraftSounds == "Yes":
                                    pygame.mixer.music.play(0)
                                CreditScene()
                                return
                        elif GoBackMainMenu_rect.collidepoint(pygame.mouse.get_pos()):
                                if AllowMinecraftSounds == "Yes":
                                    pygame.mixer.music.play(0)
                                EnterName()
                                return
                        elif Settings_rect.collidepoint(pygame.mouse.get_pos()):
                                if AllowMinecraftSounds == "Yes":
                                    pygame.mixer.music.play(0)
                                GameSettings()
                                return
                        elif QuitGameMenu_rect.collidepoint(pygame.mouse.get_pos()):
                            MainMenuRunning = False
                            pygame.quit()
                            quit()
def Control():
    global ControlsStartGame
    global GoBackControls
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
        gameDisplay.fill(black)
        gameDisplay.blit(Controls, (463,84))
        gameDisplay.blit(Confirm, (432,210))
        gameDisplay.blit(Cancel, (432,301))
        gameDisplay.blit(Menu, (432,392))
        gameDisplay.blit(Quit, (432,483))
        gameDisplay.blit(ControlsStartGame, (890,600))
        gameDisplay.blit(GoBackControls, (250,600))
        if ControlsStartGame_rect.collidepoint(pygame.mouse.get_pos()):
                ControlsStartGame = InstructionsSizeTitle.render("Begin Game", True, (yellow))
        else:
                ControlsStartGame = InstructionsSizeTitle.render("Begin Game", True, (white))
        if GoBackControls_rect.collidepoint(pygame.mouse.get_pos()):
                GoBackControls = InstructionsSizeTitle.render("Go back", True, (yellow))
        else:
                GoBackControls = InstructionsSizeTitle.render("Go back", True, (white))
        pygame.display.update()
        ev = pygame.event.get()
        for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        print("clicked")
                        pos = pygame.mouse.get_pos()
                        if ControlsStartGame_rect.collidepoint(pygame.mouse.get_pos()):
                                if AllowMinecraftSounds == "Yes":
                                    pygame.mixer.music.play(0)
                                Start()
                                return
                        elif GoBackControls_rect.collidepoint(pygame.mouse.get_pos()):
                                if AllowMinecraftSounds == "Yes":
                                    pygame.mixer.music.play(0)
                                MainMenu()
                                return
                                     
def CreditScene():
    global FirstCreditY
    global SecondCreditY
    global ThirdCreditY
    global FourthCreditY
    global FifthCreditY
    global SixthCreditY
    global ThanksForPlayingY
    print("Running Credits")
    pygame.mixer.music.load("End.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1,0.0)
    global running
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
        gameDisplay.fill(black)
        time.sleep(.01)
        # Draws the credits to the screen and adds 1 to the X value. This makes it move downward.
        gameDisplay.blit(ThanksForPlaying, (180,ThanksForPlayingY))
        ThanksForPlayingY = ThanksForPlayingY+1
        gameDisplay.blit(FirstCredit, (180,FirstCreditY))
        FirstCreditY = FirstCreditY+1
        gameDisplay.blit(SecondCredit, (180,SecondCreditY))
        SecondCreditY = SecondCreditY+1
        gameDisplay.blit(ThirdCredit, (180,ThirdCreditY))
        ThirdCreditY = ThirdCreditY+1
        gameDisplay.blit(FourthCredit, (180,FourthCreditY))
        FourthCreditY = FourthCreditY+1
        gameDisplay.blit(FifthCredit, (180,FifthCreditY))
        FifthCreditY = FifthCreditY+1
        gameDisplay.blit(SixthCredit, (180,SixthCreditY))
        SixthCreditY = SixthCreditY+1
        pygame.display.update()
        if SixthCreditY == 740:
                print("End Scene completed")
                return
def EnterName():
    global howDark
    global CurrentCharacters
    global MaxCharactersForYourName
    global Username
    global CharacterNamePart3
    input_box = pygame.Rect(170, 400, 900, 150)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    done = False
    text = ''
    CurrentCharacters = 0
    global running
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if active:
                            print(event.key)
                            if event.key == pygame.K_RETURN:
                                if CurrentCharacters > 0:
                                    Username = text
                                    MainMenu()
                                    return
                            elif event.key == pygame.K_BACKSPACE:
                                    if CurrentCharacters >= 1:
                                        text = text[:-1]
                                        CurrentCharacters = CurrentCharacters-1
                                        print("Subtracting a character",CurrentCharacters)
                                    elif CurrentCharacters == 0:
                                        print("Cant remove anymore characters")
                                
                            elif event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9 or event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_c or event.key == pygame.K_d or event.key == pygame.K_e or event.key == pygame.K_f or event.key == pygame.K_g or event.key == pygame.K_h or event.key == pygame.K_i or event.key == pygame.K_j or event.key == pygame.K_k or event.key == pygame.K_l or event.key == pygame.K_m or event.key == pygame.K_n or event.key == pygame.K_o or event.key == pygame.K_p or event.key == pygame.K_q or event.key == pygame.K_r or event.key == pygame.K_s or event.key == pygame.K_t or event.key == pygame.K_u or event.key == pygame.K_v or event.key == pygame.K_w or event.key == pygame.K_x or event.key == pygame.K_y or event.key == pygame.K_z:
                                        if CurrentCharacters < MaxCharactersForYourName:
                                            text += event.unicode
                                            CurrentCharacters = CurrentCharacters+1
                                            print(CurrentCharacters)
                                        elif CurrentCharacters == MaxCharactersForYourName:
                                            print("Max reached")
                if event.type == pygame.MOUSEBUTTONDOWN:
                        print("clicked")
                        pos = pygame.mouse.get_pos()
                        if CharacterNamePart3_rect.collidepoint(pygame.mouse.get_pos()):
                                if CurrentCharacters > 0:
                                    if AllowMinecraftSounds == "Yes":
                                         pygame.mixer.music.play(0)
                                Username = text
                                MainMenu()
                                return
        gameDisplay.fill(black)
        # Render the current text.
        txt_surface = size4.render(text, True, color)
        # Resize the box if the text is too long.
        '''width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
        '''
        gameDisplay.blit(txt_surface, (171,415))
        gameDisplay.blit(CharacterNamePart1, (155,80))
        gameDisplay.blit(CharacterNamePart2, (155,140))
        gameDisplay.blit(CharacterNamePart3, (500,600))
        CharacterNamePart1.set_alpha(howDark)
        CharacterNamePart2.set_alpha(howDark)
        CharacterNamePart3.set_alpha(howDark)
        # Global CharacterNamePart3_rect
        if CharacterNamePart3_rect.collidepoint(pygame.mouse.get_pos()):
                CharacterNamePart3 = size3.render("Continue", True, (yellow))
        else:
                CharacterNamePart3 = size3.render("Continue", True, (white))
        # Blit the input_box rect.
        pygame.draw.rect(gameDisplay, color, input_box, 2)
        pygame.display.update()

# Starts the game, handles all the functions and runs them when needed.
def Start():
        gameDisplay.fill(black)
        pygame.mixer.music.load("Evil Laugh Sound Effect.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(0,0.0)
        pygame.mixer.fadeout(100)
        fightTxt("DEATH AWAITS YOU, MORTAL!")
        transitionWhite()
        transitionBlack()
        pygame.mixer.music.load("BattleTheme.mp3")
        pygame.mixer.fadeout(100)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1,0.0)

        if bossDead == True:
            pygame.mixer.music.stop
        
        main_loop()
        winScreen()
        deathScreen()
        if AllowCredits:
            CreditScene()
        pygame.quit()
        quit()

# Runs the Intro and once Z is pressed it runs Main Menu.
def main_():
        global gameExit
        global x
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True
                        return pygame.quit()
                # Alpha value changes the transparency of the text
                for i in range(howDark):
                    if x == howDark:
                            break
                    else:
                            keys=pygame.key.get_pressed()
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                        if event.type == pygame.QUIT:
                                            gameExit = True
                                        if event.key == pygame.K_z:
                                            print("going into the game, z has been pressed")
                                            EnterName()
                                        if event.key == pygame.K_ESCAPE:
                                            pygame.quit()
                                            quit()
                                x = x + 1
                                gameDisplay.fill((0,0,0))
                                GameTitle.set_alpha(i)
                                gameDisplay.blit(GameTitle, (320,270))
                                BeginGameText.set_alpha(i)
                                gameDisplay.blit(BeginGameText, (469,500))
                                pygame.display.update()
                                clock.tick(fadeTick)
                    while True:
                        x = 30
                        keys=pygame.key.get_pressed()
                        for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_z:
                                        print("going into the game, z has been pressed")
                                        EnterName()
                                    if event.key == pygame.K_ESCAPE:
                                        pygame.quit()
                                        quit()
                                if event.type == pygame.QUIT:
                                        gameExit = True
                        for i in range(howDark-30):
                                x = x + 1
                                gameDisplay.fill((0,0,0))
                                BeginGameText.set_alpha(x)
                                gameDisplay.blit(BeginGameText, (469,500))
                                GameTitle.set_alpha(210)
                                gameDisplay.blit(GameTitle, (320,270))
                                pygame.display.update()
                                clock.tick(fadeTick)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.type == pygame.QUIT:
                                            gameExit = True
                                        if event.key == pygame.K_z:
                                            print("going into the game, z has been pressed")
                                            EnterName()
                                        if event.key == pygame.K_ESCAPE:
                                            pygame.quit()
                                            quit()
                        for i in range(howDark-30):
                                x = x - 1
                                gameDisplay.fill((0,0,0))
                                BeginGameText.set_alpha(x)
                                gameDisplay.blit(BeginGameText, (469,500))
                                GameTitle.set_alpha(210)
                                gameDisplay.blit(GameTitle, (320,270))
                                pygame.display.update()
                                clock.tick(fadeTick)
                                for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_z:
                                                print("going into the game, z has been pressed")
                                                EnterName()
                                            if event.key == pygame.K_ESCAPE:
                                                pygame.quit()
                                                quit()
                                        if event.type == pygame.QUIT:
                                                gameExit = True

main_() # Calls the Intro to be run right away.
