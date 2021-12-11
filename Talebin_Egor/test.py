import pygame

if __name__ == '__main__':
    global pos
    pygame.init()

width, height = list(map(int, "800 800".split()))
size = width, height
screen = pygame.display.set_mode(size)

running = True
st1 = float(0)
st2 = 1
x = 0
y = 0
z = 0
n = 0
clock = pygame.time.Clock()

while running:
    if x >= 255:
        x = 0
        y = 0
        z = 0
    screen.fill((150, 150, 150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            st1 = 0
            st2 = 0
    while st2 != 1:
        if x != 255 and y == 0 and z == 0:
            pygame.draw.circle(screen, (x, y, z), pos, st1)
            pygame.display.flip()
            st1 += 5
            x += 5
            n = 0

        if x == 255 and y != 255 and z == 0:
            pygame.draw.circle(screen, (x, y, z), pos, st1)
            pygame.display.flip()
            st1 -= 5
            y += 5
            n = 0

        if x == 255 and y == 255 and z != 255:
            pygame.draw.circle(screen, (x, y, z), pos, st1)
            pygame.display.flip()
            st1 += 5
            z += 5
            n += 1

        if x != 0 and y != 0 and z != 0 and n >= 51:
            pygame.draw.circle(screen, (x, y, z), pos, st1)
            pygame.display.flip()
            x -= 5
            y -= 5
            z -= 5
            st1 -= 5

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                st2 = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((150, 150, 150))
                pygame.display.flip()
                pos = event.pos
                st1 = 0
    pygame.display.flip()
pygame.quit()