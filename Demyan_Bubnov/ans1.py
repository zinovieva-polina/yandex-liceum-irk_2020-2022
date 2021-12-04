import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Слава Украине')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 10  # пикселей в секунду
    fps = 60
    clock = pygame.time.Clock()
    blue = pygame.Color("blue")
    yellow = pygame.Color("yellow")
    size = 0
    drawing = False
    x1, y1 = 0, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                size = 0
                drawing = True
                x1, y1 = event.pos

        screen.fill(blue)
        if drawing:
            size += 10 / 60
            pygame.draw.circle(screen, yellow, (x1, y1), size)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()