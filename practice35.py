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
        
n = int(input())
m = int(input())

parent = [[] for _ in range(n + 1)]
for i in range(n + 1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)

travels = list(map(int, input().split()))
result = True

for i in range(m - 1):
    if find_parent(parent, travels[i]) != find_parent(parent, travels[i + 1]):
        result = False
        
if result:
    print("YES")
else:
    print("NO")