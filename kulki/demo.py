import sys
import pygame
from random import randint
from ball import Ball


class Demo(object):
    atoms = []
    def __init__(self, num, board_size):

        # Config                            # H = ηH * R  (R = 9)
        self.size = board_size              # L = ηL * R
        board_left = 50
        board_top = 110
        board_width = board_height = self.size * 9
        legend_width = 300
        self.tps_max = 40.0
        self.width = board_width + board_left * 3 + legend_width
        self.height = board_height + board_top + 150
        self.border = 7

        # Init
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        # Fonts
        self.main_menu_font = pygame.font.SysFont('Tahoma', 50, True, False)
        self.normal_font = pygame.font.SysFont('Calibri', 20, False, False)
        self.normal_bold_font = pygame.font.SysFont('Calibri', 20, True, False)
        self.legend_font = pygame.font.SysFont('Calibri', 30, False, False)

        # Colors
        self.color0 = (255, 255, 255)       # white
        self.color1 = (206, 216, 232)       # very light blue
        self.color1_2 = (124, 149, 202)     # medium blue
        self.color2 = (43, 45, 66)          # dark blue
        self.color3 = (239, 35, 60)         # magenta
        self.color4 = (255, 97, 110)        # pink

        # Layout variables
        button_width = 300
        button_height = 40

        # Layout
        board = pygame.Rect(board_left, board_top, board_width, board_height)
        button_1 = pygame.Rect(self.width/2-(button_width/2), self.height-button_height-20, button_width, button_height)

        # Initialising atoms
        self.atoms.clear()
        for i in range(num):
            self.atoms.append(Ball(self, board_left, board_top,
                                   randint(board_left + 30, board_left + board_width - 30),
                                   randint(board_top + 30, board_top + board_height - 30), randint(1, 360),
                                   randint(5, 10)))

        # Variables
        loop = True
        timer = 0

        while loop:

            # Variables
            mx, my = pygame.mouse.get_pos()

            crash_count = 0                                             # Zliczanie zderzeń wszystkich atomów
            for i in range(num):
                crash_count = crash_count + self.atoms[i].crashes

            # Event Handler
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button_1.collidepoint((mx, my)):             # (powrót do menu głównego)
                            self.width = 700                            # resetowanie ustawień okna do wymiarów
                            self.height = 700                           # okna menu
                            pygame.init()
                            self.screen = pygame.display.set_mode((self.width, self.height))

                            for i in range(len(self.atoms)):            # resetowanie listy atomów w celu wygenerowania
                                self.atoms[i].atoms.clear()             # nowych danych po kolejnym wywołaniu
                            self.atoms.clear()
                            loop = False


            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max
                timer = timer + 1

            # Rendering layout
            self.screen.fill(self.color0)
            pygame.draw.rect(self.screen, self.color2, button_1, 2)
            pygame.draw.rect(self.screen, self.color2, board, 7)
            # pygame.draw.rect(self.screen, self.color4, pause_button, 0)

            # Rendering text
            self.draw_text("Wersja testowa", self.main_menu_font, self.color2, 50)
            self.draw_text("Powrót do menu głównego", self.normal_font, self.color2, self.height - 35)
            self.draw_legend_text("Liczba atomów: {}".format(len(self.atoms)),
                                  self.legend_font, self.color2, board_top + 30, board_width + board_left * 2)
            self.draw_legend_text("Liczba zderzeń : {}".format(crash_count),
                                  self.legend_font, self.color2, board_top + 70, board_width + board_left * 2)
            self.draw_legend_text("Czas: {}s".format(round(timer/self.tps_max, 1)),
                                  self.legend_font, self.color2, board_top + 110, board_width + board_left * 2)
            if timer > 0:
                self.draw_legend_text("Zderzeń na sekundę: {}".format(round(crash_count/(timer/self.tps_max), 1)),
                                      self.legend_font, self.color2, board_top + 150, board_width + board_left * 2)

            # Rendering atoms
            for i in range(len(self.atoms)):
                self.atoms[i].draw()
            pygame.display.flip()

    def tick(self):
        for i in range(len(self.atoms)):
            self.atoms[i].tick()

    def draw_text(self, text, font, color, h):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        (x, y) = text_rect.bottomright
        self.screen.blit(text_obj, (self.width / 2 - x / 2, h - y / 2))

    def draw_legend_text(self, text, font, color, h, w):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        (x, y) = text_rect.bottomright
        self.screen.blit(text_obj, (w, h - y / 2))

    def draw_border(self):
        pygame.draw.rect(self.screen, (148, 126, 176), pygame.Rect(0, 0, self.width, self.border))
        pygame.draw.rect(self.screen, (148, 126, 176), pygame.Rect(0, 0, self.border, self.height))
        pygame.draw.rect(self.screen, (148, 126, 176), pygame.Rect(0, self.height - self.border, self.width, self.border))
        pygame.draw.rect(self.screen, (148, 126, 176), pygame.Rect(self.width - self.border, 0, self.border, self.height))

