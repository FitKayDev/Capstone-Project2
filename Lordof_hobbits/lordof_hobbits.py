#Simple game assignment
#import all needed functions
import pygame
import random
import sys

#initialise the pygame modules
pygame.init()

#setting the screen dimentions width as 'w' and height as 'h'
screen_w = 1200
screen_h = 700
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Lord of the Rings")

#player and enemies' images loaded and positions as 'x' and 'y' created
player = pygame.image.load("bilbo.png")
enemy1 = pygame.image.load("nazgul.png")
enemy2 = pygame.image.load("gollum.png")
enemy3 = pygame.image.load("smaug.png")
prize = pygame.image.load("one_ring.png")

#player and enemies' width as 'w'and height as 'h' determined
player_h = player.get_height()
player_w = player.get_width()
enemy1_h = enemy1.get_height()
enemy1_w = enemy1.get_width()
enemy2_h = enemy2.get_height()
enemy2_w = enemy2.get_width()
enemy3_h = enemy3.get_height()
enemy3_w = enemy3.get_width()

#player and enemies' 'x' and 'y' start positions created different from player start position
#prize position randomised in small section 
player_x = 50
player_y = 50

enemy1_x =  screen_w
enemy1_y =  random.randint(100, (screen_h + enemy1_h)) 
enemy2_x =  screen_w
enemy2_y =  random.randint(100, (screen_h - enemy2_h)) 
enemy3_x =  screen_w
enemy3_y =  random.randint(100, (screen_h + enemy3_h))  

prize_x = random.randint(700, 1100)
prize_y = random.randint(500, 600)

#player movement keys initialized to False
#clock module used for slightly smoother image movements
#game loop with screen colour, player movement keys and images on screen created
keyUp = False
keyDown = False
keyRight = False
keyLeft = False

clock = pygame.time.Clock()
game_on = True

while game_on:
    screen.fill((40, 40, 40)) 
    
    screen.blit(player, (player_x, player_y))
    screen.blit(enemy1, (enemy1_x, enemy1_y))
    screen.blit(enemy2, (enemy2_x, enemy2_y))
    screen.blit(enemy3, (enemy3_x, enemy3_y))
    screen.blit(prize, (prize_x, prize_y))

    pygame.display.flip()
    clock.tick(120)

    for event in pygame.event.get():
       if  event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP: 
            keyUp = True
        if event.key == pygame.K_DOWN:
            keyDown = True
        if event.key == pygame.K_LEFT: 
            keyLeft = True
        if event.key == pygame.K_RIGHT:
            keyRight = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP: 
            keyUp = False
        if event.key == pygame.K_DOWN:
            keyDown = False
        if event.key == pygame.K_LEFT: 
            keyLeft = False
        if event.key == pygame.K_RIGHT:
            keyRight = False
    
    #player movement set to 3 pixels per key presses
    if keyUp == True:
        if player_y > 0 :
            player_y -= 3
    if keyDown == True:
        if player_y < screen_h - player_h:
            player_y += 3
    if keyLeft == True:
        if player_x > 0 :
            player_x -= 3
    if keyRight == True:
        if player_x < screen_w - player_w:
            player_x += 3

    #player, enemies' and prize hitboxes determined 
    #collisions between player and enemies or prize initialised to loose or win game with if statements
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = player_y
    playerBox.left = player_x

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1_y
    enemy1Box.left = enemy1_x

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2_y
    enemy2Box.left = enemy2_x

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3_y
    enemy3Box.left = enemy3_x

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prize_y
    prizeBox.left = prize_x

    if playerBox.colliderect(enemy1Box): 
        print("You lose!")
        pygame.quit()
        sys.exit()
    if playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        sys.exit()
    if playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        sys.exit()
    if playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit()
        sys.exit()

    #enemy speeds and different directions set
    # I was unable to figure out how to correctly ricochet enemies on wall so did an object "wrap around"
    # "wrap around" method learnt from https://www.cs.ucf.edu/dmarino/ucf/cop2
    enemy1_x -= 1
    enemy1_y -= 1
    if enemy1_x > screen_w or enemy1_x <0:
        enemy1_x = random.randint(0, (screen_w - enemy1_w))
    if enemy1_y > screen_h or enemy1_y <0:
        enemy1_y = random.randint(0, (screen_h - enemy1_h))

    enemy2_x -= 1
    enemy2_y += 1
    if enemy2_x > screen_w or enemy2_x <0:
        enemy2_x = random.randint(0, (screen_w - enemy2_w))
    if enemy2_y > screen_h or enemy2_y <0:
        enemy2_y = random.randint(0, (screen_h - enemy2_h))

    enemy3_x += 1
    enemy3_y += 1
    if enemy3_x > screen_w or enemy3_x <0:
        enemy3_x = random.randint(0, (screen_w - enemy3_w))
    if enemy3_y > screen_h or enemy3_y <0:
        enemy3_y = random.randint(0, (screen_h - enemy3_h))

# images references:
#player - bilbo : by hextic on https://imgbin.com/png/GQ4WYHzP/brave-frontier-bilbo-baggins-the-hobbit-fan-art-png
#enemy1 - nazgul : https://PNGio.com
# enemy2 - gollum : by murme on https://imgbin.com/png/U2DKfg5n/sticker-gollum-sketch-png
#enemy3 - smaug : by Rentalcarsfinder https://pngitem.com/middle/oJRwRh_smaug-the-hobbit-bilbo-baggins-the-lord-of/
# prize - one_ring : https://www.pngwing.com/en/free-png-skofu