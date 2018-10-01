#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import unittest
import heapq
from point import Point
# from graph import Graph
from cluster import Cluster
from clusterGraph import ClusterGraph


class testClusterGraph(unittest.TestCase):
    def testInsertFirstPoint(self):
        CG = ClusterGraph()
        p0 = Point(0,0)
        CG.insertPoint(p0)
        self.assertEqual(CG.centers, {Point(0,0)})
        self.assertTrue(p0 == CG.H[0].center)

# Test a single cluster
    def testInsertPointsI(self):
        CG = ClusterGraph()
        p00 = Point(0,0)
        p10 = Point(1,0)
        p01 = Point(0,1)
        pn10 = Point(-1,0)
        p0n1 = Point(0,-1)
        CG.insertPoint(p00)
        CG.insertPoint(p10)
        CG.insertPoint(p01)
        CG.insertPoint(pn10)
        CG.insertPoint(p0n1)
        # print(CG.H[0].points)


# Test inserting a point with two established clusters
    def testInsertPointsII(self):
        #Setup
        CG = ClusterGraph()
        CG.centers = {Point(3,3), Point(-3,-3)}
        I = Cluster(Point(3,3))
        I.insertPoint(Point(2,3))
        I.insertPoint(Point(4,3))
        I.insertPoint(Point(3,4))
        I.insertPoint(Point(3,2))
        III = Cluster(Point(-3, -3))
        III.insertPoint(Point(-2,-3))
        # III.insertPoint(Point(-4,-3))
        III.insertPoint(Point(-3,-4))
        III.insertPoint(Point(-3,-2))
        CG.G.insertVertex(I)
        CG.G.insertVertex(III)
        CG.G.insertEdge(I, III)
        heapq.heappush(CG.H, I)
        heapq.heappush(CG.H, III)
        #actual test
        CG.insertPoint(Point(-4, -3))
        self.assertEqual(len(CG.H[0].points), 4)
        self.assertEqual(len(CG.H[1].points), 4)

    def testRemovePointsI(self):
        CG = ClusterGraph()
        p00 = Point(0,0)
        p10 = Point(1,0)
        p01 = Point(0,1)
        pn10 = Point(-1,0)
        p0n1 = Point(0,-1)
        p99 = Point(9,9)
        CG.insertPoint(p00)
        CG.insertPoint(p10)
        CG.insertPoint(p01)
        CG.insertPoint(pn10)
        CG.insertPoint(p0n1)
        CG.insertPoint(p99)
        self.assertEqual(len(CG.H[0].points), 5)
        CG.removePoint()
        print(CG.centers)
        print(CG.H[0].points)
        print(CG.H[1].points)
        # self.assertEqual(len(CG.H[0].points), 4)
        # self.assertEqual(len(CG.H[1].points), 0)








        # G = Graph()
        # # clustercenters = [Point(3,3), Point(-3, 3), Point(-3, -3), Point(3, -3)]
        # I = Cluster(Point(3,3))
        # I.insertPoint(Point(2,3))
        # I.insertPoint(Point(4,3))
        # I.insertPoint(Point(3,4))
        # I.insertPoint(Point(3,2))
        # II = Cluster(Point(-3, 3))
        # II.insertPoint(Point(-2,3))
        # II.insertPoint(Point(-4,3))
        # II.insertPoint(Point(-3,4))
        # II.insertPoint(Point(-3,2))
        # III = Cluster(Point(-3, -3))
        # III.insertPoint(Point(-2,-3))
        # III.insertPoint(Point(-4,-3))
        # III.insertPoint(Point(-3,-4))
        # III.insertPoint(Point(-3,-2))
        # IV = Cluster(Point(3, -3))
        # IV.insertPoint(Point(-2,-3))
        # IV.insertPoint(Point(-4,-3))
        # IV.insertPoint(Point(-3,-2))
        # IV.insertPoint(Point(-3,-4))
        # G.insertVertex(I)
        # G.insertVertex(II)
        # G.insertVertex(III)
        # G.insertVertex(IV)
        # G.insertEdge(I,II)
        # G.insertEdge(II,III)
        # G.insertEdge(III, IV)
        # self.assertEqual(G.getRel(I), {II})
        # self.assertEqual(G.getRel(II), {III})
        #
        # self.assertEqual(G.getRel(II), {III})





    # def testInsertFirstPoint(self):
    #     G = GreedyHeap()
    #     p = Point(0, 0)
    #     G.insertPoint(p)
    #     L = G.getCenters()
    #     self.assertEqual(L[0], Point(0, 0))
    #
    # def testHeapOneCenter(self):
    #     G = GreedyHeap()
    #     P = [Point(0,0), Point(0, 5), Point(0, 3), Point(0, 2), Point(0, 1), Point(0, 4)]
    #     for p in P:
    #         G.insertPoint(p)
    #     for entry in G.H:
    #         self.assertEqual(entry.c, Point(0, 0))
    #
    # def testHeapTwoCenter(self):
    #     G = GreedyHeap()
    #     G.C.append(Point(0,0))
    #     G.C.append(Point(0,7))
    #     P = [Point(1, 5), Point(0, 3), Point(0, 2), Point(0, 1), Point(0, 4)]
    #     f
    #     for p in P:
    #         G.insertPoint(p)
    #         if p.x > 3.5:
    #             self.assertEqual()

if __name__ == '__main__':
    unittest.main()
