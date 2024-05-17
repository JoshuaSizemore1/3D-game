import pygame
import random
import os
import math
import threading
import sys

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
        self.vol_cap = 2
        self.orientation_speed = 2.5
        self.look_start_point = pygame.math.Vector2(self.x_pos, self.y_pos)
        self.angle = self.orientation
        self.look_end_point = pygame.math.Vector2(50, 0)
        self.current_look_end_point = self.look_start_point + self.look_end_point.rotate(self.angle)
        self.new_x = 0
        self.new_y = 0
        self.old_orientation = self.orientation


    def update_pos(self):
        self.x_pos += self.x_vol
        self.y_pos += self.y_vol
        self.look_start_point = pygame.math.Vector2(self.x_pos, self.y_pos)
        self.current_look_end_point = self.look_start_point + self.look_end_point.rotate(self.angle)


    def check_movement(self):
        check = False
        check = self.check_key_w()
        if check == True:
            return None
        
        check = self.check_key_d()
        if check == True:
            return None
        
        check = self.check_key_s()
        if check == True:
            return None
        
        check = self.check_key_a()
        
        if check == False:
            self.x_vol = 0
            self.y_vol = 0

    def check_key_left(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.orientation  > 0:
                self.old_orientation = self.orientation
                self.orientation -= self.orientation_speed
            else:
                self.orientation = 360
            self.angle = (self.orientation)
            self.current_look_end_point = self.look_start_point + self.look_end_point.rotate(self.angle)

    def check_key_right(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            if self.orientation  < 360:
                self.old_orientation = self.orientation
                self.orientation += self.orientation_speed
            else:
                self.orientation = 0
            self.angle = (self.orientation)
            self.current_look_end_point = self.look_start_point + self.look_end_point.rotate(self.angle)
    
    def check_key_a(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_a]:

            self.check_key_right()
            self.check_key_left()

            b = math.sqrt(2)

            self.new_x = (b*(-((math.sin(math.radians(self.orientation + 135))) + (math.cos(math.radians(self.orientation + 135))))) + self.x_pos)
            self.new_y = (b*(((math.cos(math.radians(self.orientation + 135))) - (math.sin(math.radians(self.orientation + 135))))) + self.y_pos)

            new_run = (self.new_x - self.x_pos) 
            new_rise = (self.new_y - self.y_pos)

            self.x_vol = new_run
            self.y_vol = new_rise
            return True

        else:
            return False
    
    def check_key_w(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_w]:

            self.check_key_right()
            self.check_key_left()

            b = math.sqrt(2)
            self.new_x = (b*(((math.sin(math.radians(self.orientation + 45))) + (math.cos(math.radians(self.orientation + 45))))) + self.x_pos)
            self.new_y = (b*(-((math.cos(math.radians(self.orientation + 45))) - (math.sin(math.radians(self.orientation + 45))))) + self.y_pos)
            new_run = (self.new_x - self.x_pos) 
            new_rise = (self.new_y - self.y_pos)

            self.x_vol = new_run
            self.y_vol = new_rise
            return True
        else:
            return False
        
    def check_key_d(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_d]:

            self.check_key_right()
            self.check_key_left()

            b = math.sqrt(2)
            self.new_x = (b*(((math.sin(math.radians(self.orientation + 135))) + (math.cos(math.radians(self.orientation + 135))))) + self.x_pos)
            self.new_y = (b*(-((math.cos(math.radians(self.orientation + 135))) - (math.sin(math.radians(self.orientation + 135))))) + self.y_pos)
            new_run = (self.new_x - self.x_pos) 
            new_rise = (self.new_y - self.y_pos)

            self.x_vol = new_run
            self.y_vol = new_rise
            return True
        else:
            return False

    def check_key_s(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_s]:

            self.check_key_right()
            self.check_key_left()

            b = math.sqrt(2)
            self.new_x = (b*(((math.sin(math.radians(self.orientation + 225))) + (math.cos(math.radians(self.orientation + 225))))) + self.x_pos)
            self.new_y = (b*(-((math.cos(math.radians(self.orientation + 225))) - (math.sin(math.radians(self.orientation + 225))))) + self.y_pos)
            new_run = (self.new_x - self.x_pos) 
            new_rise = (self.new_y - self.y_pos)

            self.x_vol = new_run
            self.y_vol = new_rise
            return True
        else:
            return False

        
    

    def draw_on_map(self):
        pygame.draw.circle(screen, self.map_color, (self.x_pos, self.y_pos), 3)
        pygame.draw.line(screen, "red", self.look_start_point, self.current_look_end_point, 2)
        
        b = math.sqrt(162)

        nnew_x = (b*(((math.sin(math.radians(self.orientation + 45))) + (math.cos(math.radians(self.orientation + 45))))) + self.x_pos)
        nnew_y = (b*(-((math.cos(math.radians(self.orientation + 45))) - (math.sin(math.radians(self.orientation + 45))))) + self.y_pos)
        pygame.draw.line(screen, "green", (self.x_pos, self.y_pos), (nnew_x, nnew_y))

        nnnew_x = (b*(((math.sin(math.radians(self.orientation + 135))) + (math.cos(math.radians(self.orientation + 135))))) + self.x_pos)
        nnnew_y = (b*(-((math.cos(math.radians(self.orientation + 135))) - (math.sin(math.radians(self.orientation + 135))))) + self.y_pos)
        pygame.draw.line(screen, "orange", (self.x_pos, self.y_pos), (nnnew_x, nnnew_y))


        nnnnew_x = (b*(((math.sin(math.radians(self.orientation + 225))) + (math.cos(math.radians(self.orientation + 225))))) + self.x_pos)
        nnnnew_y = (b*(-((math.cos(math.radians(self.orientation + 225))) - (math.sin(math.radians(self.orientation + 225))))) + self.y_pos)
        pygame.draw.line(screen, "pink", (self.x_pos, self.y_pos), (nnnnew_x, nnnnew_y))


        new_x = (b*(-((math.sin(math.radians(self.orientation + 135))) + (math.cos(math.radians(self.orientation + 135))))) + self.x_pos)
        new_y = (b*(((math.cos(math.radians(self.orientation + 135))) - (math.sin(math.radians(self.orientation + 135))))) + self.y_pos)
        pygame.draw.line(screen, "blue", (self.x_pos, self.y_pos), (new_x, new_y))


player1 = Player(500,250,"red")
players = [player1]

def update_players():
    for player in players:
        player.update_pos()
        player.check_key_left()
        player.check_key_right()
        player.draw_on_map()
        player.check_movement()



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


pygame.quit()
sys.exit()