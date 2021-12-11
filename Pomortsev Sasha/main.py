import pygame


try:
    # a = input('введите через пробел 2 числа\n').split()
    a = '1100 5'.split()
    SIZE = [WIDTH, HEIGHT] = [int(a[0]), int(a[0]) - 300]
    size_of_rect = int(a[1])
    BACKGROUND = (0, 0, 0)
except Exception:
    print('Неправильный формат ввода')
    exit()


def krest(screen, x, y, c='orange'):
    x += 10
    y += 10
    pyame.draw.circle(screen, c, (x, y), 50, 5, draw_bottom_right=True)
    pygame.draw.line(screen, c, [x + 45, y], [x + 87, y], 5)
    pygame.draw.circle(screen, c, (x + 135, y), 50, 5, draw_bottom_left=True)
    pygame.draw.line(screen, c, [x + 135, y + 45], [x + 135, y + 94], 5)
    pygame.draw.circle(screen, c, (x + 135, y + 140), 50, 5, draw_top_left=True)
    pygame.draw.line(screen, c, [x + 45, y + 138], [x + 87, y + 138], 5)
    pygame.draw.circle(screen, c, (x, y + 140), 50, 5, draw_top_right=True)
    pygame.draw.line(screen, c, [x, y + 45], [x, y + 94], 5)


def player(screen, x, y, c):
    x += 75
    y += 60
    pygame.draw.polygon(screen, c, ([x, y], [x + 20, y], [x + 20, y + 20],
                        [x + 10, y + 20], [x + 20, y + 40], [x, y + 40], [x + 10, y + 20],
                                    [x, y + 20], [x, y]), 0)


def draw(screen):
    screen.fill(BACKGROUND)
    lol = (HEIGHT // size_of_rect)

    for i in range(size_of_rect):
        for j in range(size_of_rect):
            x = (w := WIDTH - 300) - (w - lol * i)
            y = (h := WIDTH - 300) - lol * j - lol
            if (i == 4 and j == 0) or (i == 0 and j == 2) or (i == 2 and j == 4):
                c = 'blue'
            elif i == 2 and j == 2:
                continue
            elif i == 4 and j == 3:
                c = 'yellow'
            else:
                c = 'white'
            print(c, (x, y), lol, (w, h), (i, j))
            pygame.draw.rect(screen, c, (x + 5, y + 5, lol - 10, lol - 10), 5)
            if (i % 4 != 0 or j % 4 != 0) and (i + j) % 2 == 0:
                krest(screen, x, y)
            elif i == 0 and j == 0:
                player(screen, x, y, 'green')
            elif i == 4 and j == 0:
                player(screen, x, y, 'white')
    krest(screen, 850, 630)
    pygame.draw.rect(screen, 'blue', (850, 200, 150, 200), 5, border_radius=15)
    pygame.draw.rect(screen, 'red', (850, 420, 150, 200), 5, border_radius=15)
    pygame.draw.line(screen, 'white', (820, 0), (820, 800), 20)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Шахматная доска')
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

