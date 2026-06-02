import random

n = int(input(": "))

state = []

def randomGeneration(n):
    for i in range(n):
        state.append(random.randint(1, n))

randomGeneration(n)

def fitness(board):
    attacks = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):

            # Same row
            if board[i] == board[j]:
                attacks += 1

            # Same diagonal
            elif abs(board[i] - board[j]) == abs(i - j):
                attacks += 1

    return attacks

def getNeighbours(board):
    neighbours = []

    for i in range(n):
        temp = board.copy()

        temp[i] = (temp[i] + 1) % 8

        neighbours.append(temp)

    return neighbours

def hillClimb():
    optimum = False

    global state

    while (not optimum):
        optimum = True
        fit = fitness(state)

        neighbours = getNeighbours(state)

        for i in neighbours:
            if fit > fitness(i):
                state = i
                optimum = False

hillClimb()

def stateToGrid(state):
    n = len(state)

    grid = []

    for row in range(n):
        grid.append([0] * n)

    for col in range(n):
        row = state[col] - 1      # convert 1-based row to 0-based
        grid[row][col] = 1

    return grid

board = stateToGrid(state)

print(state)

for row in board:
    print(row)