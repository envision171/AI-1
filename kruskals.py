def kruskal_mst(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX != rootY:
            parent[rootX] = rootY
    
    mst_cost = 0
    mst_edges = 0
    
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst_cost += weight
            mst_edges += 1
            if mst_edges == n - 1:
                break

    return mst_cost

# Example edges for a graph with 5 nodes
edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7)]
print("Kruskal's MST Cost:", kruskal_mst(5, edges))
