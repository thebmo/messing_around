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
    pygame.display.set_caption("This is a Test Title")
    
    x_origin = 50
    y_origin = 50
    
    x = x_origin
    y = y_origin
    
    x_change = 5
    y_change = 5
    score = 0
    rect_path = []
    while not stop:

        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                stop = True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                score+=1
            
        
        
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        
        


        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        
        x+= x_change
        y+= y_change
        rect_path.insert(0,(x,y))
        while(len(rect_path) > score):
            rect_path.pop()
        
        # Bounce the rectangle if needed
        if y > 550 or y < 0:
            y_change = y_change * -1
        if x > 750 or x < 0:
            x_change = x_change * -1
     
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
     
     
        
        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        
        # resets the canvas
        screen.fill(black)
        
        # main box
        pygame.draw.rect(screen, white, [x, y, 50, 50])
        
        # draws tail
        for pos in rect_path:
            pygame.draw.rect(screen, white, [pos[0]+20, pos[1]+20, 5, 5])
        font = pygame.font.Font(None, 25)
        text = font.render("SCORE: "+str(score),True, white)
        
        # Put the image of the text on the screen at 1x1
        screen.blit(text, [1,1])

        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        

        # Flips the screen to update
        pygame.display.flip()
        
        # Limit to 20 frames per second
        clock.tick(20)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
