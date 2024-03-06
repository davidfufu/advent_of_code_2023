import os


INPUT_TEXT_PATH = "./3_input.txt"
INPUT_TEXT_TEST_PATH = "./3_input_test.txt"

class Machine:
    def __init__(self, input_path):
        with open(INPUT_TEXT_TEST_PATH, "r") as f:
            lines = f.readlines()
            self.schematic2D = [[*line] for line in lines]

            self.buildSymbolsList()
            self.partOne_SumOfPartNumbers()

    def partOne_SumOfPartNumbers(self):
        partNumbers = []

        for idx_row, row in enumerate(self.schematic2D):
            newNum = ""
            newNumIsPart = False
            for idx_column, char in enumerate(row):
                if not char.isnumeric():
                    if newNumIsPart:
                        # create the number
                        partNumbers.append(int(newNum))
                        newNumIsPart = False
                    newNum = ""
                else:
                    newNum += char
                    adjacent = self.checkIfSymbolAdjacent(idx_row, idx_column)
                    if adjacent:
                        newNumIsPart = True
            
            #edgecase: if the row is done and the last number is at the edge: numbers might remain
            if len(partNumbers) > 0:
                if newNumIsPart:
                    # create the number
                    partNumbers.append(int(newNum))
                    newNumIsPart = False
                newNum = ""

        print(sum(partNumbers))

    def checkIfSymbolAdjacent(self, row_idx, column_idx):
        changes = [1, 0, -1]
        adjacent = False

        for row_movement in changes:
            for column_movement in changes:
                new_row_idx = row_idx + row_movement
                new_column_idx = column_idx + column_movement

                try:
                    targetLocation = self.schematic2D[new_row_idx][new_column_idx]
                    if targetLocation in self.symbols:
                        adjacent = True
                except IndexError:
                    continue

        return adjacent

    def buildSymbolsList(self):
        self.symbols = []
        for row in self.schematic2D:
            for char in row:
                if not char.isnumeric() and char != ".":
                    if char not in self.symbols:
                        self.symbols.append(char)


if __name__ == "__main__":
    machine = Machine(INPUT_TEXT_PATH)
