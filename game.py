import pygame
import random
import os
import math
import threading

pwd = os.getcwd()

#Setting up game window for the game
pygame.init()

screen_size = [1000, 500]


screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
timer = pygame.time.Clock()
fps = 60
pygame.display.set_caption("3D Game") 


#Setting up map window for game
screen_size = [1000, 500]






#Global vars
running = True



#Player and their position 
class Player():
    def __init__(self, x_pos, y_pos, map_color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.map_color = map_color
        self.orientation = 0
        self.x_vol = 0
        self.y_vol = 0
        self.vol_cap = 4

    def update_pos(self):
        self.x_pos += self.x_vol
        self.y_pos += self.y_vol

    def check_key_left(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.orientation  < 360:
                self.orientation += 5
            else:
                self.orientation = 0

    def check_key_right(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            if self.orientation  > 0:
                self.orientation -= 5
            else:
                self.orientation = 360
    
    def check_key_a(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_a]:
            pass


player1 = Player(0,0,"red")
players = [player1]

def update_players():
    for player in players:
        player.update_pos()
        player.check_key_left()
        player.check_key_right()


def run_game():
    global running
    while running:
        timer.tick(fps)
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_players() 

        pygame.display.flip()

run_game()