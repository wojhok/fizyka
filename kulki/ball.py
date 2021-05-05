import pygame
from math import pi, atan, sqrt, sin, cos, radians
from copy import deepcopy
from random import randint


class Ball:
    atoms = []

    def __init__(self, board, board_left, board_top, x, y, angle, speed):

        # Init board
        self.board = board
        self.board_border = 7
        self.board_width = self.board_height = self.board.size * 9  # szerokość i długość planszy (self.board.width to szerokość całego okna)
        self.board_left = board_left  # przesunięcie planszy względem lewej krawędzi okna
        self.board_top = board_top  # przesunięcie planszy względem górnej krawędzi okna

        # Variables
        self.radius = 9  # Promień atomu
        self.mas = 1  # Masa atomu
        self.pos = [x, y]  # Wektor, który określa pozycję atomu
        self.crashes = 0  # Liczba zderzeń danego atomu z innymi atomami
        self.angle = radians(angle)
        self.speed = speed
        self.tick_count = 0
        self.last_hit = []

        # Add atom to list of atoms
        self.atoms.append(self)

        # Define color of ball
        self.r = randint(0, 255)
        self.g = randint(0, 255)
        self.b = randint(0, 255)

    def tick(self):

        # zabezpieczenie przed blokowaniem się atomów
        self.tick_count += 1
        if self.tick_count % 10 == 0:  # co ile ticków sprawdzamy, czy zderzenia się powtarzają (40 ticks = 1 second)
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
        elif self.pos[0] + delta_x >= self.board_left + self.board_width - self.board_border - self.radius:
            self.angle = pi - self.angle
            self.pos[0] += int(self.speed * cos(self.angle))
            hit = True

        # Przy zderzeniu ze ścianą na osi Y:

        elif self.pos[1] + delta_y <= self.board_top + self.board_border + self.radius:
            self.angle = self.angle * (-1)
            self.pos[1] += int(self.speed * sin(self.angle))
            hit = True
        elif self.pos[1] + delta_y >= self.board_top + self.board_height - self.board_border - self.radius:
            self.angle = self.angle * (-1)
            self.pos[1] += int(self.speed * sin(self.angle))
            hit = True
        else:
            self.pos[0] += delta_x
            self.pos[1] += delta_y

        # print(f"{self}, Angle = {self.angle}, Speed = {self.speed}, DeltaX = {delta_x}, DeltaY = {delta_y}")
        for atom in self.atoms:
            if atom not in self.last_hit: # Zabezpieczenie przed blokowaniem
                if hit is False and atom is not self and self.distance(atom) <= (self.radius + atom.radius):
                    print("\nId:\nPrzed zderzeniem:", self.angle)
                    self.angle = self.angle - pi
                    print("Po zderzeniu:", self.angle)
                    hit = True
                    self.last_hit.append(atom)
                    self.crashes += 1
                elif hit is True:
                    break

    def draw(self):
        pygame.draw.circle(self.board.screen, (self.r, self.g, self.b), self.pos, self.radius)

    def distance(self, atom):
        DISTANCE = sqrt((atom.pos[0] - self.pos[0]) ** 2 + (atom.pos[1] - self.pos[1]) ** 2)
        return DISTANCE