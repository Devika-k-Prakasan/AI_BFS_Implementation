from collections import deque

def bfs(graph, costs, start, goal):

    
    queue = deque([start])
   
    visited = {start}
   
    came_from = {start: None}
 
    g_costs = {start: 0}

    while queue:
        current = queue.popleft()

        if current == goal:
           
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
       
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                
                new_cost = g_costs[current] + costs.get(neighbor, 0)
                

                if neighbor not in g_costs or new_cost < g_costs[neighbor]:
#If the neighbor hasn’t been explored before (neighbor not in g_costs).
#Or if the new cost to reach the neighbor is cheaper than any previously recorded cost (new_cost < g_costs[neighbor]).
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    g_costs[neighbor] = new_cost
                    queue.append(neighbor)

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H', 'I'],
    'F': ['I'],
    'G': ['J'],
    'H': ['J'],
    'I': ['J'],
    'J': [] 
}


costs = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 1,
    'E': 2,
    'F': 3,
    'G': 4,
    'H': 1,
    'I': 2,
    'J': 5  
}
start = 'A'
goal = 'J'

path = bfs(graph, costs, start, goal)
if path:
    print("BFS Path found:", path)
else:
    print("No path found.")
