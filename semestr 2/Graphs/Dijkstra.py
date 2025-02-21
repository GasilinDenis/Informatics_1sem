
G={
    5:[(4,1)],
    4:[(1,0.5)],
    1:[(2,1),(3,3)],
    2:[(3,1)],
    3:[(0,2)],
    0:[(4,0.5)]
}

def Deij(G,s):
    V = len(G.keys())
    dist = [float('inf') for i in range(V)]
    filt = [float('inf') for i in range(V)]
    prev = [None for i in range(V)]
    dist[s]=0
    filt[s]=0
    S = set()
    while len(S) < V:
        v=filt.index(min(filt))
        if min(filt) == float('inf'):
            return dist
        print('v= ',v,' G[v]= ',G[v])
        S.add(v)
        for u,w in G[v]:
            print(u,w)
            if u not in S and dist[u] > dist[v]+w:
                prev[u]=v
                dist[u]=dist[v] + w
                filt[u]=dist[v] + w
                print('dist= ',dist)
                print('prev= ',prev)
                print('S= ',S)
        filt[v]=float('inf')
        print('filt: ',filt)
    return dist

print(Deij(G,0))

