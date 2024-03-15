import os
import pprint
import re
import math

INPUT_TEXT_PATH = "./3_input.txt"
INPUT_TEXT_TEST_PATH = "./3_input_test.txt"


class Machine:
    def __init__(self, input_path):
        with open(INPUT_TEXT_PATH, "r") as f:
            self.lines = [line.strip() for line in f.readlines()]

            self.partOne()
            self.partTwo()

    def partOne(self):
        symbolRegex = r"[^.\d]"

        numbersAdjacentToSymbols = set()
        for i, line in enumerate(self.lines):
            for m in re.finditer(symbolRegex, line):
                for r in range(i - 1, i + 2):
                    for c in range(m.start() - 1, m.end() + 1):
                        numbersAdjacentToSymbols.add((r, c))

        sum = 0
        numberRegex = r"\d+"

        for i, line in enumerate(self.lines):
            for m in re.finditer(numberRegex, line):
                if any(
                    (i, j) in numbersAdjacentToSymbols
                    for j in range(m.start(), m.end())
                ):
                    sum += int(m.group())

        print("The total sum of parts is ", sum)

    def partTwo(self):
        gearRegex = r"[\*]"
        gears = {}

        for i, line in enumerate(self.lines):
            for m in re.finditer(gearRegex, line):
                j = m.start()
                gears[(i, j)] = []

        # now let's find each number and look at every single adjacent index around it

        numberRegex = r"\d+"

        for i, line in enumerate(self.lines):
            for m in re.finditer(numberRegex, line):
                for r in range(i - 1, i + 2):
                    for c in range(m.start() - 1, m.end() + 1):
                        if (r, c) in gears:
                            gears[(r, c)].append(int(m.group()))

        gearRatio = 0
        for value in gears.values():
            if len(value) == 2:
                gearRatio += math.prod(value)
        print("Total Gear Ratio ", gearRatio)


if __name__ == "__main__":
    machine = Machine(INPUT_TEXT_PATH)
