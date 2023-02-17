import pygame
import numpy as np
import time

# It initializes the pygame module.
pygame.init()

# Defining the width and height of the screen.
width = 600
height = 600

# It creates a window with the given dimensions.
screem = pygame.display.set_mode((height, width))

# Setting the background color to a dark gray.
bg = 25, 25, 25
screem.fill(bg)

# Defining the number of cells in the X and Y axis.
ncX, ncY = 50, 50

# Defining the width and height of each cell.
dimCW = width / ncX
dimCH = height / ncY

# Creating a matrix of zeros with the dimensions of the number of cells in the X and Y axis.
gameState = np.zeros((ncX, ncY))

# Setting the initial state of the game.
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

# Setting the variable `pauseExect` to `False`.
pauseExect = False

# Creating a new game state and filling the screen with the background color. It is also sleeping for
# 0.1 seconds and getting the events.
while True:

    newGameState = np.copy(gameState)

    screem.fill (bg)

    time.sleep(0.1)

    ev = pygame.event.get()

    # Getting the events and checking if the event is a keydown. If it is, it is changing the value of
    # the variable `pauseExect` to the opposite of what it was. If it is not, it is getting the mouse
    # clicks and checking if the sum of the mouse clicks is greater than 0. If it is, it is getting
    # the position of the mouse and setting the value of the cell to 1.
    for event in ev:

        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1

    # Creating a new game state and filling the screen with the background color. It is also sleeping
    # for
    # # 0.1 seconds and getting the events.
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

    # Copying the new game state to the game state.
    gameState = np.copy(newGameState)

    # Updating the full display Surface to the screen.
    pygame.display.flip()