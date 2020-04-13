from collections import defaultdict 
class Graph: 
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
    def addEdge(self,v,w): 
        self.graph[v].append(w) #Add w to v_s list 
        self.graph[w].append(v) #Add v to w_s list 
    def isCyclicUtil(self,v,visited,parent): 
        visited[v]= True
        for i in self.graph[v]: 
            if visited[i]==False : 
                if(self.isCyclicUtil(i,visited,v)): 
                    return True
            elif parent!=i: 
                return True
        return False
    def isCyclic(self): 
        visited =[False]*(self.V) 
        for i in range(self.V): 
            if visited[i] ==False: 
                if(self.isCyclicUtil(i,visited,-1))== True: 
                    return True
        return False
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    degree = [0]*n
    edges = []
    for _ in range(m):
        tup = tuple(list(map(int, input().split())))
        kup = tuple([tup[0]-1, tup[1]-1])
        degree[kup[0]] += 1
        degree[kup[1]] += 1
        edges.append(kup)
    g = Graph(n)
    for i in edges:
        g.addEdge(i[0], i[1])
    
    if g.isCyclic():
        pass
    else:
        print(-1)
        continue
    flag = 0
    minimum = max((m-n+1), 2)
    for i in range(n):
        if degree[i] < minimum:
            continue
        g = Graph(n)
        if flag == 1:
            break
        for edge in edges:
            if edge[0] != i and edge[1] != i:
                g.addEdge(edge[0], edge[1])
        if not g.isCyclic():
            print(i+1)
            flag = 1
            break
    if flag == 1:
        continue
    else:
        print(-1)
        continue