import pygame
from settings import *
from player import Player
from ray_casting import ray_casting
from ray import ray_casting2
from map import world_map
import connect
from sprites_obj import *

connect.start()
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
f1 = pygame.font.Font(None, 36)
textures = {1: pygame.image.load('img/1.png').convert(),
            2: pygame.image.load('img/2.png').convert(),
            3: pygame.image.load('img/1.png').convert(),
            4: pygame.image.load('img/2.png').convert(),
            's': pygame.transform.scale(pygame.image.load('img/sky.png'), (1920, 1080)).convert()}
sprites = Sprites()
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    player.mouse_control()
    sc.fill(BLACK)
    sky_offset = 5 * math.degrees(player.angle) % WIDTH
    sc.blit(textures['s'], (sky_offset, 0))
    sc.blit(textures['s'], (sky_offset - WIDTH, 0))
    sc.blit(textures['s'], (sky_offset + WIDTH, 0))

    # pygame.draw.rect(sc, WHITE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, RED, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    walls = ray_casting2(player.pos, player.angle, textures)
    for obj in sprites.list_of_objects:
        walls.append(obj.object_locate(player))
    for obj in sorted(walls, key=lambda n: n[0], reverse=True):
        if obj[0]:
            _, object, object_pos = obj
            sc.blit(object, object_pos)
    # ray_casting(sc, player.pos, player.angle)

    scale = 5
    map_TILE = TILE // scale
    dx = 000
    dy = 000
    i = 1
    for gamer in gamers.values():
        color = (0 * i, 85 * i, 0 * i)
        text = f1.render(gamer['name'], True, color)
        sc.blit(text, (10, 200 + 50 * i))
        xx, yy, aa = gamer['pos']['x'], gamer['pos']['y'], gamer['pos']['angle']
        pygame.draw.circle(sc, color, (int(xx / TILE * map_TILE) + dx, int(yy / TILE * map_TILE) + dy), 12)
        pygame.draw.line(sc, color, (int(xx / TILE * map_TILE) + dx, int(yy / TILE * map_TILE) + dy),
                         (xx / scale + 20 * math.cos(aa) + dx,
                          yy / scale + 20 * math.sin(aa) + dy), 2)
        i += 1
    for x, y in world_map:
        pygame.draw.rect(sc, DARKGRAY,
                         (x // TILE * map_TILE + dx, y // TILE * map_TILE + dy, TILE // scale, TILE // scale), 0)

    pygame.display.flip()
    clock.tick(FPS)
    # print(clock.get_fps())
