import re
import os
import time

INPUT_TEXT_PATH = "./24_input.txt"
TEST_INPUT_TEXT_PATH = "./24_test_input.txt"


class ScratchCards:
    def __init__(self, filePath):
        # self.partOne()
        self.partTwo()

    def partOne(self):
        puzzleInput = open(INPUT_TEXT_PATH).read()
        total = 0
        numbersRegex = r":(.*)\|(.*)"

        # for card
        # print(re.findall(numbersRegex, puzzleInput))
        for winNums, myNums in re.findall(numbersRegex, puzzleInput):
            wins = set(myNums.strip().split()) & set(winNums.strip().split())
            if wins:
                points = 2 ** (len(wins) - 1)
                total += points

        print(total)

    def partTwo(self):
        puzzleInput = open(INPUT_TEXT_PATH).read()
        numbersRegex = r"Card\s*(\d*):(.*)\|(.*)"
        cards = re.findall(numbersRegex, puzzleInput)
        print(type(cards), len(cards))
        print(cards)
        totalCards = {}

        def cardCounter(card: tuple, totalCards):
            print("Evaluating: ", card)

            cardNumber, winNums, myNums = card

            if cardNumber not in totalCards:
                totalCards[cardNumber] = 1
            else:
                totalCards[cardNumber] += 1

            overlaps = self.findOverlaps(winNums, myNums)

            for i in range(int(cardNumber) + 1, int(cardNumber) + len(overlaps) + 1):
                try:
                    cardCounter(cards[i - 1], totalCards)
                except IndexError:
                    continue

        for card in cards:
            cardCounter(card, totalCards)

        print(totalCards)

        print("Total Amount Of Scratch Cards: ", sum(totalCards.values()))

    def findOverlaps(self, winNumStr, myNumStr) -> set:
        return set(myNumStr.strip().split()) & set(winNumStr.strip().split())


if __name__ == "__main__":
    t1 = time.time()
    scratchCard = ScratchCards(TEST_INPUT_TEXT_PATH)
    elapsed = time.time() - t1
    print("Took: ", elapsed)
