from random import randint as rand


def rendwave(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand (0, 3)
    dx, dy = moves[t][0], moves [t][1]
    return (x + dx, y + dy)