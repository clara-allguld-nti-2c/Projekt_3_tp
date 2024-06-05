import pygame
from settings import*
from sprites import*


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initierar spel-skärmen och ställ in titel och klocka och vinststatus
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.win = False  #vinststatus


    def new(self): #nytt spelbräde skapas
        self.board = Board()
        self.board.display_board()


    def run(self): #huvudspelsloopen typ
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        else:
            self.end_screen()


    def draw(self): #fyller i bakrgunden och ritar skälva brädet med brickorna
        self.screen.fill(BGCOLOUR)
        self.board.draw(self.screen)
        pygame.display.flip()

    def check_win(self): #kollar igeonom hela boarden, om den hittar en bricka som inte är en mina och inte är avslöjad så returnar false och spelet forsätter
        for row in self.board.board_list: #eller om den inte hittar en bricka som inte är en mina eller inte är avslöjad - alltså att alla brickor är avsöjade, förutom minorna, då returnar true och spelet tar slut
            for tile in row: #man måste inte flagga alltså utan man kan vinna öndå, men den kommer flagga alla minor åt dig i slutet
                if tile.type != "X" and not tile.revealed:
                    return False
        return True

    def events(self): #spelhändelser
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()  #se exakt vilken bricka vi klickar på genom att hämta musens pos(ition) och omvandlar till koordinater på brädet som ett grid basically
                mx //= TILESIZE  
                my //= TILESIZE
                
                if event.button == 1: #vänsterklick
                    if not self.board.board_list[mx][my].flagged:
                        # gräva och också kolla ifall den har exploderat
                        if not self.board.dig(mx, my):
                            # explodera
                            for row in self.board.board_list:
                                for tile in row:
                                    if tile.flagged and tile.type != "X": #så om en bricka r flaggad och INTE är en mina så vill vi avflagga den och visa den och byta bilden till inte-mina
                                        tile.flagged = False
                                        tile.revealed = True
                                        tile.image = tile_not_mine
                                    elif tile.type == "X":
                                        tile.revealed = True
                            self.draw()  # visar alla minor
                            pygame.time.wait(1000)  # väntar 1 sekund innan spelet slutar
                            self.win = False
                            self.playing = False   

                if event.button == 3: # högerklick (flagga)
                    if not self.board.board_list[mx][my].revealed:
                        self.board.board_list[mx][my].flagged = not self.board.board_list[mx][my].flagged
                
                if self.check_win(): #kontrollera om vi vann
                    self.win = True #vi vann, vi har alltså avslöjat alla brickor förutom minorna 
                    self.playing = False
                    for row in self.board.board_list:
                        for tile in row:
                            if not tile.revealed: # då checkar vi alla brickor, och om den inte är avslöjad så är det en mina 
                                tile.flagged = True # och då flaggar vi minan
                    self.draw()  # visar alla minor
                    pygame.time.wait(1000)  # väntar 1 sekund innan spelet slutar
                    self.win_screen() #visa vinstkärmen



    def end_screen(self): #välj vilken slutskärm beroende på vinststatusen
        if self.win:
            self.win_screen()
        else:
            self.lose_screen()


    def win_screen(self): #vinstkärmen
        self.screen.blit(tile_win, (0, 0))
        pygame.display.flip()
        while True:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                     quit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

    def lose_screen(self): #förlorarskärmen
        self.screen.blit(tile_lose, (0, 0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return


game = Game()
while True:
    game.new()
    game.run()