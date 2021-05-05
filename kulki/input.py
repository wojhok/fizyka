import sys
import pygame
from start import Start
from demo import Demo
from Graphs import Graph

class Input(object):

    def __init__(self, version):

        # Config
        self.tps_max = 10.0
        self.width = 700
        self.height = 700

        # Init
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        # Fonts
        self.main_menu_font = pygame.font.SysFont('Tahoma', 40, True, False)
        self.small_bold_font = pygame.font.SysFont('Calibri', 25, True, False)
        self.small_font = pygame.font.SysFont('Calibri', 22, False, False)
        self.normal_font = pygame.font.SysFont('Calibri', 35, False, False)
        self.normal_bold_font = pygame.font.SysFont('Calibri', 35, True, False)

        # Colors
        self.color0 = (255, 255, 255)
        self.color1 = (206, 216, 232)
        self.color1_2 = (124, 149, 202)
        self.color2 = (43, 45, 66)
        self.color3 = (239, 35, 60)
        self.color4 = (255, 97, 110)

        # Variables
        atoms_input = ''
        board_size_input = ''
        self.err_message = ''
        loop = True
        input1_on = False
        input2_on = False

        while loop:

            # Variables
            mx, my = pygame.mouse.get_pos()
            button_width = 300
            button_height = 70

            # Layout
            input_rect1 = pygame.Rect(self.width/2-(button_width/2), 230-(button_height/2), button_width, button_height)
            input_rect2 = pygame.Rect(self.width/2-(button_width/2), 385-(button_height/2), button_width, button_height)
            button_2 = pygame.Rect(self.width/2-(button_width/2), 480-(button_height/2), button_width, button_height)
            button_3 = pygame.Rect(self.width/2-(button_width/2), 640, 300, 40)
            button_4 = pygame.Rect(self.width/2-(button_width/2),170-(button_height/2), button_width , 60)
            button_5 = pygame.Rect(self.width/2-(button_width/2),320-(button_height/2), button_width, 60)
            text_surface1 = self.normal_font.render(atoms_input, True, self.color2)
            text_surface2 = self.normal_font.render(board_size_input, True, self.color2)

            # Event Handler
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    sys.exit(0)

                # naciśnięcie klawisza klawiatury
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        input1_on = False
                        input2_on = False
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if self.input_check(atoms_input) and self.input_check(board_size_input):
                            if self.numbers_check(int(atoms_input), int(board_size_input)):
                                if version == 1:
                                    Start(int(atoms_input), int(board_size_input))
                                elif version == 2:
                                    Demo(int(atoms_input), int(board_size_input))
                    elif input1_on:
                        if event.key == pygame.K_BACKSPACE:
                            atoms_input = atoms_input[:-1]
                            print(atoms_input)
                        else:
                            atoms_input += event.unicode
                            print(atoms_input)
                    elif input2_on:
                        if event.key == pygame.K_BACKSPACE:
                            board_size_input = board_size_input[:-1]
                            print(board_size_input)
                        else:
                            board_size_input += event.unicode
                            print(board_size_input)

                # kliknięcia myszką
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if version == 3:
                            if button_4.collidepoint(mx, my):
                                Graph(50, 1)
                            elif button_5.collidepoint(mx, my):
                                Graph(50, 2)
                            elif button_3.collidepoint(mx, my):
                                input2_on = False
                                input1_on = False
                                loop = False
                        elif input_rect1.collidepoint(mx, my):
                            input1_on = True
                            input2_on = False
                        elif input_rect2.collidepoint(mx, my):
                            input2_on = True
                            input1_on = False
                        elif button_2.collidepoint(mx, my):
                            print("Kliknieto button2")
                            input2_on = False
                            input1_on = False
                            if self.input_check(atoms_input) and self.input_check(board_size_input):
                                if self.numbers_check(int(atoms_input), int(board_size_input)):
                                    if version == 1:
                                        Start(int(atoms_input), int(board_size_input))
                                    elif version == 2:
                                        Demo(int(atoms_input), int(board_size_input))
                        elif button_3.collidepoint(mx, my):
                            print("Kliknieto button3")
                            input2_on = False
                            input1_on = False
                            loop = False
                        else:
                            input2_on = False
                            input1_on = False


            if version == 1 or version == 2:
                # Ticking
                self.tps_delta += self.tps_clock.tick() / 1000.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # Rendering layout
                self.screen.fill(self.color0)
                pygame.draw.rect(self.screen, self.color1, (0, 0, self.width, 130), 0)
                pygame.draw.rect(self.screen, self.color4, button_2, 0)
                pygame.draw.rect(self.screen, self.color1, (0, self.height - 100, self.width, 100), 0)
                pygame.draw.rect(self.screen, self.color2, button_3, 2)
                if input1_on is True:
                    pygame.draw.rect(self.screen, self.color3, input_rect1, 4)
                else:
                    pygame.draw.rect(self.screen, self.color2, input_rect1, 2)
                if input2_on is True:
                    pygame.draw.rect(self.screen, self.color3, input_rect2, 4)
                else:
                    pygame.draw.rect(self.screen, self.color2, input_rect2, 2)

                # Rendering text
                self.draw_text("Podaj dane wejściowe", self.main_menu_font, self.color2, 60)
                self.draw_text("Liczba atomów N:", self.normal_font, self.color2, 170)
                self.draw_text("Współczynnik ηH i ηH:", self.normal_font, self.color2, 320)
                self.draw_text("DALEJ", self.normal_font, self.color0, 480)
                self.draw_text("Powrót do menu głównego", self.small_font, self.color2, 662)
                if self.err_message != '':
                    self.draw_text(self.err_message, self.small_font, self.color4, 550)

                # wyświetlanie wpisywanego tekstu
                self.draw_input_text(text_surface1, atoms_input, 215)
                self.draw_input_text(text_surface2, board_size_input, 370)

                pygame.display.update()
            elif version == 3:
                self.screen.fill(self.color0)
                self.tps_delta += self.tps_clock.tick() / 1000.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                pygame.draw.rect(self.screen, self.color2, button_3, 2)
                pygame.draw.rect(self.screen, self.color2, button_5, 0)
                pygame.draw.rect(self.screen, self.color2, button_4, 0)

                self.draw_text("Wybierz Wykres:", self.main_menu_font,self.color2,40)
                self.draw_text("Wykres nr I", self.normal_font, self.color0, 170)
                self.draw_text("Wykres nr II", self.normal_font, self.color0, 320)
                self.draw_text("Powrót do menu głównego", self.small_font, self.color2, 662)
                pygame.display.update()

    def tick(self):
        pass

    def draw_text(self, text, font, color, h):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        (x, y) = text_rect.bottomright
        self.screen.blit(text_obj, (self.width / 2 - x / 2, h - y / 2))

    def draw_border(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0, 0, self.width, self.border))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0, 0, self.border, self.height))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0, self.height - self.border, self.width, self.border))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.width - self.border, 0, self.border, self.height))

    def draw_input_text(self, text_surface, text, height):
        self.screen.blit(text_surface, (self.width / 2 - 9 * len(text), height))

    def input_check(self, input_text):
        try:
            num = int(input_text)
        except ValueError:
            print("Nie podano liczby całkowitej")
            self.err_message = "Wprowadzono błędne dane."
            return False

        if num <= 0:
            print("Podana liczba jest zbyt mała")
            self.err_message = "Wprowadzono błędne dane."
            return False
        else:
            print("Wprowadzona liczba =", num)
            return True

    def numbers_check(self, atoms, board_size):
        if atoms > board_size**2 / 4:
            self.err_message = "Podana liczba atomów jest zbyt wielka dla danego rozmiaru pojemnika."
            return False
        else:
            return True