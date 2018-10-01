#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import unittest
from point import Point
# from GreedyHeap import GreedyHeap
from graph import Graph
from cluster import Cluster

class testGreedyHeap(unittest.TestCase):
    def testIsEmpty(self):
        G = Graph()
        self.assertTrue(G.isEmpty())

    def testGraph(self):
        G = Graph()
        G.insertVertex(1)
        G.insertVertex(2)
        G.insertVertex(3)
        G.insertVertex(4)
        G.insertEdge(1, 2)
        G.insertEdge(2, 3)
        G.insertEdge(3, 4)
        self.assertTrue(2 in G.getRels(1))
        self.assertTrue(3 in G.getRels(2))
        self.assertTrue(4 in G.getRels(3))
        self.assertFalse(3 in G.getRels(1))
        G.insertEdge(1, 3)
        self.assertTrue(3 in G.getRels(1))


if __name__ == '__main__':
    unittest.main()
