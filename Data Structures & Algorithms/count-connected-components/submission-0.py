class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()
        ret = 0
        for node in range(n):
            if node not in visited:
                print(visited)
                ret +=1
                q = deque([node])
                while q:
                    node = q.popleft()
                    new_nodes = graph[node]
                    for new_node in new_nodes:
                        if new_node not in visited:
                            visited.add(new_node)
                            q.append(new_node)
                
        return ret
                