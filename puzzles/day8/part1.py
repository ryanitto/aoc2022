"""
Author: Ryan Metcalf
Day:    8
Part:   1
"""

from pathlib import Path
import numpy

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def show_coords(a, axis):
    print(a[axis], axis)
    return a

def run():
    lines = [[int(i) for i in l] for l in puzzle.read_text().splitlines()]
    grid = numpy.array(lines)
    m_grid = numpy.ma.MaskedArray(grid, mask=[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]])
    # return masked_grid
    # return numpy.argmax(masked_grid, axis=0)
    # return numpy.piecewise(m_grid, [grid >= 0, grid > 0], [0, 1])

    new_grid = []
    top, bottom = grid[0], grid[-1]
    left, right = grid.transpose()[0], grid.transpose()[-1]
    for i, row in enumerate(grid):
        new_row = []
        if 0 < i < len(top) - 1:
            column = grid.transpose()[i]
            for j in range(len(row[1:-1])):
                print(row[j+1], row, column[j+1], column)

            # trim_row, trim_col = row[1:-1], column[1:-1]
            # start = 1
            # stop = len(row) - 1
            # for j in range(start, stop):
            #     vis_from_edge = list(map(lambda x: row[j] > x, (left[i], right[i], top[i], bottom[i])))
            #     if any(vis_from_edge):
            #         vis_from_row = list(map(lambda x: row[j] > x, row[1:-1]))
            #         vis_from_col = list(map(lambda x: column[j] > x, column[1:-1]))
            #         print(any(vis_from_row), any(vis_from_col), row[j], row, '<--')
            #
            #     else:
            #         new_row.append(0)

    return grid


if __name__ == '__main__':
    print(run())
