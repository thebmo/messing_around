#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys
import pygame
import math
import random


# Define a main() function that prints a little greeting.
def main():
    stop = False
    pi = 3.141592653
    pygame.init()
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # colors
    black    = (   0,   0,   0)
    white    = ( 255, 255, 255)
    green    = (   0, 255,   0)
    red      = ( 255,   0,   0)
    
    # Set the width and height of the screen
    size = (800,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snowy Ninja")
    
    
    x_change = 5
    y_change = 5
    rect_path = []
    
    # makes snow list with lists
    snow = []
    for i in range(200):
        x = random.randrange(0, 800)
        y = random.randrange(0, 600)
        snow.append([x,y])
    
    
    
    # ################# #
    # MASTER WHILE LOOP #
    # ################# #
    y = 100
    while not stop:

        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                stop = True # Flag that we are done so we exit this loop

            
        
        
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        
        
        
        


        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        
        x+= x_change
        y+= y_change

        
        # Bounce the rectangle if needed
        if y > 100 or y < 1:
            y_change = y_change * -1
        if x > 750 or x < 0:
            x_change = x_change * -1
     
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
     
     
     
     
        
        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        
        # resets the canvas
        screen.fill(black)        
        
        # Draws the snow/stars from list
        for i in range(len(snow)):
            pygame.draw.circle(screen, white, [snow[i][0], snow[i][1]], 2)
            snow[i][1]+=1
        
            # Resets snow/stars
            if snow[i][1] > 600:
               snow[i][1] = random.randrange(-50, -10)
               snow[i][0] = random.randrange(0, 800)
        
        # the head
        pygame.draw.circle(screen, black, [400, 400], 300)
        
        # whites of pupils
        pygame.draw.ellipse(screen,white,[100,350,250,y])
        pygame.draw.ellipse(screen,white,[450,350,250,y])

        # iriss
        pygame.draw.circle(screen, black, [225, 400], 51)
        pygame.draw.circle(screen, black, [575, 400], 51)
        

        

        

        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # Limit to 20 frames per second
        clock.tick(20)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
