import pygame
pygame.init()

detalisation = 5
scale = 0.25
xpos = 0
ypos = 0
size = 600

win = pygame.display.set_mode((size, size))
pygame.display.set_caption("Mandelbrot set")


def MandelbrotDraw(detalisation=detalisation, scale=scale, xpos=xpos, ypos=ypos):
    for x in range(size):
        for y in range(size):
            i = (x - size // 1.5 + xpos) / (size // (1/scale))
            j = (y - size // 2 + ypos) / (size // (1/scale))
            c = (i + j * (-1)**.5)

            In_Mandelbrot = True
            z = 0
            for i in range(round(detalisation)):
                z = z**2 + c
                if abs(z) >= 2:
                    In_Mandelbrot = False
                    break
            if In_Mandelbrot:
                pygame.draw.line(win, (255, 255, 255), (x, y), (x+1, y+1), 1)


RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xpos -= 30
            elif event.key == pygame.K_RIGHT:
                xpos += 30
            elif event.key == pygame.K_UP:
                ypos -= 30
            elif event.key == pygame.K_DOWN:
                ypos += 30
            elif event.key == pygame.K_m:
                scale /= 2
            elif event.key == pygame.K_p:
                scale *= 2
            elif event.key == pygame.K_h:
                detalisation += 2
            elif event.key == pygame.K_l:
                if detalisation >= 2:
                    detalisation -= 2

    win.fill((0, 0, 0))
    MandelbrotDraw(detalisation, scale, xpos, ypos)
    pygame.display.flip()
    pygame.time.delay(33)

pygame.quit()