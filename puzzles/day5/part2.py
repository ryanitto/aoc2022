"""--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a
CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup
holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the
same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to
be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each
stack?



"""

from pathlib import Path
from collections import deque

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    lines = puzzle.read_text().splitlines()
    crate_lines = lines[:9]
    move_lines = lines[10:]
    column_line = crate_lines.pop(-1)
    column_count = column_line.split()

    columns = {int(k): [] for k in column_count}

    # Initial placement for crates
    for c in crate_lines:
        row = deque(c)

        for c in columns:
            r = row[1]
            row.rotate(-4)
            if r != ' ':
                columns[c].insert(0, r)

    # Time to move
    for m in move_lines:
        moves = [int(x) for x in ''.join([c for c in m if not c.isalpha()][1:]).split('  ')]
        crates_to_move, from_column, to_column = moves
        stack = []
        for i in range(crates_to_move):
            stack.append(columns[from_column].pop(-1))

        stack.reverse()
        columns[to_column] += stack

    top_crates = ''.join([v[-1] for v in columns.values()])

    return top_crates


if __name__ == '__main__':
    print(run())
