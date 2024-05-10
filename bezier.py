'''
fun bezier problems
-PaiShoFish49
'''

import pygame
from typing import Literal

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

class Node():
    def __init__(self, x, y, nodeType: Literal['onPath', 'offPath']) -> None:
        self.vector = pygame.Vector2(x, y)
        self.nodeType = nodeType

class Shape():
    def __init__(self, nodes: list[Node], closed: bool = True) -> None:
        self.nodes = nodes
        self.closed = closed
        self.points = []

    def addNewNode(self, node):
        self.nodes.append(node)

    def getPaths(self):
        if len(self.nodes) > 1 and len([i for i in self.nodes if i.nodeType == 'onPath']) > 0:
            # get all paths
            paths = []
            pathPoints = []
            firstOnPathPoint = -1
            for i, node, in enumerate(self.nodes):
                pathPoints.append(node.vector)
                if node.nodeType == 'onPath':
                    if firstOnPathPoint == -1:
                        firstOnPathPoint = i
                    else:
                        paths.append(pathPoints)
                    pathPoints = [node.vector]

            for i in range(firstOnPathPoint + 1):
                pathPoints.append(self.nodes[i].vector)
            paths.append(pathPoints)

            self.paths = paths

    def getLines(self):
        self.points = []
        for i, path in enumerate(self.paths):
            for t in range(20):
                lerpList = path.copy()
                for j in range(len(path) - 1):
                    lerpList = [pygame.Vector2.lerp(lerpList[k], lerpList[k + 1], 1/19*t) for k in range(len(lerpList) - 1)]
                self.points.append(lerpList[0])

nodePoints = [
    [screen.get_width()/2, screen.get_height()/3, 'onPath'],
    [screen.get_width()/4, screen.get_height()/3, 'offPath'],
    [screen.get_width()/4, screen.get_height()/3*2, 'offPath'],
    [screen.get_width()/2, screen.get_height()/3*2, 'onPath'],
    [screen.get_width()/4*3, screen.get_height()/2, 'onPath'],
]

shape1 = Shape([Node(*i) for i in nodePoints])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    shape1.getPaths()
    shape1.getLines()
    for i in shape1.points:
        pygame.draw.circle(screen, 'blue', i, 3)
    for i in shape1.nodes:
        pygame.draw.circle(screen, 'black', i.vector, 8)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()