from pathlib import WindowsPath

puzzle = WindowsPath(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    calories_per_elf = [sum((int(s) for s in (e.split('\n')))) for e in puzzle.read_text().split('\n\n')]

    return max(calories_per_elf)  # Part 1
    # return sum(sorted(calories_per_elf)[-3:])  # Part 2


if __name__ == '__main__':
    print(run())