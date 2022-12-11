"""
Author: Ryan Metcalf
Day:    8
Part:   1

i did not create this; i got the solution from https://www.reddit.com/r/adventofcode/comments/zfpnka/comment/izhcy8c/?utm_source=share&utm_medium=web2x&context=3

"""

from pathlib import Path
import numpy

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    lines = [[int(i) for i in l] for l in puzzle.read_text().splitlines()]
    grid = numpy.array(lines)
    t_grid = grid.transpose()
    vis = 0
    for a in range(len(grid[0])):
        for b in range(len(grid)):
            t = grid[a][b]
            top = all(x < t for x in grid[a][0:b])
            bot = all(x < t for x in grid[a][b+1:])
            left = all(x < t for x in t_grid[b][0:a])
            right = all(x < t for x in t_grid[b][a+1:])
            if top or bot or left or right:
                vis += 1
    return vis


if __name__ == '__main__':
    print(run())
