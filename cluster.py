     #! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

class Cluster:
    def __init__(self, center):
        self.center = center
        self.points = set()

    def insertPoint(self, p):
        self.points.add(p)

    def getFarthestPoint(self):
        currFarthest = self.center
        for p in self.points:
            if p.dist(self.center) > currFarthest.dist(self.center):
                currFarthest = p
        return currFarthest
        # return max(self.points, key = self.center.dist)

    def getFarthestDist(self):
        return self.center.dist(self.getFarthestPoint())

    def deg(self):
        return len(self.points)

    def removeFarthestPoint(self):
        p = self.getFarthestPoint()
        self.points.remove(p)
        return p

    def removePoint(self, point):
        self.points.remove(point)

    def __contains__(self, point):
        return point in self.points

    def __hash__(self):
        return hash(self.center)

    def __lt__(self, other):
        return self.getFarthestDist() < other.getFarthestDist()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.center) + " : " + str(self.points)
