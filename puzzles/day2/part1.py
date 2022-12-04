"""

"""

from pathlib import WindowsPath
from itertools import pairwise, chain

puzzle = WindowsPath(__file__).parent / 'puzzle.txt'  # .txt file next to .py file

left_plays = 'ABC'
right_plays = 'XYZ'


def run():
    lines = [pair.split() for pair in puzzle.read_text().splitlines()]
    for l in lines:
        left = left_plays.index(l[0])
        right = right_plays.index(l[1])

        tie = left == right
        left_win = left > right if not left == 0 and not right == 2 else False
        right_win = right > left if not right == 0 and not left == 2 else False

        print(l)
        print(tie, left_win, right_win)


if __name__ == '__main__':
    print(run())
