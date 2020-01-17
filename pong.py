#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 06:50:48 2019

@author: davinpc
"""

# Import the pygame library and initialise the game engine
import pygame
# Import Paddle class and Ball class
from paddle import Paddle
from ball import Ball

pygame.init()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Pong")

# Create the paddles and the ball
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1.rect.y = 200
 
paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 670
paddle2.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# This will be a list that will contain all the sprites I intend to use in the game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles and the ball to the list of sprites
all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)
all_sprites_list.add(ball)
 
# The loop will carry on until the user exit the game
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Initialise player scores
score1 = 0
score2 = 0
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Exit this loop
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # The pause button
            while True: # Infinite loop that will be broken when the user presses the space bar again
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break # Exit infinite loop
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            # Pressing the X key will quit the game
            carryOn = False
                     
    # Moving the paddles when the user uses "W/S" keys (player 1) or the arrow keys (player 2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.moveUp(7)
    if keys[pygame.K_s]:
        paddle1.moveDown(7)
    if keys[pygame.K_UP]:
        paddle2.moveUp(7)
    if keys[pygame.K_DOWN]:
        paddle2.moveDown(7)
 
    all_sprites_list.update()
    
    # Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        score1+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        score2+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]
        
    # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
      ball.bounce()
 
    # --- Drawing code
    # Clear the screen to black. 
    screen.fill(BLACK)
    # Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    # Draw all the sprites in one go.
    all_sprites_list.draw(screen)
    
    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(score1), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(score2), 1, WHITE)
    screen.blit(text, (420,10))

    # Winning condition
    # If a player wins, it will display a statement 'Player X wins!'
    if score1 == 5:
        text = font.render('Player 1 Wins !', True, BLACK, WHITE)
    elif score2 == 5:
        text = font.render('Player 2 Wins !', True, BLACK, WHITE)
        
    if score1 == 5 or score2 == 5:
        textRect = text.get_rect()  
        textRect.center = (700 // 2, 500 // 2)
        screen.blit(text, textRect)
        carryOn = False
        
    # --- Update the screen
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()