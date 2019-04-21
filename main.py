#!/usr/bin/env python3
"""
Python implementation of a (somewhat) general 2D cellular automaton

Conway's Game of Life is implemented.

Implementation of the single rotation rule is a goal:
http://dmishin.blogspot.com/2013/11/the-single-rotation-rule-remarkably.html

HackerNews discussion:
https://news.ycombinator.com/item?id=19188361

2019.04.12  --  L. Boyd
"""

import time

import numpy as np
import pygame

class CA(object):
    def __init__(self, board, rule, clock=0.2, neighborhood='normal'):
        """
        board is an image.Image type with the initial board state
        rule is a function that takes a 3x3 array and updates the state
        """
        self.board = board
        self.rule = rule
        self.clock = clock
        self.neighborhood = neighborhood # can have value 'normal' or 'margolus'

    def update(self, parity=0):
        """
        Update the board state according to the provided rule.
        The parity input is used for the Margolus neighborhood
        """
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                chunk = self.board.take(range(-1,2), mode='wrap', axis=0)
                chunk = chunk.take(range(-1,2), mode='wrap', axis=1)
                #self.board.set((i,j), self.rule(chunk))
                self.rule(chunk)

    def run(self):
        """Continually update the state and render the screen with PyGame"""
        # initialize PyGame
        pygame.init()
        screen = pygame.display.set_mode(self.board.shape)

        #scaled_shape = [x*10 for x in self.board.shape] 
        #surf = pygame.transform.scale(surf, scaled_shape)

        clock = pygame.time.Clock()
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            surf = pygame.surfarray.make_surface(self.board)
            screen.blit(surf, (0,0))
            pygame.display.flip()
            self.update()
            clock.tick(1)


def game_of_life(data):
    self = data[1, 1]
    neighbors = data[0, 0] + data[0, 1] + data[0, 2] + \
                data[1, 0] +              data[1, 2] + \
                data[2, 0] + data[2, 1] + data[2, 2]

    if self:
        if neighbors < 2 or neighbors > 3:
            return 0
    elif neighbors == 3:
        return 1
    return 0

# initialize a board to a game-of-life glider
board = np.zeros((100,100), dtype=np.uint8)
board[3,2] = 255
board[4,2] = 255
board[5,2] = 255
board[5,2] = 255
board[4,2] = 255

ca = CA(board, game_of_life)

ca.run()

print('All done.')

