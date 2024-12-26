import pygame
from pygame import Rect

from Game import Game

class GameUI:
    def __init__(self):
        self.cell_size = (64, 64)

        self.game = Game()

        pygame.init()
        self.screen = pygame.display.set_mode(( self.cell_size[0] * 8,  self.cell_size[1] * 8))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('шашки')
        
        self.clock = pygame.time.Clock()
        self.w_sprite = pygame.image.load('w.png')
        self.w_sprite.set_colorkey((255,255,255))
        self.sw_sprite = pygame.image.load('sw.png')
        self.sw_sprite.set_colorkey((255,255,255))
        self.b_sprite = pygame.image.load('b.png')
        self.b_sprite.set_colorkey((255,255,255))
        self.sb_sprite = pygame.image.load('sb.png')
        self.sb_sprite.set_colorkey((255,255,255))
    def draw_shashki(self):
        name_to_sprite = {"w": self.w_sprite, "sw": self.sw_sprite, "b": self.b_sprite, "sb": self.sb_sprite}
        for y in range(8):
            for x in range(8):
                cell = self.game.get_piece(x, y)
                if cell != " ":
                    self.screen.blit(name_to_sprite[cell], (x*self.cell_size[0], y*self.cell_size[1]))

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for i in range(8*8):
            x, y = i % 8, i // 8
            if x % 2 != y % 2:
                pygame.draw.rect(self.screen, (0, 0, 0), Rect((x * self.cell_size[0], y * self.cell_size[1]), self.cell_size))
                
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
        
                x, y = pygame.mouse.get_pos()
                x, y = x//self.cell_size[0], y//self.cell_size[0]
                print("Вы ввели", x, y, "здесь находится фигура", self.game.get_piece(x, y))
                self.game.input(x,y)

    def run(self):
        while True:
            self.input()
            self.draw_board()

            self.draw_shashki()

            pygame.display.update()
            self.clock.tick(30)
