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

# colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)


# ------------------------------------ #
# selects a random (x, y) for an apple #
# takes resolu and current x/y coords  #
# returns a tuple                      #
# ------------------------------------ #
def spawn_apple(resolution, pos_x, pos_y):
    apple_x = random.randrange(resolution[0])
    apple_y = random.randrange(resolution[1])
    apple_tup = (apple_x, apple_y)
    return apple_tup

def draw_apple(screen, resolution, x, y):
    pygame.draw.rect(screen, red, [x, y, 5, 5])
    
    

# Define a main() function that prints a little greeting.
def main():
    stop = False
    pi = 3.141592653
    pygame.init()
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # Set the width and height of the screen
    size = (800,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("This is a Test Title")
    
    x_origin = (size[0]/2)
    y_origin = (size[1]/2)
    
    x = x_origin
    y = y_origin
    
    x_change = 1
    y_change = 1
    
    # clock tick (for fps and timer)
    TICK = 60
    
    timer = 61.000
    spawn_timer = 0
    score = 0
    rect_path = []
    apples = []
    game_over = False
    
    # controls object movemnt [0 up | 1 right | 2 down | 3 left]
    direction = 0
    while not stop:

        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                stop = True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 1:
                    direction = 3
                if event.key == pygame.K_RIGHT and direction != 3:
                    direction = 1
                if event.key == pygame.K_UP and direction != 2:
                    direction = 0
                if event.key == pygame.K_DOWN and direction != 0:
                    direction = 2
                # remove this later
                if event.key == pygame.K_SPACE: 
                    score+=1
        
        
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        


        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        
        # increments spawn timer
        spawn_timer += (1/(float(TICK)))
        
        # addes an apple ot the list
        if int(timer) %5 == 0 and (clock.get_time() == 70188):
            apples.append(spawn_apple(size, x, y))

        
        # timer logic based on tick
        if timer > 0:
            timer-=(1/(float(TICK)))
            
        
        
        # controls the flow of the snake
        if direction == 0:
            y-=y_change
        elif direction == 1:
            x+=x_change
        elif direction == 2:
            y+=y_change
        elif direction == 3:
            x-=y_change
        
        # game over triggers
        if x >= size[0] or x <= 0:
            game_over = True
        if y >= size[1] or y <= 0:
            game_over = True
        if timer <= 0:
            game_over = True
            x_change = 0 # put these somewhere else
            y_change = 0 # put these somewhere else
            
        # populates and maintains the length of snake
        if( not game_over ):
            rect_path.insert(0,(x,y))
        
        # how long to multiply the tail
        tail_length = 5
        while(len(rect_path) > score*tail_length):
            rect_path.pop()
        

     
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
     
     
        
        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        
        # resets the canvas
        screen.fill(black)
        
        # main box
        pygame.draw.rect(screen, green, [x, y, 5, 5])
        
        # draws tail
        for pos in rect_path:
            pygame.draw.rect(screen, green, [pos[0], pos[1], 5, 5])
        
        # draws apples
        for apple in apples:
            draw_apple(screen, size, apple[0], apple[1])
        
        
        # text to draw
        font = pygame.font.Font(None, 25)
        scoreLabel = font.render("SCORE: "+str(score),True, green)
        timerLabel = font.render("TIME: "+str(int(timer)),True, green)
        spawn_timerLabel = font.render("SP: "+str(int(spawn_timer)),True, green)
        
        # Put the image of the text on the screen at 1x1
        screen.blit(scoreLabel, [1,1])
        screen.blit(timerLabel, [400,1])
        screen.blit(spawn_timerLabel, [700,1])

        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        

        # Flips the screen to update
        pygame.display.flip()
        
        # Limit to 20 frames per second
        clock.tick(TICK)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
