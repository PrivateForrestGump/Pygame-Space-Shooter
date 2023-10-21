import pgzrun
import random
from pgzhelper import *

WIDTH = 1000
HEIGHT = 600

player = Actor('playership1_blue')
player.x = WIDTH/2 
player.bottom = HEIGHT
player.hp = 1000000
player.losthp = 0
playerhpbar = Rect(player.x-50,player.y-50, 50, 20)

enemies = []
lasers = []
elasers = []

def fire():
    laser = Actor('lasers/laserblue01')
    laser.x = player.x
    laser.bottom = player.top

    #autoaim
    if len(enemies) > 0:
        enemy = random.choice(enemies)
        laser.angle = laser.angle_to(enemy)
    else:
        laser.angle = 90

    lasers.append(laser)

def input():
    if keyboard.w:
        player.y -= 5
    if keyboard.s:
        player.y += 5
    if keyboard.a:
        player.x -= 5
    if keyboard.d:
        player.x += 5
    if keyboard.space:
        fire()

def border():
    if player.right > WIDTH:
        player.right = WIDTH
    if player.left< 0:
        player.left = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.top< 0:
        player.top = 0

def spawn_enemy():
    enemy = Actor('enemies/enemyblack1')
    enemy.x = random.randint(0, WIDTH)
    enemy.top = 0
    enemies.append(enemy)

def update_lasers():
    for laser in lasers:
        #laser.y -= 15
        laser.move_forawrd(15)
        if laser.bottom < 0:
            lasers.remove(laser)
        for enemy in enemies:
            if laser.colliderect(enemy):
                lasers.remove(laser)
                enemies.remove(enemy)
                break

def update_enemies():
    for enemy in enemies:
        if random.randint(0,100) < 10:
            elaser = Actor('lasers/laserred12')
            elaser.top = enemy.bottom
            elaser.x = enemy.x
            elasers.append(elaser)
            
def update_elasers():
    for elaser in elasers:
        elaser.y += 15

        if elaser.top > HEIGHT:
            elasers.remove(elaser)
        elif elaser.collide_pixel(player):
            elasers.remove(elaser)
            player.hp -= 1
            player.losthp += 1
            continue

def update():
    input()
    border()
    if random.randint(0, 100) < 3:
        spawn_enemy()

    update_lasers()
    update_elasers()
    update_enemies()
        
def draw():
    screen.clear()
    hp_bar = Rect(player.x-50,player.y-60, player.hp/player.hp*100, 15)
    losthp_bar = Rect(hp_bar.x + hp_bar.width,player.y-60, player.losthp/player.hp*100, 15)
    hp_bar_outline = Rect(player.x-50-1.5,player.y-60-2.5, 100+3, 20)
    screen.draw.filled_rect(hp_bar,('green'))
    screen.draw.filled_rect(losthp_bar,('red'))
    screen.draw.rect(hp_bar_outline,('white'))
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for laser in lasers:
        laser.draw()
    for elaser in elasers:
        elaser.draw()

pgzrun.go()