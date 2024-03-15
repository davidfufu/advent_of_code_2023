import os
import pprint
import re

INPUT_TEXT_PATH = "./3_input.txt"
INPUT_TEXT_TEST_PATH = "./3_input_test.txt"


class Machine:
    def __init__(self, input_path):
        with open(INPUT_TEXT_PATH, "r") as f:
            self.lines = [line.strip() for line in f.readlines()]
            self.schematic2D = [[*line] for line in self.lines]

            self.rowMaxIdx = len(self.schematic2D) - 1
            self.columnMaxIdx = len(self.schematic2D[0]) - 1

            # a set of all the coords adjacent to parts
            # if a num coord is in here, it's a part
            # self.allPartAdjacentCoords = set()

            # all coords adjacent to gears
            self.allPartAdjacentCoords = set()

            # # a list of lists [partNumber, (coord tuple)]
            self.numbersAndTheirCoords = []
            self.allGearAdjacentCoords = set()
            self.adjacentCoordToGearMapping = {}
            # self.getAllAdjacentGearCoords()

            self.getAllCoordsForEachNumber()

            # self.checkWhichNumbersAreAdjacentToParts()

            self.findGearAdjacentCoords()

            self.findNumbersAdjacentToEachGear()

    def findGearAdjacentCoords(self):
        gearRegex = r"[\*]"
        gearAdjacent = set()
        adjacentCoordToGearMapping = {}

        for i, line in enumerate(self.lines):
            for m in re.finditer(gearRegex, line):
                j = m.start()

                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        gearAdjacent.add((r, c))
                        adjacentCoordToGearMapping[(r, c)] = (i, j)

        self.allGearAdjacentCoords = gearAdjacent
        self.adjacentCoordToGearMapping = adjacentCoordToGearMapping
        # print(symbol_adjacent)

    def findNumbersAdjacentToEachGear(self):
        adjacentNumbersPerGear = {}

        numberRegex = r"\d+"
        for i, line in enumerate(self.lines):
            for m in re.finditer(numberRegex, line):
                print(m.span())
                allIndexesOfNumber = [(i, j) for j in range(m.span()[0], m.span()[1])]

                # This is a subset of the all indexes of the number that are adjacent to a gear
                adjacentCoords = [
                    coord
                    for coord in allIndexesOfNumber
                    if coord in self.allGearAdjacentCoords
                ]

                numberIsBesideAGear = len(adjacentCoords) > 0

                if numberIsBesideAGear:
                    number = m.group()
                    coordOfGearItsAdjacentTo = self.adjacentCoordToGearMapping[
                        adjacentCoords[-1]
                    ]

                    if coordOfGearItsAdjacentTo not in adjacentNumbersPerGear:
                        adjacentNumbersPerGear[coordOfGearItsAdjacentTo] = [number]
                    else:
                        adjacentNumbersPerGear[coordOfGearItsAdjacentTo].append(number)

                    print(
                        f"The number {number} is beside the gear at the coord {coordOfGearItsAdjacentTo}"
                    )

        print(adjacentNumbersPerGear)

        validGears = sum(
            [
                int(pair[1][0]) * int(pair[1][1])
                for pair in adjacentNumbersPerGear.items()
                if len(pair[1]) == 2
            ]
        )

        print(validGears)

    def checkWhichNumbersAreAdjacentToParts(self):
        sum = 0
        for numberData in self.numbersAndTheirCoords:
            number, coords = numberData
            for coord in coords:
                if coord in self.allPartAdjacentCoords:
                    print("ADDING: ", number)
                    sum += int(number)
                    break

        print(sum)

    def getAllCoordsForEachNumber(self):
        numbersToCoordinates = []

        for idx_row, row in enumerate(self.schematic2D):
            newNum = ""
            newNumCoords = set()
            for idx_column, char in enumerate(row):
                if not char.isnumeric():
                    # create the number
                    if newNum != "":
                        numbersToCoordinates.append([int(newNum), newNumCoords])
                        newNum = ""
                        newNumCoords = set()
                else:
                    newNum += char
                    newNumCoords.add((idx_row, idx_column))

            # edgecase: if the row is done and the last number is at the edge: numbers might remain
            if newNum != "":
                # create the number
                numbersToCoordinates.append([int(newNum), newNumCoords])
                newNum = ""
                newNumCoords = set()

        self.numbersAndTheirCoords = numbersToCoordinates

    def finalAllAdjacentCoords(self, rowIdx, columnIdx):
        validAdjacentCoords = set()
        changes = [1, 0, -1]

        for row_movement in changes:
            for column_movement in changes:
                new_row_idx = rowIdx + row_movement
                new_column_idx = columnIdx + column_movement

                if (
                    new_row_idx < 0
                    or new_column_idx < 0
                    or new_row_idx > self.rowMaxIdx
                    or new_column_idx > self.columnMaxIdx
                ):
                    # print(f"{new_row_idx}, {new_column_idx} is not valid")
                    continue

                # a valid adjacent coord to the gear is added as a tuple
                validAdjacentCoords.add((new_row_idx, new_column_idx))

        return validAdjacentCoords

    def getAllAdjacentGearCoords(self):
        self.symbols = []
        for row_idx, row in enumerate(self.schematic2D):
            for column_idx, char in enumerate(row):
                if not char.isnumeric() and char != ".":
                    if char not in self.symbols:
                        self.symbols.append(char)

                    adjacentCoords = self.finalAllAdjacentCoords(row_idx, column_idx)
                    self.allPartAdjacentCoords.update(adjacentCoords)

                    # print(f"for {char} at {row_idx},{column_idx} there are {len(adjacentCoords)} adjacent coords")
                    # print(adjacentCoords)


if __name__ == "__main__":
    machine = Machine(INPUT_TEXT_PATH)
# https://aoc-puzzle-solver.streamlit.app/
