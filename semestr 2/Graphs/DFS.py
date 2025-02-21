
#                    0
#                1/     \2     \6
#           3/      \4/
#       5/

graph = {0:[1,2,6],
         1:[3,4],
         2:[4],
         3:[5],
         4:[],
         5:[],
         6:[]
}

color= ['white' for i in graph.keys()]
final=[]

def dfs(graph,v,final):
    color[v] = 'gray'
    #print(v)
    final.append(v)

    for u in graph[v]:
        if color[u] == 'white':
            #print(color)
            dfs(graph,u,final)
    color[v]='black'
    return final

print(dfs(graph,0,final))

