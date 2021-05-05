import pygame
import sys
from input import Input


class Menu(object):

    def __init__(self):

        # Config
        self.tps_max = 10.0
        self.width = 700
        self.height = 700
        self.border = 5

        # Init
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        # Fonts
        self.main_menu_font = pygame.font.SysFont('Tahoma', 40, True, False)
        self.small_font = pygame.font.SysFont('Calibri', 25, True, False)
        self.normal_font = pygame.font.SysFont('Calibri', 35, False, False)
        self.normal_bold_font = pygame.font.SysFont('Calibri', 35, True, False)

        # Colors
        self.color0 = (255, 255, 255)           # white
        self.color1 = (206, 216, 232)           # very light blue
        self.color1_2 = (124, 149, 202)         # medium blue
        self.color2 = (43, 45, 66)              # dark blue
        self.color3 = (239, 35, 60)             # magenta
        self.color4 = (255, 97, 110)            # pink

        while True:

            # Variables
            mx, my = pygame.mouse.get_pos()
            button_width = 300
            button_height = 70

            # Button layout
            button_1 = pygame.Rect(self.width/2-(button_width/2), 250-(button_height/2), button_width, button_height)
            button_2 = pygame.Rect(self.width/2-(button_width/2), 350-(button_height/2), button_width, button_height)
            button_4 = pygame.Rect(self.width / 2 - (button_width / 2), 450 - (button_height / 2), button_width,button_height)
            button_3 = pygame.Rect(self.width/2-(button_width/2), 550-(button_height/2), button_width, button_height)

            # Event Handler
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == True:
                        if button_1.collidepoint(mx, my):
                            print("Kliknieto przycisk nr 1: Start")
                            Input(1)
                        elif button_2.collidepoint(mx, my):
                            print("Kliknieto przycisk nr 2: Demo")
                            Input(2)
                        elif button_3.collidepoint(mx, my):
                            print("Kliknieto przycisk nr 3: Zamknij")
                            sys.exit(0)
                        elif button_4.collidepoint(mx, my):
                            print("Kliknięto przysik: Wykresy")
                            Input(3)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # Rendering
            self.screen.fill(self.color0)
            pygame.draw.rect(self.screen, self.color1, (0, 0, self.width, 160), 0)
            pygame.draw.rect(self.screen, self.color2, button_1, 4)
            pygame.draw.rect(self.screen, self.color3, button_2, 2)
            pygame.draw.rect(self.screen, self.color4, button_3, 0)
            pygame.draw.rect(self.screen,self.color2, button_4, 3)
            pygame.draw.rect(self.screen, self.color1, (0, self.height-100, self.width, 100), 0)

            self.draw_text("ZADANIE PROGRAMISTYCZNE", self.main_menu_font, self.color2, 70)
            self.draw_text("WARIANT B", self.small_font, self.color2, 110)
            self.draw_text("START", self.normal_bold_font, self.color2, 250)
            self.draw_text("WERSJA DEMO", self.normal_font, self.color4, 350)
            self.draw_text("WYKRESY", self.normal_bold_font, self.color2, 450)
            self.draw_text("ZAMKNIJ", self.normal_font, self.color0, 550)
            pygame.display.update()

    def tick(self):
        pass

    def draw_text(self, text, font, color, h):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        (x, y) = text_rect.bottomright
        self.screen.blit(text_obj, (self.width / 2 - x / 2, h - y / 2))
