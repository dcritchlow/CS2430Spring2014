def Dijkstra(graph, start, target):
    for i in range(1,len(n)):


procedure Dijkstra(G: weighted connected simple graph, with all weights positive)
{G has vertices a = v0, v1, . . . , vn = z and lengths w(vi , vj )
    where w(vi , vj ) = infinity if {vi , vj } is not an edge in G}
    for i := 1 to n
        L(vi ) := infinity
        L(a) := 0
        S := {}
{the labels are now initialized so that the label of a is 0 and all
other labels are., and S is the empty set}
    while z is not in S
        u := a vertex not in S with L(u) minimal
        S := S union {u}
        for all vertices v not in S
            if L(u) + w(u, v) < L(v) then L(v) := L(u) + w(u, v)
            {this adds a vertex to S with minimal label and updates the labels of vertices not in S}
    return L(z) {L(z) = length of a shortest path from a to z}
