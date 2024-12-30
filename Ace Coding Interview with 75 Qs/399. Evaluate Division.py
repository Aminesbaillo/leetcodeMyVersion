 
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        pass
    
    
    
from collections import defaultdict

def creat_representation(equations, values):
    graph = defaultdict(list)
    for equation, value in zip(equations, values):
        graph[equation[0]].append((equation[1], value))
        graph[equation[1]].append((equation[0], 1 / value))  # Always add the inverse
    return graph

equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

graph = creat_representation(equations, values)

def dfs(graph, start, end, visited, product):
    if start == end:
        return product        
    visited.add(start)
    for neighbor, value in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, visited, product * value)
            if result != -1:
                return result 
    return -1


results = []
for query in queries:
    start, end = query
    if start not in graph or end not in graph:
        results.append(-1.0)
    else:
        results.append(dfs(graph, start, end, set(), 1.0))
print(results)
