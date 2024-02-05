from enum import Enum

from typer import Typer

from rich.table import Table
from rich.console import Console

from puzzle.puzzle import Puzzle
from puzzle.heuristic_funcs import (h_missplace,
                                    h_manhattan,
                                    h_combine_missplaced_with_manhattan,
                                    h_euclidean,
                                    h_combine_euclidean_with_manhattan)
from puzzle.util import get_start_and_goal_puzzle

app = Typer()


class FuncName(Enum):
    manhattan = "Manhattan"
    misplaced = "MissPlaced"
    combine_miss_manhat = "CombineMissManhat"
    euclidean = "Euclidean"
    combine_eucli_manhat = "CombineEucliManhat"


@app.command(name="chosse")
def main(h_name: FuncName):
    start, goal = get_start_and_goal_puzzle()
    match h_name:
        case FuncName.manhattan:
            puzzle = Puzzle(start, goal, 3, h_manhattan)
        case FuncName.misplaced:
            puzzle = Puzzle(start, goal, 3, h_missplace)
        case FuncName.combine_miss_manhat:
            puzzle = Puzzle(start, goal, 3,
                            h_combine_missplaced_with_manhattan)
        case FuncName.euclidean:
            puzzle = Puzzle(start, goal, 3, h_euclidean)
        case FuncName.combine_eucli_manhat:
            puzzle = Puzzle(start, goal, 3, h_combine_euclidean_with_manhattan)

    puzzle.calculate(True)


@app.command(name="compare")
def compare(show_steps: bool = False):
    start, goal = get_start_and_goal_puzzle()
    data = []
    if show_steps:
        printed = False

    for h in [h_missplace, h_manhattan, h_combine_missplaced_with_manhattan,
              h_euclidean, h_combine_euclidean_with_manhattan]:
        p = Puzzle(start, goal, 3, h)
        if show_steps and not printed:
            printed = True
            p.calculate(show_steps)
        else:
            p.calculate(False)
        data.append((str(h.__name__), str(p.steps), str(p.node_searched)))

    table = Table("Heuristic Function Name", "Steps", "Searched Nodes")
    for r in data:
        table.add_row(*r)

    console = Console()
    console.print(table)


if __name__ == "__main__":
    app()
