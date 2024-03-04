#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <limits>
#include <optional>
#include <map>
#include <cstdlib>

std::map<std::string, int> numberLiterals = {
    {"one", 1},
    {"two", 2},
    {"three", 3},
    {"four", 4},
    {"five", 5},
    {"six", 6},
    {"seven", 7},              
    {"eight", 8},
    {"nine", 9},
};  
 

int createIntList(const std::string& input){
    int firstDigit = 0, lastDigit = 0;

    for(std::size_t i = 0; i < input.size(); ++i){
        //is one of the keys in the mapped string to int numbers
        char c = input.at(i);
        int intValue = c - '0';

        //check if the char is a digit
        if(std::isdigit(c)){
            if(firstDigit == 0){
                firstDigit = intValue;
            }

            lastDigit = intValue;
        }
        else{
            //if not check if the substring starting from this index
            for (const auto& pair : numberLiterals){
                int length = pair.first.length();
                std::string slice = input.substr(i, length);

                if(slice == pair.first){
                    if (firstDigit == 0){
                        firstDigit = numberLiterals.at(slice);
                    }
                    lastDigit = numberLiterals.at(slice);
                }
            }
        }
    }
    std::string firstNumberToString = std::to_string(firstDigit);
    std::string lastNumberToString  = std::to_string(lastDigit);
    std::string combined = firstNumberToString + lastNumberToString;
    return stoi(combined);
}

int main(){
    std::ifstream file("./input.txt");
    std::string line;
    int finalVal = 0;

    if(file.is_open()){
        while(std::getline(file, line)){
            int foundInt = createIntList(line);
            std::cout << "\n" << foundInt;
            finalVal += foundInt;
        }
        file.close();
    } else {
        std::cout << "Unable to open file";
    }

    std::cout << "\n" << finalVal;

    std::cout << "\nPress Enter to close...";
    std::cin.get();

    return 0;
}