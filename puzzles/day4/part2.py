"""--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number
of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,
7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

"""

from pathlib import WindowsPath

puzzle = WindowsPath(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    sections = [[(int(i)) for i in r.split('-')] for l in puzzle.read_text().splitlines() for r in l.split(',')]
    count = 0
    for r in range(0, len(sections), 2):
        elf_one = {*range(sections[r][0], sections[r][1]+1)}
        elf_two = {*range(sections[r+1][0], sections[r+1][1]+1)}
        overlaps = elf_one.intersection(elf_two)
        count += 1 if overlaps else 0
    return count


if __name__ == '__main__':
    print(run())
