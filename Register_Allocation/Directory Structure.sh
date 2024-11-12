register_allocator_project/
├── src/
│   ├── main.cpp             # Main entry point of the program
│   ├── register_allocator.h # Header file for the register allocator
│   ├── register_allocator.cpp # Implementation of register allocator
│   ├── graph.h              # Header file for the interference graph
│   ├── graph.cpp            # Implementation of the interference graph
│   ├── liveness.h           # Header file for liveness analysis
│   ├── liveness.cpp         # Implementation of liveness analysis
│   └── utils.h              # Helper functions and definitions
├── tests/
│   ├── test_program1.txt    # Sample test input programs
│   ├── test_program2.txt
└── Makefile                 # Makefile for building the project

Step-by-Step File Explanations
main.cpp: Entry point that orchestrates the register allocation process.
register_allocator.h/.cpp: The main register allocator that interfaces with the graph and performs the allocation.
graph.h/.cpp: Contains code for constructing and managing the interference graph used in graph coloring.
liveness.h/.cpp: Manages liveness analysis, identifying variable lifetimes.
utils.h: Contains helper functions for diagnostics, debugging, or common operations.
