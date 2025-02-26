from collections import deque


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            
            # To add neighbors to stack in reverse order
            # (so they're popped in the original order)
            # for neighbor in reversed(graph[vertex]):
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited


# Iterative BFS
def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return visited

# Example graph
graph = {0: [1, 3], 1: [2],2:[], 3: [4, 6, 7], 4: [2, 5], 5: [2],6:[],7:[],}

print("Recursive DFS:")
dfs_recursive(graph, 0)
print("\nIterative DFS:")
dfs_iterative(graph, 0)

print("BFS Iterative:")
bfs_iterative(graph, 0)

