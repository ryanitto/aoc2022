"""
Author: Ryan Metcalf
Day:    8
Part:   1

although i didn't do the solution for part 1 myself -- i did for this

"""

from pathlib import Path
import numpy
from math import prod

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    lines = [[int(i) for i in l] for l in puzzle.read_text().splitlines()]
    grid = numpy.array(lines)
    t_grid = grid.transpose()
    vis_totals = []
    for a in range(len(grid[0])):
        for b in range(len(grid)):
            tree_vis = None
            tree = grid[a][b]
            left = [x < tree for x in grid[a][0:b]]
            right = [x < tree for x in grid[a][b+1:]]
            top = [x < tree for x in t_grid[b][0:a]]
            bot = [x < tree for x in t_grid[b][a+1:]]
            if any(top) and any(bot) and any(left) and any(right):
                tree_vis = []
                top.reverse()
                left.reverse()
                for x in [top, left, right, bot]:
                    if len(x) < 2:
                        tree_vis.append(1)
                        continue
                    for i, y in enumerate(x):
                        if not y:
                            tree_vis.append(i + 1)
                            break
                    if all(x):
                        tree_vis.append(len(x))
            if tree_vis:
                # print(tree_vis, '<----', [top, left, right, bot]) if tree_vis else None
                vis_totals.append(prod(tree_vis))
    return max(vis_totals)


if __name__ == '__main__':
    print(run())
