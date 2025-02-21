
#            0
#        1       5
#    2                 6
#3       4

graph = {0:[1,5],
         1:[2],
         2:[3,4],
         3:[],
         4:[],
         5:[6],
         6:[]}

def BFS(graph,start):
    visited=set()
    que=[]
    que.append(start)
    visited.add(start)
    final=[]

    while que:
        node = que.pop(0)
        final.append(node)
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                que.append(i)
    return final

print(BFS(graph,0))