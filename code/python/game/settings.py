import math

gamers = dict()
client = 1
socket_num = 1555
server = '192.168.0.35', socket_num
name = 'Gekichan'

# game settings
WIDTH = 1920
HEIGHT = 1080
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100

PENTA_HEIGHT = 5 * HEIGHT
DUBLE_HEIGHT = 2 * HEIGHT
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 200
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (100, 100)  # (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = TILE // 1  # 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (25, 220, 5)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)

# sprite settings
DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 1000
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS






































player_speed = TILE // 10
