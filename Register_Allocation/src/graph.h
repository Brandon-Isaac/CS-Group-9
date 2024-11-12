#ifndef GRAPH_H
#define GRAPH_H

#include <unordered_map>
#include <unordered_set>

class Graph {
public:
    void addNode(int node);
    void addEdge(int node1, int node2);
    bool colorGraph(int numRegisters);

private:
    std::unordered_map<int, std::unordered_set<int>> adjList;
};

#endif
