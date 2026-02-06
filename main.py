import itertools
from collections import Counter

alive = "🥳"
dead = "😞"
width = 5
height = 5
board ={(2, 1), (2, 2), (2, 3)}
neighbors = list(itertools.product([0, 1, -1], repeat=2))[1:]
counter = Counter((x + dx, y + dy) for x, y in board for dx, dy in neighbors)

def row(y):
    return (alive if (x, y) in board else str(counter[(x,y)]) for x in range(width))

def draw(board):
    for y in range(height):
        print("".join(row(y)))

def update(board):
    # for each living cell count number of alive neighbors
    counter = Counter((x + dx, y + dy) for x, y in board for dx, dy in neighbors)
    # rules for survival b3/s23
    return {cell for cell, neighbors in counter.items()
            if neighbors == 3 or (neighbors == 2 and cell in board)}

def play(board, n=5):
    for i in range(n):
        draw(board)
        print("---")
        board = update(board)


# draw(board)
play(board)
