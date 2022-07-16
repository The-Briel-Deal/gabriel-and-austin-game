import sys, pygame

pygame.init()

size = width, height = 320, 240
speed = [0, 0]
black = 255, 255, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == 771:
            print("Key was pressed!")
            if event.text == "s":
                speed[1] = 1

            if event.text == "w":
                speed[1] = -1

            if event.text == "a":
                speed[0] = -1

            if event.text == "d":
                speed[0] = 1

        if event.type == 769:
            if event.unicode == "s":
                speed[1] = 0
            if event.unicode == "w":
                speed[1] = 0
            if event.unicode == "a":
                speed[0] = 0
            if event.unicode == "d":
                speed[0] = 0

        print(event.type, event)
        if event.type == pygame.QUIT:
            sys.exit()


    ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
