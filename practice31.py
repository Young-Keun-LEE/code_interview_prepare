INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
result = 0

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
    
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    flag = False
    for j in range(1, n + 1):
        if graph[i][j] == INF and graph[j][i] == INF:
            flag = False
            break
        else:
            flag = True
            
    if flag is True:
        result += 1

print(result)
                    