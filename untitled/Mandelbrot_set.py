import pygame
pygame.init()

size = 600
win = pygame.display.set_mode((size, size))
detalisation = 20
scale = 0.25
xpos = 0
ypos = 0
default_color = (255, 255, 255)

pygame.display.set_caption("Mandelbrot set")

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
        default_color = (255, 255, 255)
        if In_Mandelbrot:
            pygame.draw.line(win, default_color, (x, y), (x+1, y+1), 1)

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    pygame.display.update()
    pygame.time.delay(33)

pygame.quit()