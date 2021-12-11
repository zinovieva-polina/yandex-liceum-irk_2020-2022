import pygame
import sys

width, height = list(map(int, "250 250".split()))
size = width, height
pygame.init()
size_block = 50
screen = pygame.display.set_mode(size)

margin = 15
blue = (255, 0, 255)
white = (0, 255, 255)
red = (255, 255, 0)
pygame.display.set_caption('Tic tac toe')
mas = [[0] * 5 for i in range(3)]
query = 0



def check_win(mas):
    # x
    if mas[0][0] == 'x' and mas[0][1] == 'x' and mas[0][2] == 'x':
        print('Крестики выиграли')
    if mas[1][0] == 'x' and mas[1][1] == 'x' and mas[1][2] == 'x':
        print('Крестики выиграли')
    if mas[2][0] == 'x' and mas[2][1] == 'x' and mas[2][2] == 'x':
        print('Крестики выиграли')
    #
    if mas[0][0] == 'x' and mas[1][0] == 'x' and mas[2][0] == 'x':
        print('Крестики выиграли')
    if mas[0][1] == 'x' and mas[1][1] == 'x' and mas[2][1] == 'x':
        print('Крестики выиграли')
    if mas[0][2] == 'x' and mas[1][2] == 'x' and mas[2][2] == 'x':
        print('Крестики выиграли')
    #
    if mas[0][0] == 'x' and mas[1][1] == 'x' and mas[2][2] == 'x':
        print('Крестики выиграли')
    if mas[0][2] == 'x' and mas[1][1] == 'x' and mas[2][0] == 'x':
        print('Крестики выиграли')
    # o
    if mas[0][0] == 'o' and mas[0][1] == 'o' and mas[0][2] == 'o':
        print('Нолики выиграли')
    if mas[1][0] == 'o' and mas[1][1] == 'o' and mas[1][2] == 'o':
        print('Нолики выиграли')
    if mas[2][0] == 'o' and mas[2][1] == 'o' and mas[2][2] == 'o':
        print('Нолики выиграли')
    #
    if mas[0][0] == 'o' and mas[1][0] == 'o' and mas[2][0] == 'o':
        print('Нолики выиграли')
    if mas[0][1] == 'o' and mas[1][1] == 'o' and mas[2][1] == 'o':
        print('Нолики выиграли')
    if mas[0][2] == 'o' and mas[1][2] == 'o' and mas[2][2] == 'o':
        print('Нолики выиграли')
    #
    if mas[0][0] == 'o' and mas[1][1] == 'o' and mas[2][2] == 'o':
        print('Нолики выиграли')
    if mas[0][2] == 'o' and mas[1][1] == 'o' and mas[2][0] == 'o':
        print('Нолики выиграли')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
            query += 1
    for row in range(3):
        for col in range(3):
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen, blue, (x, y, size_block, size_block))
            if mas[row][col] == 'x':
                pygame.draw.line(screen, red, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 8)
                pygame.draw.line(screen, red, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 8)
            elif mas[row][col] == 'o':
                pygame.draw.circle(screen, red, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 8)
            #
            check_win(mas)
            if query == 9:
                print('ничЬя')
    pygame.display.update()