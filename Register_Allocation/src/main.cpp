#include "register_allocator.h"
#include <iostream>
#include <fstream>
#include <vector>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <input_program>" << std::endl;
        return 1;
    }

    std::ifstream inputFile(argv[1]);
    if (!inputFile) {
        std::cerr << "Error opening input file!" << std::endl;
        return 1;
    }

    RegisterAllocator allocator;
    allocator.allocateRegisters(inputFile);
    
    std::cout << "Register allocation completed successfully!" << std::endl;
    return 0;
}
