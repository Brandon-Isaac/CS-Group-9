#include "graph.h"

void Graph::addNode(int node) {
    adjList[node];
}

void Graph::addEdge(int node1, int node2) {
    adjList[node1].insert(node2);
    adjList[node2].insert(node1);
}

bool Graph::colorGraph(int numRegisters) {
    // Graph coloring implementation
    return true;
}
