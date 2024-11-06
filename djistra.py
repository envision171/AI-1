import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    min_heap = [(0, start)]
    
    while min_heap:
        curr_dist, u = heapq.heappop(min_heap)
        
        if curr_dist > distances[u]:
            continue
        
        for v, weight in graph[u]:
            distance = curr_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(min_heap, (distance, v))
                
    return distances

# Example graph as an adjacency list
graph = [
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5)],
    []
]

print("Dijkstra's Shortest Path from Node 0:", dijkstra(graph, 0))
