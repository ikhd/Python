#!/usr/bin/env python

# to run this script you need install (PyAlgDat 1.0.2):
# https://pypi.python.org/pypi/PyAlgDat

def graph():

    graph = UnDirectedWeightedGraph(7)


    vertex1 = UnWeightedGraphVertex(graph, "A")
    vertex2 = UnWeightedGraphVertex(graph, "B")
    vertex3 = UnWeightedGraphVertex(graph, "C")
    vertex4 = UnWeightedGraphVertex(graph, "D")
    vertex5 = UnWeightedGraphVertex(graph, "E")
    vertex6 = UnWeightedGraphVertex(graph, "F")
    vertex7 = UnWeightedGraphVertex(graph, "G")


    graph.add_vertex(vertex1)
    graph.add_vertex(vertex2)
    graph.add_vertex(vertex3)
    graph.add_vertex(vertex4)
    graph.add_vertex(vertex5)
    graph.add_vertex(vertex6)
    graph.add_vertex(vertex7)

	
    graph.add_edge(vertex1, vertex2, 4)   
    graph.add_edge(vertex1, vertex4, 9)    
    graph.add_edge(vertex2, vertex3, 10)   
    graph.add_edge(vertex2, vertex4, 14)    
    graph.add_edge(vertex2, vertex5, 7)    
    graph.add_edge(vertex3, vertex5, 5)  
    graph.add_edge(vertex4, vertex5, 15)   
    graph.add_edge(vertex4, vertex6, 3)    
    graph.add_edge(vertex5, vertex6, 8)   
    graph.add_edge(vertex5, vertex7, 1)   
    graph.add_edge(vertex6, vertex7, 11)   
    return graph

if __name__ == "__main__":
    if __package__ is None:
       import sys
       from os import path
       sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
       from py_alg_dat.graph import UnDirectedWeightedGraph
       from py_alg_dat.graph_vertex import UnWeightedGraphVertex
       from py_alg_dat.graph_algorithms import GraphAlgorithms
    else:
       from ..py_alg_dat.graph import UnDirectedWeightedGraph
       from ..py_alg_dat.graph_vertex import UnWeightedGraphVertex
       from ..py_alg_dat.graph_algorithms import GraphAlgorithms

    GRAPH = graph()

    MST = GraphAlgorithms.kruskals_algorithm(GRAPH)

    print MST