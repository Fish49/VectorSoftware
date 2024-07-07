import pygame
from pygame import Vector2
from shapeHelpers import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

defaultCube = Drawing([Curve([Path(Node((100, 100)), Node((100, 100)), [])])])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                defaultCube.curves[0].paths[-1].addHandle(Handle(pygame.mouse.get_pos()))

            elif event.key == pygame.K_n:
                defaultCube.curves[0].paths.append(Path(Node((pygame.mouse.get_pos())), Node((pygame.mouse.get_pos())), []))

        elif event.type == pygame.MOUSEMOTION:
            defaultCube.curves[0].paths[-1].nodeEnd.vector.update(pygame.mouse.get_pos())

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    #actualCodeStart
    for curve in defaultCube.curves:
        for path in curve.paths:
            pygame.draw.lines(screen, defaultCube.strokeColorRGBA, False, path.getPoints(9*len(path.handles), True))

            pygame.draw.lines(screen, defaultCube.strokeColorRGBA, False, path.getNodeAndHandlePoints())
            for point in path.getNodeAndHandlePoints():
                pygame.draw.circle(screen, defaultCube.strokeColorRGBA, point, 3)
    #actualCodeEnd

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()