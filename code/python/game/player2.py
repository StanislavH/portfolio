from settings import *
import pygame
import math
import map


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_w]:
            dx = player_speed * cos_a
            dy = player_speed * sin_a
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a
            dy = -player_speed * sin_a
        if keys[pygame.K_a]:
            dx = player_speed * sin_a
            dy = -player_speed * cos_a
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a
            dy = player_speed * cos_a

        if ((self.x + dx) // TILE * TILE, (self.y + dy) // TILE * TILE) in map.world_map:
            dx = 0
            dy = 0
        self.x += dx
        self.y += dy
        if keys[pygame.K_LEFT]:
            self.angle -= 0.04
        if keys[pygame.K_RIGHT]:
            self.angle += 0.04
