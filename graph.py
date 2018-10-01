#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

class Graph:
    def __init__(self):
        self.E = dict()

    def insertVertex(self, vertex):
        self.E[vertex]= set()

    def insertEdge(self, v1, v2):
        if v1 not in self.E or v2 not in self.E:
            return
        self.E[v1].add(v2)
        self.E[v2].add(v1)

    def getRels(self, vertex):
        return self.E[vertex]

    def reoveEdge(self, v1, v2):
        self.E[v1].remove(v2)
        self.E[v2].remove(v1)

    def isEmpty(self):
        return not self.E

    def __contains__(self, item):
        return item in self.E

    def __iter__(self):
        return iter(self.E)
