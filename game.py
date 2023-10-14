import pgzrun
import random

WIDTH = 1000
HEIGHT = 600

player = Actor('playership1_blue')
player.x = WIDTH/2
player.bottom = HEIGHT

enemies = []
lasers = []

def fire():
    laser = Actor('lasers/laserblue01')
    laser.x = player.x
    laser.y += 5
    laser.bottom = player.top
    lasers.append(laser)

def update_lasers():
    for laser in lasers:
        laser.y -= 15
        if laser.bottom < 0:
            lasers.remove(laser)
    for emeny in enemies:
        if laser.colliderect(enemy):
            laser.remove(laser)
            enemies.remove(enemy)
            break

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

def update():
    input()
    border()
    if random.randint(0, 100) < 1:
        spawn_enemy()
    update_lasers()
    
        
def draw():
    screen.clear()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for laser in lasers:
        laser.draw()

pgzrun.go()