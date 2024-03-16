import re
import os
import time

INPUT_TEXT_PATH = "./24_input.txt"
TEST_INPUT_TEXT_PATH = "./24_test_input.txt"


class ScratchCards:
    def __init__(self, filePath):
        self.setUp()
        self.partOne()
        self.partTwo()

    def setUp(self):
        puzzleInput = open(INPUT_TEXT_PATH).read()
        self.numbersRegex = r"Card\s*(\d*):(.*)\|(.*)"
        self.cards = re.findall(self.numbersRegex, puzzleInput)

    def partOne(self):
        total = 0

        for card in self.cards:
            _, winNums, myNums = card
            wins = self.findOverlaps(winNums, myNums)
            if wins:
                points = 2 ** (len(wins) - 1)
                total += points

        print("Parrt One Points ", total)

    def cardCounter(self, card: tuple, totalCards):
        cardNumber, winNums, myNums = card

        if cardNumber not in totalCards:
            totalCards[cardNumber] = 1
        else:
            totalCards[cardNumber] += 1

        overlaps = self.findOverlaps(winNums, myNums)

        for i in range(int(cardNumber) + 1, int(cardNumber) + len(overlaps) + 1):
            try:
                self.cardCounter(self.cards[i - 1], totalCards)
            except IndexError:
                continue

    def partTwo(self):
        totalCards = {}
        for card in self.cards:
            self.cardCounter(card, totalCards)

        print("Part Two: Total Amount Of Scratch Cards: ", sum(totalCards.values()))

    def findOverlaps(self, winNumStr, myNumStr) -> set:
        return set(myNumStr.strip().split()) & set(winNumStr.strip().split())


if __name__ == "__main__":
    t1 = time.time()
    scratchCard = ScratchCards(TEST_INPUT_TEXT_PATH)
    elapsed = time.time() - t1
    print("Took: ", elapsed)
