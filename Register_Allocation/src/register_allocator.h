#ifndef REGISTER_ALLOCATOR_H
#define REGISTER_ALLOCATOR_H

#include <vector>
#include <istream>
#include "graph.h"
#include "liveness.h"

class RegisterAllocator {
public:
    void allocateRegisters(std::istream& programStream);

private:
    void performLivenessAnalysis();
    void constructInterferenceGraph();
    void assignRegisters();
    Graph interferenceGraph;
};

#endif
