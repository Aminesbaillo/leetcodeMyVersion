 
 
# # n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]] 
# class Solution(object):
#     def minReorder(self, n, connections):
#         """
#         :type n: int
#         :type connections: List[List[int]]
#         :rtype: int
#         """
#         pass
    
    
    
    
# from collections import defaultdict

# def build_bidirectional_graph(connections):
#     graph = defaultdict(list)
#     for a, b in connections :
#         graph[a].append((b, True)) # original direction a->b
#         graph[b].append((a, False))# reverse direction b->a

#     return graph

# # test the function : 
# connections = [[0, 1], [1, 2], [2, 3]]
# print(build_bidirectional_graph(connections))


# def neighbors(graph, city):
#     for neighbor, is_original in graph[city]:
#         direction  = "is_original" if is_original else "reverse"
#         print(f"City {city} is connected to {neighbor}. Original direction: {direction}")
            
# graph = {
#     0: [(1, True)],
#     1: [(0, False), (2, True)],
#     2: [(1, False), (3, True)],
#     3: [(2, False)]
# }
# for key in graph.keys():
#     print(neighbors(graph, key))





from collections import deque, defaultdict

def build_bidirectional_graph(connections):
    graph = defaultdict(list)
    for a, b in connections :
        graph[a].append((b, True)) # original direction a->b
        graph[b].append((a, False))# reverse direction b->a
    return graph


# test the solution : 
# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3

graph_1 = build_bidirectional_graph([[0,1],[1,3],[2,3],[4,0],[4,5]])
print(graph_1)

# def dfs(graph, start_city):
#     visited = set() # create an empty tuple to keep track of visited city
#     queue = deque([start_city]) # will be used to track current visited city
#     count = 0
#     while queue :
#         city = queue.popleft() # if not visited we will visit 
#         if city not in visited:
#             print(f"Visited city {city}")
#             visited.add(city)
#             for neighbor, is_original in graph[city]:
#                 if neighbor not in visited :
#                     queue.append(neighbor)
#                 if city !=  0: 
#                     if  not is_original and graph[city][0] == (neighbor,is_original): #i need to see the first element in the 1: [(0, False), (3, True)] => 1 and  0 if false add 1
#                         count += 1
#     return count, visited


from collections import deque

def dfs(graph, start_city):
    visited = set()  # Track visited cities
    queue = deque([start_city])  # Queue for BFS traversal
    count = 0  # Count of roads to reorient

    while queue:
        city = queue.popleft()
        if city not in visited:
            print(f"Visited city {city}")
            visited.add(city)
            for neighbor, is_original in graph[city]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    # Count reoriented roads (only if the edge is in the original direction)
                    if is_original:
                        count += 1

    return count

print(dfs(graph_1, 0))