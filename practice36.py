def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
g = int(input())
p = int(input())
parent = [[] for _ in range(g + 1)]
result = 0

for i in range(g + 1):
    parent[i] = i

for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    else:
        union_parent(parent, data, data - 1)
        result += 1
print(result)