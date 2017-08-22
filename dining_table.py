def dining_table(n):
    if(n==0):
        return 1
    x = 1
    while(n//x >= x+1):
        n = n//x
        x += 1
    return x+1
n = int(input())
print(dining_table(n))
