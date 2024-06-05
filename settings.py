import pygame
import os

# färger (r, g, b)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BGCOLOUR = DARKGREY #bakgrundsfärgen

# spelinställningar
TILESIZE = 32
ROWS = 20
COLS = 20
AMOUNT_MINES = 15
WIDTH = TILESIZE * ROWS
HEIGHT = TILESIZE * COLS
FPS = 60
TITLE = "Minröjjjj"

tile_numbers = []
for i in range (1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("minroj", "assets", f"Tile{i}.png")), (TILESIZE, TILESIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("minroj", "assets", "TileEmpty.png")), (TILESIZE, TILESIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("minroj", "assets", "TileExploded.png")), (TILESIZE, TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("minroj", "assets", "TileFlag.png")), (TILESIZE, TILESIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("minroj", "assets", "TileMine.png")), (TILESIZE, TILESIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("minroj", "assets", "TileUnknown.png")), (TILESIZE, TILESIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("minroj", "assets", "TileNotMine.png")), (TILESIZE, TILESIZE))
tile_win = pygame.transform.scale(pygame.image.load(os.path.join("minroj", "assets", "TileWin.png")), (WIDTH, HEIGHT))
tile_lose = pygame.transform.scale(pygame.image.load(os.path.join("minroj", "assets", "TileLose.png")), (WIDTH, HEIGHT))

