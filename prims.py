import heapq

def prim_mst(graph, start=0):
    n = len(graph)
    mst_cost = 0
    visited = [False] * n
    min_heap = [(0, start)]
    
    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if visited[node]: continue
        visited[node] = True
        mst_cost += cost
        
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight, neighbor))
                
    return mst_cost

# Example graph represented as an adjacency list
graph = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8)],
    [(1, 5), (2, 7)]
]

print("Prim's MST Cost:", prim_mst(graph))
