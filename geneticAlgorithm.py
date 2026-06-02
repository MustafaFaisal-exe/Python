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

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2

def mutation(population):
    mutation_Rate = 0.1

    total_genes = len(population) * n

    no_of_mutate = mutation_Rate * total_genes

    for i in range(no_of_mutate):
        gene = random.randint(1, total_genes)

        population[gene // len(population)][gene % len(population)] += 1

    return population

def selection(population, fit):

    n = len(population)

    # Step 1: sort indices based on fitness (ascending because lower is better)
    sorted_idx = sorted(range(n), key=lambda i: fit[i])

    # Step 2: assign ranks (best = n, worst = 1)
    ranks = [0] * n

    for rank, idx in enumerate(sorted_idx):
        ranks[idx] = rank + 1   # 1..n

    # Step 3: compute selection probabilities based on rank
    total_rank = sum(ranks)
    probs = [r / total_rank for r in ranks]

    # Step 4: roulette wheel selection
    r = random.random()
    cumulative = 0

    for i in range(n):
        cumulative += probs[i]
        if r <= cumulative:
            return population[i]

def geneticAlgo():
    global state

    population = []

    for i in range(4):
        population.append(randomGeneration(n))

    isBetter = True

    while (not isBetter):
        fit = []

        for i in range(4):
            fit.append(fitness(population[i]))

        count = []





def stateToGrid(state):
    n = len(state)

    grid = []

    for row in range(n):
        grid.append([0] * n)

    for col in range(n):
        row = state[col] - 1
        grid[row][col] = 1

    return grid

board = stateToGrid(state)

print(state)

for row in board:
    print(row)