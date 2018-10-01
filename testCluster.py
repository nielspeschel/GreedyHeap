#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import unittest
from point import Point
# from GreedyHeap import GreedyHeap
from graph import Graph
from cluster import Cluster

class testCluster(unittest.TestCase):
    def testPoint(self):
        a = Point(0, 0)
        b = Point(2, 2)
        c = Point(2, 1)
        d = Point(6, 4)
        self.assertEqual(a.dist(b), 8**0.5)
        self.assertEqual(a.dist(a), 0.0)
        self.assertEqual(b.dist(b), 0.0)
        self.assertEqual(c.dist(d), 5.0)

    def testPointEq(self):
        a = Point(1, 2)
        self.assertEqual(a, Point(1, 2))

    def testCluster(self):
        center = Point(0, 0)
        a = Point(1, 0)
        b = Point(2, 0)
        c = Point(3, 0)
        d = Point(4, 0)
        e = Point(5, 0)
        C = Cluster(center)
        C.insertPoint(b)
        C.insertPoint(d)
        C.insertPoint(a)
        C.insertPoint(c)
        C.insertPoint(e)
        self.assertEqual(C.deg(), 5)
        self.assertEqual(C.getFarthestPoint(), e)
        self.assertEqual(C.getFarthestDist(), 5)
        C.removeFarthestPoint()
        self.assertEqual(C.deg(), 4)
        self.assertEqual(C.getFarthestPoint(), d)
        self.assertEqual(C.getFarthestDist(), 4)
        self.assertTrue(b in C)
        C.removePoint(b)
        self.assertFalse(b in C)
        self.assertEqual(C.deg(), 3)



if __name__ == '__main__':
    unittest.main()
