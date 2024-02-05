from puzzle.util import get_tile_pos


def h_missplace(start, goal):
    # Calculates the difference between the given puzzles
    temp = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if start[i][j] != goal[i][j] and start[i][j] != '_':
                temp += 1
    return temp


def h_manhattan(start, goal):
    misplaced = []
    for i in range(3):
        for j in range(3):
            if start[i][j] != goal[i][j] and start[i][j] != "_":
                misplaced.append((start[i][j], (i, j)))

    distance = 0
    for tile, pos in misplaced:
        x1, y1 = pos
        x2, y2 = get_tile_pos(tile, goal)
        distance += (abs(x1 - x2) + abs(y1 - y2))

    return distance


def h_combine_missplaced_with_manhattan(start, goal):
    h_origin = h_missplace(start, goal)
    h_manhat = h_manhattan(start, goal)

    distance = (h_origin + h_manhat) / 2

    return distance


def h_euclidean(start, goal):
    misplaced = []
    for i in range(3):
        for j in range(3):
            if start[i][j] != goal[i][j] and start[i][j] != "_":
                misplaced.append((start[i][j], (i, j)))

    distance = 0
    for tile, pos in misplaced:
        x1, y1 = pos
        x2, y2 = get_tile_pos(tile, goal)
        distance += ((x1 - x2)**2 + (y1 - y2)**2)

    return distance


def h_combine_euclidean_with_manhattan(start, goal):
    h_eucli = h_euclidean(start, goal)
    h_manhat = h_manhattan(start, goal)

    distance = (h_eucli + h_manhat) / 2
    return distance
