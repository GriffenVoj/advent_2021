import sys
import numpy as np
from collections import defaultdict
from queue import PriorityQueue
data=open("realdata.txt").read().splitlines()
new=[]
newnew=[]
for item in data:
    new=[int(x) for x in item]
    newnew.append(new)    
matrix=np.array(newnew)
data=open("testdata.txt").read().splitlines()

def oner(yeah):
    yeah=yeah+1
    b,m=np.where(yeah>9)
    for i in range(len(b)):
        yeah[b[i]][m[i]]=1
    return yeah

plus1=oner(matrix)
plus2=oner(plus1)
plus3=oner(plus2)
plus4=oner(plus3)
plus5=oner(plus4)
plus6=oner(plus5)
plus7=oner(plus6)
plus8=oner(plus7)

columnone=np.concatenate((matrix,plus1,plus2,plus3,plus4),axis=0)
columntwo=np.concatenate((plus1,plus2,plus3,plus4,plus5),axis=0)
columnthree=np.concatenate((plus2,plus3,plus4,plus5,plus6),axis=0)
columnfour=np.concatenate((plus3,plus4,plus5,plus6,plus7),axis=0)
columnfive=np.concatenate((plus4,plus5,plus6,plus7,plus8),axis=0)

newmatrix=np.concatenate((columnone,columntwo,columnthree,columnfour,columnfive),axis=1)

newmatrix[0][0]=0

dictionary=defaultdict()
xarray=[]
yarray=[]
for i in range(len(newmatrix)):
    xarray.append(int(i))
    for z in range(len(newmatrix[0])):
        yarray.append(int(z))
        dictionary[i,z]=int(newmatrix[i][z]) 
xarray.sort()
yarray.sort()
max_x=xarray[-1]
max_y=yarray[-1]
nodes=np.arange((max_x+1)*(max_y+1)).reshape((max_x+1),(max_y+1))

def find_neighbours(arr):
    neighbors = []
    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):

            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])  # top neighbor
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1])  # right neighbor
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j])  # bottom neighbor
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])  # left neighbor

            else:
                # add neighbors
                new_neighbors = [
                    arr[i - 1][j],  # top neighbor
                    arr[i][j + 1],  # right neighbor
                    arr[i + 1][j],  # bottom neighbor
                    arr[i][j - 1]   # left neighbor
                ]

            neighbors.append({
                "value": value,
                "neighbors": new_neighbors})

    return neighbors
x=find_neighbours(nodes)

costnode=dict()

for i in range(len(newmatrix)):
    for m in range(len(newmatrix[i])):
        costnode[nodes[i][m]]=int(newmatrix[i][m])

def edgeconstruct(costlist,nodelist):
    tuplelist=[]
    for i in range(len(nodelist)):
        a=nodelist[i]['value']
        b=nodelist[i]['neighbors']
        for item in b:
            c=item
            d=costlist[item]
            tupe=(a,c,d)
            tuplelist.append(tupe) 
    return tuplelist

edges=edgeconstruct(costnode,x)

INF = int(0x3f3f3f3f)
class Graph:
    def __init__(self, V: int) -> None:
 
        self.V = V

        self.adj = [[] for _ in range(V)]
    def addEdgeRev(self, u: int, v: int, w: int) -> None:
        self.adj[v].append((u, w))
    def shortestPath(self, dest: int) -> None:
        pq = PriorityQueue()
        dist = [INF for _ in range(V)]
        pq.put((0, dest))
        dist[dest] = 0
        while not pq.empty():
            u = pq.get()[1]
            for i in self.adj[u]:
                v = i[0]
                weight = i[1]
                if (dist[v] > dist[u] + weight):
                    dist[v] = dist[u] + weight
                    pq.put((dist[v], v))
        for i in range(V):
            if i==V-1:
                print(dist[i]+newmatrix[-1][-1])
                
 
if __name__ == "__main__":
 
    V = (max_x+1)*(max_y+1)
    g = Graph(V)
 
    for item in edges:
        g.addEdgeRev(item[0],item[1],item[2])
 
    g.shortestPath(0)
    


 