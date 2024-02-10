#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <limits>
#include <optional>

int createIntList(const std::string& input){
    char firstDigit = '\0', lastDigit = '\0';

    for (char c : input){
        if(std::isdigit(c)){
            if(firstDigit == '\0'){
                firstDigit = c;
            }
            lastDigit = c;
        }
    }

    std::string combined1 = {firstDigit, lastDigit};
    return stoi(combined1);
}

int main(){
    std::ifstream file("./input.txt");
    std::string line;
    int finalVal = 0;

    if(file.is_open()){
        while(std::getline(file, line)){
            int foundInt = createIntList(line);
            finalVal += foundInt;
        }
        file.close();
    } else {
        std::cout << "Unable to open file";
    }

    std::cout << finalVal;

    std::cout << "Press Enter to close...";
    std::cin.get();

    return 0;
}