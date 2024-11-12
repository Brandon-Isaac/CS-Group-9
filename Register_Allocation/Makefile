CXX = g++
CXXFLAGS = -std=c++11 -Wall
SRC = main.cpp register_allocator.cpp graph.cpp liveness.cpp
OBJ = $(SRC:.cpp=.o)

all: register_allocator

register_allocator: $(OBJ)
	$(CXX) $(CXXFLAGS) -o register_allocator $(OBJ)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f register_allocator $(OBJ)
