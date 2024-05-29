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
        self.b = math.sqrt(.3)


    def update_pos(self):
        self.x_pos += self.x_vol
        self.y_pos += self.y_vol
        self.look_start_point = pygame.math.Vector2(self.x_pos, self.y_pos)
        self.current_look_end_point = self.look_start_point + self.look_end_point.rotate(self.angle)


    def check_movement(self):
        check = 0

        check += self.check_key_w()
        self.update_pos()
        check += self.check_key_s()
        self.update_pos()
        
        if check == 0:
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
    

    def check_key_w(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_w]:
            if key[pygame.K_a]:
                self.check_key_right()
                self.check_key_left()
                self.new_x = (self.b*(-((math.sin(math.radians(self.orientation + 180))) + (math.cos(math.radians(self.orientation + 180))))) + self.x_pos)
                self.new_y = (self.b*(((math.cos(math.radians(self.orientation + 180))) - (math.sin(math.radians(self.orientation + 180))))) + self.y_pos)
                new_run = (self.new_x - self.x_pos)
                new_rise = (self.new_y - self.y_pos)
                self.x_vol = new_run
                self.y_vol = new_rise
                return 1
            elif key[pygame.K_d]:
                self.check_key_right()
                self.check_key_left()
                self.new_x = (self.b*(-((math.sin(math.radians(self.orientation + 270))) + (math.cos(math.radians(self.orientation + 270))))) + self.x_pos)
                self.new_y = (self.b*(((math.cos(math.radians(self.orientation + 270))) - (math.sin(math.radians(self.orientation + 270))))) + self.y_pos)
                new_run = (self.new_x - self.x_pos)
                new_rise = (self.new_y - self.y_pos)
                self.x_vol = new_run
                self.y_vol = new_rise
                return 1
            else:
                self.check_key_right()
                self.check_key_left()
                self.new_x = (self.b*(((math.sin(math.radians(self.orientation + 45))) + (math.cos(math.radians(self.orientation + 45))))) + self.x_pos)
                self.new_y = (self.b*(-((math.cos(math.radians(self.orientation + 45))) - (math.sin(math.radians(self.orientation + 45))))) + self.y_pos)
                new_run = (self.new_x - self.x_pos) 
                new_rise = (self.new_y - self.y_pos)

                self.x_vol = new_run
                self.y_vol = new_rise
                return 1
            
        elif key[pygame.K_a] and not key[pygame.K_s]:
            self.check_key_right()
            self.check_key_left()


            self.new_x = (self.b*(-((math.sin(math.radians(self.orientation + 135))) + (math.cos(math.radians(self.orientation + 135))))) + self.x_pos)
            self.new_y = (self.b*(((math.cos(math.radians(self.orientation + 135))) - (math.sin(math.radians(self.orientation + 135))))) + self.y_pos)

            new_run = (self.new_x - self.x_pos) 
            new_rise = (self.new_y - self.y_pos)

            self.x_vol = new_run
            self.y_vol = new_rise
            return 1
        
        elif key[pygame.K_d] and not key[pygame.K_s]:
            self.check_key_right()
            self.check_key_left()


            self.new_x = (self.b*(((math.sin(math.radians(self.orientation + 135))) + (math.cos(math.radians(self.orientation + 135))))) + self.x_pos)
            self.new_y = (self.b*(-((math.cos(math.radians(self.orientation + 135))) - (math.sin(math.radians(self.orientation + 135))))) + self.y_pos)
            new_run = (self.new_x - self.x_pos) 
            new_rise = (self.new_y - self.y_pos)

            self.x_vol = new_run
            self.y_vol = new_rise
            return 1
        else:
            return 0
        


    def check_key_s(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_s]:
            if key[pygame.K_a]:
                self.check_key_right()
                self.check_key_left()
                self.new_x = (self.b*(-((math.sin(math.radians(self.orientation + 90))) + (math.cos(math.radians(self.orientation + 90))))) + self.x_pos)
                self.new_y = (self.b*(((math.cos(math.radians(self.orientation + 90))) - (math.sin(math.radians(self.orientation + 90))))) + self.y_pos)
                new_run = (self.new_x - self.x_pos)
                new_rise = (self.new_y - self.y_pos)
                self.x_vol = new_run
                self.y_vol = new_rise
                return 1
            
            elif key[pygame.K_d]:
                self.check_key_right()
                self.check_key_left()
                self.new_x = (self.b*(-((math.sin(math.radians(self.orientation + 0))) + (math.cos(math.radians(self.orientation + 0))))) + self.x_pos)
                self.new_y = (self.b*(((math.cos(math.radians(self.orientation + 0))) - (math.sin(math.radians(self.orientation + 0))))) + self.y_pos)
                new_run = (self.new_x - self.x_pos)
                new_rise = (self.new_y - self.y_pos)
                self.x_vol = new_run
                self.y_vol = new_rise
                return 1
            else:
                self.check_key_right()
                self.check_key_left()


                self.new_x = (self.b*(((math.sin(math.radians(self.orientation + 225))) + (math.cos(math.radians(self.orientation + 225))))) + self.x_pos)
                self.new_y = (self.b*(-((math.cos(math.radians(self.orientation + 225))) - (math.sin(math.radians(self.orientation + 225))))) + self.y_pos)
                new_run = (self.new_x - self.x_pos) 
                new_rise = (self.new_y - self.y_pos)

                self.x_vol = new_run
                self.y_vol = new_rise
                return 1
        else:
            return 0

        
    

    def draw_on_map(self):
        pygame.draw.circle(screen, self.map_color, (self.x_pos, self.y_pos), 3)
        pygame.draw.line(screen, "red", self.look_start_point, self.current_look_end_point, 1)

        #b = math.sqrt(162)
        """b= math.sqrt(162)

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

        new_xx = (b*(-((math.sin(math.radians(self.orientation + 90))) + (math.cos(math.radians(self.orientation + 90))))) + self.x_pos)
        new_yy = (b*(((math.cos(math.radians(self.orientation + 90))) - (math.sin(math.radians(self.orientation + 90))))) + self.y_pos)
        pygame.draw.line(screen, "yellow", (self.x_pos, self.y_pos), (new_xx, new_yy))

        new_xxx = (b*(-((math.sin(math.radians(self.orientation + 0))) + (math.cos(math.radians(self.orientation + 0))))) + self.x_pos)
        new_yyy = (b*(((math.cos(math.radians(self.orientation + 0))) - (math.sin(math.radians(self.orientation + 0))))) + self.y_pos)
        pygame.draw.line(screen, "grey", (self.x_pos, self.y_pos), (new_xxx, new_yyy))

        neww_xx = (b*(-((math.sin(math.radians(self.orientation + 180))) + (math.cos(math.radians(self.orientation + 180))))) + self.x_pos)
        neww_yy = (b*(((math.cos(math.radians(self.orientation + 180))) - (math.sin(math.radians(self.orientation + 180))))) + self.y_pos)
        pygame.draw.line(screen, "black", (self.x_pos, self.y_pos), (neww_xx, neww_yy))

        newww_xx = (b*(-((math.sin(math.radians(self.orientation + 270))) + (math.cos(math.radians(self.orientation + 270))))) + self.x_pos)
        newww_yy = (b*(((math.cos(math.radians(self.orientation + 270))) - (math.sin(math.radians(self.orientation + 270))))) + self.y_pos)
        pygame.draw.line(screen, "purple", (self.x_pos, self.y_pos), (newww_xx, newww_yy))"""
        


class Wall():
    def __init__(self, x_pos, y_pos, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = None
        self.top = None
        self.bottom = None
        self.can_draw = True
        self.color = color

    def check_height(self):
        for player in players:
            player_x_distance = abs(player.x_pos - self.x_pos)
            total_distance = 5*(player_x_distance/10)
            self.height = 2*total_distance

            self.top = 0 + (self.height /2)
            self.bottom = 500 - (self.height /2)
            self.top = int(self.top)
            self.bottom = int(self.bottom)

    def draw_on_map(self):
        pass
    
    
    def draw(self):
        pygame.draw.line(screen, self.color, (500, self.top), (500, self.bottom))







player1 = Player(500,250,"red")
players = [player1]



wall1 = Wall(700, 350, "black")
walls = [wall1]


def update_players():
    for player in players:
        player.update_pos()
        player.check_key_left()
        player.check_key_right()
        player.draw_on_map()
        player.check_movement()


def update_walls():
    for wall in walls:
        wall.check_height()
        wall.draw()


def run_game():
    global running
    while running:
        timer.tick(fps)
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_players() 
        update_walls()
        pygame.display.flip()

run_game()


pygame.quit()
sys.exit()