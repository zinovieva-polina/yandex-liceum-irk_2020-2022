import pygame, sys
import random 


def main():
    coord = []
    pygame.init()
    width, height = random.randint(150, 800), random.randint(150, 800)
    size = 25
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                coord.append((list(event.pos), [-1, 1]))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return  

        screen.fill((0, 0, 200))
        
        for num, (pos, vec) in enumerate(coord):
            pos[0] += vec[0]
            pos[1] += vec[1]
            for i in range(2):
                if pos[i] > (width, height)[i] or pos[i] < 0:
                    vec[i] = -vec[i]
            rect = (pos[0] - size // 2, pos[1] - size // 2, size,  size)
            pygame.draw.ellipse(screen, (200, 200, 0), rect) 
            coord[num] = pos, vec

        pygame.display.update()

        dt = clock.tick(60)

if __name__ == '__main__':
    main()
