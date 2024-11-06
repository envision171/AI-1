import heapq

def a_star(maze, start, goal):
    # Initialize open list as a priority queue
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Initialize dictionaries for tracking cost and path
    g_cost = {start: 0}
    came_from = {start: None}
    
    while open_list:
        # Get the node with the lowest f-score
        _, current = heapq.heappop(open_list)
        
        # If goal is reached, reconstruct path
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Return reversed path
        
        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Left, right, up, down
            neighbor = (current[0] + dx, current[1] + dy)
            
            if (0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0])  # Check bounds
                    and maze[neighbor[0]][neighbor[1]] != 1):  # 1 means obstacle
                
                # Calculate new g-cost
                tentative_g_cost = g_cost[current] + 1
                
                # If the neighbor is unvisited or found a cheaper path
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current
                    
    return None  # No path found

def heuristic(a, b):
    # Manhattan distance heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Define a simple maze where 0 is a free space and 1 is an obstacle
maze = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Start and goal positions
start = (0, 0)
goal = (4, 4)

# Find and print path
path = a_star(maze, start, goal)
print("Path:", path)
