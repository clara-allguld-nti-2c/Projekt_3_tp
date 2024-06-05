import pygame
import random
from settings import *

# types list
# "." -> unknown
# "X" -> mine
# "C" -> clue
# "/" -> empty

class Tile: #initiera bricka
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = x * TILESIZE, y * TILESIZE
        self.image = image
        self.type = type 
        self.revealed = revealed
        self.flagged = flagged


    def draw(self, board_surface): #rita ut brickan på brädet
        if not self.flagged and self.revealed:
            board_surface.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            board_surface.blit(tile_flag, (self.x, self.y))
        elif not self.revealed:
            board_surface.blit(tile_unknown, (self.x, self.y))

    def __repr__(self):
        return self.type


class Board: #initiera brädet 
    def __init__(self):
                self.board_surface = pygame.Surface((WIDTH, HEIGHT))                self.board_list = [[Tile(col, row, tile_empty, ".") for row in range(ROWS)] for col in range(COLS)]

                self.place_mines()
                self.place_clues()
                self.dug = []


    def place_mines(self): #placera ut minor på brädet
        for _ in range(AMOUNT_MINES):
            while True:
                x = random.randint(0, ROWS-1)
                y = random.randint(0, COLS-1)

                if self.board_list[x][y].type == ".":
                    self.board_list[x][y].image = tile_mine
                    self.board_list[x][y].type = "X"
                    break


    def place_clues(self): #placera ut ledtrådar/clues på brädet, exempelvis 1, 2 eller 3
        for x in range(ROWS):
            for y in range(COLS):
                if self.board_list[x][y].type != "X":
                    total_mines = self.check_neighbours(x, y)
                    if total_mines > 0:
                        self.board_list[x][y].image = tile_numbers[total_mines-1]
                        self.board_list[x][y].type = "C"


    @staticmethod
    def is_inside(x, y): #kontrollera om en position är inom brädets gränser
        return 0 <= x < ROWS and 0 <= y < COLS

    def check_neighbours(self, x, y): #kollar igenom alla brickors grannar
        total_mines = 0               #för att senare få fram hur många minor
        for x_offset in range(-1, 2):        #som är granne med vald bricka (sedan kommer antalet visas på själva brickan)
            for y_offset in range(-1,2):  # både -1 och 1 är en tile iväg från bestämd tile men man skriver 2 eftersom det ska stoppa innan dess typ
                neighbour_x = x + x_offset
                neighbour_y = y + y_offset
                if self.is_inside(neighbour_x, neighbour_y) and self.board_list[neighbour_x][neighbour_y].type == "X":
                    total_mines += 1


        return total_mines


    def draw(self, screen): #Rita hela brädet
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0, 0))

    def dig(self, x, y): #kolla om bricka redan är grävd, då är den altlså redan i listan och behöver inte grövas igen
        self.dug.append((x, y))
        if self.board_list[x][y].type == "X":
            self.board_list[x][y].revealed = True
            self.board_list[x][y].image = tile_exploded #så när man vänsterklickar på en mina ("X") så byter den brickans bild till exploderad ikon
            return False
        elif self.board_list[x][y].type == "C":
            self.board_list[x][y].revealed = True # så om vi klickar på en ledtråd/clue ("C") kommer den bli revealed/inte dold/synas
            return True

        self.board_list[x][y].revealed = True # om vi inte tryckte på en mina och det är inte en ledtråd
            
        for row in range(max(0, x-1), min(ROWS-1, x+1)+1):
            for col in range(max(0, y-1), min(COLS-1, y+1)+1):
                if (row, col) not in self.dug:
                    self.dig(row, col)
        return True


    def display_board(self): 
        for row in self.board_list:
            print(row)
