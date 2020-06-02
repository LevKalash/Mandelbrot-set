import pygame
pygame.init()

size = 700
win = pygame.display.set_mode((size, size))
detalisation = 40
scale = 1

pygame.display.set_caption("Mandelbrot set")

for x in range(size):
    for y in range(size):
        i, j = (x - size // 2) / (size // 4), (y - size // 2) / (size //4)
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

    pygame.display.update()
    pygame.time.delay(33)

pygame.quit()