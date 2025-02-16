# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     else:
#         return x

def find_parent(parent, x): # Using path compression
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
        
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
print("The set of each element: ", end = "")
for i in range(1, v + 1):
    print(find_parent(parent, i), end = " ")

print()

print("parent's table: ", end = "")
for i in range(1, v + 1):
    print(parent[i], end = " ")
    