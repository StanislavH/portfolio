import sys
import map
import settings
from settings import *
import pygame
import math
import connect


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.sensitivy = 0.004

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        i = 0
        if keys[pygame.K_w]:
            dx = player_speed * cos_a
            dy = player_speed * sin_a
            i = 1
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a
            dy = -player_speed * sin_a
            i = 1
        if keys[pygame.K_a]:
            dx = player_speed * sin_a
            dy = -player_speed * cos_a
            i = 1
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a
            dy = player_speed * cos_a
            i = 1
        if keys[pygame.K_LEFT]:
            self.angle -= 0.06
            i = 1
        if keys[pygame.K_RIGHT]:
            self.angle += 0.06
            i = 1

        if i == 1:
            if (self.x // TILE * TILE, (self.y + dy) // TILE * TILE) in map.world_map:
                dy = 0
            if ((self.x + dx) // TILE * TILE, self.y // TILE * TILE) in map.world_map:
                dx = 0
            self.x += dx
            self.y += dy
            connect.send_pos(self.x, self.y, self.angle)
        if keys[pygame.K_ESCAPE]:
            sys.exit()

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivy
            connect.send_pos(self.x, self.y, self.angle)
