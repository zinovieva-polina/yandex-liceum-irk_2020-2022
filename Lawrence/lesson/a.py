import pygame, sys
import random 


def main():
    size = 0
    coord = () 
    pygame.init()
    screen = pygame.display.set_mode((random.randint(150, 800),
                                       random.randint(150, 800)))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                coord = event.pos
                size = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return  
        size += 5

        screen.fill((0, 0, 200))
        
        if coord:
            rect = (coord[0] - size // 2, coord[1] - size // 2, size,  size)
            pygame.draw.ellipse(screen, (200, 200, 0), rect) 

        pygame.display.update()

        dt = clock.tick(60)

if __name__ == '__main__':
    main()
