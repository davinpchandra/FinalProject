#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:08:41 2019

@author: davinpc
"""

import pygame
from random import randint

BLACK = (0,0,0)
 
class Ball(pygame.sprite.Sprite):
    # This class represents the ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite)
        super().__init__()
        
        # Pass in the color of the ball, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(9,13),randint(-3,13)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        # Moving the ball
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-3,13)