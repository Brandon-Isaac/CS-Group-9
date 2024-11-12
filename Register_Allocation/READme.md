Running the Code
1.Compile the Code
In the root of register_allocator, run:

make

This command compiles the code and creates an executable named register_allocator

2.Run the Register Allocator
To run the allocator on a test program, use:

./register_allocator tests/test_program1.txt

Make sure that test_program1.txt contains the sample code to test register allocation. You should see log messages or results printed as specified by the allocator functions.

3.Cleaning Up
To clean up compiled files, run:

make clean