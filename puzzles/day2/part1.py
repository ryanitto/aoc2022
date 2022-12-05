"""

"""

from pathlib import WindowsPath

puzzle = WindowsPath(__file__).parent / 'puzzle.txt'  # .txt file next to .py file

opponent_plays = 'ABC'
your_plays = 'XYZ'
win_map = {0: 1, 1: 2, 2: 0}

def run():
    score = 0
    lines = [pair.split() for pair in puzzle.read_text().splitlines()]
    for l in lines:
        opponent = opponent_plays.index(l[0])
        you = your_plays.index(l[1])
        win_condition = win_map[opponent]

        # Right wins
        if you == win_condition:
            score += 6
        # Tie
        elif you == opponent:
            score += 3

        # Increment from left's choice
        score += you + 1

    return score


if __name__ == '__main__':
    print(run())
