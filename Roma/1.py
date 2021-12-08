import pygame
from random import randint


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[2] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.turn = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        colors = (pygame.Color(255, 0, 0), pygame.Color(0, 0, 255), pygame.Color(0, 0, 0))
        for y in range(self.height):
            for x in range(self.width):
                if not self.board[y][x]:
                    pygame.draw.ellipse(
                        screen,
                        colors[self.board[y][x]],
                        (x * self.cell_size + self.left + 2, y * self.cell_size + self.top + 2,
                         self.cell_size - 2, self.cell_size - 2),
                        2
                    )
                else:
                    pygame.draw.line(
                        screen,
                        colors[self.board[y][x]],
                        (x * self.cell_size + self.left + 2, y * self.cell_size + self.top + 2),
                        ((x + 1) * self.cell_size + self.left - 2, (y + 1) * self.cell_size + self.top - 2),
                        3
                    )
                    pygame.draw.line(
                        screen,
                        colors[self.board[y][x]],
                        ((x + 1) * self.cell_size + self.left - 2, y * self.cell_size + self.top + 2),
                        (x * self.cell_size + self.left + 2, (y + 1) * self.cell_size + self.top - 2),
                        3
                    )
                pygame.draw.rect(
                    screen,
                    pygame.Color(255, 255, 255),
                    (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size),
                    1
                )

    def get_click(self, mouse_pos):
        pos = self.get_cell(mouse_pos)
        self.on_click(pos)

    def on_click(self, cell_coords):
        if cell_coords:
            x, y = cell_coords
            if self.board[y][x] == 2:
                self.board[y][x] = self.turn
                self.turn = not self.turn

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y


# поле 5 на 7
board = Board(5, 7)
board.set_view(100, 100, 50)
running = True
while running:
    screen = pygame.display.set_mode((500, 500))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(pygame.mouse.get_pos())
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()