import pygame
import numpy as np
import time

pygame.init()

width = 600
height = 600

screem = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screem.fill(bg)

ncX, ncY = 50, 50

dimCW = width / ncX
dimCH = height / ncY

gameState = np.zeros((ncX, ncY))

gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

pauseExect = False

while True:

    newGameState = np.copy(gameState)

    screem.fill (bg)

    time.sleep(0.1)

    ev = pygame.event.get()

    for event in ev:

        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1

    for y in range(0, ncX):
        for x in range(0, ncY):

            if  not pauseExect:

                n_neigh = gameState[(x-1) % ncX, (y-1) % ncY] + \
                          gameState[(x)   % ncX, (y-1) % ncY] + \
                          gameState[(x+1) % ncX, (y-1) % ncY] + \
                          gameState[(x-1) % ncX, (y)   % ncY] + \
                          gameState[(x+1) % ncX, (y)   % ncY] + \
                          gameState[(x-1) % ncX, (y+1) % ncY] + \
                          gameState[(x)   % ncX, (y+1) % ncY] + \
                          gameState[(x+1) % ncX, (y+1) % ncY]

                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            poly = [((x) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screem, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screem, (255, 255, 255), poly, 0)

    gameState = np.copy(newGameState)

    pygame.display.flip()