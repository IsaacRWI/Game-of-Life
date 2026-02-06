alive = "🥳"
dead = "😞"
width = 5
height = 5
board ={(2, 1), (2, 2), (2, 3)}

def row(y):
    return (alive if (x, y) in board else dead for x in range(width))

def draw(board):
    for y in range(height):
        print("".join(row(y)))



draw(board)