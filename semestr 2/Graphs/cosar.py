
G = {1:[2,3],
         2:[4],
         3:[4],
         0:[],
         4:[0,1],
         5:[1]
}

def dfs(graph,v,final,top,color):
    color[v] = 'gray'
    final.append(v)
    for u in graph[v]:
        if color[u] == 'white':
            #print(color)
            dfs(graph,u,final,top,color)
    top.append(v)
    color[v]='black'
    return final,top,color

def Topology(G):
    final=[]
    top=[]
    S = set()
    color = ['white' for i in G.keys()]
    for i in G:
        if color[i]=='white':
            dfs(G,i,final,top,color)
    return top[::-1]

def tran(graph):
    S = set()
    tran = {i: [] for i in graph.keys()}
    #print(tran)
    for i in graph.keys():
        for u in graph[i]:
            #print(u)
            if i not in S:
                tran[u].append(i)
    return tran

Tar = Topology(G)
#print(Tar)

G=(tran(G))
#print(G)

color= ['white' for i in G.keys()]
final=[]

def dfs_1(graph,v,final,color):
    color[v] = 'gray'
    #print(v)
    final.append(v)

    for u in graph[v]:
        if color[u] == 'white':
            #print(color)
            dfs(graph,u,final)
    color[v]='black'
    return final,color

S=set()
color = ['white' for i in G.keys()]
top=[]
final=[]
for i in Tar:
    if i not in S:
        final, top,color=(dfs(G,i,final,top,color))
        print(top)
        for j in top:
            S.add(j)
        top = []
