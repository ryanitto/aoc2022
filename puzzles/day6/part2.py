"""--- Part Two ---

Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also
needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather
than 4.

Here are the first positions of start-of-message markers for all of the above examples:

mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

How many characters need to be processed before the first start-of-message marker is detected?
"""

from pathlib import Path

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file


def run():
    line = puzzle.read_text()
    i = 0
    while len(set(line[:14])) < 14:
        line = line[1:]
        i += 1
    i += 14

    return i


if __name__ == '__main__':
    print(run())
