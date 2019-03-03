import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([155, 144, 194])
ball = pygame.image.load("beach_ball.png")
background = pygame.image.load("set640.jpg")
x = 50
y = 50
x_speed = 5
y_speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(10)
    #pygame.draw.rect(screen, [155, 144, 194], [x, y, 90, 90], 0)
    screen.blit(background, [0, 0])
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 90 or x < 0:
        x_speed = -x_speed
    if y > screen.get_height() - 90 or y < 0:
        y_speed = -y_speed
    screen.blit(ball, [x, y])
    pygame.display.flip()
pygame.quit()
