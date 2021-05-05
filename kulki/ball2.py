import pygame
from math import pi, atan, sqrt, sin, cos, radians
from copy import deepcopy
from timeit import default_timer as timer


class Ball2:
    atoms = []

    def __init__(self, board, board_left, board_top, x, y, color, angle, speed):
        # Init board
        self.board = board
        self.board_border = 7
        self.board_width = self.board_height = self.board.size * 9     # szerokość i długość planszy (self.width to szerokość całego okna)
        self.board_left = board_left                                   # przesunięcie planszy względem lewej krawędzi okna
        self.board_top = board_top                                     # przesunięcie planszy względem górnej krawędzi okna

        # Variables
        self.radius = 9                             # Promień atomu
        self.mas = 1                                # Masa atomu
        self.pos = [x, y]                           # Wektor, który określa pozycję atomu
        self.angle = radians(angle)                 # Kąt względem układu współrzędnych pod którym porusza się atom
        self.speed = speed                          # Prędkość atomu
        self.crashes = 0                            # Liczba zderzeń danego atomu z innymi atomami
        self.color = color
        self.start = timer()
        self.end = timer()
        self.droga = 0                              # droga swobodna pomiędzy odbiciami
        self.suma = 0                               # suma dróg swobodnych pomiędzy odbiciami
        self.time = 0
        self.srednia_droga = 0
        self.last_hit = []                          # tablica atomów, z którymi doszło do zderzenia
        self.tick_count = 0

        # Add atom to list of atoms
        self.atoms.append(self)

        # Print generated position
        print(self.pos)

    def tick(self):

        # zabezpieczenie przed blokowaniem się atomów
        self.tick_count += 1
        if self.tick_count % 10 == 0:     # co ile ticków sprawdzamy, czy zderzenia się powtarzają (40 ticks = 1 sec)
            self.last_hit.clear()

        # Physics
        # Przewidzenie przyszłych współrzędnych atomu w układzie
        delta_x = int(self.speed * cos(self.angle))
        delta_y = int(self.speed * sin(self.angle))
        hit = False

        # Warunki opisujące zachowanie atomu, gdy zderzy się z jedną ze ścian pojemnika
        # Przy zderzeniu ze ścianą na osi X:
        if self.pos[0] + delta_x <= self.board_left + self.board_border + self.radius:
            self.angle = pi - self.angle
            self.pos[0] += int(self.speed * cos(self.angle))
            hit = True
            if self.color == 'r':
                self.red()

        elif self.pos[0] + delta_x >= self.board_left + self.board_width - self.board_border - self.radius:
            self.angle = pi - self.angle
            self.pos[0] += int(self.speed * cos(self.angle))
            hit = True
            if self.color == 'r':
                self.red()

        # Przy zderzeniu ze ścianą na osi Y:
        elif self.pos[1] + delta_y <= self.board_top + self.board_border + self.radius:
            self.angle = self.angle * (-1)
            self.pos[1] += int(self.speed * sin(self.angle))
            hit = True
            if self.color == 'r':
                self.red()

        elif self.pos[1] + delta_y >= self.board_top + self.board_height - self.board_border - self.radius:
            self.angle = self.angle * (-1)
            self.pos[1] += int(self.speed * sin(self.angle))
            hit = True
            if self.color == 'r':
                self.red()

        else:
            self.pos[0] += delta_x
            self.pos[1] += delta_y

        # print(f"{self}, Angle = {self.angle}, Speed = {self.speed}, DeltaX = {delta_x}, DeltaY = {delta_y}")
        for atom in self.atoms:
            if self.color == 'r':
                if self.time > 0:
                    self.srednia_droga = self.suma / self.time

                if 130 >= self.time >= 100:  # Średnia droga w danym przedziale czasowym
                    self.srednia_droga = self.suma / self.time
                    print("Średnia droga swobodna: {}".format(self.srednia_droga))


            if atom not in self.last_hit:   # Sprawdzenie, czy wystąpiło powtórzenie zderzenia
                if hit is False and atom is not self and self.distance(atom) <= (self.radius + atom.radius):
                    self.angle = self.angle - pi
                    hit = True
                    self.last_hit.append(atom)
                    atom.crashes += 1
                    if self.color == 'r':
                        self.red_atm()
                elif hit is True:
                    break

    # BLUE ATOM
    def draw(self):
        pygame.draw.circle(self.board.screen, (124, 149, 202), self.pos, self.radius)

    # RED ATOM
    def draw1(self):
        pygame.draw.circle(self.board.screen, (239, 35, 60), self.pos, self.radius)

    def red(self):                                          # Po zderzeniu ze ścianą droga atomu nie jest zerowana
        print("\nOdbicie od ściany czerwonego atomu!")
        self.end = timer()
        self.time += self.end
        delta_t = self.end - self.start
        print("Czas pomiędzy zderzeniami:", delta_t)
        print("Wektor prędkości", self.speed)
        self.start = self.end
        self.droga += self.speed * delta_t
        self.suma += self.droga
        print("Droga:", self.droga)

    def red_atm(self):                                # Po zderzeniu z innym atomem, droga atomu jest zerowana
        print("\nZderzenie czerwonego atomu!")
        self.end = timer()
        self.time += self.end
        delta_t = self.end - self.start
        print("Czas pomiędzy zderzeniami:", delta_t)
        print("Wektor prędkości", self.speed)
        self.start = self.end
        self.droga += self.speed * delta_t
        self.suma += self.droga
        print("Droga:", self.droga)
        self.droga = 0

    def distance(self, atom):
        DISTANCE = sqrt((atom.pos[0] - self.pos[0])**2 + (atom.pos[1] - self.pos[1])**2)
        return DISTANCE