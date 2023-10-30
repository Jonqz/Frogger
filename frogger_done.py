import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, 32, 2, 4096) # 

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
info_font = pygame.font.SysFont(font_name, 24)
menu_font = pygame.font.SysFont(font_name, 36)

screen = pygame.display.set_mode((448,546), 0, 32)

# --- Loading Images ---
background_filename = 'bg.png'
frog_filename = 'sprite_sheets_up.png'
arrived_filename = 'frog_arrived.png'
car1_filename = 'car1.png'
car2_filename = 'car2.png'
car3_filename = 'car3.png'
car4_filename = 'car4.png'
car5_filename = 'car5.png'
platform_filename = 'trunk.png'

background = pygame.image.load(background_filename).convert()
sprite_frog = pygame.image.load(frog_filename).convert_alpha()
sprite_arrived = pygame.image.load(arrived_filename).convert_alpha()
sprite_car1 = pygame.image.load(car1_filename).convert_alpha()
sprite_car2 = pygame.image.load(car2_filename).convert_alpha()
sprite_car3 = pygame.image.load(car3_filename).convert_alpha()
sprite_car4 = pygame.image.load(car4_filename).convert_alpha()
sprite_car5 = pygame.image.load(car5_filename).convert_alpha()
sprite_platform = pygame.image.load(platform_filename).convert_alpha()


pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()


class Object():
    def __init__(self,position,sprite):
        self.sprite = sprite
        self.position = position

    def draw(self):
        screen.blit(self.sprite,(self.position))

    def rect(self):
        return Rect(self.position[0],self.position[1],self.sprite.get_width(),self.sprite.get_height())


class Frog(Object):
    def __init__(self,position,sprite_frog):
        self.sprite = sprite_frog
        self.position = position
        self.lives = 3
        self.animation_counter = 0
        self.animation_tick = 1
        self.way = "UP"
        self.can_move = 1

    def updateSprite(self,key_pressed):
        if self.way != key_pressed:
            self.way = key_pressed
            if self.way == "up":
                frog_filename = 'sprite_sheets_up.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()
            elif self.way == "down":
                frog_filename = 'sprite_sheets_down.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()
            elif self.way == "left":
                frog_filename = 'sprite_sheets_left.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()
            elif self.way == "right":
                frog_filename = 'sprite_sheets_right.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()


    def moveFrog(self,key_pressed, key_up):
         
        if self.animation_counter == 0 :
            self.updateSprite(key_pressed)
        self.incAnimationCounter()
        if key_up == 1:
            if key_pressed == "up":
                if self.position[1] > 39:
                    self.position[1] = self.position[1]-13
            elif key_pressed == "down":
                if self.position[1] < 473:
                    self.position[1] = self.position[1]+13
            if key_pressed == "left":
                if self.position[0] > 2:
                    if self.animation_counter == 2 :
                        self.position[0] = self.position[0]-13
                    else:
                        self.position[0] = self.position[0]-14
            elif key_pressed == "right":
                if self.position[0] < 401:
                    if self.animation_counter == 2 :
                        self.position[0] = self.position[0]+13
                    else:
                        self.position[0] = self.position[0]+14

    def animateFrog(self,key_pressed,key_up):
        if self.animation_counter != 0 :
            if self.animation_tick <= 0 :
                self.moveFrog(key_pressed,key_up)
                self.animation_tick = 1
            else :
                self.animation_tick = self.animation_tick - 1

    def setPos(self,position):
        self.position = position

    def decLives(self):
        self.lives = self.lives - 1

    def cannotMove(self):
        self.can_move = 0

    def incAnimationCounter(self):
        self.animation_counter = self.animation_counter + 1
        if self.animation_counter == 3 :
            self.animation_counter = 0
            self.can_move = 1

    def frogDead(self,game):
        self.setPositionToInitialPosition()
        self.decLives()
        game.resetTime()
        self.animation_counter = 0
        self.animation_tick = 1
        self.way = "UP"
        self.can_move = 1

    def setPositionToInitialPosition(self):
        self.position = [207, 475]

    def draw(self):
        current_sprite = self.animation_counter * 30
        screen.blit(self.sprite,(self.position),(0 + current_sprite, 0, 30, 30 + current_sprite))

    def rect(self):
        return Rect(self.position[0],self.position[1],30,30)

class Enemy(Object):
    def __init__(self,position,sprite_enemy,way,factor):
        self.sprite = sprite_enemy
        self.position = position
        self.way = way
        self.factor = factor

    def move(self,speed):
        if self.way == "right":
            self.position[0] = self.position[0] + speed * self.factor
        elif self.way == "left":
            self.position[0] = self.position[0] - speed * self.factor


class Platform(Object):
    def __init__(self,position,sprite_platform,way):
        self.sprite = sprite_platform
        self.position = position
        self.way = way

    def move(self,speed):
        if self.way == "right":
            self.position[0] = self.position[0] + speed
        elif self.way == "left":
            self.position[0] = self.position[0] - speed


class Game():
    def __init__(self,speed,level):
        self.speed = speed
        self.level = level
        self.points = 0
        self.time = 30
        self.gameInit = 0

    def incLevel(self):
        self.level = self.level + 1

    def incSpeed(self):
        self.speed = self.speed + 1

    def incPoints(self,points):
        self.points = self.points + points

    def decTime(self):
        self.time = self.time - 1

    def resetTime(self):
        self.time = 30


#General functions
def drawList(list):
    for i in list:
        i.draw()

def moveList(list,speed):
    for i in list:
        i.move(speed)

def destroyEnemys(list):
    for i in list:
        if i.position[0] < -80:
            list.remove(i)
        elif i.position[0] > 516:
            list.remove(i)

def destroyPlatforms(list):
    for i in list:
        if i.position[0] < -100:
            list.remove(i)
        elif i.position[0] > 448:
            list.remove(i)

def createEnemys(list,enemys,game):
    for i, tick in enumerate(list):
        list[i] = list[i] - 1
        if tick <= 0:
            if i == 0:
                list[0] = (40*game.speed)/game.level
                position_init = [-55,436]
                enemy = Enemy(position_init,sprite_car1,"right",1)
                enemys.append(enemy)
            elif i == 1:
                list[1] = (30*game.speed)/game.level
                position_init = [506, 397]
                enemy = Enemy(position_init,sprite_car2,"left",2)
                enemys.append(enemy)
            elif i == 2:
                list[2] = (40*game.speed)/game.level
                position_init = [-80, 357]
                enemy = Enemy(position_init,sprite_car3,"right",2)
                enemys.append(enemy)
            elif i == 3:
                list[3] = (30*game.speed)/game.level
                position_init = [516, 318]
                enemy = Enemy(position_init,sprite_car4,"left",1)
                enemys.append(enemy)
            elif i == 4:
                list[4] = (50*game.speed)/game.level
                position_init = [-56, 280]
                enemy = Enemy(position_init,sprite_car5,"right",1)
                enemys.append(enemy)

def createPlatform(list,platforms,game):
    for i, tick in enumerate(list):
        list[i] = list[i] - 1
        if tick <= 0:
            if i == 0:
                list[0] = (30*game.speed)/game.level
                position_init = [-100,200]
                platform = Platform(position_init,sprite_platform,"right")
                platforms.append(platform)
            elif i == 1:
                list[1] = (30*game.speed)/game.level
                position_init = [448, 161]
                platform = Platform(position_init,sprite_platform,"left")
                platforms.append(platform)
            elif i == 2:
                list[2] = (40*game.speed)/game.level
                position_init = [-100, 122]
                platform = Platform(position_init,sprite_platform,"right")
                platforms.append(platform)
            elif i == 3:
                list[3] = (40*game.speed)/game.level
                position_init = [448, 83]
                platform = Platform(position_init,sprite_platform,"left")
                platforms.append(platform)
            elif i == 4:
                list[4] = (20*game.speed)/game.level
                position_init = [-100, 44]
                platform = Platform(position_init,sprite_platform,"right")
                platforms.append(platform)




def frogOnTheStreet(frog,enemys,game):
    for i in enemys:
        enemyRect = i.rect()
        frogRect = frog.rect()
        if frogRect.colliderect(enemyRect):
            frog.frogDead(game)

def frogInTheLake(frog,platforms,game):
    #if the frog is under some platform Safe = 1
    safe = 0
    wayPlatform = ""
    for i in platforms:
        platformRect = i.rect()
        frogRect = frog.rect()
        if frogRect.colliderect(platformRect):
            safe = 1
            wayPlatform = i.way

    if safe == 0:
        frog.frogDead(game)

    elif safe == 1:
        if wayPlatform == "right":
            frog.position[0] = frog.position[0] + game.speed

        elif wayPlatform == "left":
            frog.position[0] = frog.position[0] - game.speed

def frogArrived(frog,success,game):
    if frog.position[0] > 33 and frog.position[0] < 53:
        position_init = [43,7]
        createArrived(frog,success,game,position_init)

    elif frog.position[0] > 115 and frog.position[0] < 135:
        position_init = [125,7]
        createArrived(frog,success,game,position_init)

    elif frog.position[0] > 197 and frog.position[0] < 217:
        position_init = [207,7]
        createArrived(frog,success,game,position_init)

    elif frog.position[0] > 279 and frog.position[0] < 299:
        position_init = [289,7]
        createArrived(frog,success,game,position_init)

    elif frog.position[0] > 361 and frog.position[0] < 381:
        position_init = [371,7]
        createArrived(frog,success,game,position_init)

    else:
        frog.position[1] = 46
        frog.animation_counter = 0
        frog.animation_tick = 1
        frog.can_move = 1


def whereIsTheFrog(frog):
    #If the frog hasn't crossed the road yet
    if frog.position[1] > 240 :
        frogOnTheStreet(frog,enemys,game)

    #If the frog arrived at the river
    elif frog.position[1] < 240 and frog.position[1] > 40:
        frogInTheLake(frog,platforms,game)

    #frog reached the goal
    elif frog.position[1] < 40 :
        frogArrived(frog,success,game)


def createArrived(frog,success,game,position_init):
    frog_success = Object(position_init,sprite_arrived)
    success.append(frog_success)
    frog.setPositionToInitialPosition()
    game.incPoints(10 + game.time)
    game.resetTime()
    frog.animation_counter = 0
    frog.animation_tick = 1
    frog.can_move = 1


def nextLevel(success,enemys,platforms,frog,game):
    if len(success) == 5:
        success[:] = []
        frog.setPositionToInitialPosition()
        game.incLevel()
        game.incSpeed()
        game.incPoints(100)
        game.resetTime()



text_info = menu_font.render(('Press any button to start!'),1,(0,0,0))
gameInit = 0

while gameInit == 0:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            gameInit = 1

    screen.blit(background, (0, 0))
    screen.blit(text_info,(80,150))
    pygame.display.update()

while True:
    gameInit = 1
    game = Game(3,1)
    key_up = 1
    frog_initial_position = [207,475]
    frog = Frog(frog_initial_position,sprite_frog)

    enemys = []
    platforms = []
    success = []
    #30 ticks == 1 second
    #ticks_enemys = [120, 90, 120, 90, 150]
    #ticks_platforms = [90, 90, 120, 120, 60]
    ticks_enemys = [30, 0, 30, 0, 60]
    ticks_platforms = [0, 0, 30, 30, 30]
    ticks_time = 30
    pressed_keys = 0
    key_pressed = 0

    while frog.lives > 0:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYUP:
                key_up = 1
            if event.type == KEYDOWN:
                if key_up == 1 and frog.can_move == 1 :
                    key_pressed = pygame.key.name(event.key)
                    frog.moveFrog(key_pressed,key_up)
                    frog.cannotMove()
        if not ticks_time:
            ticks_time = 30
            game.decTime()
        else:
            ticks_time -= 1

        if game.time == 0:
            frog.frogDead(game)

        createEnemys(ticks_enemys,enemys,game)
        createPlatform(ticks_platforms,platforms,game)

        moveList(enemys,game.speed)
        moveList(platforms,game.speed)

        whereIsTheFrog(frog)

        nextLevel(success,enemys,platforms,frog,game)

        text_info1 = info_font.render(('Level: {0}               Points: {1}'.format(game.level,game.points)),1,(255,255,255))
        text_info2 = info_font.render(('Time: {0}           Lives: {1}'.format(game.time,frog.lives)),1,(255,255,255))
        screen.blit(background, (0, 0))
        screen.blit(text_info1,(10,520))
        screen.blit(text_info2,(250,520))

       

        drawList(enemys)
        drawList(platforms)
        drawList(success)

        frog.animateFrog(key_pressed,key_up)
        frog.draw()

        destroyEnemys(enemys)
        destroyPlatforms(platforms)

        pygame.display.update()
        time_passed = clock.tick(30)

    while gameInit == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                gameInit = 0

        screen.blit(background, (0, 0))
        text = game_font.render('GAME OVER', 1, (255, 0, 0))
        text_points = game_font.render(('Score: {0}'.format(game.points)),1,(255,0,0))
        text_reiniciar = info_font.render('Press any key to restart!',1,(255,0,0))
        screen.blit(text, (75, 120))
        screen.blit(text_points,(10,170))
        screen.blit(text_reiniciar,(70,250))

        pygame.display.update()
