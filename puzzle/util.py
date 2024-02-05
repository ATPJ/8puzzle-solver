def get_tile_pos(tile, goal):
    for i in range(3):
        for j in range(3):
            if goal[i][j] == tile:
                return (i, j)


def accept(n: int):
    return [input().split() for _ in range(n)]


def get_start_and_goal_puzzle(n: int = 3):
    # Accept Start and Goal Puzzle state
    print("enter the start state matrix \n")
    start = accept(n)
    print("enter the goal state matrix \n")
    goal = accept(n)
    return (start, goal)
