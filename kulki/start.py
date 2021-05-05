import sys
import pygame
from random import randint
from ball2 import Ball2


class Start(object):
    atoms = []

    def __init__(self, num, board_size):

        # Config                            # H = ηH * R  (R = 9)
        self.size = board_size              # L = ηL * R
        board_left = 50
        board_top = 110
        board_width = board_height = self.size * 9
        legend_width = 550
        self.tps_max = 40.0
        self.width = board_width + board_left * 3 + legend_width
        if self.size < 30:
            self.height = board_height + board_top + 300
        else:
            self.height = board_height + board_top + 200
        self.border = 7
        loop = True
        timer = 0

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
        self.color5 = (237, 234, 233)       # grey

        # Layout variables
        board_width = board_height = self.size * 9
        board_left = 50
        board_top = 170
        button_width = 300
        button_height = 40

        # Layout
        board = pygame.Rect(board_left, board_top, board_width, board_height)
        legend = pygame.Rect(800, board_top, self.width - board_width - 150, board_height)
        button_1 = pygame.Rect(self.width/2-(button_width/2), self.height-button_height-20, button_width, button_height)

        # Initialising atoms
        # RED atom
        self.atoms.clear()
        czerwony = Ball2(self, board_left, board_top, board_left + 14,
              board_top + board_height - 14, 'r', 45, 5)
        self.atoms.append(czerwony)

        # BLUE atoms
        for i in range(num):
            self.atoms.append(Ball2(self, board_left, board_top,
                                    randint(board_left + 30, board_left + board_width - 30),
                                    randint(board_top + 30, board_top + board_height - 30),
                                    'b', randint(1, 360), randint(3, 10)))

        while loop:

            # Variables
            mx, my = pygame.mouse.get_pos()
            crash_count = self.atoms[0].crashes

            # Event Handler
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button_1.collidepoint((mx, my)):         # (powrót do menu głównego)
                            self.width = 700                        # resetowanie ustawień okna do wymiarów
                            self.height = 700                       # okna menu
                            pygame.init()
                            self.screen = pygame.display.set_mode((self.width, self.height))

                            for i in range(len(self.atoms)):        # resetowanie listy atomów w celu wygenerowania
                                self.atoms[i].atoms.clear()         # nowych daych po kolejnym wywołaniu
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
            # pygame.draw.rect(self.screen, self.color1_2, legend, 3)
            pygame.draw.rect(self.screen, self.color1, (0, 0, self.width, 120), 0)

            # Rendering text
            self.draw_text("Wersja właściwa", self.main_menu_font, self.color2, 50)
            self.draw_text("Powrót do menu głównego", self.normal_font, self.color2, self.height - 35)
            self.draw_legend_text("ηH = ηL = {}".format(self.size), self.legend_font, self.color2,
                                  board_top + 30, board_width + board_left * 3)
            self.draw_legend_text("Promień atomu R = 9", self.legend_font, self.color2, board_top + 70, board_width + board_left * 3)
            self.draw_legend_text("H = L = {}".format(self.size * 9), self.legend_font, self.color2,
                                  board_top + 110, board_width + board_left * 3)
            self.draw_legend_text("Liczba niebieskich atomów: {}".format(num),
                                  self.legend_font, self.color2, board_top + 150, board_width + board_left * 3)

            self.draw_legend_text("Liczba zderzeń czerwonego atomu: {}".format(crash_count),
                                  self.legend_font, self.color2, board_top + 230, board_width + board_left * 3)
            self.draw_legend_text("Czas: {}s".format(round(timer/self.tps_max, 1)),
                                  self.legend_font, self.color2, board_top + 270, board_width + board_left * 3)
            if timer > 0:
                self.draw_legend_text("Liczba zderzeń na sekundę: {}".format(round(crash_count/(timer/self.tps_max), 1)),
                                      self.legend_font, self.color2, board_top + 310, board_width + board_left * 3)

            # Rendering atoms
            if len(self.atoms) > 0:
                self.atoms[0].draw1()                   # czerwony atom
            for i in range(1, len(self.atoms)):         # niebieskie atomy
                self.atoms[i].draw()
            pygame.display.flip()
            #if timer > 0:
        print("Częstość zderzeń: {:.3f}".format(crash_count/(timer/self.tps_max)))
        print("Średnia droga swobodna: {:.5f}".format(czerwony.srednia_droga))

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