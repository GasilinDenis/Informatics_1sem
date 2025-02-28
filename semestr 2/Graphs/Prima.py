G={
    5:[(4,1),(6,1)],
    4:[(1,0.5)],
    1:[(2,1),(3,3)],
    2:[(3,1),(8,2)],
    3:[(7,5)],
    0:[(4,0.5),(3,2),(8,1),(1,2)],
    8:[(7,2)],
    7:[],
    6:[(1,2)]
}

def Deorientation(G):
    Gdeor={i:[] for i in G.keys()}
    for i in G.keys():
        for u,w in G[i]:
            Gdeor[i].append((u,w))
    for i in G.keys():
        #print(G[i])
        for u,w in G[i]:
            if i not in G[u]:
                Gdeor[u].append((i,w))
        #print(Gdeor)
        #print('G: ',G)
    return Gdeor

G=(Deorientation(G))
print(G)

def Prim(G):
    f = float('inf')
    h=0
    MST = []
    V = len(G.keys())
    dist = [f for i in range(V)]
    filt = [float('inf') for i in range(V)]
    dist[0]=0
    filt[0]=0
    prev=[None for i in range(V)]
    S = set()
    while len(S)!=V and h < 10:
        v=filt.index(min(filt))
        if min(filt) == float('inf'):
            weight = sum(dist)
            return dist,weight
        S.add(v)
        if prev[v] is not None:
            MST.append((prev[v],v))
        for u,w in G[v]:
            print('u,w: ',u,w)
            if u not in S and dist[u] > w:
                prev[u] = v
                dist[u] = w
                filt[u] = w
                print('dist= ', dist)
                print('prev= ', prev)
                print('S= ', S)
            filt[v] = f
            print('filt: ', filt)
        #h+=1
    weight=sum(dist)
    return MST,weight

print(Prim(G))

#           0
#       4       8
#    1     5        7
#   2       6
#  3
#