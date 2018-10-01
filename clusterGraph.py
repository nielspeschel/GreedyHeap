import heapq
from graph import Graph
from cluster import Cluster


class ClusterGraph:
    def __init__(self):
        self.G = Graph()
        self.H = [] #To be maintained as a priorityqueue
        self.centers = set()
        self.r = float('inf')

    def insertPoint(self, point):
        if self.G.isEmpty():
            cluster = Cluster(point)
            self.G.insertVertex(cluster)
            heapq.heappush(self.H, cluster)
            self.centers.add(point)
            return
        closestCluster = list(self.G.E.keys())[0]
        for cluster in self.G:
            if cluster.center.dist(point) < closestCluster.center.dist(point):
                closestCluster = cluster
        closestCluster.insertPoint(point)

    def removePoint(self):
        clust = self.H[0] #retrieves the "smallest" cluster
        r = clust.getFarthestDist()
        if r < self.r:
            self.r = r
        p = clust.removeFarthestPoint()
        self.centers.add(p)
        newC  = Cluster(p)
        self.G.insertVertex(newC)

        clusterset = set()
        for rel in self.G.getRels(clust):
            toRemove = set()
            for point in rel.points:
                if point.dist(p) < point.dist(rel.center):
                    toRemove.add(point)
                    temp.insertpoint(point)
            rel.points = rel.points - toRemove
            clusterset.add(rel)
            for relrel in G.getRels(rel):
                clusterset.add(relrel)
        for c in clusterset:
            if c.center.dist(p) <= 3*r:
                G.insertedge(newC, c)
        heapq.heappush(self.H, newC)

    def returnCenters(self):
        return self.centers



if __name__ == '__main__':
    CG = ClusterGraph()
