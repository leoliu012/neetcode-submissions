class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        print(graph)

        visited = set()

        q = deque([(0,-1)])
        while q:
            node, parent = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            new_nodes = graph[node]
            for new_node in new_nodes:
                if new_node == parent:
                    continue
                q.append((new_node, node))

        return len(visited) == n
