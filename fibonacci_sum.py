def fibonacci_sum(n):
    if(n<3):
        return n
    ans = 2
    a1 = 1
    a2 = 1
    for i in range (3,n+1):
        ans += a1+a2
        a2 = a2+a1
        a1 = a2-a1
    return ans

inp = int(input())
print(fibonacci_sum(inp))
