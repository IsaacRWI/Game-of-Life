import itertools
from collections import Counter

alive = "🥳"
dead = "😞"
width = 5
height = 5
board ={(2, 1), (2, 2), (2, 3)}
neighbors = list(itertools.product([0, 1, -1], repeat=2))[1:]
count = Counter((x + dx, y + dy) for x, y in board for dx, dy in neighbors)

def row(y):
    return (alive if (x, y) in board else str(count[(x,y)]) for x in range(width))

def draw(board):
    for y in range(height):
        print("".join(row(y)))



draw(board)
