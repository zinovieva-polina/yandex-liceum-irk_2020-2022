import pygame as pg

pg.init()
DW, DH = 500, 500

screen = pg.display.set_mode((500, 500))
fps = 60
clock = pg.time.Clock()
speed = 5
bals = []
yellow = pg.Color("yellow")
white = pg.Color("white")

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
        if e.type == pg.MOUSEBUTTONDOWN:
            x, y = e.pos
            bals.append([x, y, -1, -1])
    screen.fill((0, 0, 0))


    for i in range(len(bals)):
        if bals[i][0] + speed * bals[i][2] > DW:
            bals[i][2] *= -1
        if bals[i][0] + speed * bals[i][2] < 0:
            bals[i][2] *= -1
        if bals[i][1] + speed * bals[i][3] > DH:
            bals[i][3] *= -1
        if bals[i][1] + speed * bals[i][3] < 0:
            bals[i][3] *= -1
        bals[i][0] = bals[i][0] + speed * bals[i][2]
        bals[i][1] = bals[i][1] + speed * bals[i][3]
        pg.draw.circle(screen, white, (bals[i][0], bals[i][1]), 10)
    clock.tick(fps)
    pg.display.flip()