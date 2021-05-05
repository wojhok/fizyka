import pygame
import sys
class Graph(object):
    atoms = []

    def __init__(self,board_size, version):

        # Config
        self.X = 850
        self.Y = 700
        self.size = board_size# L = ηL * R
        self.option = version
        board_left = 50
        board_top = 110
        board_width = board_height = self.size * 10
        legend_width = 550
        self.tps_max = 40.0
        self.width = board_width + board_left * 3 + legend_width
        if self.size < 30:
            self.height = board_height + board_top + 300
        else:
            self.height = board_height + board_top + 200
        self.border = 7
        # Colors
        self.color0 = (255, 255, 255)  # white
        self.color1 = (206, 216, 232)  # very light blue
        self.color1_2 = (124, 149, 202)  # medium blue
        self.color2 = (43, 45, 66)  # dark blue
        self.color3 = (239, 35, 60)  # magenta
        self.color4 = (255, 97, 110)
        # Fonts
        self.main_menu_font = pygame.font.SysFont('Tahoma', 50, True, False)
        self.normal_font = pygame.font.SysFont('Calibri', 20, False, False)
        self.normal_bold_font = pygame.font.SysFont('Calibri', 20, True, False)
        self.legend_font = pygame.font.SysFont('Calibri', 30, False, False)

        # Init
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))

        button_width = 275
        button_height = 20
        display_surface = pygame.display.set_mode((self.X, self.Y))
        pygame.display.set_caption('Image')
        image = pygame.image.load(r'C://Pythonprojekty//fizyka//kulki//CzestośćZderzeńM500.png')
        image1 = pygame.image.load(r'C://Pythonprojekty//fizyka//kulki//CzestośćZderzeńM1k.png')
        image2 = pygame.image.load(r'C://Pythonprojekty//fizyka//kulki//CzestośćZderzeńM5k.png')
        image3 = pygame.image.load(r'C://Pythonprojekty//fizyka//kulki//CzestośćZderzeńM3k.png')
        image4 = pygame.image.load(r'C://Pythonprojekty//fizyka//kulki//SredniaDrogaM500.png')
        image5 = pygame.image.load(r'C://Pythonprojekty//fizyka//kulki//SredniaDrogaM1k.png')
        image6 = pygame.image.load(r'C://Pythonprojekty//fizyka//kulki//SredniaDrogaM5k.png')
        image7 = pygame.image.load(r'C://Pythonprojekty//fizyka//kulki//SredniaDrogaM3k.png')
        # Layout
        button_1 = pygame.Rect(self.X / 2 - (button_width / 2), self.Y - button_height -15, button_width,
                               button_height)
        loop = True

        while loop:
            # Rendering layout
            self.screen.fill(self.color0)
            # Variables
            mx, my = pygame.mouse.get_pos()
            if self.option == 1:
                display_surface.blit(image, (0, 0))
                display_surface.blit(image1, (430, 0))
                display_surface.blit(image2, (430, 330))
                display_surface.blit(image3, (0, 330))
            elif self.option == 2:
                display_surface.blit(image4, (0, 0))
                display_surface.blit(image5, (430, 0))
                display_surface.blit(image6, (430, 330))
                display_surface.blit(image7, (0, 330))
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
                            loop = False
            self.draw_text("Powrót do menu głównego", self.normal_font, self.color2, self.Y-35 )
            pygame.draw.rect(self.screen, self.color2, button_1, 2)
            # Ticking
            pygame.display.flip()

    def draw_text(self, text, font, color, h):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        (x, y) = text_rect.bottomright
        self.screen.blit(text_obj, (self.X/2 -100, h))