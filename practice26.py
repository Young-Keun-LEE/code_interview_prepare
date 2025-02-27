import copy
n = int(input())
t = [] #consuming time
p = [] #Pay for each counsel
dp = [0] * (n + 1)
max_value = 0

for i in range(n):
    data = list(map(int, input().split()))
    t.append(data[0])
    p.append(data[1])

for i in range(n - 1, -1, -1):
    time = t[i] + i
    
    if time <= n:
        dp[i] = max(max_value, dp[time] + p[i])
        max_value = dp[i]
    else:
        dp[i] = max_value
        
print(max_value)    