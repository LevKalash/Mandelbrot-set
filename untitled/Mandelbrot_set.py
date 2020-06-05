"""
Program for drawing Mondelbrot set on Python with using Pygame library
Function keys:
←, ↑, →, ↓ - Moving of camera relative to the image
h, l - Increasind and decreasing Image detalisation
p, m - "Moving" closer and further "camera" relative to the image
q - quit

-----------------------------------------------------------------

Программа для отрисовки множества Мандельброта на языке Python;
Используется библиотека Pygame.
Функциональные клавиши:
←, ↑, →, ↓ - Движение "камеры" относительно рисунка в нужном направлении
h, l - Повышение и понижение детализации изображения
p, m - "Приближение" и "Отдаление" "Камеры" от изображения
q - выход
"""

import pygame  #Import of library, which we will draw it with / Импорт библиотеи, с помощью которой отрисовываем
pygame.init()  # initialization of pygame / Инициализируем пайгейм

detalisation = 1000  # Value will change detalisation of figure (1 will make circle, 40 is good quality)
scale = 0.25  # Size of drawn figure / Размер отрисовываемой фигуры
xpos = 0  # figure position on X axis / Позиция  фигуры по оси абсцисс
ypos = 0  # figure position on Y axis / Позиция фигуры по оси оординат
size = 1000  # Window size / Размер окна

win = pygame.display.set_mode((size, size), pygame.FULLSCREEN)  # making window of nedded size / Создаём окно нужного размера
pygame.display.set_caption("Mandelbrot set")  # window title / заголовок в шапке окна


def MandelbrotDraw(detalisation=detalisation, scale=scale, xpos=xpos, ypos=ypos):  # function draws Mandelbrot set / Функция отрисует множество Мондельброта
    win.fill((0, 0, 0))
    for x in range(size):
        for y in range(size):  # checking every dot on coordinat plane / проверяем все точки на координатной плоскости
            i = (x - size // 1.5 + xpos) / (size // (1/scale))
            j = (y - size // 2 + ypos) / (size // (1/scale))  # setting center of picture / устанавливаем центр картинки
            c = (i + j * (-1)**.5)  # Complex number c from formula  of Mondelbrot set (z[n+1] = z[n]^2 + c) / Число из формулы множества мондельброта

            In_Mandelbrot = True
            z = 0  # condition of Formula working / Условия для  работы формулы
            for i in range(detalisation):
                z = z**2 + c  # Calculating for every dot on every iteration / на каждой итерации рассчитываем точку по формуле
                if abs(z) >= 2:  # Check for going beyond the set / Проверка на выход за пределы множества
                    In_Mandelbrot = False
                    break  #  If dot not in set going to the next / Если точка вне множества, переходим к следующей
            on_screen = (0 < (xpos + x) < size) and (0 < (ypos + y) < size)  # Condition of new dot is on screen
            if In_Mandelbrot and on_screen:
                pygame.draw.rect(win, (255, 255, 255), (x, y, 1, 1))  # Draw dot of set / Рисуем одну точку множества
                pygame.display.flip()
    pygame.display.flip()  # Updating screen / Обновляем экран


MandelbrotDraw()  # Drawing set first time / Рисуем множество первый раз
RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False  # Pygame library standart loop / Стандартный цикл библиотеки pygame
        elif event.type == pygame.KEYDOWN:  # Check for button press / Проверка нажатия клавиш
            if event.key == pygame.K_q:
                RUN = False
            elif event.key == pygame.K_LEFT:
                xpos -= 30  # From here / Отсюда
                MandelbrotDraw(detalisation, scale, xpos, ypos)
            elif event.key == pygame.K_RIGHT:
                xpos += 30
                MandelbrotDraw(detalisation, scale, xpos, ypos)
            elif event.key == pygame.K_UP:
                ypos -= 30
                MandelbrotDraw(detalisation, scale, xpos, ypos)
            elif event.key == pygame.K_DOWN:
                ypos += 30  # To here moving "Camera" in needed direction / До сюда движение камеры в нужном направлении
                MandelbrotDraw(detalisation, scale, xpos, ypos)
            elif event.key == pygame.K_m:
                scale /= 2  # Moving "away" from picture / Движемся "от" изображения
                MandelbrotDraw(detalisation, scale, xpos, ypos)
            elif event.key == pygame.K_p:
                scale *= 2  # Moving "to" picture / Движемся "к" изображению
                MandelbrotDraw(detalisation, scale, xpos, ypos)
            elif event.key == pygame.K_h:
                detalisation += 2  # Increace detalisation / Увеличиваем детализацию
                MandelbrotDraw(detalisation, scale, xpos, ypos)
            elif event.key == pygame.K_l:
                if detalisation >= 2:  # If detalisation won't become less than zero... / Если детализация не станет меньше нуля...
                    detalisation -= 2  # Decreace detalisation / Уменьшаем детализацию
                    MandelbrotDraw(detalisation, scale, xpos, ypos)

pygame.quit()  # Finish of program's working / Окончание работы программы