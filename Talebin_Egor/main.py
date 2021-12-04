import pygame

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

screen2 = pygame.Surface(screen.get_size())
x1, y1 = 10, 10
drawing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            screen2.blit(screen, (0, 0))
            drawing = False
        if event.type == pygame.MOUSEMOTION:
            w, h = event.pos[0] - x1, event.pos[1] - y1
            u, i = event.pos[0] - x1, event.pos[1] - y1
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing:
        pygame.draw.rect(screen, (0, 255, 0), ((x1, y1), (w, h)), 5)

while running:
    for event in pygame.event.get():
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            x1 += 1
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            x1 -= 1
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            screen2.blit(screen, (0, 0))
            drawing = False
        if event.type == pygame.MOUSEMOTION:
            u, i = event.pos[0] - x1, event.pos[1] - y1
            screen.fill(pygame.Color('black'))
            screen.blit(screen2, (0, 0))
            if drawing:
                pygame.draw.rect(screen, (255, 255, 255), ((x1, y1), (u, i)), 5)

    pygame.display.flip()
pygame.quit()
