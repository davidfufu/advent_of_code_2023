# CUBE CONUNDRUM


import os

INPUT_FILE_PATH = "./2_input.txt"
INPUT_TEST_FILE_PATH = "./2_input_test.txt"


availableCubes = {"red": "12", "blue": "14", "green": "13"}


class Game:
    def __init__(self, gameRecord: str):
        gameRecord = gameRecord.strip()
        gameStr, subsetsStr = gameRecord.split(": ")

        self.gameID = gameStr[-1]

        self.recordHighestObsInEachColor(subsetsStr)
        self.calculatePossibility()

    def recordHighestObsInEachColor(self, subsetStr: str):
        subsets = subsetStr.split("; ")
        highest = {"red": 0, "blue": 0, "green": 0}

        for subset in subsets:

            colorObservations = subset.split(", ")
            for observation in colorObservations:
                quantity, color = observation.split(" ")
                highest[color] = max(highest[color], int(quantity))

        self.highestObservedQuantities = highest

    def calculatePossibility(self):
        self.possible = True

        for color, maxCubes in availableCubes.items():
            if self.highestObservedQuantities[color] > int(maxCubes):
                self.possible = False

    def calculateCubeSetPower(self):
        product = 1
        for k, v in self.highestObservedQuantities.items():
            product *= v
        return product


def partOne_sumPossibleGameIDs():
    sumOfPossibleGameIDs = 0

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        for line in lines:
            newGame = Game(line)
            if newGame.possible:
                sumOfPossibleGameIDs += int(newGame.gameID)
    return sumOfPossibleGameIDs


def partTwo_sumOfPowerOfMininumCubeSets():
    sumOfPowers = 0
    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        for line in lines:
            newGame = Game(line)
            sumOfPowers += newGame.calculateCubeSetPower()
    return sumOfPowers


if __name__ == "__main__":
    # print(partOne_sumPossibleGameIDs())
    print(partTwo_sumOfPowerOfMininumCubeSets())
