# Prim's MST Algorithm

from sys import maxsize as mi
from tabulate import tabulate

class Prim:
    def __init__(self, v, x):
        self.v = v
        self.g = x

    def minKey(self, key, mstSet):
        min = mi
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def disp(self, parent):
        x = []
        y = []
        for i in range(1, self.V):
            x.append(str(parent[i]) + ": " + str(i))
            y.append(self.g[i][parent[i]])
        print(tabulate({"Edge": x, "Weight": y}, headers="keys", tablefmt='orgtbl'))

    def prims(self):
        key = [mi] * self.V
        parent = [None] * self.V
        mstSet = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for c in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if ((self.g[u][v] > 0) and (mstSet[v] == False) and (key[v] > self.g[u][v])):
                    key[v] = self.g[u][v]
                    parent[v] = u
        self.disp(parent)


v = int(input("Enter number of vertices : "))
x = []
for i in range(v):
    y = list(map(int, input("Enter the numbers: ").strip().split()))
    x.append(y)
    print()

o = Prim(v, x)
o.prims()
