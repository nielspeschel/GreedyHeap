class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        if other is None:
            return float("inf")
        return ((other.y - self.y)**2 + (other.x - self.x)**2)**0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return str(self)
        
    def __str__(self):
        return str((self.x, self.y))
