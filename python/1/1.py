import os

CALIBRATION_DOC_PATH = "./1_input.txt"
CALIBRATION_DOC_TEST_PATH = "./1_input_test.txt"

numStrings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def findFirstNumberChar(line: str, reverse: bool = False):
    line = line.strip()
    if reverse:
        line = line[::-1]

    for i in range(len(line)):
        char = line[i]

        if char.isnumeric():
            return char
        else:
            # if the char is not a number, see if substrings starting from here
            for key, value in numStrings.items():
                numberWord = key

                if reverse:
                    numberWord = key[::-1]

                if line[i : i + len(numberWord)] == numberWord:
                    return numStrings[key]


def sumCalibrationValues():
    total = 0

    with open(CALIBRATION_DOC_PATH, "r") as f:
        lines = f.readlines()
        for line in lines:
            firstNumChar = findFirstNumberChar(line)
            secondNumChar = findFirstNumberChar(line, reverse=True)
            combinedNumber = int(f"{firstNumChar}{secondNumChar}")
            total += combinedNumber

    return total


if __name__ == "__main__":
    print(sumCalibrationValues())
