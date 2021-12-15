import copy
import datetime

import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 20

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        colors = (pygame.Color(0, 0, 0), pygame.Color(0, 255, 0))
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(
                    screen,
                    colors[self.board[y][x]],
                    (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size)
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
            self.board[y][x] = not self.board[y][x]

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.running = False
        self.speed = 1.0
        self.lasttime = datetime.datetime.now()
        self.prev_board = []
        self.prev_prev_board = []

    def get_near_cells(self, x, y, board):
        ret = []
        for yy in range(self.height):
            for xx in range(self.width):
                if xx in range(x - 1, x + 2) and yy in range(y - 1, y + 2) \
                        and (xx, yy) != (x, y):
                    ret.append(board[yy][xx])
        return ret

    def update(self):
        if self.running:
            if (datetime.datetime.now() - self.lasttime).seconds >= self.speed:
                self.lasttime = datetime.datetime.now()
                self.next_move()

    def next_move(self):
        self.prev_prev_board = copy.deepcopy(self.prev_board)
        self.prev_board = copy.deepcopy(self.board)
        for yy in range(self.height):
            for xx in range(self.width):
                cells = self.get_near_cells(xx, yy, self.prev_board)
                if self.board[yy][xx] == 0:
                    if len([i for i in cells if i]) == 3:
                        self.board[yy][xx] = 1
                elif self.board[yy][xx] == 1:
                    if len([i for i in cells if i]) < 2 \
                            or len([i for i in cells if i]) > 3:
                        self.board[yy][xx] = 0
        if self.prev_board == self.board or self.prev_prev_board == self.board:
            print("STOP")
            self.running = False


pygame.init()
game = Life(23, 23)
running = True
while running:
    screen = pygame.display.set_mode((500, 500))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game.running:
            game.get_click(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            game.speed -= 0.05
            print(game.speed)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            game.speed += 0.05
            print(game.speed)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            game.running = not game.running
    screen.fill((0, 0, 0))
    game.update()
    game.render(screen)
    pygame.display.flip()