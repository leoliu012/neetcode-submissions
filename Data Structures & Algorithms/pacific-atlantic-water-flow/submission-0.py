class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_visited = set()
        atlantic_visited = set()
        ret = []
        def dfs(r,c,graph, atlantic):
            if atlantic: 
                if (r,c) not in atlantic_visited:
                    atlantic_visited.add((r,c))
                    if r-1>=0 and graph[r-1][c] >= graph[r][c]:
                        dfs(r-1, c, graph, atlantic)
                    if r+1<len(graph) and graph[r+1][c] >= graph[r][c]:
                        dfs(r+1, c, graph, atlantic)
                    if c-1>0 and graph[r][c-1] >= graph[r][c]:
                        dfs(r, c-1, graph, atlantic)
                    if c+1<len(graph[0]) and graph[r][c+1] >= graph[r][c]:
                        dfs(r, c+1, graph, atlantic)
            else:
                if (r,c) not in pacific_visited:
                    pacific_visited.add((r,c))
                    if r-1>=0 and graph[r-1][c] >= graph[r][c]:
                        dfs(r-1, c, graph, atlantic)
                    if r+1<len(graph) and graph[r+1][c] >= graph[r][c]:
                        dfs(r+1, c, graph, atlantic)
                    if c-1>0 and graph[r][c-1] >= graph[r][c]:
                        dfs(r, c-1, graph, atlantic)
                    if c+1<len(graph[0]) and graph[r][c+1] >= graph[r][c]:
                        dfs(r, c+1, graph, atlantic)
        r = 0
        for c in range(len(heights[0])):
            if (r,c) not in pacific_visited:
                dfs(r,c, heights,0)
        c = 0
        for r in range(len(heights)):
            if (r,c) not in pacific_visited:
                dfs(r,c, heights,0)
        
        r = len(heights)-1
        for c in range(len(heights[0])):
            if (r,c) not in atlantic_visited:
                dfs(r,c, heights,1)
        
        c = len(heights[0])-1
        for r in range(len(heights)):
            if (r,c) not in atlantic_visited:
                dfs(r,c, heights,1)
        print((0,2) in atlantic_visited)
        return list(pacific_visited & atlantic_visited)