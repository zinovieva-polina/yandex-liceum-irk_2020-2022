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
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                w = pygame.Color("white")
                x_left = self.left + x * self.cell_size
                y_top = self.top + y * self.cell_size
                pygame.draw.rect(screen, w, (x_left, y_top, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        if 0 < x < self.cell_size * self.width and 0 < y < self.cell_size * self.height:
            cell_x = x // self.cell_size
            cell_y = y // self.cell_size
            return cell_x, cell_y

    def on_click(self, cell):
        print(cell)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    # поле 5 на 7
    DW, DH = 400, 400
    screen = pygame.display.set_mode((DW, DH))
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()