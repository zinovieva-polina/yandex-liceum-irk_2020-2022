import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    y_pos = 0
    v = 100  # пикселей в секунду
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((50, 205, 50))
        pygame.draw.rect(screen, (255, 255, 255), (300, 0, 200, 1000))
        pygame.draw.circle(screen, (255, 0, 0), (400, y_pos), 30)
        y_pos += v * clock.tick() / 1000  # v * t в секундах
        pygame.display.flip()
    pygame.quit()